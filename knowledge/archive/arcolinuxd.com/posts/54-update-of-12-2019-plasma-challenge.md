---
title: "54 update of 12/2019 Plasma challenge"
url: https://www.arcolinuxd.com/54-update-of-12-2019-plasma-challenge/
date: 2019-12-02 23:07:44
type: post
categories: ["Plasma"]
source_site: arcolinuxd.com
---

# 54 update of 12/2019 Plasma challenge

![](https://www.arcolinuxd.com/wp-content/uploads/2019/12/fb-plasma.jpeg)![](https://www.arcolinuxd.com/wp-content/uploads/2019/12/arcolinuxb-plasma.jpeg)![](https://www.arcolinuxd.com/wp-content/uploads/2019/12/arcolinux-surfn-scaled.jpeg)

> The Plasma Challenge originated in beginning of **November 2018** and was never touched without filming it every step of the way.
> 
> We just keep on updating

ArcoLinux and Arch Linux is a rolling release linux distribution.

There are no half-yearly releases. Instead there are year round updates - some small - some large. The updates just keep coming in.

So there is no need to do a clean install. You can keep on rolling.

**And this is already the second ssd where I proof to you that it is possible to just keep updating.**

This ssd is now **1 year and 1 month** old. You can check this with the command **last**.

First we **update (Arch Linux and ArcoLinux).** Later we do a **upall** for the AUR packages.

We have **not** checked if we still have the fastest servers for Arch Linux servers with **mirrors**.

## TIP

**sudo pacman -S archlinux-keyrings**

if you get issues with keyrings. There was no need this time to do so during our update.

We will explain you the alias **skel** and its function and where the files and folders are : /etc/skel

We explain the alias **bupskel**.

We install also the last package of **arcolinux-lightdm-gtk-greeter-plasma** to get rid of a message.

We accept all name changes coming in during the update.

In dolphin we add the open the terminal here at the top.

When you do 2 bupskels, you can compare with meld to see what changed over time.

We install our new packages
    
    
    sudo pacman -S surfn-arc-breeze-git arcolinux-arc-kde

and we remove a dependency that is no longer needed.
    
    
    sudo pacman -R python2-xapp

Video: <https://youtu.be/LfoNfRU-I6M>

We totally forgot to do a skel, cb and check our rolling folders Skel = alias to copy/paste settings over We only have 2 mirrors - We need to get the new .bashrc in. The bashrc.latest contains all our new settings and aliases. 
    
    
    sudo pacman -S arcolinux-root-git

We are going to load the .bashrc with 
    
    
    cb

It will make sure the .bashrc-latest will applied everywhere. Then we take a look at ~/.bin/stay-rolling and see if we need to change anything. We install also 
    
    
    sudo pacman -S arcolinux-config-plasma-git

We show you some of the conkies that we have created for plasma.

Video: <https://youtu.be/HkHwk9Wrdaw>
