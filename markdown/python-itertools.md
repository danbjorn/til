---
created: 2021-04-23
tag: python
title: `more-itertools` is a treasure trove of goodies
---
Python's `itertools` library is a lovely set of widgets for manipulating and using
iterators, and can be used to make some wonderfully graceful code. However, it does
still have some limitations that can frustrate. I certainly have had dreams dashed when
launching in to new code, and have had written many awkward workarounds.

Enter [more-itertools](https://more-itertools.readthedocs.io/en/stable/index.html), a
further set of widgets to extend the standard library. Some are just extra useful tools,
some make it easier to use iterators in python, and some do horrendous (but wonderful)
things to iterators that arguably violate what an iterator even is!

Some highlights:

* [always_iterable](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.always_iterable)
  and [always_reversible](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.always_reversible)
  protect you from awkward situations where you can't necessarily trust what kind of
  iterable you have been passed. No more extra guard steps, these guarantee the
  operations you can perform.
* [roundrobin](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.roundrobin)
  picks elements from a set of iterables in a round-robin fashion until they are all
  exhausted, without getting confused by iterables of different lengths. One of those
  that is rarely needed but surprisingly messy to implement when you do.
* [peekable](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.peekable)
  and [seekable](https://more-itertools.readthedocs.io/en/stable/api.html#more_itertools.seekable)
  allow you to do things to iterators that you really shouldn't be able to do! And yet,
  don't you really want to?

As ever with libraries like this, the source code is an excellent place to learn. This
library in particular makes extensive use of iterators and generators, as well as
mucking around with protocols and magic methods. The authors have also been careful to
use fast implementations, so working through their decisions is enlightening.
