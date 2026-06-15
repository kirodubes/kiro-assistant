---
title: "All in one Arch Linux installation BIOS with Xmonad"
url: https://www.arcolinuxd.com/22-all-in-one-arch-linux-installation-bios-with-xmonad-aio/
date: 2018-12-30 17:05:37
type: post
categories: ["ArchWayAllinone", "ArchWayDesktop"]
tags: ["aio", "arch installation", "tty"]
source_site: arcolinuxd.com
---

# All in one Arch Linux installation BIOS with Xmonad

![](https://www.arcolinuxd.com/wp-content/uploads/2018/12/archlinx-xmonad.jpg)

It takes 20 minutes to install Arch Linux.

This video will give you an overview of all the necessary steps to take. You willl have a working system with Xmonad desktop.

We follow [the guide of this page](<../5-the-actual-installation-of-arch-linux-phase-1-bios/>).

This video will guide you  
through Phase 1, 2 and 3  
of the Arch Linux installation guide

Video: <https://www.youtube.com/watch?v=sq_sMamdAfU>

In phase 4 we choose our desktop

We have the **standard** **lightdm** , **lightdm-gtk-greeter** and **lightdm-gtk-greeter-setttings** installed but we still do not have a desktop.

Basically we can not login as lightdm can not start anything.

With **right** **CTRL** and **F2** or F3 etc you can go to a **TTY** and run your commands.

(CTRL + ALT + F2 on ssd) 

Installing **Xmonad** is more complex than installing Xfce for example.  
We learn from the[ Arch Wiki](<https://wiki.archlinux.org/index.php/xmonad>) that we need to install these packages.
    
    
    sudo pacman -S xmonad xmonad-contrib

We will also install these packages
    
    
    sudo pacman -S xmonad-utils xmobar

We will later install **xmonad-log** from AUR.

Since Xmonad does **not** provide a config to work with we decide quite rapidly to get all the needed packages from the **ArcoLinuxD** **github**.
    
    
    sudo pacman -S git
    git clone https://github.com/arcolinuxd/arco-xmonad

In the video we will go over all the scripts and select them one by one and discuss them.

 

We can run **script 400** since it uses the Arch repositories and all we need is **pacman**.

We show you what you need to do if you want to "spice up" your Arch Linux with ArcoLinux packages or "spices". Check the folder Arch Way for that.

> Importing the keys can take a while.

We are adding the ArcoLinux repos to /etc/pacman.conf.

We add a new repo to /etc/pacman.conf to be able to install **trizen** and **yay** called **arcolinux_repo_ISO**.

Then we install our AUR helpers
    
    
    sudo pacman -S yay trizen

Now we can run script nr 500 with uses yay and trizen to install packages from AUR.

> nomad-log is now installed.

Running **script** **600** will import the the **configuration** of **Xmonad**. That is the most important. But we will need the others too.

We resolve the conflict between lightdm and arcolinux-lightdm by removing the standard Arch Linux package.
    
    
    sudo pacman -R lightdm-gtk-greeter lightdm-gtk-greeter-settings

After this line you can restart script 600 and there will be no conflicts.

Fonts are important so we install script 700. 

Video: <https://www.youtube.com/watch?v=KeXPlFK2Hmo>

Tweaking our installation

We install more packages in this video but first we check if we did not forget to run any script. It **skips** anything that is already installed. So no danger there.

I misspoke in the video - I did not install bluetooth but sound instead.

Script 200 and 300 will be installed as well.

A tiling window manager uses keyboard shortcuts to run its applications. If you do not install the packages behind the keyboard shortcut, nothing will happen.

##  Azerty and Qwerty

**setxkbmap be** will change by keyboard to azerty.  
But it is also defined in the **autostart.sh** file in ~/.xmonad/scripts.

More info about setxkbmap on the [Arch Wiki](<https://wiki.archlinux.org/index.php/Xorg/Keyboard_configuration#Using_setxkbmap>).

## bashrc is not the bashrc from ArcoLinux

We get our content from bashrc from ArcoLinux so that commands like **update** , **upall** , **skel** , ... will work.

 

Then we discover that there are aliases that work with applications that we have installed on ArcoLinux but not on Arch Linux.

Since the video there is a script for those packages in the Arch Way folder for

  * reflector
  * youtube-dl
  * expac
  * hwinfo
  * and maybe more to follow in the future hence the script.



Then we start tweaking the system and we change the

  * icons
  * themes
  * cursors



Video: <https://www.youtube.com/watch?v=UdzL1mrJc1o>

AUTOLOGIN in LIGHTDM

This applies **to any desktop environment** as long as you are using **lightdm**. 

All we need to do, is to make script 800 work on Arch Linux.

On ArcoLinux we created a group called autologin.

On Arch Linux **you** need to take care of that. (see **script** in folder Arch Way)

Let us now create a system group called autologin.
    
    
    sudo groupadd -r autologin

Now you can run script 800 to change the settings of lightdm and add your personal account to this newly created group called autologin.

Video: <https://www.youtube.com/watch?v=_7tN4Ywpl-4>

If and when updates of **haskell** or **Xmonad** come in. 

Recompile **Xmonad** after installation - **do not reboot before recompiling**.
    
    
    xmonad --recompile

or

Super + Shift + R

Video: <https://www.youtube.com/watch?v=mxiyGHJM9vY>
