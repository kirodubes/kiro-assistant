---
title: "Fix for error no space left on device"
url: https://arcolinux.com/fix-for-error-no-space-left-on-device/
date: 2017-11-29 08:21:36
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fix for error no space left on device

![](https://arcolinux.com/wp-content/uploads/2017/11/error-no-space-left-on-device.jpg)

When making the article about upgrading ArchMerge 6.1 to 6.2 we encountered an error that I had to fix already several times. It deserves to have its own 'fix article'.

How to fix this error message : **no space left on device**

Solution :
    
    
    mount -o remount,size=4G,noatime /tmp

Change the size to 6G (or 6 gigabyte or more if needed)

Source: <https://wiki.archlinux.org/index.php/tmpfs>

Start watching at 29:07 

Video: <https://www.youtube.com/watch?v=kfgRXJEe1A0>
