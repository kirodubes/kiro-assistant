---
title: "5 Where is the Xmonad configuration - autostart"
url: https://www.arcolinuxd.com/5-where-is-the-xmonad-configuration-autostart/
date: 2019-01-17 20:03:38
type: post
categories: ["Xmonad"]
source_site: arcolinuxd.com
---

# 5 Where is the Xmonad configuration - autostart

![](https://www.arcolinuxd.com/wp-content/uploads/2019/01/arcolinuxb-xmonad-sublime-text-xmonad.hs_.jpg)

two major documents to configure

Xmonad has **actually** just **one** **document** where all the settings are :

  * xmonad.hs



The other one is connected to Xmonad but it is not from Xmonad.

  * scripts/autostart.sh



Video: <https://www.youtube.com/watch?v=z5oQWcXWgQE>

Autostart.sh  
Resolution

Find out the names of your screen/monitor with **xrandr** or **arandr**.

You can use it to set your screen in the autostart.

We show you how in the video.

Xmonad will autodetect the resultion of your screen on real metal. Virtualbox is NOT real metal.

**VirtualBox stays a simulation. Hence the issues for ALL tiling window managers.**

There is also an example script present if you want to install Xmonad in a virtual machine but your native screen resolution is NOT available in the dropdown in your virtual machine.  
You can solve that too.

Video: <https://youtu.be/J7o9hyhqr6I>

Autostart.sh  
Polybar

We will use **polybar** on the most of our tiling window managers.

We have created so many tutorials about it and have so many modules available for it.  
Polybar is now used on Openbox, i3, Bspwm and now Xmonad.

Video: <https://youtu.be/ENN71iskFvY>

Autostart.sh  
autostart your applications at boot

Autostart.sh is also there for you.

We all have our preferences regarding wallpapers and how to set them.

We use **variety** as a wallpaper changer and provider. But there is also **feh** or **nitrogen** to set your **wallpaper** and not rotate it at all.

You can launch **discord** automatically at boot and so much more.

We go over the rest of the content of autostart.sh.

We will keep updating this file. The content may differ from the content of the video.

Video: <https://www.youtube.com/watch?v=_ZMi2eeqmOY>
