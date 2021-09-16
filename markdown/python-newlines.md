---
created: 2021-08-06
tag: python
title: Reminder that Python translates file newlines silently
---
This is less a TIL and more a "I suddenly and painfully remember this", so I guess this
is more of a PSA. I recently was working on some code that ran on linux but needed to
write files with windows-style line endings. The code clearly wrote `\r\n`, and the
tests seemed to agree, but when the files were transferred to a windows machine they
were broken. A mystery!

When you use `open`, or anything that uses `TextIO` underneath (e.g. pathlib's
`read_text`), then by default "universal newlines" are enabled. This means that when
reading or writing, Python will exchange any newline characters (i.e. `\n`, `\r\n` and
`\r`) for `\n`.

Normally this is very handy, particularly when reading random files, as it means you
don't need to care about the line endings - you can just use `\n` everywhere and it will
work regardless of platform.

What caught me out was that this works for writing as well: writing `\r\n`
to a file to try and get a windows-style newline will be converted to the target
platform's line ending - in this case I was on linux, and so it was writing `\n`.

The trick to writing other line endings, or to get the raw line endings from a file, is
to set the `newline` parameter to `""`, for example:

```python
with open("blargh.txt", "w", newline="") as f:
    f.write("hi\r\n")
```

Doing this effectively disables the special newline handling - it will write whatever
you specify, and read in the raw newline characters. It will still split lines as
expected however.

Of course, the actual lesson to learn here is to not do what I did: the reason I didn't
spot that the lines weren't being correctly written was that the tests were doing the
same thing as the code - they were trying to write `\r\n` but actually writing `\n`. The
moral of the story is when testing file writing, make sure you test against at least one
hand crafted file!

You can read about the universal newline support in the
[documentation for open](https://docs.python.org/3/library/functions.html#open-newline-parameter),
and (as noted in the docs), PEPs [278](https://www.python.org/dev/peps/pep-0278/) and
[3116](https://www.python.org/dev/peps/pep-3116/) have a bit more on the history. Also
credit to [this Stack Overflow answer](https://stackoverflow.com/questions/20350305/python-read-crlf-text-file-as-is-with-crlf#20350545) for shining a light when I was
staring in disbelief at the issue.
