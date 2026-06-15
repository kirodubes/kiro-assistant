---
title: "All in one Arch Linux installation BIOS with Fvwm"
url: https://www.arcolinuxd.com/all-in-one-arch-linux-installation-bios-with-fvwm/
date: 2021-05-05 16:25:09
type: post
categories: ["ArchWayAllinone", "ArchWayDesktop"]
tags: ["aio", "archlinux"]
source_site: arcolinuxd.com
---

# All in one Arch Linux installation BIOS with Fvwm

![](https://www.arcolinuxd.com/wp-content/uploads/2021/05/fvwm.jpg)

It takes 20 minutes to install Arch Linux.

This video will give you an overview of all the necessary steps to take.

We install version 2 of Fvwm coming from Arch Linux repositories.  
**ArcoLinux** uses version 3 of Fvwm coming from AUR.

We follow [the guide of this page](<https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-bios/>) and will compare it with the [Arch Linux installation page](<https://wiki.archlinux.org/index.php/Installation_guide>).

This video will guide you  
through Phase 1, 2, 3 and 4  
of OUR Arch Linux installation guide  
this is an ALL IN ONE installation

Video: <https://youtu.be/itiwCtjzJk0>

In phase 4 we choose our desktop

We can install **lightdm** , **lightdm-gtk-greeter** and **lightdm-gtk-greeter-setttings** but ...

> we choose sddm and enabled that.

We need to install our desktop now.
    
    
    sudo pacman -S fvwm

Fvwm provides a config to work with and we decide to take a look.

We will copy/paste over the default config of the developers.
    
    
    mkdir ~/.fvwm
    cp -r /usr/share/fvwm/default-config/* ~/.fvwm

There is still much work in your configs for fvwm to become a functional and beautiful desktop.

That can be a challenge.
