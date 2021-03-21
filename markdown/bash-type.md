---
created: 2021-02-17
tag: bash
---
# Bash's `type` builtin is very handy

`which` is great for finding where applications are installed, but it can’t handle
anything that isn’t a regular binary. Enter `type`, a bash builtin, that will find
anything that bash can find, and provide useful context.

* `type <name>` will return the path to what will run if you just ran `<name>`.
* `type -p <name>` will do the same but without extra fluff - it’ll just be the path.
* `type -a <name>` will list all places that provide `<name>` - handy if you think
  something is overriding the executable.
* `type -t <name>` will give the type of the target - file, builtin, alias, function
  etc.

The best trick is that if `<name>` is a bash function or an alias, it will print out
the code for it! So even if your function is embedded in a huge file, this will neatly
snip out the code and print it for you. Very handy.

