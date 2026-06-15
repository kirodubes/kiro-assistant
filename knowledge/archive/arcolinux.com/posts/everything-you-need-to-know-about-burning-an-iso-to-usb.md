---
title: "Everything you need to know about burning an iso to usb"
url: https://arcolinux.com/everything-you-need-to-know-about-burning-an-iso-to-usb/
date: 2020-03-20 09:33:09
type: post
categories: ["Must read", "Pre-installation", "Utilities"]
tags: ["anydesktop"]
source_site: arcolinux.com
---

# Everything you need to know about burning an iso to usb

![](https://arcolinux.com/wp-content/uploads/2019/12/etcher.jpg)

> **We do not recommend Ventoy - too many users report issues with our isos.  
> **

**Etcher** seems to be a good all-rounder.  
Meaning **Etcher** will work on Linux, Windows and macOS.

<https://www.balena.io/etcher/>

On **ArcoLinux** we have mintstick installed - in the menu accessories/**usb image writer**

[**Check the Arch Wiki on this matter.**](<https://wiki.archlinux.org/index.php/USB_flash_installation_media>)

WINDOWS : Burn a linux iso to usb on Windows

Video: <https://www.youtube.com/watch?v=YbyEz4Hv_Qw>

MACOS : Burn a linux iso to usb on macos

Video: <https://youtu.be/Edp-uGV8Lh0>

ARCOLINUX : Burn a linux iso to usb on ARCOLINUX

We have been using **mintstick** from Linux Mint since the start of the project 6 years ago.

It can format a usb or burn an iso to the usb.

Reliable and fast.

It is part of the ArcoLinux isos.

Video: <https://youtu.be/zywopEaZ1nA>

use the terminal and dd

The **dd** command will almost always result in a working Live USB. You need to change the paths to the correct paths for your system.

The USB drive is specified as /dev/sdX. The most common path of a USB drive is /dev/sdb BUT yours might be different depending on your system.

To view a list of all drives currently attached to your system run this command:
    
    
    sudo fdisk -l

To write ArcoLinux to your USB run the following command:
    
    
    sudo dd bs=4M if=/path/to/arcolinux...iso of=/dev/sdX status=progress && sync

![](https://arcolinux.com/wp-content/uploads/2019/12/burn-dd-usb.jpg)

Other alternatives are :

  * [suse imagewriter](<https://aur.archlinux.org/packages/imagewriter/>)
  * [unetbootin](<http://unetbootin.sourceforge.net/>)
  * [rufus](<https://rufus.ie>)
  * gnome-multi-writer



Playlist on Youtube

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS66cv5ONu_I8HVNpTVLzQxy>
