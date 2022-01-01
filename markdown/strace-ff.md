---
created: 2021-07-28
tag: strace
title: Following the trace of child processes
---
Strace is a wonderful program for understanding why a program is doing something weird.
However, many programs rely on sub-processes to get things done, and strace by default
will only follow the initial program.

Luckily strace has `-f` which instructs strace to also gather calls for any child
processes created during the trace. When you do this the output is changed slightly to
include the process ID as the first field.

The real magic is using the `-ff` flag with `-o`. When you use this form, strace will
track each child, but will then write the output to a separate file per process. So if
you used `strace p 123 -ff -o blargh`, and the process created three processes, you'd
end up with files named `blargh.123`, `blargh.124`, `blargh.125` and `blargh.126`.

This was particularly useful when we were digging in to a `uwsgi` instance that was
refusing to play ball. `uswgi`'s log output is notoriously bad, so being able to watch
what the processes were actually trying to do really opened our eyes.

As an aside, if you want to play about with strace, I cannot recommend Julia Evan's
[zine about strace](https://wizardzines.com/zines/strace/) highly enough. All of her
zines are amazingly useful.
