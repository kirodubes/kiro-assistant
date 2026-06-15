---
title: "ATT - Start with Xfce4 and add openbox and i3 to your system"
url: https://www.arcolinuxd.com/att-start-with-xfce4-and-add-openbox-and-i3-to-your-system/
date: 2021-07-11 06:38:12
type: post
categories: ["Phase 4"]
source_site: arcolinuxd.com
---

# ATT - Start with Xfce4 and add openbox and i3 to your system

![](https://www.arcolinuxd.com/wp-content/uploads/2021/07/xfce-openbox-i3.jpg)

We talk about the look of this Xfce4 and refer you to the articles on [https://arcolinuxb.com](<https://arcolinuxb.com/personal/>), the personal folder and personal alias.

We update the system and we use our ATT to install **Openbox** and **I3wm**. This used to be our old flagship combo for years.

Video: <https://youtu.be/smKrUZxdTVE>

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
