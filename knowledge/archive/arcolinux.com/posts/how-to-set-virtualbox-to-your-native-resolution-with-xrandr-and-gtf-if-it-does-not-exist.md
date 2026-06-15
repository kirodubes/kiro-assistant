---
title: "How to set virtualbox to your native resolution with xrandr and gtf if it does not exist"
url: https://arcolinux.com/how-to-set-virtualbox-to-your-native-resolution-with-xrandr-and-gtf-if-it-does-not-exist/
date: 2019-01-02 00:09:40
type: post
categories: ["Virtual Machines"]
tags: ["anydesktop", "resolution", "virtual machines"]
source_site: arcolinux.com
---

# How to set virtualbox to your native resolution with xrandr and gtf if it does not exist

![](https://arcolinux.com/wp-content/uploads/2019/01/setscreenresolution.jpg)

Virtual Box was released on 31/12/2018 and they had changed one of their graphics controller settings. Standard we used to have **VboxVGA** and now the standard is set to **VMSVGA.** This might be your issue with Virtualbox 6. Check this link first. 

<https://arcolinux.com/how-to-set-virtualbox-6-the-correct-way-graphical-controller-workflow/>

****

Before we found the above mentioned solution we found a work around with xrandr and gtf.

Even though our solution is solved this remains a valid solution and as a result we will use another graphics controller aka VMSVGA or VMware’s SVGA II graphics adapter.

****

![](https://arcolinux.com/wp-content/uploads/2019/01/vmwarsvga.jpg)

Follow the solution I found in the video. It is now applied on Xmonad. But the desktop does not really matter.

If your resolution is not correct, first check the display manager of your desktop environment. What if your native screen resolution is not there.

> This is a solution for those instances that your native resolution is not among the choices in your display settings

Video: <https://youtu.be/mxLkoPHyas8>
