---
title: "Installation of Xfce on Arch Linux Phase 4"
url: https://www.arcolinuxd.com/9-installation-of-xfce-on-arch-linux-phase-4/
date: 2018-09-20 08:54:48
type: post
categories: ["ArchWayDesktop"]
tags: ["arch installation", "archlinux"]
source_site: arcolinuxd.com
---

# Installation of Xfce on Arch Linux Phase 4

install desktop environment XFCE ![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-xfce-1.jpg)Installing xfce4 requires only a few lines. Theming and tweaking your Arch Linux system will require more time. All the information about this desktop is here: <https://wiki.archlinux.org/index.php/xfce>
    
    
    sudo pacman -S xfce4
    sudo pacman -S xfce4-goodies

If you **forget** to activate the **lightdm.service** in the previous article you will **never** be able to boot into the **graphical** environment. I forgot that and I **fix** it here. 

Video: <https://youtu.be/Nu5mNrFebi4>

ArcoLinuxD github is the source 

We will get our scripts from our github. Change the scripts any way you want. That is the idea. Add lines for extra software. Hashtag out software you do not want. Then run the scripts.
    
    
    sudo pacman -S git
    git clone https://github.com/arcolinuxd/arco-xfce

Then we have the scripts on our system. You decide what you run or not.

There is also a folder called **Arch Way**. This folder will contain all the scripts for people who do an Arch Linux installation. 

Video: <https://youtu.be/upDlwB2Lj4M>

After some theming and tweaking you can end up with this desktop environment. ![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-xfce-vb.jpg)![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-xfce-theming.jpg)

After some theming and tweaking you can end up with this desktop environment.

We change the name of the **whiskermenu** from ArcoLinux to Arch Linux Xfce.

We also change the logo's to Arch Linux everywhere.

We get the .**bashrc** from ArcoLinux to get **upall** and **mirror** for example. [More info about getting .bashrc](<https://www.arcolinuxd.com/24-getting-the-bashrc-from-arcolinux-on-arch-linux/>).

**sudo pacman -S reflector** — You need to install **reflector** to use mirror.

We activate a conky and change the logo.

We change the theme, icons and cursor.

We also install the arcolinux-nemesis scripts that I normally use after a clean install of ArcoLinux. You decide if you will install those.

Video: <https://youtu.be/9EOzv7sXi88>
