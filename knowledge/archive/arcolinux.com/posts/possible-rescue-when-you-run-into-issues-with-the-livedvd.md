---
title: "Possible rescue when you run into issues with the livedvd"
url: https://arcolinux.com/possible-rescue-when-you-run-into-issues-with-the-livedvd/
date: 2021-04-04 11:09:12
type: post
categories: ["Fixes"]
source_site: arcolinux.com
---

# Possible rescue when you run into issues with the livedvd

![](https://arcolinux.com/wp-content/uploads/2019/09/livedvd.jpg)

You can login via **TTY** in ArcoLinux - **No** **password** required

Bare metal = CTRL + ALT + F2 till F6

VirtualBox = right CTRL + F2 till F6

Then you need to update the **pacman database** with
    
    
    sudo pacman -Syyu

Then you can install and remove packages with pacman.

With **df** you can see that we gave you 10GB of cowspace or **space** to install applications.

We also show you how to stop and start lightdm.
    
    
    sudo systemctl stop sddm.service
    
    
    sudo systemcl start sddm.service

We hope this will give more room to 'fix things' on your hardware.

The '**rip** ' alias gives you an overview of all the packages that were installed last.

Video: <https://youtu.be/Hy4IRy5eFbw>
