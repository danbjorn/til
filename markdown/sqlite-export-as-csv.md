---
created: 2021-03-11
tag: sqlite
title: Export data to file from SQLite's CLI
---
The SQLite shell can export to a file in various formats quite easily.

To export a query as a CSV:

```
.headers on
.mode csv
.once output.csv
select * from whatever;
```

Another fun one is exporting the query as a HTML table - everything but the
`<table></table>` tags:

```
.headers on
.mode html
.once output.html
select * from whatever;
```

The general form is to use `.mode` to switch to the appropriate output, and `.once` to
specify where the query will be written to. As hinted by the name, only the next query
will be written out - after that it will go back to outputting to the shell. When you're
done you can set `.mode list` to go back to SQLite's default output.

Note the use of `.headers on`. By default SQLite doesn't output headers. I find this is
generally useful one to have on permanently.

You can read more about all this in the
[output formats documentation](https://sqlite.org/cli.html#changing_output_formats).
