---
title: "Change the color of the conky Aur-ArcoLinux in xfce"
url: https://arcolinux.com/change-the-color-of-the-conky-aur-arcolinux-in-xfce/
date: 2017-10-24 21:42:03
type: post
categories: ["Conky"]
tags: ["conky", "gpick", "xfce"]
source_site: arcolinux.com
---

# Change the color of the conky Aur-ArcoLinux in xfce

![](https://arcolinux.com//wp-content/uploads/2017/10/ArchMerge-aur-archmerge-change-orange-to-green.jpg)

Changing the color of a conky could not be easier with a tool like **gpick**.  
Here we start with the end-result to the fact that my webcam had been connected to a wrong usb and had no sound.

Tip : change the webcam from usb to get the microphone to work

We show you the ease and comfort that **variety** and **desktoppr** bring to our system.

We figure out what conky is displayed via **conkyzen**.

We need to know in what folder all the conky's are kept i.e **~/.config/conky**

As extra tip we talk about the **fonts** and the **images** folder. You can edit all these .svg logo's and change their color to match your wallpaper. With inkscape it takes 5 seconds.

Easy way to figure at what variable is orange or green. Change it to FF0000 which is red.

Video: <https://www.youtube.com/watch?v=5eRIjtsuQAk>

# General conky info

> A conky will NEVER EVER work on all desktops.

**There are just too much differences between all the different window managers.**

It will also depend on the software you have installed.

There are two versions of the application called 'conky'.

  1. version 1.9 and earlier - old syntax
  2. version 1.10 and higher - new syntax - LUA (and old syntax)



We install the application **conky-lua-archers (1.10)** on ArcoLinux

**Options to explore when encountering issues :**

  * own_window_type = 'desktop', # options are: normal/override/dock/desktop/panel
  * own_window_transparent = true, # options are : true and false
  * own_window_argb_visual = true, # options are : true and false
  * own_window_argb_value = 0, # options are : 0-255



#### More information about conkies can be found here :

[Arch wiki](<https://wiki.archlinux.org/index.php/conky>)

[Conky github configuration](<https://github.com/brndnmtthws/conky/wiki>)

[Conky github faq](<https://github.com/brndnmtthws/conky/wiki/FAQ>)

[Conky github user configs](<https://github.com/brndnmtthws/conky/wiki>)

[Conky configuration on sourceforge](<http://conky.sourceforge.net/config_settings.html>)

[Conky variables on sourceforge](<http://conky.sourceforge.net/variables.html>)
