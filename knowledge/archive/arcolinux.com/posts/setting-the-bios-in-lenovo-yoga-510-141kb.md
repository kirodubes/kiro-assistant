---
title: "Setting the bios in Lenovo Yoga 510-141KB"
url: https://arcolinux.com/setting-the-bios-in-lenovo-yoga-510-141kb/
date: 2018-04-29 07:19:21
type: post
categories: ["Bios &amp; Uefi"]
tags: ["bios"]
source_site: arcolinux.com
---

# Setting the bios in Lenovo Yoga 510-141KB

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-lenovo-yoga-510.jpg)   


We investigate how to get inside the bios of this HP computer. It might be a different in every computer. I think it is [this](<https://www3.lenovo.com/be/nl/laptops/yoga/500-series/Yoga-510-14-Intel/p/88YG5000788>) computer. It is a recent computer from 2017. I can only boot from usb to ArcoLinux from it since it is not mine. We can take a look at the bios settings

In our case it is **FN + F2** what we need to get into the bios.

We check 3 things:

  * can we boot from usb
  * is virtualization enabled to be able to have virtualbox later - it was NOT enabled - configuration
  * secure boot



What you see beneath is the bootmenu **FN + F12**. That is needed if you have your usb plugged in and want to boot from USB.

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-lenovo-boot-menu.jpg)   


## I know it is not properly tested installing ArcoLinux all the way. You might need to change more settings. This is as far as I will go on someone else's computer.

Video: <https://www.youtube.com/watch?v=kUsrPeEnwaQ>

  


**SECURE BOOT WAS ENABLED AGAIN AFTER REBOOTING IN THE BIOS AUTOMATICALLY.**
