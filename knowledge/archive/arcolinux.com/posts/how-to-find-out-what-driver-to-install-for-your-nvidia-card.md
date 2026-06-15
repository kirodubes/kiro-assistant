---
title: "How to find out what driver to install for your Nvidia card - April 2018"
url: https://arcolinux.com/how-to-find-out-what-driver-to-install-for-your-nvidia-card/
date: 2018-04-27 09:29:05
type: post
categories: ["Nvidia"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# How to find out what driver to install for your Nvidia card - April 2018

![](https://arcolinux.com/wp-content/uploads/2018/04/nvidia.jpg) This video is about finding out what driver you should install for your nvidia graphical card. First of all there might be **NO NEED** to install the **nvidia** **proprietary** driver since the **opensource nouveau** driver might be functioning super. It is only for educational reasons here and if you experience problems when running applications that need more 'stamina'. Think about high-demanding games.   We look up what hardware we have with **inxi -b**. It is a **Nvidia Geforce GTX970**. We surf to two sites : <https://wiki.archlinux.org/index.php/NVIDIA> <http://www.nvidia.com/Download/index.aspx> We analyze what driver to choose and install it. 
    
    
    sudo pacman -S nvidia

I could also install the utility package. 
    
    
    sudo pacman -S nvidia-utils

Video: <https://www.youtube.com/watch?v=0nzzfaPV0YM>
