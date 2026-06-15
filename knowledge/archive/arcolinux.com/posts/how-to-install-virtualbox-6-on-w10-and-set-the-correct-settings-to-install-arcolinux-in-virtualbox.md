---
title: "How to install virtualbox 6 on W10 and set the correct settings to install ArcoLinux in virtualbox"
url: https://arcolinux.com/how-to-install-virtualbox-6-on-w10-and-set-the-correct-settings-to-install-arcolinux-in-virtualbox/
date: 2019-01-30 19:04:19
type: post
categories: ["Pre-installation", "Virtual Machines"]
tags: ["update", "virtual machines", "windows"]
source_site: arcolinux.com
---

# How to install virtualbox 6 on W10 and set the correct settings to install ArcoLinux in virtualbox

![](https://arcolinux.com/wp-content/uploads/2019/01/virtualbox-w10-arcolinux.jpg)

You can install an operating system in a virtual machine like **virtualbox** , vmware, boxes, qemu,... and others.

BUT

Operating systems should run on "real metal". They need to be installed on your laptop or desktop.

> All the RAM and all the power of the CPU and GPU should be available for the operating system and NOT HALF.

HOWEVER Virtualbox is a good way to see if this operating system is interesting enough to install it on your machine. If you do not like it in virtualbox, you will still not like it on real metal.

I have found myself a solution to easily switch my operating system [with a bay that contains an SSD](<https://arcolinux.com/how-to-mount-an-ssd-bay-in-your-desktop-to-easily-switch-between-windows-and-linux/>). SSD's are preferable over harddisks as they are much faster to boot up from... more responsive. Even an old computer will seem to fly, if you give it an **SSD**.

We download virtualbox from the website :

<https://virtualbox.org>

We download the ArcoLinux iso from the website :

<https://sourceforge.net/projects/arcolinux/files/>

We explain that there are more than one server to download from.   
Choose the fastest server for you.

We install virtualbox.

Then we create a new **template**.

Check the video for the settings. Same settings we use on ArcoLinux will work.

We can clone that template later to get us started faster when we test out iso's.

Then we install ArcoLinux as usual and reboot.

We get rid of the iso in Virtualbox so it boots up from the harddisk.

Video: <https://www.youtube.com/watch?v=-AvshDoC1pc>

After installing ArcoLinux we will update this ArcoLinux 19.01.4 in order to keep rolling.

[There is an article just about updating here.](<https://arcolinux.com/how-to-update-any-arcolinux-or-stay-rolling/>)

There is a new **kernel** and new **systemd**. After the update you best reboot and let the new kernel kick in.

Compton received a major update so we updated our compton.conf. [More info in this article](<https://arcolinux.com/all-information-regarding-compton-and-compton-conf/>).

We go over the most important aliases:

  * bupskel
  * alias
  * skel
  * update
  * pksyua



We visit the AUR from Arch Linux and see how you can **order** by **vote** or by **popularity**.  
<https://aur.archlinux.org>

We delete one obstructing file with this command
    
    
    sudo rm /usr/share/icons/Numix-Circle/icon-theme.cache

We should use all the cores of your cpu.

There is a command you should run after a clean install

**~/.bin/main/000-use-all-cores-makepkg-conf-v*.sh**

[There is a funscript on ArcoLinux.](<https://arcolinux.com/installing-fun-stuff-for-the-terminal-on-arcolinux/>)

You can use the script to install the linux-lts kernel.

We explain what an out-of-date package means in pksyua.

Help maintainers to keep their packages up-to-date and flag a package out-of-date.

We stay rolling when we run our script.

Then we change lsb-release to 19.02.4.

Video: <https://www.youtube.com/watch?v=lYbdGmsMOX8>
