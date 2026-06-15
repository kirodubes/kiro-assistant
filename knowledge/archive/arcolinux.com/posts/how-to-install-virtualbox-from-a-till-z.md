---
title: "How to install VirtualBox from A to Z and learn to use it"
url: https://arcolinux.com/how-to-install-virtualbox-from-a-till-z/
date: 2021-10-21 10:00:56
type: post
categories: ["Pre-installation", "Virtual Machines"]
tags: ["bios"]
source_site: arcolinux.com
---

# How to install VirtualBox from A to Z and learn to use it

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-virtualbox.jpg) 

## How to install VirtualBox

### Option 1 : Calamares

We recommend this option as it is the easiest way to get VirtualBox on your computer.

During the ArcoLinux installation Calamares will provide you the choice to either install:

  1. VirtualBox for a linux kernel
  2. VirtualBox for a linux-lts kernel

![](https://arcolinux.com/wp-content/uploads/2020/06/virtualbox-calamares.png)

### Option 2: Nemesis scripts

Use our scripts to install VirtualBox and many other applications.

Type this in a terminal
    
    
    git clone https://github.com/erikdubois/arcolinux-nemesis

Navigate to the AUR folder and launch the right script. Choose for linux or linux-lts.
    
    
    ./install...

There is an advantage if you run this script.  
It will ensure you **do not see all these messages** when you first boot up VirtualBox.

## _ALWAYS REBOOT AFTER INSTALLING VIRTUALBOX_

### Option 3

Just copy/paste the right code in your terminal and install **manually**.   
Type '**neofetch** ' in your terminal to read what kernel you have.

When you are working on Linux kernel
    
    
    sudo pacman -S virtualbox  
    sudo pacman -S virtualbox-host-modules-arch  
    sudo pacman -S linux-headers

When you are working on Linux-lTS kernel
    
    
    sudo pacman -S virtualbox  
    sudo pacman -S virtualbox-host-dkms  
    sudo pacman -S linux-lts-headers  
    update-grub

When you are working on Linux-ZEN kernel
    
    
    sudo pacman -S virtualbox  
    sudo pacman -S virtualbox-host-dkms  
    sudo pacman -S linux-zen-headers  
    update-grub

When you are working on Linux-HARDENED kernel
    
    
    sudo pacman -S virtualbox  
    sudo pacman -S virtualbox-host-dkms  
    sudo pacman -S linux-hardened-headers  
    update-grub

When you are working on Linux-ANY kernel (xanmod, mainline, next, ...)
    
    
    sudo pacman -S virtualbox  
    sudo pacman -S virtualbox-host-dkms  
    sudo pacman -S linux-....-headers (search for the package)  
    update-grub

##  _ALWAYS REBOOT AFTER INSTALLING VIRTUALBOX_

allow virtualization - Motherboard setting

Have you changed the setting in the motherboard to **allow virtualization**?

[This article tries to make a summary what you need to know about bios and uefi to boot up and install linux.](<https://arcolinux.com/everything-you-need-to-know-about-installing-linux-bios-uefi-motherboard-settings/>)

[You will find all information about bios and uefi in this category. Many examples how to change it on real metal.](<https://arcolinux.com/category/arcolinux/bios-uefi/>)

[![](https://arcolinux.com/wp-content/uploads/2018/04/intel-virtualization-technology-1024x380.jpg)](<https://arcolinux.com/wp-content/uploads/2018/04/intel-virtualization-technology.jpg>)

Video: <https://youtu.be/WOv1Z0UFD1E>

 

GO TO TTY IN VIRTUALBOX

In order to go to the **TTY** in **VirtualBox** you use the

**RIGHT CTRL + F2 till F6**

On real metal we use

**CTRL + ALT + F2 till F6**

SHARE FOLDER BETWEEN HOST AND GUEST

You can **share** a **folder** between the **host** operating system and the **guest** operating system . In this manner you can share files and folders between two operating systems. Alternatives are usb's and cloud services.

**Host** is the operating system (OS) that is running on your computer.

**Guest** is the OS that is running inside virtualbox.

We have added a script to easily and quickly share a folder between the host computer and the guest computer.

We have created an alias for it

**vbm** \- this alias stands for**v** irtual**b** ox**m** ount

It will launch a script called **arcolinux-vbox-share**.

**Only to be used in a virtual box.**

## Actions on the host computer

On the host computer you need to go into the virtual machine settings to be able to**share** a folder and to **AUTOMOUNT** it. 

![](https://arcolinux.com/wp-content/uploads/2020/06/vboxmount.png) 

## Actions on the guest computer

When you have booted up in VirtualBox there are just two things to remember.

1\. Type this in the terminal
    
    
    vbm

2\. **Log out** and**log back in**

**If** you have set the folder to **automount** it will be **present** in the filemanager.  
Dolphin file manager is the exception on the rule. Thunar is present on Plasma.

Video: <https://youtu.be/WIH7BkE-bYQ>

 

Video: <https://youtu.be/kVp2w5waTUw>

 Seeing this - just reboot![](https://arcolinux.com/wp-content/uploads/2018/07/error-vb.png) 

What are my current settings of VirtualBox

Video: <https://youtu.be/zW03Vs2CVZo>

 

Make virtualbox fullscreen  
on tiling window managers

Video: <https://youtu.be/UfC3_K-hx7I>

![](https://arcolinux.com/wp-content/uploads/2021/10/vb-fullscreen.png)

Moving files between

guest and host

Video: <https://youtu.be/YiTaKsRmZeg>

![](https://arcolinux.com/wp-content/uploads/2021/10/file-explorer.jpg)

Give your VirtualBox more video memory  
from 128MB to 256MB

Video: <https://youtu.be/NLsf08bMs9U>

![](https://arcolinux.com/wp-content/uploads/2021/10/vb-videomemory.png)

make the terminals  
transparent in virtual box

Video: <https://www.youtube.com/watch?v=uaC2E0jieI4>

USE snapshot  
to revert back to   
a previous state

Video: <https://youtu.be/oUyDLkPwQu0>

VIRTUalbox on windows 10 proper settings install arcolinuxFollow the video to see what I do to install virtualbox on your W10 machine (1803). Solving the issue of seeing only 32 bits in the dropdown by just rebooting. Creating a template for later - use the proper settings. Installing ArcoLinux.

Video: <https://www.youtube.com/watch?v=DCKnZred-U8>

 

Video: <https://www.youtube.com/watch?v=pXd4K8ZJnf8>

 

VIRTUalbox on windows 10  
another example  
Arcolinux 19.5 and virtual box 6.0.8

Video: <https://youtu.be/5bf0wnPtMAs>

 HOw to use virtualbox -- makeuseof.comDOWNLOAD THEIR PDF HERE. Read all about their way of using virtualbox on their website @ <https://www.makeuseof.com/tag/how-to-use-virtualbox/>Virtualbox only showing 32 bits

Read all about this issue of virtualbox on Windows on this website @  
<http://www.fixedbyvonnie.com/2014/11/virtualbox-showing-32-bit-guest-versions-64-bit-host-os/>

Superuser  
<https://superuser.com/questions/1241956/virtualbox-only-allowing-32-bit-os>

# VirtualBox: Diagnose and fix 'VT-x/AMD-V hardware acceleration' errors

Read all about this issue of virtualbox on Windows on this website @ <https://www.itworld.com/article/2981515/virtualization/virtualbox-diagnose-and-fix-vt-xamd-v-hardware-acceleration-errors.html>

# YOUTUBE PLAYLIST

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS675Lz6kE6JyJMoAkwuJjkA>
