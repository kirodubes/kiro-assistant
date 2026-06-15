---
title: "How to make your conky smaller so it fits on your screen"
url: https://arcolinux.com/how-to-make-your-conky-smaller-so-it-fits-on-your-screen/
date: 2018-05-14 07:29:46
type: post
categories: ["Conky"]
tags: ["conky"]
source_site: arcolinux.com
---

# How to make your conky smaller so it fits on your screen

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-aur-nemesis-resizing.jpg)

If text and information is falling off from your screen, you have only two options.

  1. make the font smaller
  2. delete elements you do not want anyway



There is also a tutorial about the [size of the conky and the position of the conky](<https://arcolinux.com/how-to-change-the-position-and-size-of-a-conky/>).

Video: <https://youtu.be/vvai79l5FJI>

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
