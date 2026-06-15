---
title: "Installation of Arch Linux UEFI with Jwm"
url: https://www.arcolinuxd.com/29-how-to-install-arch-linux-on-uefi-and-install-jwm-all-in-one/
date: 2020-04-22 10:55:11
type: post
categories: ["ArchWayDesktop"]
source_site: arcolinuxd.com
---

# Installation of Arch Linux UEFI with Jwm

![](https://www.arcolinuxd.com/wp-content/uploads/2020/04/archlinux-jwm.jpg)

We install Arch Linux on VirualBox with **UEFI** activated. [We use this tutorial](<https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-uefi/>).

We get our Arch Linux ISO from archlinux.org and boot from it.

The correct Virtualbox settings must be applied. Check them out.

Then we follow the guide.

Cloning a VirtualBox makes sense, reuse the work you have done.

And then install Deepin or Mate or Plasma or ...

Video: <https://youtu.be/6gVBsaJKc2w>

We start from the last video. We have a basic Arch Linux on our Virtualbox.

Now we need to install the desktop. Lightdm is already activated but there is no desktop behind it yet.

**We go to the TTY with Right-CTRL + F3.**

**On real metal you use Ctrl + Alt + F3**.

We install jwm with
    
    
    sudo pacman  -S jwm

Now we get our config.
    
    
    cp -i /etc/system.jwmrc ~/.jwmrc

**This is Jwm from Arch Linux.**  
Now you need to configure it.

Now we get our ArcoLinux packages into Arch Linux. ArcoLinux created an application for that called

arcolinux-spices

[Download it from here.](<https://arcolinux.info/download-applications/>)

Then we install it.

> Since there is no **polkit** yet, we have to run arcolinux-spices as sudo for certain buttons.

If you install **polkit-gnome** and reboot then you will see the normal popups to become root. We did not see those in the video because it was not installed yet.
    
    
    sudo pacman -S polkit-gnome

![](https://www.arcolinuxd.com/wp-content/uploads/2020/04/arch-jmw-polkit-gnome.jpg)

Arcolinux-spices needs to be run as **sudo** for certain buttons and **normal** **user** for others.

To get the**.bashrc** I need to start the arcolinux-spices as **Erik** and not as **Root**.

We install the package **arcolinux-jwm-git** to have our Jwm config and move it from /etc/skel to the home directory.

Then you need to figure out what is needed to get a working menu, working icons, etc.
    
    
    sudo pacman -S xdgmenumaker

We install also yay-bin.

We install our logout application.
    
    
    sudo pacman -S arcolinux-logout-git

We discover we need an extra dependency on a virgin Arch Linux. It is not an issue on ArcoLinux.

Because of the video we have added python-cairo to the pkgbuild. Problem solved for the Arch Linux users.

Video: <https://youtu.be/jb0CwXOlKVA>
