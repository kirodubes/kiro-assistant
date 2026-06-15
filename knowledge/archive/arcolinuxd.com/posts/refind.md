---
title: "Refind"
url: https://www.arcolinuxd.com/refind/
date: 2022-02-02 12:14:58
type: post
categories: ["Arch Way"]
source_site: arcolinuxd.com
---

# Refind

rEFInd

You can choose to install **rEFInd** instead of **Grub**. Tested on EXT4.
    
    
    pacman -S refind
    
    
    refind-install

Now we need to edit the /boot/refind_linux.conf and make it a writable partition.

Further study on my part is necessary.  
The refind.conf file contains lots of settings.  
More info on [Arch Linux](<https://wiki.archlinux.org/title/REFInd>) and on [Refind](<https://www.rodsbooks.com/refind/>).

![](https://www.arcolinuxd.com/wp-content/uploads/2021/12/efiboot0.jpg)![](https://www.arcolinuxd.com/wp-content/uploads/2021/12/efiboot1.jpg)
