---
created: 2021-03-09
tag: python
title: How `findall` handles groups
---
`re.findall` in its basic form is quite handy. But if you specify a group in the
pattern, `findall` will search for all occurrences of the pattern, but only return the
group. And not a group object or weird structure, literally as strings.

I learned this when completing an exercism challenge, making an acronym from a phrase.
So the following:

```python
"".join(re.findall(r"([A-Z])[A-Z]*", words.upper()))
```

Would turn "portable network graphics" into "PNG". Note that only the first letter is in
a group and so that’s the only bit that's returned.

If you specify multiple groups it will return a list of tuples, with each tuple holding
the matches for each group.
