---
created: 2021-03-16
tag: python
title: Reversing a `range`
---
`range` objects have an `__reversed__` attribute, which means that you can use them with
`reversed()` without having to instantiate the list, e.g.

```python
for index in reversed(range(5)):
```

Note that this is not true of `enumerate()` objects - to reverse an enumerated iterator
you have to consume the whole thing first. This means if you want to iterate through
something in reverse with indexes, it’s best to do something like:

```python
for index in reversed(range(len(data))):
    item = data[index]
```

Although this feels super ugly so I'm curious if there's an alternate option. It is
possible, if somewhat unwieldy, to make use of `zip()` to get it on one line:

```python
for index, item in zip(reversed(range(len(data))), reversed(data)):
```

You could also muck around with `itertools.count()` or something to remove the extra
`reversed()`:

```python
for index, item in zip(count(len(data)-1, -1), reversed(data)):
```

But I don't think that's much better. Open to suggestions.
