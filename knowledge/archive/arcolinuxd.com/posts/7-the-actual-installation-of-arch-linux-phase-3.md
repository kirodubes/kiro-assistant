---
title: "7 The actual installation of Arch Linux Phase 3"
url: https://www.arcolinuxd.com/7-the-actual-installation-of-arch-linux-phase-3/
date: 2020-01-01 12:59:11
type: post
categories: ["Arch Way"]
tags: ["archlinux"]
source_site: arcolinuxd.com
---

# 7 The actual installation of Arch Linux Phase 3

let us get graphicalAll this time we have been in this terminal environment. We want to be able to install some kind of desktop environment now : xfce, openbox, i3, deepin, cinnamon,... anything...![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/displaygraphicsdisplaydesktop.png)These are the steps we need to take now.install display serverXORG

We investigate the matter on[ the Arch Wiki.](<https://wiki.archlinux.org/index.php/Xorg>)

We need to install the xorg packages. 
    
    
    sudo pacman -S xorg-server xorg-apps xorg-xinit

Xterm is optional.

Video: <https://youtu.be/NKKoLPsQ1KA>

graphics driver

The linux kernel can handle many  
graphical cards  
So try first without  
any extra installation

Ati - intel - nvidia![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-overview-drivers.jpg)**There is no need to install a driver in virtual box.** Start on the [xorg wiki page](<https://wiki.archlinux.org/index.php/Xorg>) find out what driver you need for your hardware. Most common hardware vendors are: 

  * nvidia
  * intel
  * amd/ati

With **lspci** you can find out what hardware you have in your computer. Then you need to investigate further to find out what driver you want to install. 
    
    
    lspci | grep -e VGA -e 3D

Then you need to continue your investigation or install with trial and error.

Video: <https://youtu.be/542tvN062rg>

install display managerlightdm![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-lightdm.jpg)We need to install a display manager or a login manager. [There are a lot of choices out there](<https://wiki.archlinux.org/index.php/display_manager>). Each with their advantages and disadvantages. We choose to install **lightdm**.We will install the desktop environment **Deepin** later on. We do **not** need to install **line 2** now. Deepin has its own lightdm greeter.
    
    
    sudo pacman -S lightdm
    
    
    sudo pacman -S lightdm-gtk-greeter lightdm-gtk-greeter-settings
    
    
    sudo systemctl enable lightdm.service

Do not FORGET TO ENABLE LightdmDo not reboot until you have a desktop environment

Video: <https://youtu.be/zaUVRD-HPV4>

Or install SDDM instead of Lightdm
    
    
    sudo pacman -S sddm
    
    
    sudo systemctl enable sddm.service

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-sddm.png)

CHOOSE  
YOUR  
DESKTOP  
is  
Phase 4

It helps to see your  
operating system as layers upon layers.

![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/building-blocks-arch.png)

[NEXT STEP](<https://www.arcolinuxd.com/choose-a-desktop/>)
