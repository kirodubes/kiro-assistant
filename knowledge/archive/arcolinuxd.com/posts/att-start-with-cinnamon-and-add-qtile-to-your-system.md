---
title: "ATT - Start with Cinnamon and add qtile to your system"
url: https://www.arcolinuxd.com/att-start-with-cinnamon-and-add-qtile-to-your-system/
date: 2021-07-11 06:42:35
type: post
categories: ["Phase 4"]
source_site: arcolinuxd.com
---

# ATT - Start with Cinnamon and add qtile to your system

![](https://www.arcolinuxd.com/wp-content/uploads/2021/07/xfce-qtile.jpg)

We start up with Cinnamon update, skel and reboot.

Then we install Qtile with the ATT.

You will see that the icons for the folders in thunar could be nicer. 

You still need to set the layout of Qtile. All the info can be found on this website.

Video: <https://youtu.be/rJ-IKR_xBPM>

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
