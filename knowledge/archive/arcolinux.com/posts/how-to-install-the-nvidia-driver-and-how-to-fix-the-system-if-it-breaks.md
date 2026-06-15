---
title: "How to install the nvidia driver and how to fix the system if it breaks - April 2018"
url: https://arcolinux.com/how-to-install-the-nvidia-driver-and-how-to-fix-the-system-if-it-breaks/
date: 2018-04-27 10:50:35
type: post
categories: ["Fixes", "Nvidia", "Post-installation"]
tags: ["fix", "nvidia"]
source_site: arcolinux.com
---

# How to install the nvidia driver and how to fix the system if it breaks - April 2018

We concentrate all our arch-chroot information in this article.  
<https://www.arcolinuxd.com/10-use-the-power-of-arch-chroot-when-your-computer-crashes/>

![](https://arcolinux.com/wp-content/uploads/2018/04/computer-crash.jpg)

We are working on a motherboard of Asus P8Z77-V LE and have an Nvidia Geforce GTX970.

[In this tutorial](<https://arcolinux.com/how-to-find-out-what-driver-to-install-for-your-nvidia-card/>) we have seen how I knew what package to install for this card.

**BUT what do you do when you broke your system** because you installed (in this case intentionally) the wrong drivers.

A clean install is always a good answer (if you keep your most important files in cloud services) but lets try to figure it out without reinstalling.

We install the wrong drivers for our Nvidia card and it will break the system.

This installation will **break** my system. I do this for educational purposes. Showing you how to fix your computer afterwards.
    
    
    sudo pacman -S nvidia-340xx

When your system crashes, you might still be able to go into a **TTY**.

**CTRL + ALT + F2, F3, F4, F5 and F6**

**Virtualbox : RIGHT-CTRL +F2, F3, F4, F5 and F6**

> TTY = TeleTYpewriter

Sources :  
<https://en.wikipedia.org/wiki/Terminal_emulator>  
<https://en.wikipedia.org/wiki/Computer_terminal>

![](https://arcolinux.com/wp-content/uploads/2018/04/tty2.jpg)

We see the image above that we are in **TTY2.**

Then you have to retrace your steps. What did I do to get here? Did I install something? Was there an update gone wrong?

In our case we installed the wrong nvidia drivers so we uninstall them with
    
    
    sudo pacman -R nvidia-340xx

and reboot and we are back in the system using the nouveau driver.

Then we will install the proper driver for this system with **Nvidia GTX970** :
    
    
    sudo pacman -S nvidia

You can also install the nvidia utilities if you like with
    
    
    sudo pacman -S nvidia-utils

To be able to install my drivers I first had to uninstall all the left-overs of previous installations. Always try to start with a clean slate.

Use **sudo pacman -R nvidia** and press twice on TAB to see what you have as left-overs and remove before attempting a new driver.

If you can not get into TTY then there is second way to fix your computer and we will change the root with **arch-chroot** command.

You can follow [this article from the Arch Way installation](<https://arcolinuxd.com/10-use-the-power-of-arch-chroot-when-your-computer-crashes/>) series or this one.

Video: <https://youtu.be/-XRRkHmmALw>
