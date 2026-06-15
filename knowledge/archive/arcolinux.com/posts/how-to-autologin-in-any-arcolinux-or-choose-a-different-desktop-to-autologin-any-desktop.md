---
title: "How to autologin in any ArcoLinux or choose a different desktop to autologin - any desktop"
url: https://arcolinux.com/how-to-autologin-in-any-arcolinux-or-choose-a-different-desktop-to-autologin-any-desktop/
date: 2018-12-30 22:16:46
type: post
categories: ["Login", "Post-installation"]
tags: ["anydesktop", "autologin", "login"]
source_site: arcolinux.com
---

# How to autologin in any ArcoLinux or choose a different desktop to autologin - any desktop

![](https://arcolinux.com/wp-content/uploads/2018/12/lightdm.jpeg)

This procedure will work on 

  * ArcoLinux
  * ArcoLinuxD
  * ArcoLinuxB
  * Arch Linux



All you need to remember is that we work with [lightdm display manager](<https://wiki.archlinux.org/index.php/LightDM>).

You can find the lightdm configuration files in /etc/lightdm.

Edit the **/etc/lightdm/lightdm.conf** with sublime text.

Choose to view it as **PERL** at the bottom right.

And change the relevant lines and use your own login name.

## ArcoLinux Iso

If you want to autologin into i3 then you change the lines like this.

**user-session=i3**  
**autologin-user=erik**  
**autologin-session=i3**

If you want to autologin into openbox then you change the lines like this.

**user-session=openbox**  
**autologin-user=erik**  
**autologin-session=openbox**

If you want to autologin into xfce again then you change the lines like this.

**user-session=xfce**  
**autologin-user=erik**  
**autologin-session=xfce**

You do not want to autologin at all. But you like to login into xfce.

**user-session=xfce**  
**#autologin-user=erik**  
**#autologin-session=openbox**

## ArcoLinuxD Iso

**ArcoLinuxD** has a script to change the lightdm.conf.  
You can still change it manually as well.

## ArcoLinuxB Iso

**ArcoLinuxB iso** is based upon **ArcoLinux iso**.

**Therefor** the /etc/lightdm/lightdm.conf will always contain **xfce** as default desktop.   
Calamares, our installer, will not change the content of lightdm.conf for you.

You need to change **xfce** **manually** into **your** **desktop** like awesome, bspwm, plasma, cinnamon, mate, ...  
You can always find the name of your desktop in this folder : **/usr/share/xsessions**.

## Arch Linux Iso

When working with **Arch Linux** we will download our scripts from <https://github.com/arcolinuxd>. All the desktops are hosted there.

You can use the **same** **script** we use on the **ArcoLinuxD iso**.

Video: <https://youtu.be/74iVGW_jnsM>
