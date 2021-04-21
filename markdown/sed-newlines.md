---
created: 2021-04-21
tag: bash
title: Sed not matching newlines
---
This is less a "today I learned" and more of a "I'm embarrassed this confused me". I was
massaging a CSV file with sed to get it to line up with another similar CSV. I wanted to
remove an extra empty column, and so I did (edited for clarity):

```bash
sed -e 's/,$//' file.csv
```

And to my surprise, it didn't work. It took me too long to figure out why; I blame it
being nice outside today.

For those not familiar with sed and regexes, this is
a little script (the `-e`) that tells sed to substitute (the `s`) the pattern between
the first and second forward slashes (in this case `,$`) with the string between the
second and third forward slashes (in this case, with nothing), for each line of
`file.csv`.

The pattern I am matching is a single comma. The `$` indicates that the next character
after the comma should be the end of the line. So effectively I am removing an empty
last column from the CSV.

It turns out that the reason this didn't work is because of line endings. The file was
created on Windows, which (by default) ends lines with two characters, `CR` and `LF`,
whereas I am using Linux, which ends lines with just one, `LF`.

I've spent years fighting files from all kinds of sources, line endings,
magic characters, and other nonsense, so yeah I'm kinda embarrassed I forgot to look at
the line endings.

The solution is simply to also match the bonus `CR` character:

```bash
sed -e 's/,\r$//' file.csv
```

And I have my massaged file.
