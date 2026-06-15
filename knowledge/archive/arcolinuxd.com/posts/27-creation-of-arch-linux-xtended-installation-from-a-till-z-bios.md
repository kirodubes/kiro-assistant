---
title: "Creation of Arch Linux Xtended - installation from A till Z - BIOS"
url: https://www.arcolinuxd.com/27-creation-of-arch-linux-xtended-installation-from-a-till-z-bios/
date: 2019-11-03 15:54:14
type: post
categories: ["Arch Way", "ArchWayAllinone", "ArchWaySpices"]
source_site: arcolinuxd.com
---

# Creation of Arch Linux Xtended - installation from A till Z - BIOS

![](https://www.arcolinuxd.com/wp-content/uploads/2019/11/archlinux-xtended.png)

Begin November 2019 we launched an ISO to promote the tiling window managers.

**ArcoLinuxB Xtended**

[This is the release article to read more about it.](<https://arcolinux.info/launch-of-a-new-project-called-arcolinuxb-xtended/>)

![](https://www.arcolinuxd.com/wp-content/uploads/2019/11/ArcoLinuxB_Xtended.png)

Let us create something similar starting from Arch Linux

**Arch Linux Xtended**

This time however we will not install Openbox just the TWMs. 

![](https://www.arcolinuxd.com/wp-content/uploads/2019/11/archlinux-xtended-post.png)

Beware  
I forgot the step of the locale in phase 1

 

ArcoLinux is based on Arch Linux so we always follow the progress/news at https://arcolinux.org.

First we download the Arch Linux ISO via torrent.

We have a virtualbox set up as a BIOS environment [so later we will follow this article](<https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-bios/>).

> The goal is an all in one installation from A till Z and install 6 tiling window managers (see above image).

Our typo had no consequences at 6:17.

**We check which of the Arch Linux servers is the fastest. We show you how.**

Always type the command to enable the lightdm service before rebooting
    
    
    systemctl enable lightdm

There is no desktop behind the lightdm. We show you how to solve that.

Go to the TTY with ctrl + alt + F2 or on virtualbox Right Ctrl + F2.

> Getting the spices in means getting arcolinux packages from the ArcoLinux repos.

We get the desktop related package in.
    
    
    sudo pacman -S arcolinux-i3-git

**I messed up** the copy/paste over from /etc/skel to the home directory.

I will show you how to fix it.

We install **termite** and **thunar** to be able to work in i3 afterwards.

We install **arcolinux-xfce-git** for more settings for thunar.

We install **arcolinux-root-git** to get our .bashrc.

We get our own .bashrc in. Afterwards we can use aliases like cb, update, bupskel, upall.

We install **yay** and **sublime** -**text**.

We install **neofetch**.

We install **arcolinux-termite-themes**.

We install **sardi-icons**.

We install **arcolinux-config-i3-git**.

We install **arcolinux-arc-themes-nico-git.**

We did not install the **arc-gtk-theme** hence it stayed white.

We install our own ArcoLinux lightdm greeter - settings and the **arcolinux-wallpapers-git**.

We investigate the i3status error and we figure out here that we skipped a part in phase 1 Arch Linux installation.

> We forget to set our locale!!

We install **variety** and **nitrogen** to set wallpapers.

For variety to work we probably still need **feh**.

We install the **dmenu** to have a menu at the top.

With setxkbmap be I always set my keyboard to be until I got tired of typing it.

To set the keyboard forever then I need this code found on the [arch wiki](<https://wiki.archlinux.org/index.php/Xorg/Keyboard_configuration#Using_X_configuration_files>).
    
    
    localectl set-x11-keymap be

We install **compton for transparency of the terminals.**

We set our own ArcoLinux gtk greeter.

We install **polkit-gnome**.
    
    
    Use the knowledge from our githubs to figure out the pieces of the puzzle.

We install the package **meld** to compare two folders with each other.

**Now we get all the Tiling Window Managers in.**

We install the desktop packages in from ArcoLinux but we should get the applications themselves as well.

We get polybar in but first make sure all cores are set to work - otherwise it will take longer.

We install the packages themselves

awesome vicious bspwm sxhkd herbstluftwm qtile xmonad haskell-dbus xmonad-contrib arcolinux-polybar-git

We should install **rxvt-unicode** to have a terminal in Xmonad. 

We should have **oblogout** and also the **themes** for it.

We install **python-psutil** for qtile.

We also get our awesome font in -**awesome-terminal-fonts** for qtile.

We need another font for awesome -- **ttf-font-awesome**. 

We figure it we need fonts for awesome - **noto-fonts**.

 

EXPERIMENT EXPERIMENT EXPERIMENT  
HAVE FUN

Video: <https://youtu.be/3TS7aD4dJ7U>
