---
created: 2021-04-28
tag: ssh
title: Running a script before an SSH connection
---
I like having as much configuration as possible in my `~/.ssh/config` and avoid aliases
and scripts. We have a sufficiently complex (not large, just complicated) that it's
really useful to use the `Host` directive to ensure I'm using the right user, and to
allow for host tab-completion.

However, for some hosts it's necessary that I am on a Wireguard VPN first, and I often
forget, which slows me down. For a while I've had to run a little script that sets up
the VPN and then connects. And that's just untidy!

So I was glad to learn today about the `Match exec` direction. `Match` has a variety of
sub-directives all of which have to match. This includes `host` which works much like
`Host`, and `exec` which calls a command that must return 0 for the connection to go
ahead.

This means I can trigger the VPN connection as part of the ssh command, for example:

```
Match host example.com exec "sudo wg-quick up wg0 || exit 0"
    User blargh
```

The `|| exit 0` is included as `wg-quick` returns 1 if the VPN is already connected,
which is fine.

This works surprisingly well - it even takes in to account the `sudo` prompt. However,
there are a couple of issues.

The first is that if `wg-quick` fails (incorrect configuration or something), then it
also returns 1. This means that the `Match` statement will still pass, and it will try
and make the SSH connection without the VPN, which is not ideal. The solution is to
write a script for managing the VPN that's a bit smarter, and call that instead. As long
as it returns a 0 when the VPN is ready and non-zero otherwise, it'll work. I'll leave
the specifics as an exercise for the reader.

The second is that you lose tab completion of hostnames. This is actually a pretty
sizeable issue and I'm not sure of the best way to get around this. I haven't dug in to
it yet but I am assuming there is a completion script somewhere that looks only for
`Host` directives, and it needs extending to include `Match host` directives. I couldn't
find any quick fixes on the internet, but if you happen to know of an answer do let me
know.
