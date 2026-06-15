---
title: "How to change the position and size of a conky"
url: https://arcolinux.com/how-to-change-the-position-and-size-of-a-conky/
date: 2018-04-28 09:06:01
type: post
categories: ["Conky"]
tags: ["conky"]
source_site: arcolinux.com
---

# How to change the position and size of a conky

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-conky-position.jpg)

Changing the size and position of a conky is possible.

First you need to know what conky you want to change. Then choose an appropriate editor.

We are on the look out for this code.
    
    
    --Placement
    
     alignment = 'middle_right', 
     --Arch Duoscreen
     --gap_x = -1910,
     gap_x = 10, 
     gap_y = 20, 
     minimum_height = 600, 
     minimum_width = 230, 
     maximum_width = 230,

We change all the variables in the video and you will see the effect instantly.

If you have a dualscreen and want the conky to be on your second screen then use : **gap_x = -1910,**

 

There is also a tutorial about the resizing the conky [by changing the font or deleting lines](<https://arcolinux.com/how-to-make-your-conky-smaller-so-it-fits-on-your-screen/>).

Video: <https://youtu.be/n-uqyA6rlBg>

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
