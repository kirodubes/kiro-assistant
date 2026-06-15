---
title: "Installation of i3 on Arch Linux Phase 4"
url: https://www.arcolinuxd.com/12-installation-of-i3-on-arch-linux-phase-4/
date: 2020-11-26 14:38:05
type: post
categories: ["ArchWayDesktop"]
tags: ["arch installation", "archlinux", "tty"]
source_site: arcolinuxd.com
---

# Installation of i3 on Arch Linux Phase 4

install desktop environmentI3wm![](https://www.arcolinuxd.com/wp-content/uploads/2020/11/archlinux-i3-gaps.jpg)

Installing i3 requires only a few commands. Theming and tweaking your Arch Linux system will require more time. All the information about this desktop is here:

<https://wiki.archlinux.org/index.php/i3>
    
    
    sudo pacman -S i3-gaps  
    sudo pacman -S i3status  
    sudo pacman -S i3lock

If you want you can **experiment** later with i3-gaps-next-git, i3-gaps-rounded-git and even more.

## You can always fall back on the scripts of our github.

> <https://github.com/arcolinuxd/arco-i3>

Video: <https://youtu.be/K7PEk-YHYRA>

[Original video : Arch Linux : 42 Installing i3wm next gaps and adding spices of ArcoLinux to i3](<https://youtu.be/mBpJqqkke9U>)

[Original video : Arch Linux : 43 Arch Linux i3wm seasoned with Arco spices - Phase 4 - overview](<https://youtu.be/hKJI9ifEC7s>)

## Tip

To set our keyboard we may use [setxbmap](<https://wiki.archlinux.org/index.php/Keyboard_configuration_in_Xorg#Using_setxkbmap >) as well.
    
    
    setxkbmap -model pc104 -layout be

Or in short
    
    
    setxkbmap be

## Tip

We install **yay-bin** and we install **autotiling**.

We decide which package to install for autotiling.

## Tip

If you want to have an AUR helper during TTY, you can check out this article.

<https://www.arcolinuxd.com/get-your-aur-helpers-in-on-any-arch-linux-based-system/>

## Tip

We install **dmenu** to have a menu to launch applications.
    
    
    sudo pacman -S dmenu

## Tip

**Termite** is installed. We want to make the font bigger so you can read it better.  
We show you how in the video.

## Tip

Get the manpages in with
    
    
    sudo pacman -S man-pages

Original look of i3 gaps  
No theming or tweaking

![](https://www.arcolinuxd.com/wp-content/uploads/2018/10/standard-i3-screen.jpg)
