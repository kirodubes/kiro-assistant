---
title: "Fixing the message Key could not be looked up remotely"
url: https://arcolinux.com/fixing-the-message-key-could-not-be-looked-up-remotely/
date: 2017-10-28 16:15:56
type: post
categories: ["Fixes", "Update"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fixing the message Key could not be looked up remotely

![](https://arcolinux.com//wp-content/uploads/2017/10/key-could-not-be-looked-up.png)

What I can not check now anymore is that reinstalling the archlinux-keyring would probably have fixed this without initializing and populating it. Will try that next time.
    
    
    sudo pacman-key --init
    sudo pacman-key --populate archlinux

If necessary this one
    
    
    sudo pacman-key --refresh-keys

In our example this eventually helped. I remember on my other ssd there was an update of this one. Keep track of this one when updating.  
Keep also track of the 'linux' package. That is your kernel. Reboot afterwards.
    
    
    sudo pacman -S archlinux-keyring
    

**Sources for you to check**

<https://wiki.archlinux.org/index.php/Pacman/Package_signing#Cannot_import_keys>

There you can read this :

> There are multiple possible sources of this problem:
> 
>   * An outdated [archlinux-keyring](<https://www.archlinux.org/packages/?name=archlinux-keyring>) package.
>   * Incorrect date.
>   * Your ISP blocked the port used to import PGP keys.
>   * Your  _pacman_ cache contains copy of unsigned packages from previous attempts.
>   * `dirmngr` is not correctly configured
> 


In addition I found a news post that can also be useful in this situation and other situations regarding the pacman-key.

<https://www.archlinux.org/news/gnupg-21-and-the-pacman-keyring/>

"In addition, we recommend installing haveged, a daemon that generates system entropy; this speeds up critical operations in cryptographic programs such as gnupg (including the generation of new keyrings)."

For the record I did not do this and everything was speedy enough and **haveged**.**service** was **not** enabled.

> 
>     sudo pacman -Syu haveged
>     sudo systemctl start haveged
>     sudo systemctl enable haveged
>     
>     sudo rm -fr /etc/pacman.d/gnupg
>     sudo pacman-key --init
>     sudo pacman-key --populate archlinux
>     sudo systemctl stop haveged

Video: <https://www.youtube.com/watch?v=U04q--LSGSI>
