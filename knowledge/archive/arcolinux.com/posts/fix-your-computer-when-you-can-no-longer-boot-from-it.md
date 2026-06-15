---
title: "Fix your computer when you can no longer boot from it"
url: https://arcolinux.com/fix-your-computer-when-you-can-no-longer-boot-from-it/
date: 2018-04-15 11:42:17
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fix your computer when you can no longer boot from it

![](https://arcolinux.com/wp-content/uploads/2018/04/archlinux-arch-chroot.jpg)   


THIS APPLIES TO ALL ARCH LINUX BASED DISTRO'S

Changing root is commonly done for performing system maintenance on systems where booting and/or logging in is no longer possible. Common examples are:

  * Reinstalling the [bootloader](<https://wiki.archlinux.org/index.php/Bootloader> "Bootloader").
  * Rebuilding the [initramfs image](<https://wiki.archlinux.org/index.php/Mkinitcpio> "Mkinitcpio").
  * Upgrading or [downgrading packages](<https://wiki.archlinux.org/index.php/Downgrading_packages> "Downgrading packages").
  * Resetting a [forgotten password](<https://wiki.archlinux.org/index.php/Password_recovery> "Password recovery").
  * or just when you broke your system and can no longer boot.



Then we mount the partitions we need and undo whatever broke your system.
    
    
    loadkeys be-latin1
    mount /dev/sda3 /mnt
    mount /dev/sda1 /mnt/boot
    arch-chroot /mnt

Video: <https://youtu.be/zkGzNVV4l7Q>
