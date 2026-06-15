---
title: "2 Where is the Spectrwm configuration and how to make minor changes"
url: https://www.arcolinuxd.com/where-is-the-spectrwm-configuration-and-how-to-make-minor-changes/
date: 2020-12-12 19:06:58
type: post
categories: ["Spectrwm"]
source_site: arcolinuxd.com
---

# 2 Where is the Spectrwm configuration and how to make minor changes

![](https://www.arcolinuxd.com/wp-content/uploads/2020/12/spectrwm.jpg)

spectrwm.conf

**Spectrwm** is a tiling window manager. Check out the [website](<https://github.com/conformal/spectrwm#readme>). You can get more information on the [Arch Wiki](<https://wiki.archlinux.org/index.php/spectrwm>).

We need to know a file and a folder for Spectrwm

  * ~/.config/spectrwm
  * ~/.spectrwm.conf



**Polybar** is going to be our menu at the top. [You can read all the articles about polybar here](<https://arcolinux.com/category/arcolinux/design/theming/polybar/>).

I need to set my keyboard to azerty.... I need to do much more. [That is covered in this article](<https://www.arcolinuxd.com/4-change-bspwm-from-qwerty-to-azerty-keyboard/>).

> We go over all the components. 

 

Video: <https://youtu.be/EwL3mKHMf3E>

picom.conf

Picom (used to be be compton) has 3 big parts in its file.

  * Shadow
  * Opacity
  * Fading



We have an [Arch Wiki page](<https://wiki.archlinux.org/index.php/Picom>) to learn even more.

Choose **glx** or **xrender**. Only if you have trouble with your graphical hardware.

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
