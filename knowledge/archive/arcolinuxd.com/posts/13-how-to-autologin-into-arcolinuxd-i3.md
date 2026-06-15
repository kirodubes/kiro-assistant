---
title: "13 -  how to autologin into ArcoLinuxD i3"
url: https://www.arcolinuxd.com/13-how-to-autologin-into-arcolinuxd-i3/
date: 2017-11-10 18:57:18
type: post
categories: ["i3"]
tags: ["autologin", "login"]
source_site: arcolinuxd.com
---

# 13 -  how to autologin into ArcoLinuxD i3

What I always prefer (at home) is that any operating system will autologin and I will be presented with my desktop (random wallpaper) and all my cloud syncing applications have gotten their updates in when I enter the room with my morning coffee. Topic is : **autologin** It all depends what you have chosen as [display manager](<https://wiki.archlinux.org/index.php/display_manager>). We have chosen for lightdm so we consult our [wiki](<https://wiki.archlinux.org/index.php/LightDM>). We need to change a file in
    
    
    /etc/lightdm/lightdm.conf

We edit this file with SUBLIME TEXT. This tool can save the changes on this protected place. We show you how I know what the name is to type in i.e. i3. After editing you need to add a user (yourself) to the autologin group.
    
    
    sudo groupadd -r autologin
    sudo gpasswd -a erik autologin

Then reboot. Done

Video: <https://youtu.be/n8HZvrEiSUE>
