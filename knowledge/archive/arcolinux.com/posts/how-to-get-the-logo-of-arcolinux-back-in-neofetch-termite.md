---
title: "How to get the logo of ArcoLinux back in neofetch/termite"
url: https://arcolinux.com/how-to-get-the-logo-of-arcolinux-back-in-neofetch-termite/
date: 2018-12-27 06:33:11
type: post
categories: ["Terminal"]
tags: ["terminal"]
source_site: arcolinux.com
---

# How to get the logo of ArcoLinux back in neofetch/termite

![](https://arcolinux.com/wp-content/uploads/2018/12/neofetch-logo.jpg)![](https://arcolinux.com/wp-content/uploads/2018/12/neofetch-ascii.jpg)

**Update of 27 December 2018**

Neofetch is an application to have an overview of the most important settings.

You can either have an **ASCII** look or an **IMAGE** look.

After the update and the skel to copy/paste the new configs to your home directory, there should be only two neofetch configurations in your home folder : ~/.config/neofetch

  * **config.conf** is the one that actually works and is an ascii logo
  * **logo-config.conf** is the one with the settings to have an image logo rather than an ascii logo 



> > Delete the old configuration files.

> Do not worry about backups. /etc/skel contains one 

> You can choose many more colored logo's - standard white

> The image logo will disappear once you click elsewhere

Video: <https://youtu.be/8cnBhbVfSSM>

**Great tip**

Beware of the cache files

when experimenting with 

Neofetch

If on ArcoLinuxD -B or Arch Linux make sure the dependencies of Neofetch are installed. Most notably

  * imagemagick
  * w3m
  * feh



You can check dependencies in pamac-aur or in terminal
    
    
    sudo pacman -Qi neofetch
