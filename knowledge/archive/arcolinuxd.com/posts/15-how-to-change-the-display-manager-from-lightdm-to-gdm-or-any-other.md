---
title: "15 How to change the display manager from lightdm to gdm or any other - any desktop"
url: https://www.arcolinuxd.com/15-how-to-change-the-display-manager-from-lightdm-to-gdm-or-any-other/
date: 2018-02-12 07:56:11
type: post
categories: ["AnyDesktop"]
tags: ["anydesktop"]
source_site: arcolinuxd.com
---

# 15 How to change the display manager from lightdm to gdm or any other - any desktop

![](https://www.arcolinuxd.com/wp-content/uploads/2018/02/gdm.jpg)

You can use any display manager or login manager you want. There is no need to change to gdm because you are going to install the desktop gnome... but you can. It is the freedom of choice. And it is even not that hard.

We have chosen for lightdm a few months back when we started with ArcoLinuxD Budgie. Lightdm had proven itself already in ArchLabs and was stable. When we started with Budgie, gdm experienced glitches and decided to go for Lightdm.

It is also an advantage having one display manager for all desktops. That is something you already know. Every display manager will work differently. Have different settings.

How can we change the lightdm display manager to gdm display manager? It only takes two lines
    
    
    sudo pacman -S gdm
    sudo systemctl enable gdm.service -f

Video: <https://youtu.be/R2jgZErXeOI>
