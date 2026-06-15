---
title: "How to delete Linux from your Windows machine (MBR) and delete grub"
url: https://arcolinux.com/how-to-delete-linux-from-your-windows-machine-mbr-and-delete-grub/
date: 2018-10-27 19:18:24
type: post
categories: ["Post-installation"]
tags: ["grub", "windows"]
source_site: arcolinux.com
---

# How to delete Linux from your Windows machine (MBR) and delete grub

![](https://arcolinux.com/wp-content/uploads/2018/10/windows-linux.png)

 

DISCLAIMER

ArcoLinux is **NOT** responsible for **ANY LOSS OF DATA** resulting in these actions. We just want to help out and we point you to our Disclaimers page to make sure that you know **YOU ARE RESPONSIBLE FOR YOUR ACTIONS**. <https://arcolinux.info/disclaimer-and-licenses/>

Ran into an issue. Be prepared to completely re-install your system. Make the necessary backup. Use the power of the cloud.

**Our advice is still golden** : just single boot and use different SSD's and a SSD bay to switch operating system.

> Godspeed and good luck.

In this tutorial we are using the **virtualbox (MBR)** of a **dual boot between Windows 10 (1803) and Linux (ArcoLinuxB-Mate-Minimal)**.

It does not matter if I filmed this on virtual box or not. You need to follow the exact same steps, if you want to delete Linux from your Windows computer.

If you want to get your **Windows** **back and delete Linux** , you will need to burn the Windows iso to a usb. In order to do that, you need these things

  * a Windows iso ([download here](<https://www.microsoft.com/en-us/software-download/windows10ISO>))
  * a working usb stick 3.0 or 3.1 these days of 3GB+
  * an application to write the iso to usb like woeusb (Linux) or [Rufus](<https://rufus.ie/>) (Windows) or the Microsoft Creation tool ([MCT](<https://www.microsoft.com/en-us/software-download/windows10ISO>)) from Microsoft. We recommend **MCT**.
  * figure out how to boot from usb on your hardware ([more info](<https://arcolinux.com/category/arcolinux/bios-uefi/>))



We use **the Windows iso/usb** to boot up and repair the **MBR.**

These are the commands we used - the first one is the one that fixed the MBR.
    
    
    bootrec /FixMbr
    bootrec /FixBoot
    bootrec /ScanOs
    bootrec /RebuildBcd

More information can be found here :

<https://neosmart.net/wiki/fix-mbr/>

Video: <https://www.youtube.com/watch?v=YO70ZrY3Jds>
