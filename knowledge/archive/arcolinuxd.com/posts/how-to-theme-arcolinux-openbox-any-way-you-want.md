---
title: "How to theme ArcoLinux Openbox any way you want"
url: https://www.arcolinuxd.com/how-to-theme-arcolinux-openbox-any-way-you-want/
date: 2024-03-01 06:43:59
type: post
categories: ["Openbox"]
source_site: arcolinuxd.com
---

# How to theme ArcoLinux Openbox any way you want

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/ArchMerge_xfce-achim-reiz.jpg)

ArcoLinux has an generated menu out of the box. The advantage is that any installed or uninstalled will immediately have effect on your menu. No manual editing required. You can even have a menu with icons if you want to.

What if you want to change the menu from **language**?

Parts of the menu are **generated** and will be in your language but parts are just **plain** **text** and will **not** **change** with it.

You need to know where these files so you can change them. They are in

~/.config/obmenu-generator

Two files are important: **config.pl** and **schema.pl**

In the tutorial we will be changing schema.pl and replace it with applications and the language you want. Look up the name of the icon in /usr/share/icons.

Part of the menu is coming from obmenu-generator. The language is coming from the files inside /usr/share/applications.

We will talk about all the possibilities to make 4 obmenu-generated menu's

  1. generate a pipe menu
  2. generate a static menu
  3. generate a pipe menu with icons
  4. generate a static menu with icons



If you change the icons, you will need to refresh the icons in the menu.

Keyboard Shortcuts To Remember

SupER + SPACEBAR

get obmenu

Video: <https://www.youtube.com/watch?v=Gg_Yz2UpeUU>
