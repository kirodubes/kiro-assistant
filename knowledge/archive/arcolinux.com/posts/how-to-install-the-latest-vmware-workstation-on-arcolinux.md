---
title: "How to install the latest vmware workstation on ArcoLinux"
url: https://arcolinux.com/how-to-install-the-latest-vmware-workstation-on-arcolinux/
date: 2019-01-21 08:13:26
type: post
categories: ["Virtual Machines"]
tags: ["virtual machines"]
source_site: arcolinux.com
---

# How to install the latest vmware workstation on ArcoLinux

![](https://arcolinux.com/wp-content/uploads/2019/01/vmware-workstation-resolution.jpg)

We can install **vmware workstation** from AUR via trizen or yay but there are some specific **challenges** to **overcome**.

I have analysed the problems and made a script for it. In the future this script may not work anymore. Just report and we will check.

We explain you the power of github. Once you did a **git clone** all you need to do later is a **git pull** and you will get the changes we have put on the github on your machine.

<https://github.com/arcolinuxd/arco-gnome>

I was creating ArcoLinux-Gnome. That is why we use the script from there. Every github on ArcoLinuxD will have the same script. As well as the one on [ArcoLinux-Nemesis](<https://github.com/erikdubois/arcolinux-nemesis>).

Pgp errors... are quite common you can find an [article here](<../fix-for-one-or-more-pgp-signatures-could-not-be-verified/>) about them and how to overcome them.

**BEWARE**

The script assumes you are on **linux** kernel and NOT ON linux-lts. If you have changed the linux to **linux-lts** kernel for some reason then you need to install the linux-**lts** -headers instead of the linux-headers. There is also a **script** for **Linux-lts**.

The script will make sure that you have **network** **connection** by starting this service:
    
    
    sudo systemctl enable vmware-networks.service
    sudo systemctl start vmware-networks.service
    

Seeing this image  
Just reboot

![](https://arcolinux.com/wp-content/uploads/2018/02/dev-vmmon.jpg)

Correct resolution

Install vmware software to get the correct display resolution after installation. [More in detail in this article](<https://arcolinux.com/getting-the-best-resolution-on-vmware-workstation-for-arcolinux-2-tips/>).
    
    
    sudo pacman -S open-vm-tools
    sudo systemctl enable vmtoolsd.service
    sudo reboot

NEED USB ACCESS

If you need **usb access** from a usb plugged into your host system and you want to reach it in your virtual machine then first start a service in a terminal. No need to reboot.
    
    
    sudo systemctl enable vmware-usbarbitrator.service
    sudo systemctl start vmware-usbarbitrator.service

![](https://arcolinux.com/wp-content/uploads/2018/06/usbsupport.jpg)

As the image suggests you need to go to VM > Removable Devices and decide which ones you want to see in your virtual machine.

It does not say to **REBOOT** the virtual machine for it to work.

NEWEST VIDEO

Video: <https://youtu.be/fjtAxs7xjF8>

Older VIDEOS

You can install vmware workstation on ArcoLinux to create a virtual machine in which you can install any operating system. You could use virtualbox as well. Installing can be done via one of the AUR helpers like yaourt, packer or pacaur. packer vmware and see the choices you get While it installs, we show you that you can find the place of an application can be found with **which.** I can not use it for libcanberra-gtk-module.so since it is not an application.
    
    
    which firefox

Then we use an appliation to search your entire system in the terminal (like catfish in gui)
    
    
    sudo updatedb
    locate libcanberra-gtk-module

Then we follow the process of the installation in the **tmp** folder.

We need to install the vmware headers.
    
    
    sudo pacman -S linux-headers

Then we start vmware-workstation again. We will download Solus Budgie to try out.

You can check my settings that I would use in a vmware machine. Now your number of cpu's and your cores. In virtualbox that is quite clear.

After rebooting you will be able to run vmware.

Then we install Solus. We can change the display inside Solus. Use your resolution if it is in there.

Pisi is no longer used in Solus... it is eopkg.

The idea is to install the **budgie desktop** in **phase 3** on **ArcoLinuxD**.

Video: <https://www.youtube.com/watch?v=o3VKUIlj9gQ>

Video: <https://www.youtube.com/watch?v=tAQPbX5MGM4>
