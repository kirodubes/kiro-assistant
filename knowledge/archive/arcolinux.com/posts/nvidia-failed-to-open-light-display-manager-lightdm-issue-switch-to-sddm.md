---
title: "Nvidia - Failed to open Light Display Manager - lightdm issue - switch to sddm"
url: https://arcolinux.com/nvidia-failed-to-open-light-display-manager-lightdm-issue-switch-to-sddm/
date: 2021-01-08 09:51:22
type: post
categories: ["Lightdm", "Nvidia"]
source_site: arcolinux.com
---

# Nvidia - Failed to open Light Display Manager - lightdm issue - switch to sddm

![](https://arcolinux.com/wp-content/uploads/2021/01/failed.png)

One of the reasons of this error message

> Failed to open light display manager

is that the lightdm is really failing and that is not the Nvidia driver or the configs that are behind it.

## Solution

Switch to SDDM and rule out if it is a lightdm issue or not.
    
    
    sudo pacman -S sddm
    
    
    
    
    sudo systemctl enable gdm.service -f

and reboot.

Video: <https://youtu.be/TjHTW8SRNaY?t=399>
