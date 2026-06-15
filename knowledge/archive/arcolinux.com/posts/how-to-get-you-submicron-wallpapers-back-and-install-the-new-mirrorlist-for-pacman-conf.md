---
title: "How to get your submicron wallpapers back and install the new mirrorlist for pacman.conf"
url: https://arcolinux.com/how-to-get-you-submicron-wallpapers-back-and-install-the-new-mirrorlist-for-pacman-conf/
date: 2021-04-08 06:24:30
type: post
categories: ["Pacman", "Tips", "Update"]
tags: ["update"]
source_site: arcolinux.com
---

# How to get your submicron wallpapers back and install the new mirrorlist for pacman.conf

![](https://arcolinux.com/wp-content/uploads/2018/10/arcolinux-mirrorlist.jpg)

You can still install the old wallpapers from [Submicron](<https://www.deviantart.com/submicron>). The repository still exists.

It is just not in the /etc/pacman.conf anymore for one obvious reason. Everyone has their own set of wallpapers.

You will need to change your **/etc/pacman.conf** if you want to install them via pacman.

## Procedure

**Add** the submicron repository to **pacman.conf.**

**Do not delete the Arch Linux lines or the ArcoLinux lines.  
Just add the submicron lines at the bottom.**
    
    
    #[arcolinux_repo_testing]
    #SigLevel = Required DatabaseOptional
    #Include = /etc/pacman.d/arcolinux-mirrorlist
    
    [arcolinux_repo]
    SigLevel = Required DatabaseOptional
    Include = /etc/pacman.d/arcolinux-mirrorlist
    
    [arcolinux_repo_3party]
    SigLevel = Required DatabaseOptional
    Include = /etc/pacman.d/arcolinux-mirrorlist
    
    [arcolinux_repo_xlarge]
    SigLevel = Required DatabaseOptional
    Include = /etc/pacman.d/arcolinux-mirrorlist
    
    [arcolinux_repo_submicron]
    SigLevel = Required DatabaseOptional
    Include = /etc/pacman.d/arcolinux-mirrorlist

With this copy/paste you will get the **wallpapers** from **Submicron** back.  
We have moved these wallpapers (1 GB) to a separate github for easier mirroring and more efficiency.

Type in the terminal
    
    
    update

Now look for the names via the terminal

type
    
    
    sudo pacman arcolinux-wallpapers-

and press twice on tab. Install the screen resolution you like.

Or use **pamac** to see what extra packages can be installed.

 

![](https://arcolinux.com/wp-content/uploads/2020/12/pamac-wallpapers.jpg)

Video: <https://youtu.be/H1rW1j7wENQ>

Video: <https://youtu.be/nyi4UMdeUmA>
