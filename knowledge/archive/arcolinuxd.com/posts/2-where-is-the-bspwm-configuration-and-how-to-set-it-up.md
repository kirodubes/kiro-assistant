---
title: "2 where is the bspwm configuration and how to set it up"
url: https://www.arcolinuxd.com/2-where-is-the-bspwm-configuration-and-how-to-set-it-up/
date: 2018-05-04 09:49:10
type: post
categories: ["Bspwm"]
source_site: arcolinuxd.com
---

# 2 where is the bspwm configuration and how to set it up

![](https://www.arcolinuxd.com/wp-content/uploads/2018/05/arcolinuxd-bspwm-startscreen.jpg)Autostart.sh

**Bspwm** (Binary Space Partitioning Window Manager) is a tiling window manager and it is coming from [this github](<https://github.com/baskerville/bspwm>). You can get more information on the [Arch Wiki](<https://wiki.archlinux.org/index.php/Bspwm>).

The **conky** is there to help you learn the keyboard shortcuts, when you first boot into Bspwm. Conkies in tiling window managers are not required.

Keep the **Arco-Bspwm github** folder save for later. In the future you can do a **git pull** and see what we improved.

We need to know two folders for Bspwm

  * ~/.config/bspwm
  * ~/.config/sxhkd



Find out the names of your screen/monitor with **xrandr** or **arandr**. You can use it to set your screen in the autostart.

**Polybar** is going to be our menu at the top. [You can read all the articles about polybar here](<https://arcolinux.com/category/arcolinux/design/theming/polybar/>).

I need to set my keyboard to azerty.... I need to do much more. [That is covered in this article](<https://www.arcolinuxd.com/4-change-bspwm-from-qwerty-to-azerty-keyboard/>).

> We go over all the components of autostart.

 

 

Video: <https://youtu.be/4JS5LJYDCs8>

bspwmrc

The configuration file of bspwmrc is quite small. It is all we ever need.

We install **pigments** in Atom to actually see the colors.

We can set the colors, borders, gaps, ...

We explain the settings for dual screens.

There are rules availabe, if you want an application to **float** , **tile** or be **full-screen**.

 

Video: <https://youtu.be/1ynYGhAZo4E>

compton.conf

Compton has 3 big parts in its file.

  * Shadow
  * Opacity
  * Fading



We have an [Arch Wiki page](<https://wiki.archlinux.org/index.php/Compton>) to learn even more.

Choose **glx** or **xrender**. Only if you have trouble with your graphical hardware.

Video: <https://youtu.be/w8NimwtvClM>

conky to remember keyboard shortcuts

The conky is only here to learn you in those **first hours to learn and to remember the keyboard shortcuts**.  
You can hashtag this conky out in autostart later.

Video: <https://youtu.be/nkA2W33wJIQ>

Keyboard shortcut settings

Sxhkd is a simple X hotkey daemon. There is an [Arch Wiki page](<https://wiki.archlinux.org/index.php/Sxhkd>) to read all about it.  
You can also checkout [its github](<https://github.com/baskerville/sxhkd>).

We use it to make sure that CTRL + ALT + T opens a terminal and many other keyboard shortcuts.

In order for it to work we launch the sxhkd (d=daemon) in autostart.

The files needs to be in some kind of syntax.

  * If it starts with `#`, it is ignored.
  * If it starts with one or more white space commands, it is read as a command.
  * Otherwise, it is parsed as a hotkey: each key name is separated by spaces and/or `+` characters.



> All the keyboard shortcuts you know, will be the same in all our desktops.

Video: <https://youtu.be/L1Ayy-L8T3o>

ANALYZING THE POLYBAR CONFIG OF BSPWM - removing last icon is the goal

Video: <https://youtu.be/9pWRLf98NrI>
