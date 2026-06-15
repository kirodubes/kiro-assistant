---
title: "How to change your grub theme"
url: https://arcolinux.com/how-to-change-your-grub-theme/
date: 2019-01-04 15:00:37
type: post
categories: ["Grub", "Themes", "Utilities"]
tags: ["grub"]
source_site: arcolinux.com
---

# How to change your grub theme

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-wallpaper.jpg)

**Just download and install. The easy installation is at the end of the article.**

First we visit the [Arch wiki page](<https://wiki.archlinux.org/index.php/GRUB>) to learn more about GRUB and the [tips and trics of GRUB](<https://wiki.archlinux.org/index.php/GRUB/Tips_and_tricks#Theme>).

We navigate to where the grub configuration file is and the grub themes are.

**/boot/grub/**

Copy/paste the original grub.cfg to have a backup. You will need it later.

****

**Start grub-customizer and choose your theme.**

Only the standard theme "**starfield** " will show up when you start it for the first time.

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-grubcustomizer-themes.jpg)

Choose the theme, save and reboot.

But first we use **meld** to **compare** the two files and learn from it.

Dimensions of grub will be  
small on virtualbox

This is the **vimix theme** from [gnome-look.org](<https://www.gnome-look.org/p/1009236/>). Found it later on the AUR as grub2-theme-vimix-git.

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-grub-vimix.jpg)

This is the **Arch silence** theme from [gnome-look.org](<https://www.gnome-look.org/p/1111545/>).

Arch Silence theme is actually in the **AUR** and lots more are in there. You try them out.  
https://aur.archlinux.org/packages/arch-silence-grub-theme/
    
    
    trizen arch-silence-grub-theme

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-grub-themes.jpg)

I do not see a setting to set everything back the way it was before grub-customizer. We had made a backup so we can set it now back. Comparing with meld again.

Video: <https://youtu.be/A-jKVSm8QI8>

Take a wallpaper as background

I continued to have some fun with a **wallpaper** I wanted to put as background in the grub.

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-wallpaper.jpg)![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-grub-ok.jpg)

THINGS CAN GO WRONG

I choose the **wrong** **font** here and was able to log back in.

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-grub-wrong-font.jpg)

Try it out on virtualbox first  
another example how to change  
your grub  
Download and install   
the Easy way

 

Video: <https://youtu.be/oUyDLkPwQu0>
