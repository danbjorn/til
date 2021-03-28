---
created: 2021-03-26
tag: ssh
title: Slow SSH connections caused by broken IPv6 records
---
We've been puzzling over slow SSH connections to a couple of our servers. Once you're
logged in it was fine, but the initial connection would take a good fifteen seconds,
which feels like aeons.

Running SSH with `-vv` to get some extra debug output, we could see that the process
would pause on the following line (domain changed to protect the innocent):

```
debug2: resolving "blargh.com" port 22
```

This seemed odd as `dig blargh.com` returned immediately. Why would it be hanging on the
resolution of the hostname?

After some digging I stumbled across
[this two year old comment](https://jrs-s.net/2017/07/01/slow-ssh-logins/#div-comment-5469)
on a four year old blog post:

> Yet another one... DNS for the server has AAAA and A records. Client OS thinks it's
> got IPv6 routing but actually it hasn't – but you have to wait for the IPv6 attempt to
> fail before it falls back to "legacy" IPv4.

This turned out to be it. `dig blargh.com` would return a full answer, but
`dig blargh.com AAAA` returned a `CNAME` to a record that didn't have a `AAAA` record.
To put it another way, it had a IPv6 record, but it didn't actually resolve to an
address.

This appears to severely confuse the SSH client. It sees the `AAAA` record and tries to
resolve it, happily waiting until it fails. It then tries the `A` record, which works
instantly. I'm not sure why it takes so long for the hunt for an IPv6 address to fail,
let me know if you figure it out.

The resolution is straightforward. Ideally, you fix the DNS issue itself - either add
the missing IPv6 record, or remove the broken `CNAME`. If this isn't possible, then you
can tell the client to connect only using IPv4 with `-4`:

```
ssh -4 blargh.com
```

Alternatively you can add the following to your `~/.ssh/config/`:

```
Host blargh.com
    AddressFamily inet
```

If you wish to force IPv6 you can use `-6` and `AddressFamily inet6`.
