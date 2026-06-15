---
title: "Installing the nvidia driver for GEFORCE GTX970 via nvidia .run - November 2019"
url: https://arcolinux.com/installing-the-nvidia-driver-for-geforce-gtx970-via-nvidia-run-november-2019/
date: 2019-10-29 19:24:49
type: post
categories: ["Nvidia"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# Installing the nvidia driver for GEFORCE GTX970 via nvidia .run - November 2019

![](https://arcolinux.com/wp-content/uploads/2019/10/nvidia-run.jpg)

[In the other article we install via pacman](<https://arcolinux.com/installing-the-nvidia-driver-for-geforce-gtx970-via-pacman-november-2019/>). That is the preferred way. Then pacman can actually manage the package. In this article we will use the .run file from[ nvidia.com](<https://www.geforce.com/drivers>).

First watch the first video. You will be on your own in a TTY later to be able to install the nvidia driver. This can not be filmed.

Video: <https://youtu.be/1QtUCvM91VE>

After the installation of the driver we go to TTY with **CTRL + ALT + F2.** Then we need to shutdown XORG. 
    
    
    sudo systemctl stop lightdm

Then we install 
    
    
    sudo pacman -S linux-headers

or the linux-lts-headers if you are using the linux-lts kernel. Only then can we run the .run file from Nvidia. 
    
    
    sudo ./NVIDIA-Linux-x86_64-430.50.run

You will see several popups. Make up your own mind what is best for you. 

  1. 32-bits libraries yes or no - I choose no
  2. nvidia xconfig auto update xorg.conf - I choose yes

Then you reboot and hope for the best.   Uninstalling is repeating the steps but now 
    
    
    sudo ./NVIDIA-Linux-x86_64-430.50.run --uninstall

The switches -A and --help may assist you as well.

Video: <https://youtu.be/P7zbTewz89k>
