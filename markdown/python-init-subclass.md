---
created: 2021-03-16
tag: python
title: Python's `__init_subclass__` is handy for class registries
---
I'd heard of `__init_subclass__` before but never found a use. But it's really handy for
class registries, e.g. for a simple plugin architecture. The method is called when the
class is created, not when an object is instantiated. This avoids metaclass shenanigans
which are fun but generally difficult to reason about.

Check out this article from 2018 that goes on to me detail: <https://blog.yuo.be/2018/08/16/__init_subclass__-a-simpler-way-to-implement-class-registries-in-python/>