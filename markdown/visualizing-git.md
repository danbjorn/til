---
created: 2021-05-10
tag: git
title: Visualizing Git
---
Git has a wonderful object model that allows for some really handy and versatile
techniques. However, as has been pointed out by smarter folk than I, the command line
tools are deeply frustrating and confusing. The object model really is much simpler than
the tools make out.

For me, as someone who used Mercurial for a long time, the most frustrating thing I find
is trying to predict exactly what a particular git command is going to do. This makes it
tricky as soon as something non-routine is required.

Thankfully there are many, many great resources out there to help. A tool I found
recently that has helped me a lot is
[Visualizing Git](https://git-school.github.io/visualizing-git/).

This is an in-browser visualisation of a git repository, and you can enter real git
commands and watch how the repository changes. It uses animation to highlight exactly
what is happening. This is very handy if you want to test that what you think is going
to happen is correct before trying it on your own repo.

Documentation is light as, by the looks of it, the site was designed to be used in an
in-person git workshop, but it's not hard to use. I suggest using the `help` command to
get an idea of what's available, and to use the `mode remote` and `mode local` commands
to switch between the "local" and "remote" repositories.

Once you're confident in the commands you need to run, you can try using `git log` with
`watch` in another terminal. It's not as good without the animations but it help give
you confidence that you're doing the right thing:

```bash
watch -c git log --color --all --decorate --oneline --graph
```

As with many excellent tools I found this referenced on Julia's Evans'
[git commit questions](https://questions.wizardzines.com/git-commits.html). The
questions pages are a great way to explore a new topic and to test your understanding of
an existing project. If you've not come across Julia Evans before, you absolutely need
to go to [wizardzines.com](https://wizardzines.com/) and read/buy everything there.
[Julia's blog](https://jvns.ca/) is also excellent and well worth a follow.
