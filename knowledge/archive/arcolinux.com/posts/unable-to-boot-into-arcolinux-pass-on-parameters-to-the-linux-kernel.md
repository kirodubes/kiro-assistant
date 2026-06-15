---
title: "Unable to boot into ArcoLinux - pass on parameters to the Linux kernel"
url: https://arcolinux.com/unable-to-boot-into-arcolinux-pass-on-parameters-to-the-linux-kernel/
date: 2021-01-03 16:45:24
type: post
categories: ["Grub", "Kernel", "Pre-installation"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# Unable to boot into ArcoLinux - pass on parameters to the Linux kernel

Use nomodeset to avoid a black screen   
booting up ArcoLinux  
BIOS

Video: <https://youtu.be/MebaBErUoqI>

> The iso may contain already such an option  
> Use TAB or E to edit

![](https://arcolinux.com/wp-content/uploads/2021/01/nomodeset.png)

Use nomodeset to avoid a black screen  
booting up ArcoLinux  
UEFI

> Use TAB or E to edit and add the parameters

![](https://arcolinux.com/wp-content/uploads/2021/01/efi-nomodeset.png)

Video: <https://youtu.be/hBgKn-kpOvM>

There are other options you can add besides **nomodeset**

  * nouveau.modeset=0 (this is a zero) or 1 (false = 0 and true = 1)
  * i915.modeset=0 or 1
  * radeon.modeset=0 or 1
  * modprobe.blacklist=nouveau nvidia



There are many other paramaters to try out if you are still stuck.

![](https://arcolinux.com/wp-content/uploads/2021/01/gentoo1.jpg)![](https://arcolinux.com/wp-content/uploads/2021/01/gentoo2.jpg)

Type in '**dmesg** ' and '**journalctl** ' in the terminal.

Try to analyze what is going wrong.

This list has been obtained from Gentoo wiki. I did not test if they work on Arch Linux or ArcoLinux.   
You are welcome to try. May it solve your issue.

<https://wiki.gentoo.org/wiki/Handbook:AMD64/Blocks/Booting>

Video: <https://youtu.be/kOnGifVXHuc>
