---
created: 2021-09-29
tag: postgres
title: Psql expanded output
---
In MySQL you can finish a query with `\G` instead of `;` to get "expanded output" - i.e.
instead of:

```
mysql> SELECT * FROM blargh;
+---+---+
| a | b |
+---+---+
| 1 | 2 |
+---+---+
| 3 | 4 |
+---+---+
2 rows in set (0.00 sec)
```

You can get:

```
mysql> SELECT * FROM blargh\G
*************************** 1. row ***************************
a: 1
b: 2
*************************** 2. row ***************************
c: 3
d: 4
2 rows in set (0.00 sec)
```

This is very useful if the query has a lot of columns, particularly if you're only
looking at one or two rows. My question was, does `psql` have something similar?

Turns out that yes, `psql` has something similar - `\gx`.

```
% SELECT * FROM blargh\gx
-[ RECORD 1 ]-+--
a             | 1
b             | 2
-[ RECORD 2 ]-+--
a             | 3
b             | 4
```

You can also toggle this behaviour on and off with `\x`.

Note that `\gx` is only available in `psql` version 10 and above, although the version
of the server shouldn't matter as it is a purely client side feature.
