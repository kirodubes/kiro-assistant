---
title: "50 update of 07/2019 Plasma challenge"
url: https://www.arcolinuxd.com/50-update-of-07-2019-plasma-challenge/
date: 2019-07-29 09:30:38
type: post
categories: ["Plasma"]
source_site: arcolinuxd.com
---

# 50 update of 07/2019 Plasma challenge

![](https://www.arcolinuxd.com/wp-content/uploads/2019/07/meld-plasma.jpeg)

> The Plasma Challenge originated in beginning of **November 2018** and was never touched without filming it every step of the way.
> 
> We just keep on updating

ArcoLinux and Arch Linux is a rolling release linux distribution.

There are no half-yearly releases. Instead there are year round updates - some small - some large. The updates just keep coming in.

So there is no need to do a clean install. You can keep on rolling.

And this is already the second ssd where I proof to you that this is possible to just keep updating.

This ssd is now 9 months old. You can check this with the command **last**.

First we **update (Arch Linux and ArcoLinux).** Later we do a **upall** for the AUR packages.

We also check if we still have the fastest servers for Arch Linux servers with mirrors.

## TIP :

**sudo pacman -S archlinux-keyrings**

if you get issues with keyrings.

**CTRL + Printscreen** does not seem to work. Let us make a keyboard shortcut for **spectacle**.   
We change the standard image output from PNG to JPEG.

We analyze we need to launch it with 
    
    
    spectacle -gui

We reboot after all the installations.

Video: <https://youtu.be/88piytpcu-c>

When I booted up, I clicked on the notification from the network manager and I have set it to off. It will never show a message again.

We rebooted and have the kernel 5.2.3 running.

CTRL + Printscreen is checked. We needed to reboot for the errors to disappear.

We delete libnm-gtk.

And delete screenkey as well and replace it with screenkey-git with yay.

**Numeric keypad** is not on. We change the setting in plasma.

Input Devices / Keyboard/ Hardware/ Turn on Numlock on Plasma startup.

We explain how AUR works. Talk about maintainers, flagging out of date, PKGBUILD, ...

We fix the bookmarks in Vivaldi first

I will now install drivers for a new keyboard I bought. Corsair Strafe MK.2.

We see that there is an Arco-Plasma and explain you get do a git pull if it is an actual github.

It may help you with an issue you are having. We update our scripts all the time.

We organize our folders a bit and get the nemesis github in.

git clone <https://github.com/erikdubois/arcolinux-nemesis>

Change what you downloaded - make your own scripts.

After a clean install I start with <https://bit.ly/arcogetstarted3>

We run the script for the corsair keyboard.

**Thunar** is always installed because of the great workflow and the custom actions.

We can open folders as root.

Then we get at the question of the user on the forum.

How do we add a service to Dolphin to compare files and folders?

We had added the service already to this SSD. We see which one it was.

Configure Dolphin/Services and we see what meld service it was.

It was the one from Romankiefer.

We delete two services so we only see one menu.

Video: <https://youtu.be/oeOe_CR99Ns>

We totally forgot to do a skel, cb and check our rolling folders

Skel = alias to copy/paste settings over

We only have 2 mirrors - We need to get the new .bashrc in.

The bashrc.latest contains all our new settings and aliases.

We are going to load the .bashrc with
    
    
    source .bashrc 

Then we run the alias 
    
    
    cb

It will make sure the .bashrc-latest will applied everywhere.

Then we take a look at ~/.bin/stay-rolling

and see if we need to change anything.

 

Video: <https://youtu.be/2XGkaooQUlY>
