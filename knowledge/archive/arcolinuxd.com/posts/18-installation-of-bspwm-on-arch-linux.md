---
title: "Installation of Bspwm on Arch Linux Phase 4"
url: https://www.arcolinuxd.com/18-installation-of-bspwm-on-arch-linux/
date: 2018-09-20 13:45:15
type: post
categories: ["ArchWayDesktop"]
tags: ["arch installation", "archlinux"]
source_site: arcolinuxd.com
---

# Installation of Bspwm on Arch Linux Phase 4

install desktop environment BSPWM ![](https://www.arcolinuxd.com/wp-content/uploads/2018/05/archlinux-bspwm.jpg) Installing bspwm requires only a few commands. Theming and tweaking your Arch Linux system will require more time. All the information about this desktop is here: <https://wiki.archlinux.org/index.php/Bspwm>
    
    
    sudo pacman -S bspwm
    

What you will get is a black screen? Not much not see or press or anything. Everything needs to be configured. We have done this already and we share now our work with you. ArcoLinuxD github is the source 

**In the case of Bspwm we immediately****get the ArcoLinuxD scripts as there is simply nothing to see after installing bspwm and sxhkd.**

Video: <https://youtu.be/3yGRKlemhP4>

We will get our scripts from our github. Change the scripts any way you want. That is the idea. Add lines for extra software. Hashtag out software you do not want. Then run the scripts.
    
    
    sudo pacman -S git
    git clone https://github.com/arcolinuxd/arco-bspwm

Then we have the scripts on our system. You decide what you run or not.

Lateron we will need wget as well
    
    
    sudo pacman -S wget

There is also a folder called **Arch Way**. This folder will contain all the scripts for people who do an Arch Linux installation.

Video: <https://youtu.be/5qU62eT8fJY>
