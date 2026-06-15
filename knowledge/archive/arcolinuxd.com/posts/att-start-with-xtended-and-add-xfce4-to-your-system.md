---
title: "ATT - Start with Xtended and add Xfce4 to your system"
url: https://www.arcolinuxd.com/att-start-with-xtended-and-add-xfce4-to-your-system/
date: 2021-07-11 06:41:31
type: post
categories: ["Phase 4"]
source_site: arcolinuxd.com
---

# ATT - Start with Xtended and add Xfce4 to your system

![](https://www.arcolinuxd.com/wp-content/uploads/2021/07/xtended-xfce-att.jpg)

Xtended has been created to promote Tiling Window Managers but Openbox can still be uncomfortable.

Let us install **Xfce4** via the ATT.

July 2021 we downgrade xorg-server for Xfce4 and VirtualBox. Real metal installations are not affected.

Video: <https://youtu.be/liRUKwpZqaE>

If you have an **error** in our **ArcoLinux Tweak Tool or ATT** you start the tool from the terminal.
    
    
    arcolinux-tweak-tool

**Pacman** will/might give a clue why the installation has failed.

There are so many reasons why it can go wrong. **Analysis** is then required.

Packages not present, conflicting packages, Arch Linux server down, ArcoLinux server down, key issues,...

**Removing** the **desktop** can be achieved by removing the most important packages.

It is not always possible for example with Plasma. Then you do a clean install.

You can use our [cheatsheet](<https://www.arcolinux.info/arcolinux-cheatsheet/>) to know what packages to remove
    
    
    sudo pacman -R ...
    
    sudo pacman -Rs ...
