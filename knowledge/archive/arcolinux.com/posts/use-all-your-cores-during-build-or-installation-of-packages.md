---
title: "Use all your cores during build or installation of packages"
url: https://arcolinux.com/use-all-your-cores-during-build-or-installation-of-packages/
date: 2018-12-28 16:10:27
type: post
categories: ["Fixes", "Manage software", "Post-installation"]
tags: ["fix"]
source_site: arcolinux.com
---

# Use all your cores during build or installation of packages

![](https://arcolinux.com/wp-content/uploads/2018/02/use-all-cores.jpg)

> We have made sure that during the installation of Calamares we configure your system to use all cores.
> 
> Only relevant if you go to phase 5 and do an Arch Linux installation

 

We have explained in[ this article](<https://arcolinux.com/how-to-speed-up-your-computer-during-building/>) that we can improve the build time of applications considerably by using all cores of your processor.

This time we are on ArchMerge 6.5.1 and we have added a script to change your makepkg.conf file to the correct maximum number of cores.

The application **arcolinux-bin-git** will provide the files. You can find this script here :
    
    
    ~/.bin/main/000-use-all-cores-makepkg-conf-vx.sh

It applies to any and all desktops as this is a **general** **Arch** **Linux** **setting**.

**In the video you will see that IF you do nothing ARCH will use 1 core while I have 4 cores available. If you have 8 cores, it will use just 1 core as well.**

We use the application "htop" to show you that and the application "Polybar" to install and build.

Video: <https://youtu.be/N9IKjXJkFy0>

The script used to be in ~/.openbox/scripts. It moved to ~/.bin
