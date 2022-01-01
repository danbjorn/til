---
created: 2021-07-29
tag: bash
title: Using `namei` to track down permissions issues
---
Permissions are one of those things that are conceptually very simple, and yet seem to
cause endless complicated problems, particuarly at the worst moments.

A handy tool to keep around for such instances is `namei`. At its most basic, it takes a
target path, and then attempts to resolve each part of it until it fails or it reaches
some sort of terminator. For example:

```bash
$ namei /home/danbjorn
f: /home/danbjorn
 d /
 d home
 d danbjorn
```

This at the very least tells you that every part of the path is accessible to the
current user, and that each part is a directory (as opposed to, say, a link).

You can add the `-om` options to get more information about the permissions for each
level:

```bash
$ namei -om /home/danbjorn
f: /home/danbjorn
 drwxr-xr-x root     root     /
 drwxr-xr-x root     root     home
 drwxr-xr-x danbjorn danbjorn danbjorn
```
