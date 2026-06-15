---
title: "Clean up your computer and delete the pacman cache"
url: https://arcolinux.com/clean-up-your-computer-and-delete-the-pacman-cache/
date: 2018-12-26 08:24:48
type: post
categories: ["Cleanup", "Pacman"]
tags: ["anydesktop", "cleanup"]
source_site: arcolinux.com
---

# Clean up your computer and delete the pacman cache

![](https://arcolinux.com/wp-content/uploads/2018/12/arcolinux-pacman-scc.jpg)

Type in the terminal
    
    
    man pacman

and start reading.

**Pacman** is **the** **most** **important** command on any Arch Linux based system.  
It is your **Pac** kage **Man** ager.  
Pacman is your application to install and remove packages aka software and so much more.

> [There is always the official Arch Wiki page as well to read.](<https://wiki.archlinux.org/index.php/pacman>)

In this article we want to delete the packages that pacman has downloaded in the past and pacman is caching them in**/var/cache/pacman/pkg/.**

When we build an iso in the project ArcoLinuxB, we use the same command to make sure we get new files in and that we are not using (possibly) corrupted packages.

There is really no reason besides the BYOI project to delete the cache of pacman. You may have your reasons to do so and this is how you do it.

sudo pacman -Scc

You read in the terminal this text. See also in the image.

"Remove packages that are no longer installed from the cache as well  
as currently unused sync databases to free up disk space. When  
pacman downloads packages, it saves them in a cache directory. In  
addition, databases are saved for every sync DB you download from  
and are not deleted even if they are removed from the configuration  
file pacman.conf(5). Use one --clean switch to only remove packages  
that are no longer installed; **use two to remove all files from the**  
**cache**. In both cases, you will have a yes or no option to remove  
packages and/or unused downloaded databases."
