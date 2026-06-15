---
title: "Installing the official nvidia driver on a hybrid graphical system - msi gt70 - geforce gtx670m"
url: https://arcolinux.com/installing-the-official-nvidia-driver-on-a-hybrid-graphical-system-msi-gt70-gforce-gtx670m/
date: 2021-01-01 16:55:03
type: post
categories: ["Nvidia"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# Installing the official nvidia driver on a hybrid graphical system - msi gt70 - geforce gtx670m

![](https://arcolinux.com/wp-content/uploads/2021/01/nvidia-gt670m.jpg)

[In the other article we install via pacman](<https://arcolinux.com/installing-the-nvidia-driver-for-geforce-gtx970-via-pacman-november-2019/>). That is the preferred way. Then pacman can actually manage the package. In this article we will use the .run file from[ nvidia.com](<https://www.geforce.com/drivers>).

Video: <https://youtu.be/ANwGtYSmqSI>

> Together we go over some of the websites that contain information about Nvidia.

<https://wiki.archlinux.org/index.php/NVIDIA>

<https://wiki.archlinux.org/index.php/hybrid_graphics>

<https://arcolinux.com/category/arcolinux/general/nvidia/>

<https://www.nvidia.com/en-us/geforce/drivers/>

Together we select the correct package and download it.

Then we install
    
    
    sudo pacman -S linux-lts linux-lts-headers optimus-manager-qt

We got to TTY with CTRL + ALT + 2 and disable lightdm.
    
    
    sudo systemctl disable lightdm

Or any other displaymanager.

Then we **reboot**. We want the linux-lts kernel to take over and lightdm or any other displaymanager.
    
    
    sudo reboot

**Only then** can we run the .run file from **Nvidia.com**. We navigate to the download folder and make the file executable.
    
    
    chmod +x NVIDIA-....runsudo ./NVIDIA-....run

You will see several popups. Make up your own mind what is best for you.

  1. 32-bits libraries - I choose **yes**
  2. nvidia xconfig auto update xorg.conf - I choose **no** \- optimus-manager will manage Xorg for me


    
    
    sudo systemctl enable lightdm

Or any other displaymanager.

Then you reboot and hope for the best.
    
    
    sudo reboot

Uninstalling is repeating the steps but now
    
    
    sudo ./NVIDIA-....run --uninstall

The switches -A and --help may assist you as well.

When updates comes in this will likely break the driver. You can add packages to ignore in /etc/pacman.conf.

Video: <https://youtu.be/P7zbTewz89k>
