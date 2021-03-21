---
created: 2021-01-08
tag: alembic
---
# Alembic complaining that a table has already been defined?

I hit a curious one today where [Alembic](https://alembic.sqlalchemy.org/) claimed
that a table had already been defined, and I was sure it wasn't. I tried it with a
blank database, I cleared out all other migrations and models, I even changed the model
name to nonsense, nothing helped.

It turns out that my `version_locations` path was incorrect, referencing the parent
package rather than the migrations directory. Apparently this causes Alembic to try and
import the model definition twice, hence the error.
