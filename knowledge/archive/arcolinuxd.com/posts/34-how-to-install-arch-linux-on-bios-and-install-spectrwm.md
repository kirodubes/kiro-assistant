---
title: "All in one Arch Linux installation BIOS with Spectrwm"
url: https://www.arcolinuxd.com/34-how-to-install-arch-linux-on-bios-and-install-spectrwm/
date: 2020-09-24 18:11:18
type: post
categories: ["ArchWayAllinone", "ArchWayDesktop"]
source_site: arcolinuxd.com
---

# All in one Arch Linux installation BIOS with Spectrwm

![](https://www.arcolinuxd.com/wp-content/uploads/2020/09/Screenshot_20200924_180832.jpg)

We install Arch Linux on VirualBox with **BIOS** activated + swap. [We use this tutorial](<https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-bios/>).

We get our Arch Linux ISO from archlinux.org and boot from it.

The correct Virtualbox settings must be applied. Check them out.

Then we follow the guide.

Cloning a VirtualBox makes sense, reuse the work you have done.

And then install Deepin or Mate or Plasma or ...

Video: <https://youtu.be/n-lyY11ZJc8>

We start from the last video. We have a basic Arch Linux on our Virtualbox.

Now we need to install the desktop. Lightdm is already activated but there is no desktop behind it yet.

**We go to the TTY with Right-CTRL + F3.**

**On real metal you use Ctrl + Alt + F3**.

We install **spectrwm** with
    
    
    sudo pacman  -S spectrwm

**This is Spectrwm from Arch Linux.**

**We need to copy/paste /etc/spectrwm.conf to the ~/.spectrwm.conf to edit it easily.**

**Many lines were still commented out.**

Now you need to configure it.

There may be missing pieces. You need to figure that out.

Video: <https://youtu.be/m9CMnljlk2Q>

Now we get our ArcoLinux packages into Arch Linux. ArcoLinux created an application for that called

**arcolinux-spices**

[Download it from here.](<https://arcolinux.info/download-applications/>)

Then we install it.

This can be a good way to learn about ArcoLinux and Arch Linux.

Video: <https://youtu.be/wU5eq4DmUcw>
