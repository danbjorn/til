---
created: 2021-09-29
tag: postgres
title: Watching a query in Postgres
---
Sometimes it is handy to be able to repeatedly query a table so that you can spot
changes in near real time. Now you can do this with the venerable `watch` command, but
it's a bit clunky to use with `psql`, needing hoop-jumping to get auth working and to
escape characters correctly.

Enter the `\watch` meta command. This repeatedly runs the last query every few seconds
until told to stop with `ctrl+c`. It even includes a timestamp for each run.

`\watch` takes a single argument, `seconds`, which is how often to run the query. It
defaults to every two seconds.

It's not quite as slick as `watch` - there is no option for highlighting differences,
and it scrolls the buffer for each run rather than replacing the screen - but it's very
convenient.

Note that `\watch` is only available in `psql` version 10 and above, although it doesn't
matter what version the server is running as it's a purely client side feature.
