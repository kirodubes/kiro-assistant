---
title: "Installed an LTS iso - how to get the linux kernel from there"
url: https://arcolinux.com/installed-an-lts-iso-how-to-get-the-linux-kernel-from-there/
date: 2019-07-20 08:21:31
type: post
categories: ["Post-installation"]
source_site: arcolinux.com
---

# Installed an LTS iso - how to get the linux kernel from there

![](https://arcolinux.com/wp-content/uploads/2019/07/delete-lts-kernel.jpg)

In the future we will see how we build our iso's but today July 2019 the linux kernel is on the iso as fallback and your linux-lts is doing all the work.

If you want to get rid of the linux-lts (often because part of your hardware is unsupported) you can delete it, using one of our scripts
    
    
    /home/$USER/.bin/main/delete-lts-kernel-v3.sh

That will delete the linux-lts kernel and the linux kernel will take over.

https://youtu.be/_iboUzPFUA0

Video: <https://youtu.be/_iboUzPFUA0>
