---
title: "How to completely destroy the content of your disk and start installing with a clean slate"
url: https://arcolinux.com/how-to-completely-destroy-the-content-of-your-disk-and-start-installing-with-a-clean-slate/
date: 2018-12-29 15:15:26
type: post
categories: ["Bios &amp; Uefi", "Cleanup", "Fixes", "Update"]
tags: ["anydesktop", "cleanup"]
source_site: arcolinux.com
---

# How to completely destroy the content of your disk and start installing with a clean slate

BEFORE

![](https://arcolinux.com/wp-content/uploads/2018/12/cleanup-disks-after.jpg)

AFTER

![](https://arcolinux.com/wp-content/uploads/2018/12/cleanup-disks-before.jpg)

This super tip has always been on the installation page of [Arch Linux in Phase 5 ](<https://arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-bios/>) and also [here](<https://arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-uefi/>).

It merits some more attention because it gives you the opportunity to start again

**as if the nvme, ssd or harddisk were just coming out of the shop.**

> All data structures will be deleted including gpt and mbr!

Remember these two commands that can help you when you want to **remove** **everything**.
    
    
    wipefs -a /dev/sda

or
    
    
    sgdisk -Z /dev/sda

Find out what your devices are called with
    
    
    lsblk

and adjust your commands accordingly.

If you get stuck for a reason, see if **gparted** can help you.

Video: <https://youtu.be/bAcoEoK7xeI>
