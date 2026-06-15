---
title: "Fixing the error message package-query: error while loading shared libraries: libalpm.so.10"
url: https://arcolinux.com/fixing-the-error-message-package-query-error-while-loading-shared-libraries-libalpm-so-10/
date: 2018-05-29 08:07:00
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fixing the error message package-query: error while loading shared libraries: libalpm.so.10

![](https://arcolinux.com/wp-content/uploads/2018/05/arcolinux-fix-package-query-libalpm.jpg)   


OPTION 1 - super quick fix

**YOU NEED TO REMOVE TWO PACKAGES AND INSTALL THEM AGAIN  
**
    
    
    sudo pacman -R package-query pamac-aur
    trizen package-query
    trizen pamac-aur

Video: <https://youtu.be/25r_apxTBgA>

  


OPTION 2 - educational building iso

Tuesday 29 May 2018 we get an error when updating with pksyua.
    
    
    package-query: error while loading shared libraries: libalpm.so.10: cannot open shared object file: No such file or directory

After analyzing the issues and googling this line of code I found a link that gave me a clue what was going on

<https://github.com/archlinuxfr/package-query/issues/3>

What I found there was ...

**package-query needs to be rebuilt because of a shared library version bump.**

So that is exactly what I did.

I rebuild the package package-query and pamac-aur.

Installing these packages again solved the update issue.

**YOU NEED TO UPDATE TWO PACKAGES**

**FIX for package-query**

Download this package  
https://github.com/arcolinux/arcolinux_repo_iso/blob/master/x86_64/package-query-1.9-3-x86_64.pkg.tar.xz

Then you install it via the terminal
    
    
    sudo pacman -U package-query-1.9-3-x86_64.pkg.tar.xz

Then you can do **pksyua** again.

**QUICK FIX for pamac-aur**

Download this package  
[https://github.com/arcolinux/arcolinux_repo_iso/blob/master/x86_64/pamac-aur-6.3.2-1-x86_64.pkg.tar.xz](<https://github.com/arcolinux/arcolinux_repo_iso/tree/master/x86_64>)

Then you install it via the terminal
    
    
    sudo pacman -U pamac-aur-6.3.2-1-x86_64.pkg.tar.xz

Then you can use pamac again.

This is what we need to do to build a proper working **iso** again.

Video: <https://youtu.be/RdF6YlZRqUg>
