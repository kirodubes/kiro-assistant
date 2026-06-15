---
title: "Superfast update of ArcoLinux"
url: https://arcolinux.com/superfast-update-of-arcolinux/
date: 2021-04-11 09:00:13
type: post
categories: ["Must read", "Update"]
tags: ["anydesktop", "update"]
source_site: arcolinux.com
---

# Superfast update of ArcoLinux

![](https://arcolinux.com/wp-content/uploads/2018/12/fastupdate.jpg)

There are lots of more tutorials about updating. There is even[ two playlists on Youtube](<https://www.youtube.com/playlist?list=PLlloYVGq5pS5RJROnazR91tD1snkoN-jD>) just about updating. Watching these videos will learn you how to manage your operating system.

**Here we just want to update and get on with our work.**

You can use these commands as you see fit.  
We have added the frequency behind it as **indication**. Again you are free to do it differently.

**update** \- ArcoLinux packages, third-party packages build for ArcoLinux and Arch Linux packages - **DAILY  
****upall - updating all AUR packages - any package you installed additionally - DAILY  
************skel** \- copy/pasting /etc/skel content to your home directory and making a backup of .config folder - **MONTHLY  
****cb** \- copy/pasting content from /etc/skel/.bashrc to ~/.bashrc + making it work (source) - **MONTHLY**********

## For Arch Linux users

**update**
    
    
    alias update='sudo pacman -Syyu'

**skel**
    
    
    alias skel='cp -Rf ~/.config ~/.config-backup-$(date +%Y.%m.%d-%H.%M.%S) && cp -rf /etc/skel/* ~'

**cb**
    
    
    alias cb='sudo cp /etc/skel/.bashrc ~/.bashrc && source ~/.bashrc'

**upall**
    
    
    alias upall='yay -Syu --noconfirm'

**At start we used to have pksyua - upall had a better ring to it. There is no difference.**

Video: <https://youtu.be/5WZZcDC8sy0>

another example of a super fast update

Video: <https://www.youtube.com/watch?v=RE03Rmh75D0>
