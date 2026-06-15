---
title: "Install nemo as extra filemanager on any ArcoLinux with many tips"
url: https://arcolinux.com/install-nemo-as-extra-filemanager-on-any-arcolinux-with-many-tips/
date: 2018-01-24 14:46:54
type: post
categories: ["File Managers"]
tags: ["nemo"]
source_site: arcolinux.com
---

# Install nemo as extra filemanager on any ArcoLinux with many tips

![](https://arcolinux.com/wp-content/uploads/2018/01/archmerge-nemo.jpg)   


Installing nemo is quite simple.
    
    
    sudo pacman -S nemo

Then you set nemo as the default application via "exo-preferred-application" or via the menu "**Preferred Applications** ".

Deleting thunar completely might break your system. I have not tried yet. We see in the video that there are dependancies. They should be deleted as well...

**I suggest leaving thunar but use nemo instead as the best option.**

**Correction** : you do **not** have the complete cinnamon desktop. You can **not** **login**.

Video: <https://www.youtube.com/watch?v=BSP4f_qfSWs>

  


How to get a preview of images?  
There is a treshold to change.

Video: <https://youtu.be/uyMAo1Treo0>

  


RIGHT mouse click on nemo  
terminal does not open

Video: <https://youtu.be/N1lwkkT4E44>

  


**Solution 1**

Nemo expects **gnome-terminal** to be installed so install it with

sudo pacman -S gnome-terminal

**Tip** : there is also a transparent gnome-terminal called "**gnome-terminal-transparency** "

 

**Solution 2**

We want the standard terminal "**Termite** " on Nemo.

We found the solution on the wiki of Arch Linux at <https://wiki.archlinux.org/index.php/Nemo>
    
    
    gsettings set org.cinnamon.desktop.default-applications.terminal termite

RIGHT mouse click on nemo  
add compress and extract  
funtionality

Video: <https://youtu.be/IFmwM2zpYhw>

  


There are more nemo extensions  
Type "sudo pacman -S nemo-"  
and press twice on tab
