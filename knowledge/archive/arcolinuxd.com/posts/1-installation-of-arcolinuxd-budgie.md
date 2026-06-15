---
title: "1 - Installation of ArcoLinuxD Budgie"
url: https://www.arcolinuxd.com/1-installation-of-arcolinuxd-budgie/
date: 2020-11-17 13:28:39
type: post
categories: ["Phase 6"]
tags: ["installation"]
source_site: arcolinuxd.com
---

# 1 - Installation of ArcoLinuxD Budgie

![](https://www.arcolinuxd.com/wp-content/uploads/2018/09/arcolinuxd-budgie.jpg)

### Install the desktop using 

### Calamares

### Install the desktop using our scripts

### Install the desktop using

### ArcOLINUXB

### Install the desktop using

### ARcolinux tweak tool

OPTION 1 : Installing the desktop with Calamares

Select during installation what **display manager** and what **desktop** you want to install.

After installation you reboot.

You end in a **black** **login** **screen**.

Log into your system.

Update your Arch LInux mirrors with the command
    
    
    mirror

Then update your computer with the command
    
    
    update

Now activate the display manager of your choice
    
    
    sudo systemctl enable lightdm.service

or others like sddm, gdm or lxdm.

Decide whether you use our **skel** command or not. [You can enjoy a virgin Arch Linux look if you want to.](<https://arcolinux.info/use-arcolinuxd-to-experience-the-arch-linux-feel-and-look/>)  
In case you are installing a **tiling window manager** I would suggest you use **skel**.
    
    
    skel

Now reboot with
    
    
    sudo reboot

You will be greeted with your selected display manager or you will autologin, if you selected to autologin in Calamares.

Video: <https://youtu.be/ycmFiK4DTXA>

OPTION 2 : Installing the desktop with scripts

[Install ArcoLinuxD](<https://www.arcolinuxd.com/installation/>) without selecting the display manager or the desktop in Calamares.

After rebooting and logging in we type this command to get the best mirrors in our neighborhood.
    
    
    mirror

Then we get a fresh sync and upgrade with this command
    
    
    update

We get our scripts from the github
    
    
    git clone https://github.com/arcolinuxd/arco-budgie

Move inside the downloaded folder with **cd** and run the scripts from the smallest number to the largest number.

Only **run script number 100** and reboot to get an Arch Linux feel. [Read more here and see examples](<https://arcolinux.info/use-arcolinuxd-to-experience-the-arch-linux-feel-and-look/>).**  
**

Decide if you want to run the other scripts. These scripts are meant to be changed by the user.

The scripts **500** & **600** will give you the **ArcoLinux** **look** **and** **feel.**

 

Video: <https://youtu.be/ycmFiK4DTXA>

OPTION 3 : Installing the desktop with ArcoLinuxB

[Continue reading here.](<https://arcolinuxb.com/>)

OPTION 4 : Installing the desktop with ArcoLinux Tweak Tool

[Continue reading here.](<https://arcolinux.com/everything-you-need-to-know-about-the-arcolinux-tweak-tool/>)
