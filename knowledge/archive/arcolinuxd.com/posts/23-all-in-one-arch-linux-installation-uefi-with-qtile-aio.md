---
title: "All in one Arch Linux installation UEFI with Qtile"
url: https://www.arcolinuxd.com/23-all-in-one-arch-linux-installation-uefi-with-qtile-aio/
date: 2019-04-10 21:49:59
type: post
categories: ["ArchWayAllinone", "ArchWayDesktop", "ArchWaySpices"]
source_site: arcolinuxd.com
---

# All in one Arch Linux installation UEFI with Qtile

![](https://www.arcolinuxd.com/wp-content/uploads/2019/04/archlinux-qtile.jpg)

It takes 20 minutes to install Arch Linux.

This video will give you an overview of all the necessary steps to take. You willl have a working system with Qtile desktop.

We follow [the guide of this page](<https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-uefi/>) and will compare it with the [Arch Linux installation page](<https://wiki.archlinux.org/index.php/Installation_guide>).

This video will guide you  
through Phase 1, 2, 3 and 4  
of OUR Arch Linux installation guide  
this is an ALL IN ONE installation

Video: <https://youtu.be/5prSvdW-Rqc>

setup of virtualbox 

We show you what settings I use in VirtualBox to have an EFI boot.   
There is a tutorial about all the settings of VirtualBox in arcolinux.com.

We use the possibility to group our virtual machines and the clone option to have different virtualboxes from each phase.

bootup screen 

Your bootscreen will tell you if you are on MBR/BIOS or UEFI.

Logo of Arch Linux is MBR/BIOS.

If you boot up with 5 lines then you are in UEFI.

Then we follow the guide till we are at Phase 4.

In phase 4 we choose our desktop

We have the **standard** **lightdm** , **lightdm-gtk-greeter** and **lightdm-gtk-greeter-setttings** installed but we still do not have a desktop. Basically we can not login as lightdm can not start anything. We need to install our desktop first with 
    
    
    sudo pacman -S qtile

Qtile provides a config to work with and we decide to take a look at how it looks without theming and tweaking. We will copy/paste over the default config of the developers. 
    
    
    mkdir -p ~/.config/qtile/
    cp /usr/share/doc/qtile_dir/default_config.py ~/.config/qtile/config.py

Lateron we decide to get all the needed packages from the **ArcoLinuxD** **github**.
    
    
    sudo pacman -S git
    git clone https://github.com/arcolinuxd/arco-qtile

In the video we will go over all the scripts and select them one by one and discuss them.

We analyze the scripts and install the bare minimum.

We can run **script 400 distro specific** since it uses the Arch repositories and all we need is **pacman**.

**Script** **500** needs an AUR helper like **yay** or trizen and that is not installed on Arch Linux.  
We use this [article](<https://www.arcolinuxd.com/get-your-aur-helpers-in-on-any-arch-linux-based-system>) to install yay.

**Script 600** is required since it contains all the ArcoLinux packages but Arch Linux does not know any of our ArcoLinux repos.

We will run the **scripts** from the folder **Arch Way** in order to be able to install elements from ArcoLinux (script 600)

We will only import the **configuration** of **Qtile**. That is the most important. We will the other packages later. Lets first check a minimal config of Qtile.
    
    
    sudo pacman -S arcolinux-qtile-git

We need to copy/paste the content from /etc/skel to our home directory.
    
    
    cp -r /etc/skel/.config/* ~/.config/

  
Then we reboot and talk about the issue we are currently experiencing of the 90 seconds countdown.

# **UNFORTUNATELY the video was cut off due to the fact that the keyboard shortcut to reset the virtualbox is the same shortcut to pause simplescreenrecorder. luckily We were almost at the end.**

# the following content was not recorded

We resolve the conflict between lightdm and arcolinux-lightdm by removing the standard Arch Linux package. You will see the conflict if you try to run script 600.
    
    
    sudo pacman -R lightdm-gtk-greeter lightdm-gtk-greeter-settings

After removing these packages you can restart **script** **600** and there will be no conflicts. 

Then you decide if you run the rest of the scripts like bluetooth, printers, script 200, 300, ... or just install one application at a time on a need to have basis.

![](https://www.arcolinuxd.com/wp-content/uploads/2019/04/archlinux-qtile-end.jpg)
