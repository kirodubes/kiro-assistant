---
title: "Use a meta package to install a bunch of wallpapers"
url: https://arcolinux.com/use-a-meta-package-to-install-a-bunch-of-wallpapers/
date: 2020-01-13 06:26:15
type: post
categories: ["Wallpaper"]
tags: ["update"]
source_site: arcolinux.com
---

# Use a meta package to install a bunch of wallpapers

![](https://arcolinux.com/wp-content/uploads/2018/10/meta-package-installation.jpg)A **meta** package is a way to install 'lots' of software. It is a **bundle** of packages installed with one command. Read all about it on the [wiki of Arch Linux](<https://wiki.archlinux.org/index.php/creating_packages#Meta_packages_and_groups>). We install all the wallpapers (500MB) with this single command: 
    
    
    sudo pacman -S arcolinux-wallpapers-submicron-3840x2400-wquxga-git-meta

Want to create a meta package for yourself - read more here <https://arcolinuxiso.com/what-is-a-meta-package-and-how-to-create-one/>  

Next video is about adding the submicron repository to your pacman.conf. It is interesting to know how pacman works. After adding the repo lines to your /etc/pacman.conf you will able to install the wallpapers with pacman. In 2019 we decided to not include this repository anymore. But we keep the repository online for those who like to install them.

Video: <https://youtu.be/-1yhfQ621mg>

You can install meta-packages. It will install multiple packages with one package. That is what we will do in the next video.

Video: <https://youtu.be/DrH9XGzWEKw>
