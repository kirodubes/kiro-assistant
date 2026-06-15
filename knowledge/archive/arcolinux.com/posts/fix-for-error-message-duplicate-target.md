---
title: "Fix for error message Duplicate Target"
url: https://arcolinux.com/fix-for-error-message-duplicate-target/
date: 2018-01-25 20:24:59
type: post
categories: ["Fixes"]
tags: ["fix", "pkgbuild"]
source_site: arcolinux.com
---

# Fix for error message Duplicate Target

![](https://arcolinux.com/wp-content/uploads/2018/01/fix-for-duplicate-target.jpg)

When I installed [zoom](<https://zoom.us/>) the other day I had an error message "Duplicate target". This has happened also with other applications. Pacman finds two pkg.tar.xz files and is confused.

When errors occur, go to your /tmp folder and check what is happening.

When you installed it with packer you will find a folder there with the same name. The same applies to trizen and yaourt. And try to figure out what is going wrong.

In my case I had two files. One was the original file and the other was the one coming from the build (PKGBUILD).

**Double click** the correct file or install with
    
    
    sudo pacman -U ....pkg.tar.xz

 

### Sometimes we run out of space in the /TMP 

Sometimes if the build is becoming too **big** you can run out of place. Tmp is too small or similar message shows up.

This is the **solution** and there is no need to reboot. [More info on Arch Wiki](<https://wiki.archlinux.org/index.php/tmpfs>).
    
    
    mount -o remount,size=4G,noatime /tmp

Video: <https://youtu.be/kQgGJ3EXOYk>
