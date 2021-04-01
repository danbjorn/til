---
created: 2021-01-05
tag: wireguard
title: See who is connected to your Wireguard VPN
---
To see currently connected Wireguard users you can see whether they have completed a handshake recently:

```bash
sudo wg show all latest-handshakes
```

If you just use `wg show` then you get the handshake time in a more human readable manner, but `latest-handshakes` gets you a clean list of "connected yes/no".

