---
title: "How to install Samba on any ArcoLinux system"
url: https://arcolinux.com/how-to-install-samba-on-any-arcolinux-system/
date: 2021-04-03 14:20:26
type: post
categories: ["Fixes", "Must read", "Samba", "Utilities"]
tags: ["samba"]
source_site: arcolinux.com
---

# How to install Samba on any ArcoLinux system

# [Samba - arch wiki](<https://wiki.archlinux.org/index.php/samba>)

# Quick and easy

OPTION 1  
use the scripts

![](https://arcolinux.com/wp-content/uploads/2021/04/samba-scripts.jpg)

Use the scripts in your home directory provided by arcolinux-bin-git.

Run script 1, 2 and 3.

Evaluate what happens to your system and change it if needed.

**This smb.conf is different as the one in the arcolinux-meta-plasma.  
There are also other examples in /etc/samba folder.**  
**Compare and create your own.**

OPTION 2  
Install the meta package

Install the meta package.
    
    
    sudo pacman -S arcolinux-meta-samba

Most of the technical steps have been taken care.

Create a user and give the user a password
    
    
    sudo smbpasswd -a erik

Now give the user a password.

Edit **/etc/samba/smb.conf** to your liking. You can use the alias **nsamba** to edit it.

In the video we create a folder called "**SHARED** " in your home folder and we make it accessible to others.

**This smb.conf is different as the one in the .bin/main/samba folder.  
There are also other examples in /etc/samba folder.**  
**Compare and create your own.**

Video: <https://youtu.be/9qsTn6PhKh4>

EXTRA OPTION PER FILEMANAGER / DESKTOP  
Install the meta package

Depending on the desktop you can install an extra package to quickly share a folder with the right mouse click or some other way. 
    
    
    sudo pacman -S --noconfirm --needed nemo-share
    sudo pacman -S --noconfirm --needed nautilus-share
    sudo pacman -S --noconfirm --needed caja-share
    sudo pacman -S --noconfirm --needed kdenetwork-filesharing
    sudo pacman -S --noconfirm --needed thunar-shares-plugin

When you install the arcolinux-meta-samba package you will see the possible options at the end.

![](https://arcolinux.com/wp-content/uploads/2021/04/smb-installation.jpg)
