---
title: "Adding jgmenu to your openbox system"
url: https://www.arcolinuxd.com/adding-jgmenu-to-your-openbox-system/
date: 2024-03-01 06:33:15
type: post
categories: ["Openbox"]
source_site: arcolinuxd.com
---

# Adding jgmenu to your openbox system

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/ArcoLinux-openbox-jgmenu_2018-06-24_09-56-42.jpg)![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/jgmenu.jpg)

Jgmenu is an X11 menu intended to be used with Openbox and Tint2.

**If you miss a "start button and menu" in your Openbox system, Jgmenu can be a solution.**

We install it with
    
    
    sudo pacman -S jgmenu

Then we need to add it to our tint2 menu with a few steps. We show you how in the video.

Video: <https://youtu.be/kzVgTp_9CqI>

Setting up **Jgmenu** is very **intuitive** IF you know how to first get the configuration file.  
Type in the terminal this command
    
    
    jgmenu init

It will create files and folders in your ~/.config/.

The file ~/.config/jgmenu/jgmenurc is the most important one.

We edit this one to change our settings. You can find the settings we used and also changed AFTER the video on [pastebin.com](<https://pastebin.com/jcQMhxSF>).

We changed the colors of the menu, transparency, size of icons, spaces, font and font size.

Have fun making your own look and feel.

You will find all the information you need on the [github of jgmenu](<https://github.com/johanmalm/jgmenu>).

Video: <https://youtu.be/3wryuoBQK_s>

Configuration of the first picture on this page

<https://pastebin.com/jcQMhxSF>
