---
created: 2021-02-23
tag: python
---
# Using `next()` to skip the first row of an iterator

Today in "new application of things I already knew". You can repeatedly use `next()` to
move through an iterator. Or you can use a for loop to do the same thing. Each has
their use.

The subtlety I'd missed is that the for loop doesn’t restart the iterator. So if you're
moving through a file and you need to skip a header row, you can do:

```python
next(file_iterator)
for row in file_iterator:
    # process row
```

Which is much cleaner than trying to count rows or use a flag.
