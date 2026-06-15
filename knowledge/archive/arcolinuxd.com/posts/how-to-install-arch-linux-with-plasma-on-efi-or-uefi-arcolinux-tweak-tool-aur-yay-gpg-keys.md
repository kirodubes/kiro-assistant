---
title: "All in one Arch Linux installation UEFI with Plasma - ArcoLinux Tweak Tool - AUR Yay - GPG keys"
url: https://www.arcolinuxd.com/how-to-install-arch-linux-with-plasma-on-efi-or-uefi-arcolinux-tweak-tool-aur-yay-gpg-keys/
date: 2020-02-20 21:11:28
type: post
categories: ["ArchWayAllinone", "ArchWaySpices"]
source_site: arcolinuxd.com
---

# All in one Arch Linux installation UEFI with Plasma - ArcoLinux Tweak Tool - AUR Yay - GPG keys

![](https://www.arcolinuxd.com/wp-content/uploads/2020/02/archlinux.jpg)

We start with downloading the latest Arch Linux from archlinux.org with ktorrent.  
We set up our Virtual Box and go over the settings.  
We will install this Arch Linux as an UEFI system and make sure you have the right graphics controller.

[We follow all the steps from this page.](<https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-uefi/>)

Video: <https://youtu.be/wW4kfhbMDts>

In the next video we do not have a terminal yet. Just xterm.

We set our keyboard first via terminal but you can set it in system settings of Plasma as well.

We install Neofetch to show we are on ArcoLinux.

We install Konsole. We tweak Konsole a bit.

We want to install yay. You can either build it via this tutorial or you can download it from Seedhost.

We install also the arcolinux-tweak-tool-git. We need to download also the dependency arcolinux-mirrorlist-spinoff-git. Then we can install the ArcoLinux Tweak Tool.

We do not have a file manager yet. So we install Dolphin.

We open /etc/pacman.conf and want to edit this file.

We need an editor.

We install Atom.

We show you how the pacman tab of the tweak tool works.

We create a custom shortcut for konsole.

We are still missing arcolinux-mirrolist-git. We get it from seedhost and install it.

The error we get is because pacman.conf is pointing to something that we want to install.

The story about the chicken and the egg.

We need to deactivate the repos of ArcoLinux then we can install the package with sudo pacman -U.

We install yakuake. F12 is the keyboard shortcut.

We first type sudo pacman -Syyu to get the database from the ArcoLinux repositories.

We fix the gpg key problem with code coming from github.com/arcolinuxd.

There is a folder ArchWay. That contains everything you need on Arch Linux.

We install arcolinux-root-git to get our .bashrc in.

Hblock of ArcoLinux can be installed automatically with the ArcoLinux Tweak Tool.

As an extra exercise we activate the repo of Hefftor and get his wallpapers in.

Video: <https://youtu.be/39SpDOCH-T4>

In the next video I just have some fun with all the packages available on the repo of Hefftor.

> Create your own .config files  
> Make a package  
> Share them on a repo  
> Share your creativity with others  
> Give us more lego blocks to play with

Video: <https://youtu.be/p3SE9PckLCo>
