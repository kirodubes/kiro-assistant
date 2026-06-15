---
title: "Fix for kernel panic when dualbooting with intel-ucode or amd-ucode"
url: https://arcolinux.com/fix-for-kernel-panic-when-dualbooting-with-intel-ucode-or-amd-ucode/
date: 2020-01-07 16:45:47
type: post
categories: ["Fixes", "Post-installation", "Update"]
source_site: arcolinux.com
---

# Fix for kernel panic when dualbooting with intel-ucode or amd-ucode

![](https://arcolinux.com/wp-content/uploads/2020/01/dual-boot.jpg)

Only for dual booters  
AND  
only if intel-ucode or amd-cude is installed

Single booting  
no amd-ucode or intel-ucode installed  
nothing to do

Single booting   
amd-ucode or intel-ucode installed  
nothing to do

Regularly check the bugs website of Arch for progress

[grub-mkconfig not including intel-ucode.img on any entry menu other than the main one](<https://bugs.archlinux.org/task/60999?string=grub+microcode&project=1&type%5B0%5D=&sev%5B0%5D=&pri%5B0%5D=&due%5B0%5D=&reported%5B0%5D=&cat%5B0%5D=&status%5B0%5D=open&percent%5B0%5D=&opened=&dev=&closed=&duedatefrom=&duedateto=&changedfrom=&changedto=&openedfrom=&openedto=&closedfrom=&closedto=>)

As always you can choose what to install. Either you **install** intel-ucode or amd-ucode**or you do not**.  
[We point you to the Arch wiki and let you decide what to do.](<https://wiki.archlinux.org/index.php/Microcode>)

In Calamares you are given the option. It is up to you to choose.

**But remember that if you intend to dual-boot you will have to fix the grub manually IF you installed intel-ucode or amd-ucode.**

We assume now that you have installed two ArcoLinux systems on one harddisk/ssd.

We boot up from the first line in your grub. That is always going to work.

Edit this file with an editor or via the terminal
    
    
    /boot/grub/grub.cfg

We make sure that the lines **between** **begin** of **30_os-prober** and **end** of **30_os-prober** are complete.

**initrd /boot/intel-ucode.img**

need to change to

**initrd /boot/intel-ucode.img /boot/initramfs-linux.img**

There are 3 instances to change.

**Never change the fall-back line - that is working just fine.**

If you have installed **linux-lts** you will have a **initramfs-linux-lts.img**. Use that name in grub.cfg.

never update your grub now

it will overwrite your manual work

Video: <https://youtu.be/F85jUDHiU-0>
