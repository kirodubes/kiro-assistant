---
title: "Getting the best resolution on Vmware Workstation for ArcoLinux - 2 tips"
url: https://arcolinux.com/getting-the-best-resolution-on-vmware-workstation-for-arcolinux-2-tips/
date: 2020-09-22 13:03:02
type: post
categories: ["Virtual Machines"]
tags: ["resolution", "virtual machines"]
source_site: arcolinux.com
---

# Getting the best resolution on Vmware Workstation for ArcoLinux - 2 tips

![](https://arcolinux.com/wp-content/uploads/2019/01/vmware-workstation-resolution.jpg)Vmware is not supported officially. Virtualbox is. All software and services are tuned for Virtualbox on ArcoLinux. If you have paid for vmware or you can get a licence (University agreements, ...), you can try out ArcoLinux in Vmware. These two tips will help you to get the proper resolution. Use XFCE setttings to change the display resolution on the livedvd. Install vmware software to get the correct display resolution after installation 
    
    
    sudo pacman -S open-vm-tools
    sudo systemctl enable vmtoolsd.service
    sudo reboot

Check if autofit guest is on. Sometimes you need to switch between these settings to let it "kick in".

![](https://arcolinux.com/wp-content/uploads/2019/01/autofit.jpg)

Video: <https://youtu.be/OgtUJwCW0bA>

Video: <https://youtu.be/Ft1FdpbI9oI>

Video: <https://youtu.be/gb1PsqxFl40>
