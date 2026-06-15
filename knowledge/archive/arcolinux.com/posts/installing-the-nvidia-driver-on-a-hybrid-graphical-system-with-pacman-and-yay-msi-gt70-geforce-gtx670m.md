---
title: "Installing the nvidia driver on a hybrid graphical system with pacman and yay – msi gt70 – geforce gtx670m"
url: https://arcolinux.com/installing-the-nvidia-driver-on-a-hybrid-graphical-system-with-pacman-and-yay-msi-gt70-geforce-gtx670m/
date: 2021-01-06 21:49:30
type: post
categories: ["Nvidia"]
source_site: arcolinux.com
---

# Installing the nvidia driver on a hybrid graphical system with pacman and yay – msi gt70 – geforce gtx670m

![](https://arcolinux.com/wp-content/uploads/2021/01/nvidia-gt670m.jpg)

The video shows the steps we take after a clean install.

You can type every command or you can put them in a text file and run that one script. The latter is more convenient.  
I have a personal github to install elements after every clean install at [github](<https://github.com/erikdubois/arcolinux-nemesis>).

Here is the content of the script on January 2021.
    
    
    sudo pacman -S --noconfirm --needed linux-lts 
    sudo pacman -S --noconfirm --needed linux-lts-headers
    sudo pacman -S --noconfirm --needed optimus-manager-qt
    yay -S nvidia-390xx-dkms
    yay -S nvidia-390xx-settings
    yay -S nvidia-390xx-utils

After installing all the software and making all the smart choices you reboot, activate optimus-manager and select nvidia.

Video: <https://youtu.be/EE_lqmKEcJI>
