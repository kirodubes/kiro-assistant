---
title: "How to install virtualbox on a computer with a linux-mainline kernel"
url: https://arcolinux.com/how-to-install-virtualbox-on-a-computer-with-a-linux-mainline-kernel/
date: 2018-10-22 09:39:56
type: post
categories: ["Virtual Machines"]
tags: ["virtual machines"]
source_site: arcolinux.com
---

# How to install virtualbox on a computer with a linux-mainline kernel

![](https://arcolinux.com/wp-content/uploads/2018/10/arcolinux-mate-minimal-virtualbox.jpg)   


Follow this procedure and you will be fine:

  * yay linux-mainline to build the newest kernel from kernel.org ([see article](<https://arcolinux.com/how-to-install-the-linux-mainline-kernel-coming-from-aur/>)) - **install also** the **linux-mainline-headers!**
  * sudo pacman -S virtualbox
  * sudo pacman -S virtualbox-host-dkms
  * update-grub
  * reboot



Video: <https://www.youtube.com/watch?v=6wLefgbwRiA>

  
![](https://arcolinux.com/wp-content/uploads/2018/10/yay-folder-linux-mainline.jpg)
