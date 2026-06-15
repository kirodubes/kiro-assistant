---
title: "5 How to autostart applications on LXQt like plank"
url: https://www.arcolinuxd.com/5-how-to-autostart-applications-on-lxqt-like-plank/
date: 2020-04-08 10:44:09
type: post
categories: ["Lxqt"]
source_site: arcolinuxd.com
---

# 5 How to autostart applications on LXQt like plank

![](https://www.arcolinuxd.com/wp-content/uploads/2020/04/plank.jpg)![](https://www.arcolinuxd.com/wp-content/uploads/2020/04/autostart-lxqt.jpg)

Most desktops offer the user a way to autostart applications. LXQt has also an application.

You can find it in **Session Settings**.

We add plank to the autostart.

> Only after clicking the close button is your new autostart setting saved

We install the applications needed to have plank
    
    
    sudo pacman -S plank
    
    
    
    
    sudo pacman -S arcolinux-plank-themes-git
    
    
    
    
    sudo pacman -S arcolinux-plank-git

We acted a bit to fast and typed **skel** in our terminal.

This means the settings from /etc/skel are copied over to the home directory and after a reboot we see the standard ArcoLinux look is back.

We show you how easy it is to get our **tweaked** **LXQt** **back**. Remember the application **meld**. As developers we use it all the time to compare files and folders.

Video: <https://youtu.be/uE5oZgV1s5k>
