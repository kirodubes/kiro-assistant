---
title: "How to autostart the conky in Xfce"
url: https://arcolinux.com/how-to-autostart-the-conky-in-xfce/
date: 2018-12-14 20:10:03
type: post
categories: ["Conky"]
tags: ["conky", "script", "xfce"]
source_site: arcolinux.com
---

# How to autostart the conky in Xfce

![](https://arcolinux.com/wp-content/uploads/2017/09/autostart.jpg)

**Any application can be autostarted upon boot or you can decide NOT to autostart the applications, that are present there.****Find "****Session and Startup****" in the menu.**

**First we activate a conky to see that it is working. Then we show where you should add the conky to****autostart****it. What application should we autostart? Conky,...**

****

****

**We learn the command****killall****. VERY useful.**

**We figure out that the command we need is actually****am-conky-session and not conky.**

**We logoff and make sure the conky is started automatically.**

**Conky's are in a hidden folder named ~/.config/conky. There you will find a very handy script to get the latest updates.**

**All conky updates will come in with a package when you update your system.  
**

Keyboard Shortcuts To Remember

SUPER + T ... CTRL + ALT+ T ... Super + Enter

Launch your terminal

Video: <https://www.youtube.com/watch?v=rjRZdIltbS0>

OPenbox and i3 have their  
Own way to launch a conky

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
