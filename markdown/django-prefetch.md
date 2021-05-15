---
created: 2021-05-15
tag: django
title: Using `Prefetch` to customise ordering of `prefetch_related()`
---
I've been using Django for a long time now, more than a decade, and still I find
features and tricks I've never come across before.

First some background -
[select_related()](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#select-related)
and [prefetch_related()](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#prefetch-related)
are methods used to modify queryset objects. They both ask Django to, in addition to the
query specified by the rest of queryset, also follow relationships to other objects and
to cache the results. These help you avoid extra database calls by pulling down as much
data as possible in as few queries as possible.

The important distinction between `select_related()` and `prefetch_related()` is that
`select_related` extends the target query by joining with other tables, and
`prefetch_related` performs extra queries to retreive the extra objects. So
`select_related` does it all in one query, and `prefetch_related` does it in one query
per relationship. This generally is still much better than one query per object, and
also allows for following relationships that can't be done with a straight inner join.

A difficulty I hit recently was in trying to follow a many-to-one relationship from a
model, but wanting to have the cached results come back from the database in a
particular order. The code I started with was something like:

```python
Parent.objects.filter(blargh=True).prefetch_related("child_set")
```

One option here is to add a
[default ordering](https://docs.djangoproject.com/en/3.2/ref/models/options/#ordering)
to the model, but that is then applied to every query involving that model. I wanted to
be able to configure it for just this situation.

Enter [Prefetch objects](https://docs.djangoproject.com/en/3.2/ref/models/querysets/#prefetch-objects).
These were added way back in Django 1.7 but apparently it passed me by. Essentially they
allow you to customise the query used in the `prefetch_related`. You could for example
use it to provide some extra filtering on what objects are cached. But anything that can
be applied to a queryset can be used, so I used it to set an ordering. This is what I
ended up with:

```python
Parent.objects.filter(blargh=True).prefetch_related(
    Prefetch("child_set", queryset=Child.objects.order_by("number"))
)
```
