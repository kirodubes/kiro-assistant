---
title: "How to change the menu in openbox with obmenu-generator"
url: https://www.arcolinuxd.com/how-to-change-the-menu-in-openbox-with-obmenu-generator/
date: 2024-03-01 06:39:56
type: post
categories: ["Openbox"]
source_site: arcolinuxd.com
---

# How to change the menu in openbox with obmenu-generator

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/archmerge-xfce-theming-1.jpg)ArcoLinux has a generated menu out of the box. The advantage is that any installed or uninstalled will immediately have effect on your menu. No manual editing required. You can even have a menu with icons if you want to. What if you want to change the menu from **language**? Parts of the menu are **generated** and will be in your language but parts are just **plain** **text** and will **not** **change** with it. You need to know where these files are so you can change them. They are in 
    
    
    ~/.config/obmenu-generator

Two files are important: **config.pl** and **schema.pl** In the tutorial we will be changing schema.pl and replace it with applications and the language you want. Look up the name of the icon in /usr/share/icons. Part of the menu is coming from obmenu-generator. The language is coming from the files inside /usr/share/applications. We will talk about all the possibilities to make 4 obmenu-generated menu's 

  1. generate a pipe menu
  2. generate a static menu
  3. generate a pipe menu with icons
  4. generate a static menu with icons

If you change the icons, you will need to refresh the icons in the menu.Keyboard Shortcuts To RememberSupER + SPACEBARget obmenu

Video: <https://www.youtube.com/watch?v=Pjp0AynvWKQ>
