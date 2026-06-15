---
title: "How to dual boot windows (UEFI) and linux and use grub-customizer"
url: https://arcolinux.com/how-to-dual-boot-windows-uefi-and-linux-and-use-grub-customizer/
date: 2018-10-27 23:57:18
type: post
categories: ["Pre-installation"]
tags: ["grub", "windows"]
source_site: arcolinux.com
---

# How to dual boot windows (UEFI) and linux and use grub-customizer

![](https://arcolinux.com/wp-content/uploads/2018/10/windows-linux.png)

DISCLAIMER

ArcoLinux is **NOT** responsible for **ANY LOSS OF DATA** resulting in these actions. We just want to help out and we point you to our Disclaimers page to make sure that you know **YOU ARE RESPONSIBLE FOR YOUR ACTIONS**. <https://arcolinux.info/disclaimer-and-licenses/>

Ran into an issue. Be prepared to completely re-install your system. Make the necessary backup. Use the power of the cloud.

**Our advice is still golden** : just single boot and use different SSD's and a SSD bay to switch operating system.

> Godspeed and good luck.

In this tutorial we will **dual boot between Windows 10 UEFI (1803) and Linux (ArcoLinuxB-Mate-Minimal)**.

It does not matter if I filmed this on virtual box or not. You need to follow the exact same steps, if you want to dual boot on an SSD or a harddisk.

If you want to install linux to your SSD or harddisk then you need these things

  * an working usb stick 3.0 or 3.1 these days of 3GB+
  * an application to write the iso to usb like mintstick or etcher ([more info](<https://arcolinux.info/download>))
  * figure out how to boot from usb on your hardware ([more info](<https://arcolinux.com/category/arcolinux/bios-uefi/>))



We use **grub-customizer** to tell him which partition or which desktop it should **boot** **up** with **by** **default**.

We can also change the **/etc/lightdm/lightdm.conf** so that we can boot up without typing a password. That is the **autologin** option. Suited for desktops, less so for laptops that leave the privacy of your home.

## TIP OR TRICK

You can also **autologin** into **W10** with the use of the application **netplwiz**.

Video: <https://youtu.be/3uuNQ_T_hpk>
