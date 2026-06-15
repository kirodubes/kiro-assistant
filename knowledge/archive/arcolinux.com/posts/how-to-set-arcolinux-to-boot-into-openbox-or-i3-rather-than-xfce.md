---
title: "How to set Arcolinux to boot into Openbox or i3 rather than Xfce"
url: https://arcolinux.com/how-to-set-arcolinux-to-boot-into-openbox-or-i3-rather-than-xfce/
date: 2017-09-28 18:03:40
type: post
categories: ["Lightdm", "Login"]
tags: ["boot", "i3", "login", "openbox", "xfce"]
source_site: arcolinux.com
---

# How to set Arcolinux to boot into Openbox or i3 rather than Xfce

**This applies to all desktop environments.** Our goal is to **change** the **autologin** from **Xfce** to **Openbox** or **i3**. If we**just want to change for one time** than you logout and click on the icon at the top right corner of the login screen. The concept of ArcoLinux is that **anyone** can use it. Your level of linux can be beginner, intermediate or expert. There will be something in it for everyone. There are enough challenges in the three desktops but in the future you will have an ArcoLinuxD as well and exciting challenges will come your way like Budgie, Cinnamon, Gnome etc. [Check out our vision about the different phases here](<..//tutorials/>). And that is why ArchMerge boots into **Xfce** rather than Openbox or i3. First time linux users can **find** their **way** more **comfortably** in **Xfce** than Openbox or i3. And for intermediate and expert users it does not matter, we need just to change one word and then we **boot** or **autologin** into Openbox or i3.     Keyboard Shortcut To Remember SUPER + X Logout, Shutdown, ... 

Video: <https://www.youtube.com/watch?v=lqvMvcqPFvw>

  **GREAT TIP** : on some desktop environments we have changed this parameter to succesful autologin into the desktop. You will get the autologin screen for a flash and then it continues to your desktop. 
    
    
    autologin-user-timeout=1

**GREAT TIP** : open up **lightdm.conf** with **sublime-text** and set the language to **PERL**. You will be able to analyze the file much faster. ![](https://arcolinux.com/wp-content/uploads/2017/09/lightdm-perl.jpg)
