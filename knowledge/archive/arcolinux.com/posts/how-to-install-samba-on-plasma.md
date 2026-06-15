---
title: "How to install Samba on Plasma"
url: https://arcolinux.com/how-to-install-samba-on-plasma/
date: 2020-06-14 09:54:00
type: post
categories: ["Samba"]
source_site: arcolinux.com
---

# How to install Samba on Plasma

![](https://arcolinux.com/wp-content/uploads/2020/06/plasma-share-samba-folder.jpg)

Our script works on the mainstream filemanagers and their desktops.

> caja - Mate
> 
> nautilus - Gnome and Budgie
> 
> dolphin - Plasma
> 
> nemo - Cinnamon
> 
> thunar - Xfce4, Openbox and all TWMs
> 
> deepin-file-manager - Deepin

There are more videos and articles about[ Samba here](<https://arcolinux.com/category/arcolinux/applications/samba/>).

This article is about installing **Samba** on ArcoLinux or Arch Linux.

After running this script(s) you will be able to share any directory in your home folder with any of the members in your home network. That is what [SAMBA](<https://wiki.archlinux.org/index.php/Samba>) is all about.

Check out what we deliver with our package arcolinux-bin-git.

You will find the samba scripts in this folder
    
    
    ~/.bin/main

We have these files:

140-install-samba that will install and activate samba - any desktop - ArcoLinux and Arch Linux

150-install-network-discovery that will allow you to see other computers in the network - any desktop - ArcoLinux and Arch Linux

This was already documented in the previous videos.

**install-samba-user-shares-for-every-desktop** is the new script.

Do not see any of these files, install this package:
    
    
    sudo pacman -S arcolinux-bin-git

![](https://arcolinux.com/wp-content/uploads/2020/06/nosharefolder.png)![](https://arcolinux.com/wp-content/uploads/2020/06/foldershare.png)

After running our scripts we have a **new tab** when we right click on a folder when we ask its properties.

Other filemanagers will have a separate line in the context menu to share.

In this new tab we tell how to share this folder. We can give it a name and allow certain people with the different permissions.

These settings will be reloaded after a reboot.

REBOOT AFTER ALL THE INSTALLATIONS

Video: <https://youtu.be/jQOwLubFL58>

Underneath you will find a video about the script itself.

We would like that you **think out of the box** if you encounter issues.

> Our improvement for samba shares on Plasma   
> comes from an article written for   
> Fedora 23.

Video: <https://youtu.be/WUuHib9ZPqs>

Navigating from Plasma to other computers in the network

Video: <https://youtu.be/5A5MDQkxUNg>
