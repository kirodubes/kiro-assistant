---
title: "7 How to change the logo in standard menu bar of ArcoLinuxD Mate"
url: https://www.arcolinuxd.com/7-how-to-change-the-logo-in-standard-menu-bar-of-arcolinuxd-mate/
date: 2018-01-31 18:04:34
type: post
categories: ["Mate"]
tags: ["theming"]
source_site: arcolinuxd.com
---

# 7 How to change the logo in standard menu bar of ArcoLinuxD Mate

![](https://www.arcolinuxd.com/wp-content/uploads/2018/01/logo-mate-menu-bar.jpg) Normally you would be looking in settings or in right mouse click and properties but they are just not present. You can now fall back on the dconf database. Here more technical info about [dconf](<https://en.wikipedia.org/wiki/Dconf>). In order to open dconf in a graphical application we install dconf-editor (if not yet installed). 
    
    
    sudo pacman -S dconf-editor

Then we go look for the setting that defines that icon at the top left. ![](https://www.arcolinuxd.com/wp-content/uploads/2018/01/dconf-editor.jpg) We change the name into an existing icon in the icon theme you have chosen. The normal icon name is "**start-here** ". You can also go look for that icon and replace that one with the one you like. On every update of the icons your changes will/might be overwritten. 

Video: <https://youtu.be/0qv5FGEfegk>
