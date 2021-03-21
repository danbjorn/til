---
created: 2021-01-05
tag: wireguard
---
# Enabling Wireguard logging

The default wireguard logging is basically nonexistent which can make debugging hard.
You can however switch extra debugging on with:

```bash
echo 'module wireguard +p' | sudo tee /sys/kernel/debug/dynamic_debug/control
```

To switch it off pass in `-p` instead. It’s pretty verbose so you won't want to leave
it on longer than you need.

It’s still not great but it may give you some clues!

Found here: <https://www.the-digital-life.com/wiki/wireguard-troubleshooting/>
