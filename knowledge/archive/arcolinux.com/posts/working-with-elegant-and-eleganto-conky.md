---
title: "Working with Elegant and Eleganto conky"
url: https://arcolinux.com/working-with-elegant-and-eleganto-conky/
date: 2018-05-27 17:12:35
type: post
categories: ["Conky"]
tags: ["conky"]
source_site: arcolinux.com
---

# Working with Elegant and Eleganto conky

8 cores

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-eleganto-8core.jpg)

4 cores

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-elgant-eleganto-4cores.jpg)

2 cores

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-elgant-eleganto-2cores.jpg)

# TIP

If you do not have an 8 core computer and you want a working conky.  
First make a **copy** of the conky and rename it.

An example

Change the **copy** of **Arco-Elegant.conkyrc** to **Arco-Elegant-4core.conkyrc**.

**If you do a copy/paste of /etc/skel in the future then it will NOT be overwritten.**

**Elegant** and **Eleganto** have been created for computers with **8 cores or more**. They are basically the same. Elegant is written in the 'old' conky code and Eleganto is written in the newer - lua coding. We will use both conkies to research how conkies behave in different desktops and display managers.

If you do **not** have 8 cores then selecting this conky will show you **NOTHING**. You will have to do some manual editing.

In the video we show you how to make this conky work on your system if you have

  * 4 cores
  * 2 cores



Video: <https://youtu.be/95yoUkKq8b0>

ADDING XIROD FONT TO THE CONKY

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-elegant-eleganto-font.jpg)

**Elegant** and **Eleganto** were designed to have a special font called **xirod**.

**Many of the conky's use special fonts**. Do not forget to install them via this [article](<https://arcolinux.com/the-7-step-installation-guide-for-arcolinux/>).

Let us install the font together. Since is is 100% copyright free you can find it in
    
    
    ~/.config/conky/fonts

Video: <https://youtu.be/ETkbU1HBAmE>

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
