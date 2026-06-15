---
title: "Using qbittorrent to download the ArcoLinux and ArcoLinuxD iso's"
url: https://arcolinux.com/using-qbittorrent-to-download-the-arcolinux-and-arcolinuxd-isos/
date: 2019-01-18 10:35:30
type: post
categories: ["Internet"]
tags: ["torrent"]
source_site: arcolinux.com
---

# Using qbittorrent to download the ArcoLinux and ArcoLinuxD iso's

![](https://arcolinux.com/wp-content/uploads/2019/01/qbittorrent-seeding.jpg)

Since January we have a data server where we can host our iso's and seed from there. [See article here](<https://arcolinux.info/arcolinux-acquires-high-speed-data-server/>).

We have started with ArcoLinux iso and ArcoLinuxD iso and will evaluate how that goes.

On the [download page](<https://arcolinux.info/download/>) you will see there is a third option to download the iso now:

> Torrents

Click on the links on our download page and get the torrents from linuxtracker.org itself.

While we were testing out the torrents, we made a choice about our default torrent application.

> We have chosen Qbittorrent over transmission.

That is why we have a script in your home folder (if you updated and 'skelled').

**~/.bin/stay-rolling/19.1-to-19.2/**

It will remove transmission and install qbittorrent.

Next iso's will contain only qbittorrent.

As you can see in the picture above we have themed it to fall inline with the Arc gtk theme. To have this nice theme you need to have a clean install of 19.01 or you should follow the keep rolling video.

Video: <https://youtu.be/GWhwYd1M7dM>
