---
title: "Installation of Icewm on Arch Linux Phase 4"
url: https://www.arcolinuxd.com/33-how-to-install-arch-linux-on-bios-and-install-icewm/
date: 2020-09-24 10:14:52
type: post
categories: ["ArchWayDesktop"]
source_site: arcolinuxd.com
---

# Installation of Icewm on Arch Linux Phase 4

![](https://www.arcolinuxd.com/wp-content/uploads/2020/09/archlinux-icewm.jpg)

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

We install **icewm** with
    
    
    sudo pacman  -S icewm

**This is Icewm from Arch Linux.**

Now you need to configure it.

There may be missing pieces. You need to figure that out.

Now we could get our ArcoLinux packages into Arch Linux. ArcoLinux created an application for that called

**arcolinux-spices**

[Download it from here.](<https://arcolinux.info/download-applications/>)

Then we install it. Not shown in the video

Video: <https://youtu.be/tlox4aeVqLM>
