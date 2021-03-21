---
created: 2021-02-09
tag: bash
---
# Bash default values for arguments

If you want an "optional" argument to a function in bash, through parameter
substitution you can define a default value for an argument. E.g. in:

```bash
local port="${1:-8000}"
```

if an argument is supplied, then `port` is set to the argument. If not, it is set to
the default value of `8000`. Note the hyphen in the middle there.

More here: <https://coderwall.com/p/s8n9qa/default-parameter-value-in-bash >
