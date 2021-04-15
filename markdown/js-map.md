---
created: 2021-04-15
tag: javascript
title: Map is better dictionary than Object
---
So file this one under "my javascript knowledge has some holes", but today I learned
about the `Map()` object.

A long standing frustration I've had when writing javascript is that Objects are
actually a pretty poor map, at least when I'm used to Python dicts. They come with so
much baggage and gotchas, not to mention awkward methods for extracting keys etc, that
they are a faff to use.

Enter `Map`, which is much more traditional. It's a little awkward to use - you have to
use `get` and `set` as if this was Java, but it's a much more solid tool all round.
Check out
[the article on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#objects_vs._maps)
for comparison between Objects and Maps.

It's got fun stuff like `has`, `keys`, `entries`, `values` and `forEach` methods, it
can use any object (including `NaN`) as keys, and it's safe against accidental
insertion and access.

It does have one big gotcha - it is at the end of the day an object, so indexed access
*looks* like it works, but it doesn't. MDN has
[a great example](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map#setting_object_properties)
walking through how this can go badly.

So this isn't a new thing, it's only new to me, but honestly I can see myself using
this in some of our data structure heavy JS.

