---
title: "How to add spices to Arch Linux Xfce - conkies - bashrc"
url: https://www.arcolinuxd.com/how-to-add-spices-to-arch-linux-xfce-conkies-bashrc/
date: 2018-12-08 10:48:22
type: post
categories: ["Arch Way", "ArchWaySpices"]
tags: ["archlinux", "conky", "spiceup"]
source_site: arcolinuxd.com
---

# How to add spices to Arch Linux Xfce - conkies - bashrc

![](https://www.arcolinuxd.com/wp-content/uploads/2018/12/archlinux-lazuli.jpg)

The topic of the video is how to get the conkies in on Arch Linux but since I jumped into a working system of Arch Linux Xfce some of the things were already installed and others not.  
ArcoLinux has evolved since the last time I was on this virtualbox and we need to update this system as well to 18.12 of ArcoLinux.

We first explain the use of desktoppr.co. A great way to share wallpapers with each other.

We check what is inside **/etc/pacman.conf** and we update that one.

We talk about the importance to get the very last code from the github.

**git pull** is my preferred solution.

We update your system with **update**.

Pamac needed to update. We use normally upall but that was still based on yaourt so we need to install an AUR helper.

We uninstall yaourt first.
    
    
    sudo pacman -Rs yaourt

Then we install yay with a pkgbuild.

Then we install pamac-aur with yay.

We see the icons are not "nice" and we install the newest version of the sardi-icons.

We need to uninstall some sardi icons
    
    
    sudo pacman -R sardi-mono-mixing-icons-git sardi-flexible-mixing-icons-git

When we open pamac the icons of sardi have been applied and it is now easier to see what is installed and what not.

We go over the list and install some packages just to show how it is done. Discord is our way to communicate with each other.

ArcoLinux-root is installed meaning the latest bashrc should be there in /etc/skel.

We copy/paste the content of /etc/skel to the home directory.

We compare .bashrc with .bashrc-latest.

We test out **mirror** and install the required applications for it to work and more apps for other aliases
    
    
    sudo pacman -S reflector youtube-dl expac

 

## What do you need for the conkies to work?

**conky-lua-archers**

**arcolinux-conky-collection-git**

**arcolinux-pipemenus-git**

 

Video: <https://youtu.be/_uXehLxaHXI>
