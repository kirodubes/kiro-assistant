---
title: "How to set double tap and drag and drop on your laptop’s touchpad – any desktop"
url: https://www.arcolinuxd.com/how-to-set-double-tap-and-drag-and-drop-on-your-laptops-touchpad-any-desktop/
date: 2018-01-02 10:43:06
type: post
categories: ["AnyDesktop"]
tags: ["anydesktop"]
source_site: arcolinuxd.com
---

# How to set double tap and drag and drop on your laptop’s touchpad – any desktop

![](https://www.arcolinuxd.com/wp-content/uploads/2018/01/archmerge-touchpad-1.jpg)

When on ArcoLinux you can set your touchpad with the gui of XFCE settings or keyboard shortcut

CTRL + ALT + M.

This will work on Xfce and Openbox. If you want to have this solution on i3 you will need to delete a hashtag in the config file.
    
    
    #exec --no-startup-id xfsettingsd &

When you are on ArcoLinux with any of the possible desktops you need to check this page. <https://wiki.archlinux.org/index.php/Libinput>.

Some of the desktop environments provide you some kind of settings manager for your touchpad and in others you will have to make a configuration file for your touchpad in
    
    
    /etc/X11/xorg.conf.d/30-touchpad.conf

The content is up to you but could be something like this.
    
    
    Section "InputClass"
        Identifier "touchpad"
        Driver "libinput"
        MatchIsTouchpad "on"
        Option "Tapping" "on"
    EndSection

If libinput fails to work on your hardware, you can also have a look at [this wiki page](<https://wiki.archlinux.org/index.php/Touchpad_Synaptics>) but it is NOT encouraged.

Video: <https://www.youtube.com/watch?v=wirwLHMjhog>
