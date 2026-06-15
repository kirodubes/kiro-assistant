---
title: "How to install caffeine - any desktop"
url: https://arcolinux.com/how-to-install-caffeine-any-desktop/
date: 2018-11-12 12:53:30
type: post
categories: ["Utilities"]
tags: ["anydesktop"]
source_site: arcolinux.com
---

# How to install caffeine - any desktop

![](https://arcolinux.com/wp-content/uploads/2018/11/caffeine.jpg)

Caffeine is an application you can install to keep your computer "awake" at all times.

> Tray bar application able to temporarily inhibit the screensaver and sleep mode.

You can find the github here : <https://github.com/caffeine-ng/caffeine-ng>

You can change some of its settings but basically it is **either on or off**.

Installing can be done with an AUR helper like yay or trizen:
    
    
    yay -S caffeine-ng

Caffeine will autostart upon reboot (in the systemtray). You need to activate it.

You will find the startup file in /etc/xdg/autostart.

Video: <https://www.youtube.com/watch?v=C663v9l-j0g>
