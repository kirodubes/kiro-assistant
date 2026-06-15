---
title: "How to add the third party repo to pacman.conf"
url: https://arcolinux.com/how-to-add-the-third-party-repo-to-pacman-conf/
date: 2018-07-11 17:36:56
type: post
categories: ["Pacman", "Update"]
tags: ["update"]
source_site: arcolinux.com
---

# How to add the third party repo to pacman.conf

![](https://arcolinux.com/wp-content/uploads/2018/07/pacman-conf-3party.jpg) Open the file **/etc/pacman.conf** with **sublime text** and add these lines to it 
    
    
    [arcolinux_repo_3party]
    SigLevel = Required DatabaseOptional
    Server = https://arcolinux.github.io/arcolinux_repo_3party/$arch

Then do an update 
    
    
    sudo pacman -Syyu

and then you can install the packages that are in this 3party repo. Mid July 2018 we have added discord and its libraries in there. Installing discord now is available with 
    
    
    sudo pacman -S discord

Video: <https://www.youtube.com/watch?v=lI8bnK2oQYk>

With the use of pamac you can easily see what packages we currently have in this repo. ![](https://arcolinux.com/wp-content/uploads/2018/07/pamac.jpg)
