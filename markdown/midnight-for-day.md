---
created: 2021-03-02
tag: python
---
# Finding midnight for a given day

Historically I’ve always found “midnight for a day” using replace, e.g.:

```python
dt.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
```

But it’s far less clunky to use `combine()` and a `time` object:

```python
dt.datetime.combine(dt.date.today(), dt.time(0, 0, 0))
```

Of course there’s still fun to be had with timezones; both `combine()` and `time()`
accept a `tzinfo` object but of course there are the normal restrictions for pytz. In
theory `zoneinfo` won’t have this restriction.
