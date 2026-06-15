---
title: "How to change the language of your desktop on ArcoLinux or Arch Linux - ANY DESKTOP"
url: https://arcolinux.com/how-to-change-the-language-of-your-desktop-on-arcolinux-or-arch-linux-any-desktop/
date: 2019-11-08 22:10:29
type: post
categories: ["Language", "Post-installation", "Pre-installation"]
source_site: arcolinux.com
---

# How to change the language of your desktop on ArcoLinux or Arch Linux - ANY DESKTOP

![](https://arcolinux.com/wp-content/uploads/2019/11/change-language.jpg)![](https://arcolinux.com/wp-content/uploads/2019/11/pacman-french.jpg)

Choose the correct language in Calamares

Best tip ever

**We would like to change our language from English to French.**

First you check if the desktop provides you an application - in settings or so to change the language.

Secondly we check if there is an application missing from Arch Linux repo's or from AUR.

Thirdly we use the information from the **Arch Wiki**.

let us use the arch wiki

remember the word locale

The page you need now is the[ locale from Arch Wiki](<https://wiki.archlinux.org/index.php/Locale>).

We recommend you see at least one video from an [all-in-one Arch Linux installation](<https://arcolinuxd.com/category/arch-way/aio/>). It provides you with all the essential information of your system.

Or you can just look at the [Arch Way installation Phase 1](<https://arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-bios/>) and look for the word **locale**. 

We select the proper language in this long list.
    
    
    sudo nano /etc/locale.gen

Then we generate a new language with
    
    
    sudo locale-gen

calamares added the language  
at the bottom

We edit /etc/locale.conf manually to reflect the language we want. No typos allowed. 
    
    
    sudo nano /etc/locale.conf

We change the language in this file and save it. We unset the variabel LANG - no language afterwards anymore. 
    
    
    unset LANG

Not sure if the next line is still needed here - you will be the judge of that - I think it was the autologin lightdm that was playing tricks on me. 
    
    
    sudo locale-gen

Than we reboot.

IF you use autologin  
logout and log back in  
do that even twice

Video: <https://youtu.be/poXvZt9iBV0>

If you autlogin, then log back out.

**You may have to do this even twice before your language kicks in.**
