---
title: "8 change the icon in the brisk menu on Mate"
url: https://www.arcolinuxd.com/8-change-the-icon-in-the-brisk-menu-on-mate/
date: 2018-01-31 19:02:59
type: post
categories: ["Mate"]
tags: ["theming"]
source_site: arcolinuxd.com
---

# 8 change the icon in the brisk menu on Mate

![](https://www.arcolinuxd.com/wp-content/uploads/2018/01/briskmenu-mate.jpg) Normally you would be looking in settings or in right mouse click and properties but they are just not present. Then you might want to look at the dconf database. Here more technical info about [dconf](<https://en.wikipedia.org/wiki/Dconf>). In order to open dconf in a graphical application we install dconf-editor (if not yet installed). 
    
    
    sudo pacman -S dconf-editor

We found lots of interesting things to change but not the icon. ![](https://www.arcolinuxd.com/wp-content/uploads/2018/01/briskmenu-dconf-editor.jpg) **Then there is only one way to change it and that is in the icon theme you are using.** We need to change the following icon : **start-here-symbolic.svg in folder places** Do not forget to **delete** the **icon-theme.cache**. Follow the tutorial and will become clear. 

Video: <https://youtu.be/m2Q2vPq39fc>
