---
title: "6 How to use compton on ArcoLinuxD Mate"
url: https://www.arcolinuxd.com/6-how-to-use-compton-on-arcolinuxd-mate/
date: 2018-01-30 20:28:49
type: post
categories: ["Mate"]
tags: ["compton", "theming"]
source_site: arcolinuxd.com
---

# 6 How to use compton on ArcoLinuxD Mate

![](https://www.arcolinuxd.com/wp-content/uploads/2018/01/archmerged-mate-compton.jpg)

Using **compton** on Mate is easily done IF you have installed **mate-tweak** (AUR) via our scripts then we install compton itself.
    
    
    sudo pacman -S compton

Next step is to know **where** compton's configuration file is.

Then copy/paste it in ~/.config and **rename** it to **marco-compton.conf**.

Then you can select it in mate-tweak.

It is not at all necessary to do this.

Advantages are the fading, shade, titlebar transparent, non-active windows are transparent, ...  
More or less the same settings as on ArcoLinux i3 and openbox.

There is always some kind of "danger" involved in such projects. Shortcuts no longer working, conky's reacting strange, windows leaving traces, you name it. In short the system becomes unresponsive = worst case scenario.

REMEMBER : CTRL + ALT + BACKSPACE will kill your xserver and will get you back working.

![](https://www.arcolinuxd.com/wp-content/uploads/2018/01/mate-tweak-compton.jpg)

Video: <https://youtu.be/EOg4WSlbxgw>
