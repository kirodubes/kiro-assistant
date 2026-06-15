---
title: "6 The actual installation of Arch Linux Phase 2"
url: https://www.arcolinuxd.com/6-the-actual-installation-of-arch-linux-phase-2/
date: 2020-01-01 12:50:38
type: post
categories: ["Arch Way"]
tags: ["archlinux"]
source_site: arcolinuxd.com
---

# 6 The actual installation of Arch Linux Phase 2

Boot from your SSD, harddisk or VirtualBox

GRUB, REFIND, SYSTEMD-BOOT OR EFISTUB

The images are shown in that order from left to right, from top to bottom.

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-grub-reboot.jpg)![](https://www.arcolinuxd.com/wp-content/uploads/2021/12/refind-boot.jpg)![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-login-root.jpg)![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/efistub.png)

Reboot selecting the first line.

Login as **root** with the password you choose.
    
    
    root

**Then type in your password.**

Confirm **NetworkManager** activated the internet with **pacman -Syu**. (sudo is not required since you are root)

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-logged-in-as-root.png)

Since pacman can download in parallel we want to activate this in /etc/pacman.conf

Delete the # before ParallelDownloads = 5 and maybe increase the number.
    
    
    nano /etc/pacman.conf

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-pacman-parallel.png)

## AUR HELPERS

Because your AUR helper may change over time, check the following webpage from time to time:

<https://wiki.archlinux.org/index.php/AUR_helpers>

ArcoLinux is using **Yay** and **Paru** as Aur helpers.

**Two** Aur helpers: if one **fails** , the other is there as **fall-back**.

[We suggest installing the helpers from a graphical environment.](<https://www.arcolinuxd.com/get-your-aur-helpers-in-on-any-arch-linux-based-system/>)

MULTILIB REPOSITORY

NOT IN ARCH WIKI

YOU CAN DO THIS LATER

SKIP IT FOR NOW

Multilib repositories include applications such as **wine** and **steam**. You can perferm these actions later at your discretion.
    
    
    nano /etc/pacman.conf

Edit the pacman.conf to include the multilib repositories. Just delete the hashtag in front of the two lines. We changed some of the settings on top as well. They are interesting but not essential. 
    
    
    [multilib]
    include = /etc/pacman.d/mirrorlist

Check out our **ArcoLinux pacman.conf** if you want to have the same settings. If you update the system after the changes, you will see an extra line for multilib.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-multilib-update.jpg)

Video: <https://youtu.be/L5gEdMX5wfM>

Bash completion

For our ease and future comfort we install bash-completion. It completes commands when you press on TAB.
    
    
    pacman -S bash-completion

Video: <https://youtu.be/dEj7y8gdBhM>

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-bash-completion.jpg)PERSONAL ACCOUNT

Next is to create our personal account for which you chose a login name.

As ane example, I will create an account "erik" with this command (**more information on** this [page](<https://wiki.archlinux.org/index.php/users_and_groups>))
    
    
    useradd -m -g users -G audio,video,network,wheel,storage,rfkill -s /bin/bash erik

To make the password for the account, type:
    
    
    passwd erik

For user "erik" to do administrative tasks requires editing the visudo file installed by the base-devel group package.

Type the following command:
    
    
    EDITOR=nano visudo

Look for this line of code and delete the hashtag in front of it.
    
    
    %wheel ALL=(ALL) ALL

Then logout with
    
    
    exit
    
    
    useradd -m -g users -G audio,video,network,wheel,storage,rfkill -s /bin/bash erik
    
    
    passwd erik
    
    
    EDITOR=nano visudo
    
    
    %wheel ALL=(ALL:ALL) ALL
    
    
    exit

Video: <https://youtu.be/IwUYkOhoC0w>

Log back in with your personal account.  
I will login with **erik** and its **password**.
    
    
    erik

**Fill in your personal password.**

Internet is activated thanks to **networkmanager**. We try it out with **sudo pacman -Syu**.
    
    
    sudo pacman -Syu

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-login-erik.png)[NEXT STEP](<https://www.arcolinuxd.com/7-the-actual-installation-of-arch-linux-phase-3>)
