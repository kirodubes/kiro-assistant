---
title: "How to fix time-out or slow Arch Linux servers"
url: https://arcolinux.com/how-to-fix-time-out-or-slow-arch-linux-servers/
date: 2018-11-24 14:17:54
type: post
categories: ["Fixes", "Update"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to fix time-out or slow Arch Linux servers

![](https://arcolinux.com/wp-content/uploads/2018/11/mirrorlist-slow.jpg)   


error: failed retrieving file 'extra.db' from mirror.ams1.nl.leaseweb.net : Operation too slow. Less than 1 bytes/sec transferred the last 10 seconds

This is the message we are talking about. You will have a different server from a different country. But these things happen.

Networking can go wrong in so many places.

  * check all cables
  * check all switches, hubs, routers, modems, ...
  * reset all switches, hubs, routers, modems, ...
  * compare with other hardware in house
  * [speedtest](<http://www.speedtest.net>) check or in terminal : **speedtest**



Here we see the issue is a couple of servers that give a time-out.

Even after a **mirror** command the issues prevails.

We edit the file **/etc/pacman.d/mirrorlist** and put a hashtag in front of all the slow servers.

Video: <https://youtu.be/PEylEZz5DEs>
