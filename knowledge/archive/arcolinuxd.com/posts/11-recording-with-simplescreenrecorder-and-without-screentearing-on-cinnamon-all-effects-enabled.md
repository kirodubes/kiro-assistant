---
title: "11 - recording with simplescreenrecorder and without screentearing on Cinnamon - all effects enabled"
url: https://www.arcolinuxd.com/11-recording-with-simplescreenrecorder-and-without-screentearing-on-cinnamon-all-effects-enabled/
date: 2018-12-24 17:15:34
type: post
categories: ["Cinnamon"]
tags: ["arch installation", "archlinux"]
source_site: arcolinuxd.com
---

# 11 - recording with simplescreenrecorder and without screentearing on Cinnamon - all effects enabled

![](https://www.arcolinuxd.com/wp-content/uploads/2018/12/cinnamon-simplescreenrecorder.jpg)

Thanks to a tip on Youtube we can now record video's without screentearing or glitches on ArcoLinuxD -B Cinnamon.

Every desktop has its own way of handling windows and all its effects.

Simplescreenrecorder's settings can be changed to get less screen tearing but often you need to find other solution like this solution for [Plasma](<https://www.arcolinuxd.com/2-how-to-improve-the-recording-quality-in-plasma-using-simplescreenrecorder-no-glitches-allowed/>).

Now we have a solution for **Cinnamon** too for people with a graphical card from INTEL.

## Option 1 - fast and lazy

Use the scripts from ArcoLinux-Nemesis.

More about [Nemesis](<https://arcolinux.com/installing-nemesis-on-any-arcolinux/>) can be found here.

In the folder **Personal** I created a script to install the correct settings for an **intel graphical card**.  
**Run script 800.**

## Option 2 - manual

Create a file on your system 
    
    
    sudo touch /etc/X11/xorg.conf.d/20-intel.conf

Navigate to it and open it with sublime text. Copy/paste this code into it and save 
    
    
    Section "Device"
       Identifier  "Intel Graphics"
       Driver      	"intel"
       Option 	"AccelMethod" "uxa"
    EndSection

Now reboot.

Video: <https://youtu.be/UtsKm9tJ0H0>
