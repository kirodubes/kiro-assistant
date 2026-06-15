---
title: "How to install a package by skipping the validity check"
url: https://arcolinux.com/how-to-install-a-package-by-skipping-the-validity-check/
date: 2018-12-06 07:43:57
type: post
categories: ["Fixes"]
tags: ["pkgbuild", "terminal", "update"]
source_site: arcolinux.com
---

# How to install a package by skipping the validity check

![](https://arcolinux.com/wp-content/uploads/2018/10/validity-check.jpg)

Sometime the maintainers of packages from AUR are just on holiday or sick and the pkgbuild needs to be updated because the sources it uses have been updated but not the validity checksums of the pkgbuild.

The normal procedure would be to get into contact with the developer or flag it out of date on the AUR website and then the waiting starts. Or you can try to fix the pkgbuild yourself.

But what if that is all to cumbersome for you and you just want to have it NOW. It installed fine yesterday and does not install anymore today.

**How to bypass these checksums if you know the packages are safe to install?**

## Yay
    
    
    yay -S --mflags --skipinteg

## Trizen
    
    
    trizen -S --skipinteg

You can make an alias for both of them.
    
    
    alias yayskip='yay -S --mflags --skipinteg'
    alias trizenskip='trizen -S --skipinteg'

We are going to add both aliases to our .bashrc in future releases.  
You can always create as much aliases as you want.

Video: <https://youtu.be/vOYpeS2wk5A>

how to fix the pkgbuild  
2 solutions 

# 1\. Calculate and put in the correct sha256sum

# 2\. Erase all trace of this html file

<https://pastebin.com/TXnDRU6M>

Video: <https://youtu.be/RYTpHKrmFBc>

3th Solution   
how to fix the pkgbuild

# 3\. Skip the sha256 checksum altogether

and big thank you to **Musikolo** , the maintainer of this package, for the quick response and the quick fix. He/she came up with the idea first to **SKIP** the whole checksum.

Video: <https://youtu.be/KwjwkM912Zo>

EXAMPLES

# Vivaldi - December 2018

![](https://arcolinux.com/wp-content/uploads/2018/12/validity-check.jpg)

Video: <https://youtu.be/SxtUbYJBlcE>
