---
title: "22 how to make applications and their windows float in a tiling window manager"
url: https://www.arcolinuxd.com/22-how-to-make-applications-and-their-windows-float-in-a-tiling-window-manager/
date: 2019-05-31 07:46:36
type: post
categories: ["Qtile"]
source_site: arcolinuxd.com
---

# 22 how to make applications and their windows float in a tiling window manager

![](https://www.arcolinuxd.com/wp-content/uploads/2019/05/arcolinuxb-xprop-qtile.jpg)

Near the bottom of the config.py we define what windows should NOT be tiled and should be made floating.

These small popup windows from applications will be tiled otherwise and occupy half of your screen like in this example of the about in variety.

This is just an example and it will not end in the code.

We want to learn a procedure how to figure it out yourself.

Use **xprop** to know the **wmclass** and add it to the list in config.py.

Reload qtile and test it out.

There is a keyboard shortcut to toggle between floating and non-floating

SUPER + SHIFT + SPACE

Video: <https://youtu.be/O7yWKoS9Nc8>
