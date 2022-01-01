---
created: 2021-09-01
tag: python
title: Using `python -m pickle` to decode pickle files
---
This is something that is apparently reasonably commonly known, but I can't find
mentioned in the docs, except for an oblique reference on the
[pickletools page](https://docs.python.org/3/library/pickletools.html?highlight=pickle#command-line-usage).

If you have a pickle file and you want to quickly look inside it, rather than firing up
a python shell and faffing with `open` etc, you can just do:

```bash
python -m pickle file.pkl
```

And it will load the object from the file and render it using
[pprint](https://docs.python.org/3/library/pprint.html?highlight=pprint#pprint.pprint).
This is particularly handy if the object has a nice rendering, for example a pandas
dataframe.

Looking at [the code](https://github.com/python/cpython/blob/main/Lib/pickle.py#L1797)
this definitely feels like a debugging entry point (e.g `-t` runs a test suite) which
might explain why it's not in the python docs. Still, it's pretty handy if you're using
pickle files for storage and need to figure out what's going on.
