---
title: "20 Using xmobar on Xmonad - discussing the system icons"
url: https://www.arcolinuxd.com/20-using-xmobar-on-xmonad-discussing-the-system-icons/
date: 2019-03-05 12:39:20
type: post
categories: ["Xmonad"]
source_site: arcolinuxd.com
---

# 20 Using xmobar on Xmonad - discussing the system icons

![](https://www.arcolinuxd.com/wp-content/uploads/2019/03/xmonad-xmobar-stalonetray.jpg)

You can install a different bar in xmonad other than polybar.

Xmobar is an alternative bar to use. There are others out there.

As always check your arch wiki and read the text.

<https://wiki.archlinux.org/index.php/Xmobar>

Then we install this xmobar with[ the help of this article](<https://www.arcolinuxd.com/19-how-to-change-to-the-xmobar-on-xmonad-instead-of-polybar/>).

We show you how xmobar looks and talk about the system icons.

  * bluetooth
  * clipboard
  * network applet
  * pamac tray icon
  * variety
  * volume
  * time
  * logout



The more software you install the more icons you will see like

  * discord
  * telegram
  * dropbox
  * insync
  * flameshot
  * ...



The video attempts to show you that in many case you do NOT need an icon to do your work and sometimes you do need the icon to set something the way you like.

## Option 1

Reinstall the polybar and set up everything the way you want and only then switch to xmobar.
    
    
    sudo pacman -S arcolinux-xmonad-polybar-git 

switch back later to
    
    
    sudo pacman -S arcolinux-xmonad-xmobar-git

## Option 2

Install **stalonetray** and set your applications that way and then kill it.
    
    
    sudo pacman -S stalonetray

The idea is to keep the xmobar clean and stable - meaning without system icons.

We have provided a configuration file for xmobar in your home folder.

It is designed to be big and not themed at all.

You can see stalonetray on the image in right window in the middle.

It is NOT meant to be there permanently.

> Set your application and stop using stalonetray is our message to you.

Video: <https://www.youtube.com/watch?v=Lfhyt6wvaHE>
