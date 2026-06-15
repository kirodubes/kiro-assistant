---
title: "32 installation, configuration and theming of latte-dock"
url: https://www.arcolinuxd.com/32-installation-configuration-and-theming-of-latte-dock/
date: 2018-11-20 10:42:50
type: post
categories: ["Plasma"]
tags: ["theming"]
source_site: arcolinuxd.com
---

# 32 installation, configuration and theming of latte-dock

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/latte-plank-equal.jpeg)![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/plank-latte-settings.jpeg)![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/plank-latte.jpeg)

Top = Latte-Dock Right = Plank   
in all 3 images

Latte-dock is an alternative you can choose for plank when on Plasma.

> Latte-dock is created for Plasma.

You see all the dependencies when you install it on Xfce or other desktops.

You can check out its [github here](<https://github.com/psifidotos/Latte-Dock>).

> Latte is a dock based on plasma frameworks that provides an elegant and intuitive experience for your tasks and plasmoids

This is the line you can read on their github. The essence of what Latte is.

Latte will be **autostarted** next time (you can find the setting in the configuration) - that is an advantage.

We go over the most important settings and download a new latte dock configuration and remove it afterwards as well.

## Preserve files for later use 

Latte saves its settings here : 

  * ~/.config/lattedockrc
  * ~/.config/latte
  * ~/.local/share/latte-layouts



## F.A.Q.

If you have issues then read their long frequent asked questions page

<https://github.com/psifidotos/Latte-Dock/wiki/F.A.Q.>

Video: <https://youtu.be/rpzYVkVdM1o>

remove plank and its themes
    
    
    sudo pacman -R plank arcolinux-plank-themes-git

Or just delete the file in ~/.config/autostart and plank becomes another file on your system and will never autostart.

Video: <https://youtu.be/8PjAPf4JFSY>

## **Plasma Challenge**

You can follow our tutorials based on either of two ISO's.

**1\. ArcoLinuxB Plasma (recommended)**

We record the plasma video's on an SSD installed from the **ArcoLinuxB Plasma ISO**.  
You can either **create** your very own ArcoLinuxB Plasma ISO [following this tutorial](<https://arcolinuxb.com/byoi-on-arcolinux-plasma/>) or [download it from Sourceforge](<https://sourceforge.net/projects/arcolinux-community-editions/files/plasma/>). (ArcoLinuxB-plasma-18.11.2.ISO of 4.3 GB - games included)

**2\. ArcoLinuxD Plasma**

You can also use the ArcoLinuxD ISO and then install Plasma with the help of the github scripts. This will not be an exact copy of the ISO.

> Learn about the Plasma desktop and enjoy it.
