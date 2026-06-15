---
title: "Get AUR helpers for any Arch Linux based system"
url: https://www.arcolinuxd.com/get-your-aur-helpers-in-on-any-arch-linux-based-system/
date: 2019-11-25 08:42:53
type: post
categories: ["ArchWayUtils"]
tags: ["archlinux", "tty"]
source_site: arcolinuxd.com
---

# Get AUR helpers for any Arch Linux based system

![](https://www.arcolinuxd.com/wp-content/uploads/2018/10/archlinux-yay-helper.jpg)

[AUR helpers](<https://wiki.archlinux.org/index.php/AUR_helpers>) will come and go. We have had our fair share already - packer and yaourt.

We have Y**ay** and **Trizen** to help us install applications from the Arch User Repository or AUR.

Installing in a desktop environment

Use the snapshot from AUR

Video: <https://www.youtube.com/watch?v=weJNQNfjdeI>

Installing in a terminal or TTY

The **easiest** **way** to get the files you need to build a package from AUR is via

**Git clone** the url

You just need to know the url.

<https://aur.archlinux.org/packages/yay-bin/>
    
    
    git clone https://aur.archlinux.org/yay-bin.git

Then we make the package with
    
    
    makepkg

and install it with
    
    
    sudo pacman -U yay-bin...

Video: <https://youtu.be/K7PEk-YHYRA?t=2243>

## **This is the more difficult way but will work just fine too.**

**Instead of getting all the files with git clone** we get just one - the **PKGBUILD**. That does **not** work for every package.

Sometimes we do **not** have a **desktop** environment.

> So know your shortcuts.
> 
> CTRL + ALT + F2 or F3 ... will give you the TTY
> 
> Right CTRL + F2 or F3 ... will give you the TTY on VirtualBox

First we figure out the url of the PKGBUILD. - plain!!

<https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=yay-bin>

Use **wget** or **curl** to get the PKGBUILD.

wget <https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=yay> -O PKGBUILD

Then make the package using **makepkg.**

Then we install the created package with
    
    
    sudo pacman -U ...

Video: <https://youtu.be/uCUAfuLcYMs>

Use the ArcoLinux repo  
Use the ArcoLinux Spices Application

When you are moving to **Phase 5** (installing Arch Linux the Arch Way) and you want to install packages from ArcoLinux, you will need the [ArcoLinux Spices Application](<https://arcolinux.info/download/arcolinux-spices-application/>).

[Many videos have been created to show you how it is done. You can see them all here.](<https://www.arcolinuxd.com/category/arch-way/spice-up-arch/>)

## Why would you add repos of ArcoLinux to a vanilla Arch installation?

  * install **yay** and **trizen** from the ArcoLinux repo (just another alternative to get AUR helpers in)
  * save time and energy
  * you want to have the config of i3, bspwm, awesome, xmonad, ...
  * you want the conkies of ArcoLinux
  * you want the many colored Arc themes
  * ...



We call these downloads and installations on Arch Linux

> **Getting the spices from ArcoLinux**

Search for the word "spice" on [**our youtube channel**](<https://www.youtube.com/erikdubois>) to learn more.
