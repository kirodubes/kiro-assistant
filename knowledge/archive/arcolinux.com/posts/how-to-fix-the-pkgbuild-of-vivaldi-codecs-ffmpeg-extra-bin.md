---
title: "How to fix the pkgbuild of vivaldi-codecs-ffmpeg-extra-bin"
url: https://arcolinux.com/how-to-fix-the-pkgbuild-of-vivaldi-codecs-ffmpeg-extra-bin/
date: 2018-12-07 11:28:37
type: post
categories: ["Fixes", "Update"]
tags: ["fix", "pkgbuild"]
source_site: arcolinux.com
---

# How to fix the pkgbuild of vivaldi-codecs-ffmpeg-extra-bin

![](https://arcolinux.com/wp-content/uploads/2018/12/fix-vivaldi.jpg)   


The developer was kind enough to give us a script that is going to look online what the version is and calculate the md5 sum.

That is awesome.

The script works with a command **pup.** ArcoLinux does not have that installed so we need to install it and its dependency **go**.
    
    
    yay -S pup-git

Then we run the script and the PKGBUILD is then fixed.

Type in the terminal
    
    
    makepkg

and install the new package with
    
    
    sudo pacman - U

Or if you like a faster way
    
    
    makepkg -si

Read more about **makepkg** on the wiki and/or in the **man makepkg** in your terminal.

<https://wiki.archlinux.org/index.php/makepkg>

Video: <https://youtu.be/JlnPofVSSKc>
