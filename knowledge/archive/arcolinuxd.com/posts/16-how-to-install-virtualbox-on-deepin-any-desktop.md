---
title: "16 How to install virtualbox on Deepin - any desktop"
url: https://www.arcolinuxd.com/16-how-to-install-virtualbox-on-deepin-any-desktop/
date: 2019-02-25 17:56:47
type: post
categories: ["AnyDesktop", "Deepin"]
source_site: arcolinuxd.com
---

# 16 How to install virtualbox on Deepin - any desktop

![](https://www.arcolinuxd.com/wp-content/uploads/2019/02/arcolinuxb-deepin-vb.png)

Installing virtual box on your Arch Linux or ArcoLinux computer should start with a visit to the Arch wiki and Nemesis scripts.

The Arch Wiki gives you an abundance of knowledge.

Follow this url and start reading : <https://wiki.archlinux.org/index.php/VirtualBox>

You can read even more in the [tips and trics](<https://wiki.archlinux.org/index.php/VirtualBox/Tips_and_tricks>).

But for the most people the scripts on the nemesis github will suffice.

<https://github.com/erikdubois/arcolinux-nemesis>

 

IF on LINUX kernel then execute these commands in the terminal
    
    
    sudo pacman -S --needed --noconfirm virtualbox-host-modules-arch
    sudo pacman -S --noconfirm --needed virtualbox
    sudo grub-mkconfig -o /boot/grub/grub.cfg

 

IF on LINUX-LTS kernel then execute these commands in the terminal
    
    
    sudo pacman -S --noconfirm --needed virtualbox
    sudo pacman -S --needed virtualbox-host-dkms
    sudo pacman -S --noconfirm --needed linux-lts-headers
    sudo grub-mkconfig -o /boot/grub/grub.cfg

 

 

Then we show you what the settings in your Virtualbox should be and install ArcoLinux in it.

> In the video I created a template. I totally forgot to clone this template and install ArcoLinux on the clone.

Video: <https://www.youtube.com/watch?v=T21qwAIzbVQ>
