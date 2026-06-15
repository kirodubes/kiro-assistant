---
title: "How to activate polybar on ArcoLinux Openbox"
url: https://www.arcolinuxd.com/how-to-activate-polybar-on-arcolinux-openbox/
date: 2024-03-01 06:36:49
type: post
categories: ["Openbox"]
source_site: arcolinuxd.com
---

# How to activate polybar on ArcoLinux Openbox

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/archmerge-openbox-polybar.jpg)You can use polybar as well in Openbox. The standard panel in ArcoLinux is tint2 but you can replace this. We edit the **autostart** file in folder ~/.config/openbox. 
    
    
    #tint2 &
    sh ~/.config/polybar/launch.sh &

These lines came in with the update of the package : **arcolinux-openbox-configs-git** and it is saved in your /etc/skel. You need to copy/paste it to your home folder or compare differences with meld. Log out and back in to see polybar at work.

Video: <https://youtu.be/t7j6M1zU8u4>
