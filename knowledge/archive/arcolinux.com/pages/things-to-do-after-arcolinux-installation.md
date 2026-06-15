---
title: "Things to do after ArcoLinux installation"
url: https://arcolinux.com/things-to-do-after-arcolinux-installation/
date: 2024-04-28 16:41:10
type: page
source_site: arcolinux.com
---

# Things to do after ArcoLinux installation

things to do after first boot

MIRROR

 

Your package manager (**pacman**) is getting the Arch Linux files from [Arch Linux servers from around the globe](<https://www.archlinux.org/mirrors/status/>).

Not all arch linux servers are near to you.

Not all arch linux servers are fast.

Not all arch linux servers are complete.

We are using the application **[reflector](<https://wiki.archlinux.org/index.php/reflector>)** to give us the fastest and fully synced Arch Linux servers.

We have created **aliases** to make the updating easier.
    
    
    mirror
    mirrord
    mirrors
    mirrore
    mirrorx

Depending on the result you can choose another alias.

**First try mirror.**

You can also try another alias
    
    
    ram  
    rams

[Here you can find everything you need to know about the aliases to have the best mirrors.](<https://arcolinux.com/how-to-get-the-best-arch-linux-servers-to-update-your-system/>)

ARCH LINUX SERVERS - WHERE DO PACKAGES COMES FROM

If you want to know which Arch Linux servers you are using, use our alias
    
    
    nmirrorlist

to check if you have received a new list of servers.

At the top of **/etc/pacman.d/mirrorlist** you may see some information.

ARCOLINUX SERVERS - WHERE DO PACKAGES COMES FROM

If you want to know which ArcoLinux servers you are using, use our alias
    
    
    narcomirrorlist

to check which of the servers is the first one. That is the one that will give you your packages.

![](https://arcolinux.com/wp-content/uploads/2024/04/narcomirrorlist.png)

UPDATE

We update our systems with two commands in the terminal

  1. update
  2. upall



Type the command
    
    
    update

in your terminal to update the **Arch Linux** packages and the **ArcoLinux** packages.

Update is an alias for "sudo pacman -Syyu".

Type
    
    
    upall

in your terminal to update the **Arch Linux** packages, the **ArcoLinux** packages and anything from **AUR**.

Typically you will have no issues updating these.

[Here you can find everything you need to know about updating your system - educational version.](<https://arcolinux.com/how-to-update-arcolinux-long-procedure-learn-and-analyze/>)

[Here you can find everything you need to know about updating your system - superfast version.](<https://arcolinux.com/superfast-update-of-arcolinux/>)

[Update videos are a great source to learn more about your system.](<https://www.youtube.com/playlist?list=PLlloYVGq5pS5RJROnazR91tD1snkoN-jD>)

[Here you can find everything you need to know about pacman.](<https://arcolinux.com/pacman/>)

 

REMOVE THINGS YOU WILL NEVER NEED

Make a list of all the apps you will never need or use and run that after a clean install. (example: arcolinux-nemesis scripts)

Here are a few scripts we use ourselves.

Removing broadcom and realtek drivers.

Removing linux kernels.

Removing debug in the /etc/makepkg.conf.

![](https://arcolinux.com/wp-content/uploads/2024/04/remove.png)![](https://arcolinux.com/wp-content/uploads/2024/04/remove-debug.png)

Video: <https://youtu.be/el96IH0iBeg>

SKEL

Some of the packages will install files and folders in /etc/skel. The system will not use those unless you copy/paste them over to your home directory. This folder is used to create your home directory when installing from an iso. Skel stands for **skeleton**.

Type the command
    
    
    skel

in your terminal to copy all files and folders to your home directory.

[Here you can find everything you need to know about skel.](<https://arcolinux.com/updating-your-system-with-skel-and-still-keeping-your-own-settings/>)

Bupskel is also interesting to know.

[Here you can find everything you need to know about bupskel.](<https://arcolinux.com/use-bupskel-to-compare-the-arcolinux-updates-coming-in/>)

HARDCODE-FIXER

In **Xfce** and other desktops you can go to the **system** **settings** and you will find "Fix Hardcoded Icons".

Others can launch it from the terminal.
    
    
    sudo hardcode-fixer

Some developers are giving their applications an hardcoded path to the icon for the application. In other words the icon will never change whatever icon theme you use. This application will change that hardcoded path into the preferred icon name without path.

[Here you can find everything you need to know about hardcode-fixer.](<https://arcolinux.com/how-to-fix-icons-that-never-change-their-look-whatever-theme-you-choose/>)

HBLOCK

In **Xfce** and other desktops you can go to the **system** **settings** and you will find "Adblock".

Others can launch it from the terminal.
    
    
    hblock

This tool will protect your computer and improve your security and privacy by blocking ads, tracking and malware domains.

[Here you can find everything you need to know about hblock.](<https://arcolinux.com/use-hblock-to-improve-your-security-and-privacy-by-blocking-ads-tracking-and-malware-domains/>)

CONKYS

A conky is an application that displays information on your screen like memory, cpu, harddisk usage etc...

You can choose your conky with **conkyzen** and activate/deactivate it there.

Activate/deactivate the conky with **SUPER + C**.

**CTRL + ALT + PAGEUP/ PAGEDOWN** will go over all the conkys we have.

[Here you can find everything you need to know about conkys.](<https://arcolinux.com/conky/>)

NEMESIS

After a clean install of ArcoLinux every user will want to add application or remove applications.

Install more themes, icons or cursors.

Nemesis is the personal tweaking of Erik Dubois. Use it with care.

I am sharing the nemesis scripts because you can reuse my work and change them to YOUR scripts.

> Change the scripts to make it your own personal installation.

**I will install more applications that are not on the iso like spotify, discord, telegram, dropbox, virtualbox, ... and the fun stuff script.**

[Here you can find everything you need to know about the nemesis scripts.](<https://arcolinux.com/installing-nemesis-on-any-arcolinux/>)

SUPERFLEX

ArcoLinux is super flexible hence the name superflex. We use the **ArcoLinux Tweak Tool** to have an easy and beautiful interface to install desktops.

> With the ArcoLinux Tweak Tool you can do so many things  
> Change your grub theme  
> Change your termite theme  
> Install any desktop  
> ...

VARIETY CHANGES YOUR WALLPAPER

Variety is an application to get wallpapers and to show wallpapers. In previous ArcoLinux versions we had set it to rotate at a certain interval. [Wallhaven](<https://youtu.be/NIBJp2i498Q>) can be the source to get the wallpapers in.

Just want one wallpaper and you do not care about variety. [Learn how to delete it.](<https://arcolinux.com/how-to-delete-variety-and-all-its-configuration-files/>)

[Here you can find everything you need to know about variety.](<https://arcolinux.com/how-to-set-up-variety-with-the-use-of-desktoppr-and-dropbox/>)

[Do not ask people for their wallpapers, but look it up yourself with this website.](<https://arcolinux.com/where-to-find-the-wallpaper-of-a-nice-screenshot/>)

 

AUTOLOGIN INTO YOUR DESKTOP OF CHOICE

You may want to decide to boot standard into one of the desktops that you have choosen.

Type "nsddmk" and change the Session line.

[Here you can find everything you need to know about autologin.](<https://arcolinux.com/how-to-autologin-in-any-arcolinux-or-choose-a-different-desktop-to-autologin-any-desktop/>)

 

![](https://arcolinux.com/wp-content/uploads/2024/04/login.png)

INSTALL DIFFERENT KERNEL 

Not every computer is build the same and ever so often the latest kernel will not work on your system.

You can install a different kernel or you can downgrade the kernel. There are many options to fix it.

Do not use gui's. Use the terminal. It is so simple.

[Here you can find everything you need to know about kernels.](<https://arcolinux.com/category/arcolinux/general/kernel/>)

 

PAMAC CAN BE YOUR GRAPHICAL UPDATER AND INSTALLER

Pamac comes from the AUR and is a graphical way to install/remove and update packages.

Personally I use pamac-aur to learn about the content of the packages.

I will update via the terminal with **update** and **upall** to read and follow what packages are changing my system.

There is Octopi as alternative for another GUI. We trust pacman in a terminal.

[Here you can find everything you need to know about kernels.](<https://arcolinux.com/category/arcolinux/general/kernel/>)

 

RESOLUTION SCREEN FOR TILING WINDOW MANAGERS

For tiling window managers I would like to give you the tip to search our websites for the words **arandr, xrandr and lxrandr** to set your resolution. Other desktops often have tools available to set your display.

Our ArcoLinux welcome app has a direct link to the Arandr application.

![](https://arcolinux.com/wp-content/uploads/2024/04/arandr.png)

NVIDIA

Linux can run without the proprietary drivers from Nvidia. There is also the possibility to use the drivers from Nvidia.

We have created many articles about Nvidia and all the possible drivers and options.

[Click here to see the list of articles.](<https://arcolinux.com/nvidia-driver/>)

 

GITHUB

Put your personal configuration files on github and reuse them after a clean install.

Create scripts and make them better after every clean install.

[Create your own github account for free. Super easy.](<https://arcolinuxd.com/easy-way-to-learn-about-git-and-github/>)

 

CLOUD SERVICES

Put your personal configuration files in the cloud and reuse them after a clean install.

**Onedrive, Dropbox, Google Drive, Pcloud, Mega,...**

You can install all these tools on ArcoLinux.
