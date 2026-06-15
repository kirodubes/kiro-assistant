---
title: "Fix for running out of space in /tmp directory"
url: https://arcolinux.com/fix-for-running-out-of-space-in-tmp-directory/
date: 2018-04-20 22:16:17
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fix for running out of space in /tmp directory

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-tmp-out-of-disk-space-error.png) Sometimes if the build is becoming too big you can run out of place. Tmp is too small or similar message shows up. This is the solution and there is no need to reboot. [More info on Arch Wiki](<https://wiki.archlinux.org/index.php/tmpfs>). 
    
    
    mount -o remount,size=4G,noatime /tmp

Please provide me with the **correct** **image** to display the error as I do not run into this issue.
