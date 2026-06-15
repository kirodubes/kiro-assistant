---
title: "7 - detailed information about compton on i3"
url: https://www.arcolinuxd.com/7-detailed-information-about-compton-on-i3/
date: 2017-11-10 18:45:50
type: post
categories: ["i3"]
tags: ["compton", "theming"]
source_site: arcolinuxd.com
---

# 7 - detailed information about compton on i3

**Compton** is compositing manager. It will supply us the **shadows** , **transparency** , **fading** in our system. You can read more on the [wiki](<https://wiki.archlinux.org/index.php/Compton>) about it.

Let us read and change the compton.conf in ~/.config/i3/compton.conf.   
**Make backups and then change the settings.**

**Screentearing** issues might be helped with changing **glx** and **xrender**.

**YOU NEED to log off to see the effects of the changes in compton.conf.**

We tell it not to make shadows anymore.

Menu-opacity is changed to 1. No opacity anymore.

Inactive-opacity is set to 1.

Fading is set to false.

Video: <https://youtu.be/7tnyJnfSiuc>
