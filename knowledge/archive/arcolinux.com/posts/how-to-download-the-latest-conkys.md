---
title: "How to download the latest conky's"
url: https://arcolinux.com/how-to-download-the-latest-conkys/
date: 2017-10-28 11:31:43
type: post
categories: ["Conky"]
tags: ["conky"]
source_site: arcolinux.com
---

# How to download the latest conky's

![](https://arcolinux.com//wp-content/uploads/2017/10/get-latest-conky.jpg)

Since 6.2.1 Archmerge conky's come in via a **package**.

When you update your system with
    
    
    sudo pacman -Syu   or pksyua

or reinstall it with
    
    
    sudo pacman -S arcolinux-conky-collection-git

you will get the updates in.

They will be saved to this folder.
    
    
    /etc/skel/.config/conky

Then it is up to **you** to **copy** /**paste** the contents of that folder to your own personal folder or not. You might have made something **personal**. Changed colors and so on. Maybe it is better to use the application **meld** and see what the **difference** is between **both** **conky** **folders**.

 

Video: <https://www.youtube.com/watch?v=No2cf-L--b4>

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
