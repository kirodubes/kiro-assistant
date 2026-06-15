---
title: "Changing the panels of xfce the easy way"
url: https://arcolinux.com/changing-the-panels-of-xfce-the-easy-way/
date: 2018-10-16 10:59:29
type: post
categories: ["Menu", "Utilities"]
tags: ["xfce"]
source_site: arcolinux.com
---

# Changing the panels of xfce the easy way

![](https://arcolinux.com/wp-content/uploads/2018/10/xfce4-panel-profiles.jpg)   


The best way is to just follow what I do in this video.

Just know that this application is called xfce4-panel-profiles.

Starting from 18.10 the newer package and its configuration are already installed.

If you want to keep rolling and do not do a clean install then ...

Install both these packages
    
    
    sudo pacman -S arcolinux-xfce4-panel-profiles-git
    yay -S xfce4-panel-profiles

The old application has to go now.
    
    
    sudo pacman -R xfpanel-switch

Video: <https://youtu.be/1n9opkGAzp4>
