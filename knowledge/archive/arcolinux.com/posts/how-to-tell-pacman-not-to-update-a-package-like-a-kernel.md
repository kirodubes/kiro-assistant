---
title: "How to tell pacman not to update a package like a kernel"
url: https://arcolinux.com/how-to-tell-pacman-not-to-update-a-package-like-a-kernel/
date: 2020-04-09 10:36:08
type: post
categories: ["Kernel", "Pacman"]
source_site: arcolinux.com
---

# How to tell pacman not to update a package like a kernel

![](https://arcolinux.com/wp-content/uploads/2020/04/kernelfix.jpg)

Open up the /etc/pacman.conf file and add the packages to the line where it says

#IgnorePkg =

Delete the # and save it.

You can also ignore packages like mate, gnome etc.

Video: <https://youtu.be/wB6F9xXyfYE>
