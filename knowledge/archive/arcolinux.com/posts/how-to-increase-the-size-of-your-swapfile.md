---
title: "How to increase the size of your swapfile"
url: https://arcolinux.com/how-to-increase-the-size-of-your-swapfile/
date: 2020-11-23 14:42:48
type: post
categories: ["System settings"]
source_site: arcolinux.com
---

# How to increase the size of your swapfile

![](https://arcolinux.com/wp-content/uploads/2020/11/swap-bigger.jpg)

Always think out of the box. Do not restrict yourself to just Arch Linux articles or ArcoLinux articles.

We use an article for [**Ubuntu**](<https://bogdancornianu.com/change-swap-size-in-ubuntu/>) to increase the swap file.

**Turn off all swap processes**
    
    
    sudo swapoff -a

**Resize the swap (from 512 MB to 8GB)  
**
    
    
    sudo dd if=/dev/zero of=/swapfile bs=1G count=8

if = input file  
of = output file  
bs = block size  
count = multiplier of blocks

**Make the file usable as swap**
    
    
    sudo mkswap /swapfile

**Activate the swap file**
    
    
    sudo swapon /swapfile

**Check the amount of swap available**
    
    
    grep SwapTotal /proc/meminfo

Or use applications such as htop, gtop, glances and others.

Video: <https://youtu.be/A11mNnLQI_o>

# Here is an older video that might interest you as well.

Video: <https://youtu.be/bE0-4Dt6lrM>
