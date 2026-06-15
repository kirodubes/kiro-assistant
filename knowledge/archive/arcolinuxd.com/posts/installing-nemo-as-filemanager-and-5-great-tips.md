---
title: "10 - Installing nemo as filemanager and 5 great tips"
url: https://www.arcolinuxd.com/installing-nemo-as-filemanager-and-5-great-tips/
date: 2018-01-24 15:55:15
type: post
categories: ["Cinnamon"]
tags: ["nemo"]
source_site: arcolinuxd.com
---

# 10 - Installing nemo as filemanager and 5 great tips

![](https://www.arcolinuxd.com/wp-content/uploads/2018/01/archmerge-nemo.jpg)   Installing nemo is quite simple. If you used the amd scripts it is already installed. 
    
    
    sudo pacman -S nemo

Then you set nemo as the default application via "exo-preferred-application" or via the menu "**Preferred Applications** " if it is not already set. 

Video: <https://www.youtube.com/watch?v=BSP4f_qfSWs>

  How to get a preview of images? There is a treshold to change. 

Video: <https://youtu.be/uyMAo1Treo0>

  RIGHT mouse click on nemo terminal does not open 

Video: <https://youtu.be/N1lwkkT4E44>

  **Solution 1** Nemo expects **gnome-terminal** to be installed so install it with sudo pacman -S gnome-terminal **Tip** : there is also a transparent gnome-terminal called "**gnome-terminal-transparency** "   **Solution 2** We want the standard terminal "**Termite** " on Nemo. We found the solution on the wiki of Arch Linux at <https://wiki.archlinux.org/index.php/Nemo>
    
    
    gsettings set org.cinnamon.desktop.default-applications.terminal termite

RIGHT mouse click on nemo add compress and extract funtionality 

Video: <https://youtu.be/IFmwM2zpYhw>

  There are more nemo extensions Type "sudo pacman -S nemo-" and press twice on tab
