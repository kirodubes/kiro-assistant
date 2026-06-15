---
title: "How to get the best Arch Linux servers to update your system"
url: https://arcolinux.com/how-to-get-the-best-arch-linux-servers-to-update-your-system/
date: 2021-01-18 09:15:58
type: post
categories: ["Fixes", "Must read", "Update", "Utilities"]
tags: ["update"]
source_site: arcolinux.com
---

# How to get the best Arch Linux servers to update your system

![](https://arcolinux.com/wp-content/uploads/2018/12/mirrors-aliases.jpg)

You may have seen me struggle with the Arch Linux servers in one of my videos.

Time to dive into the application [reflector](<https://wiki.archlinux.org/index.php/Reflector>). Read all about it on your own computer.

Type **reflector --help** in the terminal and read more.

Servers speed and service all depend on your own network, your isp, your country's policy (port blocking) and the servers around you.

As a result we have now several aliases to get the best servers out there.

**If one alias does not work to update then use another one. Until you have no more issues.**
    
    
    #get fastest mirrors in your neighborhood
    alias mirror="sudo reflector -f 30 -l 30 --number 10 --verbose --save /etc/pacman.d/mirrorlist"
    alias mirrord="sudo reflector --latest 50 --number 20 --sort delay --save /etc/pacman.d/mirrorlist"
    alias mirrors="sudo reflector --latest 50 --number 20 --sort score --save /etc/pacman.d/mirrorlist"
    alias mirrora="sudo reflector --latest 50 --number 20 --sort age --save /etc/pacman.d/mirrorlist"

Video: <https://youtu.be/9dxID2jrr0c>

creation of two new scripts  
downgrade reflector

Reflector got a recent update to version 2020.12.7-1.

We compare this version against the older version 2020.9-2.

We have to wait considerably**longer** now with the new version. That was our conclusion.

We wait for a new version from the developer and in the meantime we downgrade reflector with
    
    
    sudo downgrade reflector

Create your own alias for mirror and**put it** in your**.bashrc-personal**. [Read more here about that.](<https://arcolinux.com/add-your-personal-aliases-to-bashrc-the-smart-way/>)

![](https://arcolinux.com/wp-content/uploads/2020/12/two-scripts-reflector.jpg)

Video: <https://youtu.be/XCR3t4EQjhU>

Reflector analysis on 12/05/2020  
create your own alias  
downgrade reflector

Reflector got a recent update to version 2020.12-1.

We compare this version against the older version 2020.9-2.

We have to wait approximately **30 seconds longer** now with the new version. That was our conclusion.

We wait for a new version from the developer and in the meantime we downgrade reflector with
    
    
    sudo downgrade reflector

We also show you how to create a **personal** **alias** in your**.bashrc-personal**. [Read more here about that.](<https://arcolinux.com/add-your-personal-aliases-to-bashrc-the-smart-way/>)

Video: <https://youtu.be/AH4UsTeiReA>

January 2021   
mirrorx  
new alias 

Video: <https://youtu.be/wxw4G6Fl_Ug>

# Alias mirrorx in January 2021
    
    
    alias mirrorx='sudo reflector --age 6 --latest 20 --fastest 20 --threads 20 --sort rate --protocol https --save /etc/pacman.d/mirrorlist'
