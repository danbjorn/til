---
created: 2021-02-04
tag: python
title: Python's spread operator
---
`*` turns up in various places, but the well of little tricks it can be used for is
apparently bottomless. Here I use it to replace the first element of a tuple:

```python
a = (1, 2, 3)
b = (4, *a[1:])
```
