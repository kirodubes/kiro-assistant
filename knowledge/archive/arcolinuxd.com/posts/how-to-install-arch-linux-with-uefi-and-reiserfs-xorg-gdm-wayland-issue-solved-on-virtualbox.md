---
title: "How to install Arch Linux with UEFI and reiserfs - Xorg - Gdm - Wayland issue solved on VirtualBox"
url: https://www.arcolinuxd.com/how-to-install-arch-linux-with-uefi-and-reiserfs-xorg-gdm-wayland-issue-solved-on-virtualbox/
date: 2021-07-01 16:01:41
type: post
categories: ["ArchWayAllinone", "ArchWayDesktop"]
tags: ["aio"]
source_site: arcolinuxd.com
---

# How to install Arch Linux with UEFI and reiserfs - Xorg - Gdm - Wayland issue solved on VirtualBox

![](https://www.arcolinuxd.com/wp-content/uploads/2021/07/arch-uefi-reiserfs-gnome.jpg)

Finally the new Arch Linux arrived in the afternoon on the 1st of July.

We used it immediately on Virtual Box system.

We show you how to install Arch Linux with

  * UEFI
  * root and swap
  * Reiserfs
  * Xorg and gdm
  * Gnome



We need to solve the Wayland issue on VirtualBox.

Gnome needs to start as Xorg not Wayland.

We change the following file **/etc/gdm/custom.conf**
    
    
    WaylandEnable=false

Video: <https://youtu.be/Y_gzMq-ZPxo>
