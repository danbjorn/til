---
created: 2021-03-19
tag: libreoffice
title: Converting a LibreOffice ODS to a unicode CSV
---
On the one hand, it's great that LibreOffice can be run as a command line tool to
convert between file types. On the other hand, it's ridiculously opaque with minimal
documentation and little to no error messages.

So, for the record, if you are converting an ODS to a CSV and want the output in UTF-8,
you want something like the following:

```bash
soffice --headless --convert-to csv --infilter=CSV:44,34,76,1 --outdir "stuff" "blargh.ods"
```

The order of the arguments is important! It will sometimes fail silently if the
arguments are in the wrong order or invalid. Ask me how I know.

The magic `--infilter` string is the trick to ensure that the exported file is formatted
correctly in UTF-8. Documentation is here
<https://wiki.openoffice.org/wiki/Documentation/DevGuide/Spreadsheets/Filter_Options>,
but essentially each number corresponds to a configuration field:

1. What character is used to separate fields, as an ASCII char (44 is ,).
2. What character is used to optionally surround text fields, as an ASCII char
   (34 is “).
3. What character set is used. 76 refers to UTF-8, see the list in the wiki page above
   for more.
4. What number line is the first line of data (1-based). Not really relevant for export
   but has to be included.
