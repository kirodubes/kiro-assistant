---
title: "Fix for Failed to start lightdm manager"
url: https://arcolinux.com/fix-for-failed-to-start-lightdm-manager/
date: 2019-11-29 00:18:09
type: post
categories: ["Fixes", "Lightdm", "Nvidia"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# Fix for Failed to start lightdm manager

![](https://arcolinux.com/wp-content/uploads/2019/11/failed-to-start-lightdm-manager.jpg)![](https://arcolinux.com/wp-content/uploads/2019/11/nemesis-scripts.jpg)

Are you using the arcolinux-nemesis script?

Are you using the arcogetstarted script?

Did you read what the code does?

what is the target audience  
for these scripts

JUST ERIK DUBOIS

The nemesis is a personalized script for Erik Dubois on the computers of Erik Dubois.

You can reuse many of the code but not all of it. I choose to install extra software. You will like to install some of them too but not all of them.

In the end of the script it is going to ask you what **desktop** you have. You need to type in a number.

**Choose number 0.**

![](https://arcolinux.com/wp-content/uploads/2019/11/select.jpg)

This last bit is setting my xorg system so I can record videos without lag and jitter.

It is code to stay tear-free for my **intel** graphics card on my motherboard.

![](https://arcolinux.com/wp-content/uploads/2019/11/nemesis.jpg)

I have added a **lot of red lines** in the hopes to get your attention before it is too late.

Again **choose nr 0 aka do nothing** if you do not have an intel graphical card.

If it is too late than you need to remove a file in the /etc/X11/xorg.conf.d/20-intel.conf

We will show you in the video.

I did forget it this time and I bricked my system. 

Lightdm can not be started because of my own mistake.

This pc does not have an intel graphical card but an Nvidia graphical card.

Hence system breaks down.

**sudo rm /etc/x11/xorg.conf.d/20-intel.conf**

Video: <https://youtu.be/Cl7KOS4Mn5U>
