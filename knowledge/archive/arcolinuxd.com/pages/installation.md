---
title: "Installation"
url: https://www.arcolinuxd.com/installation/
date: 2019-12-29 10:38:00
type: page
source_site: arcolinuxd.com
---

# Installation

**_D_ stands for  
you _D_ ecide what _D_ esktop you take**

INSTALLATION OF ARCOPRO

IS YOUR COMPUTER READY FOR LINUX?

BIOS - UEFI - MOTHERBOARD SETTINGS

When you boot up your computer, every pc lets you get into the **BIOS** or **SETUP** be sure you have set everything correct so you can install Linux on your computer.

You should be able to boot from the **usb** via a **keyboard shortcut** for example F8 and if you are planning to install virtual box or any other similar application you need to **enable virtualization**.

[Here you can find everything you need to know about install linux on your computer.](<https://arcolinux.com/everything-you-need-to-know-about-installing-linux-bios-uefi-motherboard-settings/>)

[Here you can find various articles about Bios and Uefi settings on different computers.](<https://arcolinux.com/category/arcolinux/bios-uefi/>)

VIRTUALBOX OR REAL METAL

Before installing a linux distribution, you can first try it out in **VirtualBox** or other virtual machines.

As a matter of fact arcocpro is **fine-tuned** to work **smoothly** on **VirtualBox**. All packages are pre-installed.

You need to use the **proper** **settings** in VirtualBox.

You can end up with a non responding system (not enough RAM, not enough cores, not enough harddisk space).

You can end up with the wrong resolution (wrong choice of the graphics controller).

[Here you can find all our articles about VirtualBox and virtual machines in general](<https://arcolinux.com/category/arcolinux/applications/virtual-machines/>)

BURN ON USB

We recommend using a **USB** to install arcopro.

[Here you can find our article about burning an ISO to usb.](<https://arcolinux.com/everything-you-need-to-know-about-burning-an-ISO-to-usb/>)

YOU WILL BOOT UP IN A BARE XFCE DESKTOP WHY?

We use XFCE as means to install arcopro.

It is the most minimal graphical Arch Linux based ISO.

You need to choose how to proceed.

Either use the **installer** to install the software and desktop(s) you want.

Either use our **scripts** to install the software and desktop(s) you want.[ Info about scripts](<https://www.arcolinuxd.com/what-you-need-to-know-about-the-scripts/>).

HOW TO INSTALL ARCOPRO

It takes **several screens** to install arcopro and will take approx.**15 minutes** to install on newer hardware.

Thanks to [**Calamares**](<https://calamares.io>) you will have a simple and clean **graphical** interface.

Calamares is changing with every release. Every new release of arcopro we use the latest calamares installer.

Over time you will see some changes in our Calamares installer.

You can always report issues on the[ github of calamares](<https://github.com/calamares/calamares>). It is the only way to improve calamares.

**Calamares is not an ArcoLinux product.**

WHAT IS ARCOPRO

**  
Arcopro** is the **most minimal ISO**. If you do not install any packages, it is the **most bare** version we have and it can give you the **Arch Linux** look and feel.

There is no

  *     *       * bluetooth
      * printers
      * sound



You will still need to install those with our **scripts** from the **githubs**. This does not change.

With the latest version of Calamares you have the freedom to **choose what packages to install** on the fly. Internet connection is required.

You can select if you want a different **kernel** or decide to install **nvidia** packages.

You can decide to install the **microcode**.

As extra option you can also use one of **5** **available** **display** **managers**

  1.      1. lightdm
     2. sddm
     3. gdm
     4. lxdm
     5. ly



You select any of the additional software from the list.

We have created an[**ArcoLinux-meta-steam** packages](<https://arcolinux.com/how-to-install-steam-on-arcolinux/>) to install steam the efficient way.

We have created an[**ArcoLinux-meta-fun** package](<https://arcolinux.com/installing-fun-stuff-for-the-terminal-on-arcolinux/>) to install all the 'fun' packages.

Choose either Libre Office Fresh or Libre Office Still.

Choose either Virtualbox for linux or linux-lts kernel.

> If you change the language in Calamares, you will also change the language of Libre Office
> 
> Internet connection is required

Use our "everything you need to know about calamares to solve any issue"

![](https://www.arcolinuxd.com/wp-content/uploads/2019/12/squid.png)

ARCONET

ARCOPRO

ARCOPLASMA

If you do not know what to choose as bootloader then choose **Grub**. We have been using Grub for the last 6 years.

Video: <https://youtu.be/qPiN2E0hCrk>

Video: <https://youtu.be/x0LIVDqMF4Y>

Video: <https://youtu.be/a4Wf_8QuiMQ>

Easy: what you see is what you get - xfce4

Advanced: xfce4 is removed you select the desktop and more apps

PLAYLIST OF ALL ARCONET INSTALLATION VIDEOS

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS4_yK-607gnfynjoWoR8spq>

Easy: black screen - TTY - no sddm

Advanced: xfce4 is removed you select everything

PLAYLIST OF ALL ARCOPRO INSTALLATION VIDEOS

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS7uat8E_T9MAsj2jloj2xXh>

Easy: what you see is what you get - minimal Plasma

Advanced: Install the full plasma + Hyprland or Wayfire and all the apps

PLAYLIST OF ALL ARCOPLASMA INSTALLATION VIDEOS

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS7xmfCznQf1a2EuQZtcqdUm>

Arcopro is installed - NOW WHAT

After installing and booting into arcopro you end up in a **black** **screen after choosing the Easy option.**  
**Log into your system.**

First update your computer
    
    
    update

Arch Linux and ArcoLinux packages will be updated
    
    
    back-to-arch

This script will remove even more ArcoLinux packages and applications to get you even closer to an Arch Linux installation.
    
    
    skel

Skel is essential for **Tiling Window Managers** as the code for the desktop is still in /etc/skel. We move the configs to our home directory.
    
    
    upall

AUR packages will be updated

Then we may need to enable the **display** **manager** of our choice (normally automatically activated)
    
    
    sudo systemctl enable lightdm
    
    
    sudo systemctl enable sddm
    
    
    sudo systemctl enable gdm
    
    
    sudo systemctl enable lxdm
    
    
    sudo systemctl enable ly

then you reboot and you will boot into a **graphical** environment.
    
    
    sudo reboot

We have added a script that will enable the display manager that is present on the system.

Install software

Use commands to install software - sudo pacman -S ...

Use your or our scripts to install software.

Use our gui **Sofirem** to install more software.

Then it is time to learn more

Enjoy your **exploration** of your **system/dektop**. You will find many **tutorials** in the menu. They are arranged per **desktop** and in our learning phases. We **started** making videos with the **number** **1** and then continued numbering them.

The intention is that you start with number 1 and move up in the numbering. Sometimes the numbering starts to make no sense.  
[Here you can read why that is.](<https://www.arcolinuxd.com/why-are-the-articles-on-arcolinuxd-not-ordered/>)

Making backups for future installations

Everyone has a particular way how to set up his system. Once set up you want to make sure the configs are saved for a later installation.  
We advise you to learn how to use github. [You will find more info in this article.](<https://www.arcolinuxd.com/easy-way-to-learn-about-git-and-github/>)

Playlist of all installation videos

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS6-eSggHY9ZCEgj8YEiiRPk>
