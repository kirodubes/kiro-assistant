---
title: "How to fix virtualbox freezing up on kernel 4.17.2 - June 2018"
url: https://arcolinux.com/how-to-fix-virtualbox-freezing-up-on-kernel-4-17-2-june-2018/
date: 2018-06-26 10:22:23
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to fix virtualbox freezing up on kernel 4.17.2 - June 2018

![](https://arcolinux.com/wp-content/uploads/2018/06/ArcoLinuxB-Plasma-virtualbox-linux-lts_20180626_102116.jpg)This solution is interesting **now** **June** **2018** but will be void in the future. Updates for either VirtualBox and or the kernel to solve the freezing issue will be coming soon. 

**Updating from kernel  
4.16.2 to 4.17.2   
gives us issues**

We suspect the kernel and the Virtualbox additions are no longer compatible and the virtualbox additions need to be updated.

Extra interesting topics in the video

  * [neofetch issue explained again](<https://arcolinux.com/how-to-fix-the-neofetch-logo-after-updating-neofetch-to-version-5/>)
  * [lsb-release fix also explained here](<https://arcolinux.com/how-to-fix-the-logo-of-neofetch-after-a-lsb-release-update/>)
  * how to install the linux-lts kernel
  * how to get to tty in virtualbox - CTRL + F2 or F3 or ...
  * how to install the newest kernel again



In the video I say it is a kernel issue... it is more a virtualbox issue. We actually need updates for VirtualBox to be able to work on the latest kernel.

Video: <https://www.youtube.com/watch?v=OF1NLCwBVg0>

# Alternative solution - tested on ArcoLinuxB Openbox

Edit **/etc/pacman.conf** and add this line
    
    
    IgnorePkg   =   linux virtualbox-guest-modules-arch

**And then do your updates.**
