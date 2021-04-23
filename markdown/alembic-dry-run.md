---
created: 2021-04-23
tag: alembic
title: Dry-running Alembic migrations
---
On one of our projects, we have a test that simply runs all of the
[Alembic](https://alembic.sqlalchemy.org/) migrations using the command line tool. We do
this as that's exactly what the deployment pipeline does, so it's a smoke test to check
for migration problems in a clean environment. It's not perfect but it's handy to spot
silly mistakes.

For the sake of tidiness, we wanted a sort of "dry-run" mode where the migrations are
run against a real postgres instance, but then are rolled back afterwards. Now, Alembic
has an [offline mode](https://alembic.sqlalchemy.org/en/latest/offline.html), but that
just generates SQL scripts - there's no guarantee that they actually work.

Originally we used a little trick in `env.py` to rollback the transaction after the
migrations have run, when the `-x dry-run=True` option is provided. This from a
[handy stackoverflow answer](https://stackoverflow.com/questions/51556996/do-a-dry-run-of-an-alembic-upgrade/59704406#59704406):

```python
def run_migrations_online():
    arguments = context.get_x_argument(as_dictionary=True)
    connectable = get_engine(poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction() as transaction:
            context.run_migrations()

            if arguments.get("dry-run", False):
                transaction.rollback()
```

This worked fine. However this stopped working in the latest version of Alembic -
somehow the context manager was being broken by calling `rollback` early.

After trying many things to keep the context manager safe, we gave up and managed the
transaction manually:

```python
def run_migrations_online():
    arguments = context.get_x_argument(as_dictionary=True)
    connectable = get_engine(poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        try:
            context.run_migrations()

            if arguments.get("dry-run", False):
                transaction.rollback()
            else:
                transaction.commit()

        except:
            transaction.rollback()
            raise
```

Which is somewhat messier but does work quite happily.

In the end though we just got rid of the test and replaced it with
[pytest-alembic](https://pypi.org/project/pytest-alembic/) which does all this for us.

Still, it's been an interesting learning experience. Alembic is certainly powerful but
after working with Django's migrations it certainly can be very frustrating!
