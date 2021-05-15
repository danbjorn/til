---
created: 2021-05-14
tag: vscode
title: Enabling `justMyCode` when debugging Python tests in VSCode
---
When debugging Python in VSCode, by default it won't step in to or catch breakpoints in
anything that isn't "your" code - i.e. anything not in the current project. This is
normally handy as generally you don't really care about the underlying libraries.

However, sometimes you really could do with poking around with what's going on
underneath. It's also handy to learn more about the libraries that you use. This is one
of the nice things about open source python - great code is just sitting there waiting
for you to learn from it, and stepping through the code in the context of your own code
is a good way to do this.

If you look up how to do this, generally you'll see answers about setting `justMyCode`
to `false` in your `launch.json`. This is fine if you're running your tests via the
`Run and Debug` pane, but the Python extension integrates directly with the testing
pane, so you don't have such a configuration.

After doing some digging, I found what I need in the
[python testing docs for vscode](https://code.visualstudio.com/docs/python/testing#_debug-tests).
It explains that if you add a section to your `launch.json` as below, you can configure
the test behaviour:

```json
{
    "name": "Debug Unit Test",
    "type": "python",
    "request": "test",
    "justMyCode": false,
}
```

You'll then be able to step in to code outside of the current project. Credit to
[this StackOverflow post](https://stackoverflow.com/questions/52980448/how-to-disable-just-my-code-setting-in-vscode-debugger/57831657#57831657)
by user [Tenzin](https://stackoverflow.com/users/5757501/tenzin) for starting me down
the correct path.
