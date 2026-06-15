---
title: "Installation of Awesome on Arch Linux Phase 4"
url: https://www.arcolinuxd.com/13-installation-of-awesome-on-arch-linux-phase-4/
date: 2020-11-29 13:00:37
type: post
categories: ["ArchWayDesktop"]
tags: ["arch installation", "archlinux"]
source_site: arcolinuxd.com
---

# Installation of Awesome on Arch Linux Phase 4

install desktop environment AWESOME ![](https://www.arcolinuxd.com/wp-content/uploads/2020/11/archlinux-awesome-original.jpg)

Installing **Awesome** requires only one package. Theming and tweaking your Arch Linux system will require more time, more configs and more packages. All the information about this desktop is here: [https://wiki.archlinux.org/index.php/awesome.](<https://wiki.archlinux.org/index.php/awesome>)  
As the Wiki suggests we create a directory and copy/paste the rc.lua there.

Then we install Awesome:
    
    
    sudo pacman -S awesome

Since our goal is to get the **ArcoLinux** **config** in with our **ArcoLinux** **Spices** application we also install
    
    
    sudo pacman -S vicious

In the video we wanted to use the "[man mkdir](<https://wiki.archlinux.org/index.php/man_page>)". First we need to install the packages:
    
    
    sudo pacman -S man-pages man-db mandoc

In the video we want to have a terminal. Since Xterm is the standard terminal on Awesome, we will install it.
    
    
    sudo pacman -S xterm

## If the awesome menu is open, you can only access the menu.

## Close it with ESCAPE.

Video: <https://youtu.be/hb1cgosC0Us>

In the next video we will install the [ArcoLinux Spices](<https://arcolinux.info/download/arcolinux-spices-application/>) application.

There are [many tutorials](<https://www.arcolinuxd.com/category/arch-way/spice-up-arch/>) about this particular applicaton.

Let us install some more packages we might need.
    
    
    sudo pacman -S rxvt-unicode xterm termite thunar firefox
    
    
    sudo pacman -S awesome vicious

Awesome and vicious were already in previous video.

Since we created a new virtual machine I go over the motions of installing awesome once more.

**Super + Enter** opens up **xterm** (if installed).

We launch **firefox** and download the ArcoLinux Spices. Then we will install the [ArcoLinux Spices](<https://arcolinux.info/download/arcolinux-spices-application/>) application.
    
    
    sudo pacman -U arcolinux-spices...

We launch the application with sudo.
    
    
    sudo arcolinux-spices...

**Except the last one.**

We run the command again but **without sudo**.
    
    
    arcolinux-spices

We use the ArcoLinux .bashrc and load it with **source**. All the aliases will now work.

Then we get the awesome configuration in.
    
    
    sudo pacman -S arcolinux-awesome-git

Skel will work. It will copy the ArcoLinux configuration to your home directory.

To keep the .bashrc, we install this package:
    
    
    sudo pacman -S arcolinux-root-git

Video: <https://youtu.be/fVhkIiU9_JY>
