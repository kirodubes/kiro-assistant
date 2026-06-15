---
title: "1 Installation of ArcoLinuxD Berry"
url: https://www.arcolinuxd.com/1-installation-of-arcolinuxd-berry/
date: 2022-11-20 05:36:34
type: post
categories: ["Phase 6"]
source_site: arcolinuxd.com
---

# 1 Installation of ArcoLinuxD Berry

![](https://www.arcolinuxd.com/wp-content/uploads/2022/11/berry.jpg)

### Install the desktop using 

### Calamares

### Install the desktop using our scripts

### Install the desktop using

### ArcoLinuxB

### Install the desktop using

### ArcoLinux Tweak Tool

OPTION 1 : Installing the desktop with Calamares

**SDDM** is the **default** login or displaymanager. Select more sddm themes if you want.

You can also select **lightdm** or **gdm** in the installer.

**Lightdm** will be activated if you select it.  
**Gdm** will not be activated due to incompatibility between Wayland and VirtualBox.  
You can activate gdm with this command:
    
    
    sudo systemctl enable gdm -f

Select during installation what **desktop** you want to install.

After installation you reboot.

Update your **Arch Linux** mirrors with the command
    
    
    mirror

Then update your computer with the command
    
    
    update

Reboot if needed. For example if there is a new kernel.

Video: <https://youtu.be/hgHET-z8GHQ>

OPTION 2 : Installing the desktop with scripts

[Install ArcoLinuxD](<https://www.arcolinuxd.com/installation/>) without selecting the display manager or the desktop in Calamares.

Choose **Base** installation.

After rebooting and logging in we type this command to get the best mirrors in our neighborhood.
    
    
    mirror

Then we get a fresh sync and upgrade with this command
    
    
    update

We get our scripts from the github
    
    
    git clone https://github.com/arcolinuxd/arco-berry

Move inside the downloaded folder with **cd** and run the scripts from the smallest number to the largest number.

Only **run script number 100** and reboot. Some desktops will give you an Arch Linux feel. [Read more here and see examples](<https://arcolinux.info/use-arcolinuxd-to-experience-the-arch-linux-feel-and-look/>).**  
**

Decide if you want to run the other scripts. These scripts are meant to be changed by the user.

The scripts **500** & **600** will give you the **ArcoLinux** **look** **and** **feel.**

 

Video: <https://youtu.be/hgHET-z8GHQ>

OPTION 3 : Installing the desktop with ArcoLinuxB

[Continue reading here.](<https://arcolinuxb.com/>)

OPTION 4 : Installing the desktop with ArcoLinux Tweak Tool

[Continue reading here.](<https://arcolinux.com/everything-you-need-to-know-about-the-arcolinux-tweak-tool/>)
