---
title: "How to fix any Arch Linux based system like ArcoLinux, Antergos, Manjaro, ..."
url: https://arcolinux.com/how-to-fix-any-arch-linux-based-system-like-arcolinux-antergos-manjaro/
date: 2018-04-27 11:41:07
type: post
categories: ["Fixes", "Lightdm", "Nvidia"]
tags: ["fix", "nvidia"]
source_site: arcolinux.com
---

# How to fix any Arch Linux based system like ArcoLinux, Antergos, Manjaro, ...

We concentrate all our arch-chroot information in this article.  
<https://www.arcolinuxd.com/10-use-the-power-of-arch-chroot-when-your-computer-crashes/>

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-failed-to-display-lightdm.jpg)

THIS PROCEDURE IS THE SAME ON ALL ARCH BASED SYSTEMS

The goal of this article is to show you an **alternative** **way** to **fix** your computer when it is **broken**.

[In this article](<https://arcolinux.com/how-to-install-the-nvidia-driver-and-how-to-fix-the-system-if-it-breaks/>) we have deliberately broken our system in order to teach you **TTY**. That is another way to fix your computer. **But sometimes you can not even get into the TTY**.

You can always apply this solution - **ALWAYS**.

It is actually part of the installation procedure from Arch Linux and that tutorial can be found [here](<https://arcolinuxd.com/10-use-the-power-of-arch-chroot-when-your-computer-crashes/>).

**First** we **break** our system. All I need to do is install the **wrong** **nvidia** **drivers** and we end up in a black screen.
    
    
    sudo pacman -S nvidia-340xx

I hard reboot my computer and press **F8** to get into my boot manager and I will boot up from the UEFI line. You need to find your keyboard shortcut to get into your setup system. Google "keyboard shortcut bios uefi" and your computer brand.

With **lsblk** I analyze what my root is or "/".

I will have to mount /dev/sda2

Since I have azerty I have to type one line more
    
    
    loadkeys be-latin1
    mount /dev/sda2 /mnt
    arch-chroot /mnt

No need to type sudo now - we are already root.
    
    
    pacman -R nvidia-340xx
    exit
    umount -a
    reboot

The fix we do here will not help you  
you need to investigate what crashed your system  
and undo it

This is a controlled crash. Often you can not remember what you did or what you installed or why it is crashing.

It might help if you checked these files (if you can still reach them)

  * .bash_history in your home folder
  * .xsession-errors might display something
  * dmesg in the terminal



Video: <https://youtu.be/BXbSGh8uhRg>
