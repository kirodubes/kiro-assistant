---
title: "How to install nvidia drivers on ArcoLinux - November 2017"
url: https://arcolinux.com/how-to-install-nvidia-drivers-on-archmerge/
date: 2017-11-26 15:46:21
type: post
categories: ["Nvidia"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# How to install nvidia drivers on ArcoLinux - November 2017

![](https://arcolinux.com/wp-content/uploads/2017/11/nvidia.jpg) We do **not** **need** to install the **nvidia** drivers per se. We can but there is no must. Unless you experience problems with your display when working or gaming. Many of the hardware display cards are supported by the [nouveau](<https://wiki.archlinux.org/index.php/nouveau>) driver i.e. opensource driver. In this tutorial we will install the [nvidia](<https://wiki.archlinux.org/index.php/NVIDIA>) driver or the proprietary driver. First we need to know what hardware we have to decide what driver to install. Then we analyze what driver number we need. we will find that on the [nvidia website](<http://www.nvidia.com/Download/index.aspx>). Then we install the driver with pacman. Remember this command 
    
    
    lspci -v

Depending on your **neofetch** settings you see the name of the card there as well. And we have also **System** **Profiler** **and** **Benchmark**. 

Video: <https://www.youtube.com/watch?v=lXUlxYXeKvY>

After a reboot we go check if we are now using the nvidia drivers with 
    
    
    lspci -v

No such luck. [Here is a link for troubleshooting.](<https://wiki.archlinux.org/index.php/NVIDIA/Troubleshooting>)

Video: <https://www.youtube.com/watch?v=rqMXR-H38DU>
