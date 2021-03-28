---
created: 2021-03-04
tag: cron
title: Gotcha when adding an offset to cron intervals
---
`2/5 * * * *` is a handy cron expression for "every five minutes, starting at 2 minutes
past", i.e. an offset of two minutes. This helps avoid lots of cronjobs running at the
same time.

However, older versions (Debian 10 is where I found this) don’t support this shorthand,
and you must specify the full range of minutes, so: `2-59/5 * * * *`.
