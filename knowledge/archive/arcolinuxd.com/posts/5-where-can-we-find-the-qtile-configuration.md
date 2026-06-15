---
title: "5 Where can we find the qtile configuration"
url: https://www.arcolinuxd.com/5-where-can-we-find-the-qtile-configuration/
date: 2019-05-20 11:31:37
type: post
categories: ["Qtile"]
source_site: arcolinuxd.com
---

# 5 Where can we find the qtile configuration

![](https://www.arcolinuxd.com/wp-content/uploads/2019/05/arcolinuxb-qtile-configuration-files.jpg)

two major documents to configure

Qtile has **actually** just **one** **document** where all the settings are :

  * config.py



The other one is connected to Qtile but it is not from Qtile.

  * scripts/autostart.sh



Video: <https://youtu.be/kUYu9QITozw>

Autostart.sh

Find out the names of your screen/monitor with **xrandr** or **arandr**. Xrandr is not specific to any window manager [so check out these articles too](<https://www.arcolinuxd.com/?s=xrandr>).

You can use it to set your screen in the autostart if you need to.

**Qtile** will **autodetect** the resolution of your screen on real metal. Virtualbox is NOT real metal.

**VirtualBox stays a simulation. Hence the issues for ALL tiling window managers.**

There is also an example script present if you want to install Qtile in a virtual machine but your native screen resolution is NOT available in the dropdown in your virtual machine.  
You can solve that too.

We all have our preferences regarding wallpapers and how to set them.

We use **variety** as a wallpaper changer and provider. But there is also **feh** or **nitrogen** to set your **wallpaper** and not rotate it at all.

You can launch **discord** automatically at boot and so much more.

We go over the rest of the content of autostart.sh.

We will keep updating this file. The content may differ from the content of the video.

Video: <https://youtu.be/zI4Z_MQ1viQ>

config.py  
qtile code

Although I started with the autostart script, that is not the first thing that starts.

Qtile will be launched using its configuation file in ~/.config/qtile/config.py.   
At **almost the bottom** the autostart script is launched and is launched **just once**.

Video: <https://youtu.be/v1LjYSHgPgo>
