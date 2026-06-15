---
title: "42 setting icons in dolphin and thunar filemanager - why is thunar in Plasma"
url: https://www.arcolinuxd.com/42-setting-icons-in-dolphin-and-thunar-filemanager-why-is-thunar-in-plasma/
date: 2019-01-17 15:03:24
type: post
categories: ["Plasma"]
tags: ["dolphin", "icons", "thunar"]
source_site: arcolinuxd.com
---

# 42 setting icons in dolphin and thunar filemanager - why is thunar in Plasma

![](https://www.arcolinuxd.com/wp-content/uploads/2019/01/icons-thunar-dolphin.jpeg)

We see a pop-up from discord. It wants to update and asks what to do.

We install the update with:
    
    
    update
    sudo pacman -S discord

We discuss the new arcolinux-mirrorlist-git but it was already up-to-date. The packages are now coming from the new dataserver.

> We forgot to type SKEL to get the new data in from /etc/skel to our own home directory.

Then we **update** the AUR packages with **upall**.

Go to System Settings and navigate to icons.

Do not forget to **apply** it at the bottom.

> Best advice after selecting a new icon theme is to logout and login or even reboot.

**We have two filemanagers.**

**Dolphin** from Plasma - this one is defined from system settings, icons

**Thunar** from Xfce - this one is defined from system settings, Gnome Application Style (GTK)

Thunar is there because of the **workflow** possibilities. We have lots of **custom** **actions** there that we use all the time like comparing with **meld**

> There is one custom action Plasma will never have : open folder as root.

In the video we will set Thunar and Dolphin so that they have the same icon theme. 

Video: <https://youtu.be/nBuZF6fnLW8>
