---
title: "ATT - Start with Xfce4 and add Gnome to your system"
url: https://www.arcolinuxd.com/att-start-with-xfce4-and-add-gnome-to-your-system/
date: 2021-07-11 06:35:03
type: post
categories: ["Phase 4"]
source_site: arcolinuxd.com
---

# ATT - Start with Xfce4 and add Gnome to your system

![](https://www.arcolinuxd.com/wp-content/uploads/2021/07/att-gnome.jpg)

We install **Gnome** on our Xfce desktop.

Remember to login with **Gnome** **Xorg** if you are working on VirtualBox.

We install specific Gnome packages.

Video: <https://youtu.be/xfIeqbm5Eec>

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
