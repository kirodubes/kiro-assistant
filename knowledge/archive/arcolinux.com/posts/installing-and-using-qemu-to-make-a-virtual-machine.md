---
title: "Installing and using Qemu to make a virtual machine"
url: https://arcolinux.com/installing-and-using-qemu-to-make-a-virtual-machine/
date: 2020-09-22 08:56:04
type: post
categories: ["Virtual Machines"]
tags: ["resolution", "virtual machines"]
source_site: arcolinux.com
---

# Installing and using Qemu to make a virtual machine

![](https://arcolinux.com/wp-content/uploads/2019/05/ArcoLinuxD-qemu-mate.jpg)

> Virtual box is and will stay our official supported Virtual Machine emulator.

> Installing can be done on any desktop.
> 
> Look past the desktop environment

We start by re-using our installation script from [ArcoLinux-Nemesis github](<https://github.com/erikdubois/arcolinux-nemesis>).

We download the zip file and run the script to install Qemu. Follow the video for that.

Then we start setting up the Virtual Machine.

Since **Virtualbox** is our **official** **virtual** **machine** **application** that we support I have not played around with [Qemu](<https://wiki.archlinux.org/index.php/QEMU>) that much. We show you the website of [kvm](<http://www.linux-kvm.org>) and there is an Arch Linux wiki page as well about [kvm](<https://wiki.archlinux.org/index.php/KVM>).

Memory and cpu should be 50/50 for guest and host. In the video I have given the vm (virtual machine) just one core. That is why it was a bit slow.

Set it like this if you have 8 cores like me.

![](https://arcolinux.com/wp-content/uploads/2019/05/arcolinux-qemu-4cpus.jpg)

We are using an application insync (paid) to get the latest ArcoLinuxD iso from google drive. I just sync the things I need. The rest stays in the cloud.

We go over some of the settings in the video to set everything up and install ArcoLinuxD on our vm.

The resolution is not optimal but we can fix that.

And the network is not working since we did not reboot yet and copy/pasted "the code" (see video) in the terminal after reboot.

Video: <https://youtu.be/VXgMm4U-ucI>

In the next video we are going to set the screen resolution. 

Depending on the desktop you have tools to set your screens resolution but you will always have **arandr**.

With xrandr and arandr it is a walk in the park to make a command to set your resolution something like this
    
    
    xrandr --output HDMI1 --primary --mode 1920x1080 --pos 0x0 --rotate normal

We use this code more in tiling window managers (awesome, bspwm, i3, qtile, xmonad, ...) then in the window manager (cinnamon, mate, xfce, ...).

> I advise you use the application your desktop provides.

Video: <https://youtu.be/lpfvSPHIq1Q>

Going over the settings of Qemu one last time and finish this project by changing the theme and icons.

Video: <https://youtu.be/Ba15eDLY8m8>

Video: <https://youtu.be/6zWzFKVfCVE>

![](https://arcolinux.com/wp-content/uploads/2019/05/arcolinuxd-mate-qtile.jpg)
