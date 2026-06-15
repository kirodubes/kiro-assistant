---
title: "52 Plasma challenge - updating - theming - start menu - skel"
url: https://www.arcolinuxd.com/52-plasma-challenge-updating-theming-start-menu-skel/
date: 2019-10-14 09:47:43
type: post
categories: ["Plasma"]
source_site: arcolinuxd.com
---

# 52 Plasma challenge - updating - theming - start menu - skel

![](https://www.arcolinuxd.com/wp-content/uploads/2019/10/plasma-challenge.jpg)

You can know how long ago it was you booted up with the command **last**.

> Arch Linux and ArcoLinux stays up and running over time.  
> No need to update daily or even weekly.

Arch Linux and ArcoLinux is a rolling distribution.

We **update** the system with the alias update.  
We **update** the system with the alias upall.

[Keyrings are important on Arch Linux](<https://wiki.archlinux.org/index.php/Pacman/Package_signing>).
    
    
    sudo pacman -S archlinux-keyring

Some of your update go to /etc/skel folders.

With an alias called skel we copy/paste the ArcoLinux over to our Home directory.  
Make a backup of your .config folder first if you want to keep your personal setting.

We show you the alternatives for a start menu. See image above for the smallest menu possible.

We open the window about the **application menu settings**.

We can delete libc++ and libc++abi with sudo pacman -R...

If you got issues with [importing gpg keys](<https://arcolinux.com/how-to-fix-one-or-more-pgp-signatures-could-not-be-verified-libc-and-discord/>), use the script I use.

What if we delete all the configuration of ArcoLinux, will this change the Application menu?

We analyze the files in the /etc/skel.

We change the theme and look and feel.

We change the window settings of konsole.

Video: <https://youtu.be/baMyqce2H2M>

We set the splash to none again in the settings.

In next video we delete the plasma files coming ArcoLinux. 

We compare /etc/skel with our own home directory.

We delete the configuration of the konsole terminal so immediately we fall back to the standard look.

Video: <https://youtu.be/h8vtNe7GMJU>

Splash screen was active again. This time the kde/plasma.

Third time we boot up this ssd. The ArcoLinux files are no longer there.

This is the standard Plasma look.

Compare the two config folders and see what settings make up Plasma and its settings.

Video: <https://www.youtube.com/watch?v=WvuqwR9SQiU>
