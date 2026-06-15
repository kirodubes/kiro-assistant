---
title: "Fix for bluetooth not switching off - any desktop"
url: https://arcolinux.com/fix-for-bluetooth-not-switching-off-any-desktop/
date: 2019-06-23 10:11:39
type: post
categories: ["Fixes"]
tags: ["bluetooth"]
source_site: arcolinux.com
---

# Fix for bluetooth not switching off - any desktop

![](https://arcolinux.com/wp-content/uploads/2019/06/bluetooth-fix-switch.jpg)

In the above image you see a blue switch to turn bluetooth on and off.

Recently we can no longer switch it off any more. For me personally that is unimportant as I want it on all the time for my bluetooth headphones.

However if you want to be able to switch it off then we have added a solution in 

/home/$USER/.bin/stay-rolling/19.6-to-19.7/stay-rolling-v1.sh

This is the line that will be executed.
    
    
    sudo usermod -a -G rfkill $USER

It will make sure that you will be added to the group rfkill.

Reboot and it is fixed.

Video: <https://www.youtube.com/watch?v=MVQbXSmZ4Uo>
