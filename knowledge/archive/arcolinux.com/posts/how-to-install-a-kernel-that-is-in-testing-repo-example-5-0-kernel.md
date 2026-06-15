---
title: "How to install a kernel that is in testing repo - example 5.0 kernel"
url: https://arcolinux.com/how-to-install-a-kernel-that-is-in-testing-repo-example-5-0-kernel/
date: 2019-03-05 09:47:06
type: post
categories: ["Kernel"]
tags: ["kernel"]
source_site: arcolinux.com
---

# How to install a kernel that is in testing repo - example 5.0 kernel

![](https://arcolinux.com/wp-content/uploads/2019/03/linux-kernel-5.jpg)

You can install the latest kernel any time BUT the most interesting time to do so is just prior to a clean install.

Why?

You have put your configs and files online or on your external harddisk and IF something might happen (not saying it will) then nothing is lost since you wanted to clean install anyway.

You have learned that the kernel might not be right for your hardware.

Activate the **testing** repo in /etc/pacman.conf.

Update your system so the testing repo is added and then install linux

**sudo pacman -S linux**

You may see things obstructing the installation.

Get rid of them with **sudo pacman -Rs** ... and reboot

I totally agree that numbers are unimportant.

We expect a lot from a 5.0 release being on 4.20.13 but that is not the case.

Just to demonstrate how unimportant numbers are, I change the /etc/lsb-release of ArcoLinux as you can see in the image.

Video: <https://youtu.be/g6gf6UnOrvk>

Video: <https://www.youtube.com/watch?v=wMxIaUZGFx4>
