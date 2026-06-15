---
title: "Fix for libutf8proc.so.2 exists in filesystem"
url: https://arcolinux.com/fix-for-libutf8proc-so-2-exists-in-filesystem/
date: 2018-07-14 21:29:52
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fix for libutf8proc.so.2 exists in filesystem

![](https://arcolinux.com/wp-content/uploads/2018/07/libutf8proc.jpg) This article and video is here to remind you that **ArcoLinux** is based on **Arch Linux**. 
    
    
    error: failed to commit transaction (conflicting files)
    libutf8proc: /usr/lib/libutf8proc.so.2 exists in filesystem
    Errors occurred, no packages were upgraded.

  If you encounter any error, your first **reflex** should be : Let us check <https://www.archlinux.org> to see it they announced any issues together with a solution. The solution can be found on the Arch Linux website and is : 
    
    
    sudo pacman -Suy --overwrite usr/lib/libutf8proc.so.2

Video: <https://youtu.be/DDQyeWrYyxM>
