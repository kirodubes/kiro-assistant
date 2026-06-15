---
title: "41 updating plasma - fixing numix circle icon theme and deleting packages"
url: https://www.arcolinuxd.com/41-updating-plasma-fixing-numix-circle-icon-theme-and-deleting-packages/
date: 2019-01-09 18:16:39
type: post
categories: ["Plasma"]
source_site: arcolinuxd.com
---

# 41 updating plasma - fixing numix circle icon theme and deleting packages

![](https://www.arcolinuxd.com/wp-content/uploads/2019/01/updating-numix-circle.jpeg)In this video we will update our system with 
    
    
    update
    upall

At this point there is an error in the pkgbuild of numix-circle-icon-theme. We will show you that you need to delete an obstructing file and rerun upall. 
    
    
    sudo rm /usr/share/icons/Numix-Circle/icon-theme.cache

We are also delete packages that were orphaned. I means that nobody is maintaining them. 
    
    
    sudo pacman -R b43-firmware b43-fwcutter

We see that the brand new kernel of 31/12/2018 4.20 is coming in so we reboot. There is also a lot of **Plasma** and **Qt5** elements coming in. 

> Do not be afraid if this will crash your system or if this will make your system act up.

**Just reboot** and evaluate then.![](https://www.arcolinuxd.com/wp-content/uploads/2019/01/plasma-crash.jpg)

Video: <https://youtu.be/Zv2cgkpfYfU>
