---
title: "Exploring the conky wo-conky-clock-lua and wo-conky-system-lua and changing it - any desktop"
url: https://arcolinux.com/exploring-the-conky-wo-conky-clock-lua-and-changing-it-any-desktop/
date: 2017-12-27 10:31:36
type: post
categories: ["Conky"]
tags: ["anydesktop", "conky"]
source_site: arcolinux.com
---

# Exploring the conky wo-conky-clock-lua and wo-conky-system-lua and changing it - any desktop

![](https://arcolinux.com/wp-content/uploads/2017/12/archmerge-wo-system-clock-lua.jpg)   


We have two kind of conky's. The regular conky and the conky created with LUA. Lua is a programming language. You can learn more about the language [here](<https://www.lua.org/start.html>).

Conky's, that are using lua, will have those three letters in their naming. When on **ArcoLinuxD** you will have to give support for that language to be interpreted. You better install "**conky-lua-archers** ".

Go find your conky's in
    
    
    ~/.config/conky

We open it up with **ATOM to see the colors. Packages minimap and pigments are installed.  
**

With **ifconfig** you can find your name of your network interface. Change it in **settings.lua**.

We will change the font size of the day.

We will change the color of the font.

We will show where to change the colors of the dials.

We will change the look of the clock - no second hand.

We can change the look of the box as well.

All you need to do is test.

 

Video: <https://www.youtube.com/watch?v=fx8O7DdiTb8>

  


Change one parameter and test what changed.

Video: <https://youtu.be/dVLE2uExpT4>

  


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
