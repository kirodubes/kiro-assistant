---
title: "Installing the official nvidia driver for a GeForce GTX970"
url: https://arcolinux.com/installing-the-official-nvidia-driver-for-a-gforce-gtx970/
date: 2021-01-02 13:06:07
type: post
categories: ["Nvidia"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# Installing the official nvidia driver for a GeForce GTX970

![](https://arcolinux.com/wp-content/uploads/2021/01/nvidia.jpg)

[In this other article we install via pacman](<https://arcolinux.com/installing-the-nvidia-driver-for-geforce-gtx970-via-pacman-november-2019/>). That is the preferred way. Then pacman can actually manage the package. In this article we will use the .run file from[ nvidia.com](<https://www.geforce.com/drivers>).

First look at the beneath to understand the steps we will have to take.

The first video is for hybrid display laptops (Intel and Nvidia).

The second video will be on a desktop with just one GPU.

BUT it is (almost) exactly the same procedure.

Video: <https://youtu.be/ANwGtYSmqSI>

Together we go over some of the websites that contain information about Nvidia.

<https://wiki.archlinux.org/index.php/NVIDIA>

<https://wiki.archlinux.org/index.php/hybrid_graphics>

<https://arcolinux.com/category/arcolinux/general/nvidia/>

<https://www.nvidia.com/en-us/geforce/drivers/>

In order to install the Nvidia driver we first need to select the correct package and download it.

Then we install
    
    
    sudo pacman -S linux-lts linux-lts-headers

We got to TTY with CTRL + ALT + 2 and disable lightdm.
    
    
    sudo systemctl disable lightdm

Or any other displaymanager.

Then we **reboot**. We want the linux-lts kernel to take over and lightdm or any other displaymanager can not be running.
    
    
    sudo reboot

**Only then** can we run the .run file from Nvidia.

We navigate back to the download folder and make the file executable and run it.
    
    
    chmod +x NVIDIA-....run
    sudo ./NVIDIA-....run

You will see several popups. Make up your own mind what is best for you.

  1. 32-bits libraries - I choose **YES**
  2. nvidia xconfig auto update xorg.conf - I choose **YES.**



Then we enable our displaymanager again and reboot.
    
    
    sudo systemctl enable lightdm

Or any other displaymanager.

Then you reboot and hope for the best.
    
    
    sudo reboot

Uninstalling is repeating the steps but now
    
    
    sudo ./NVIDIA-Linux-x86_64-430.50.run --uninstall

The switches -A and --help may assist you as well.

When updates comes in this will likely break the driver. You can add packages to ignore in /etc/pacman.conf.

Video: <https://youtu.be/P7zbTewz89k>

And then there is an update of your Linux-lts kernel

We do the same procedure as mentioned above again.  
And with the next update ... again.

[Maybe it is time to freeze your kernel for a while.](<https://arcolinux.com/freeze-your-current-kernel-for-a-while/>)

Video: <https://youtu.be/ujf9KF5YM10>
