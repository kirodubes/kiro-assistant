---
title: "Install any desktop on any ArcoLinux or Arch Linux system"
url: https://arcolinux.com/install-any-desktop-on-any-arcolinux-or-arch-linux-system/
date: 2019-11-18 16:14:40
type: post
categories: ["Post-installation"]
source_site: arcolinux.com
---

# Install any desktop on any ArcoLinux or Arch Linux system

![](https://arcolinux.com/wp-content/uploads/2019/11/arcolinux-play-intro.jpg)![](https://arcolinux.com/wp-content/uploads/2019/11/arcolinux-play.jpg)

game changer

Learn, have fun and enjoy

Build up from scratch   
or  
add desktops to your current one

Use our githubs or our cheatsheet

Get the cheat sheet on <https://arcolinux.info/documents-arcolinux/>

We re-organized the packages so it becomes clear what "lego blocks" you need to install when you want to install additional **desktops**.

We use our **cheatsheet**. In the video we will explain what it all means and how to use it.

**Green** = install those to have a working desktop

**Orange** = ArcoLinux settings and configs

**Yellow** = not needed and if you install it then just one - otherwise you will have conflicts

We show you with a virtualbox installation how we can use our cheatsheet or our githubs on ArcoLinuxD or ArcoLinuxB.

We start here with ArcoLinuxD which does not provide any desktop at start off.

It is a little bit harder since you end in a TTY. But you can always add a desktop to ANY ArcoLinux.

**We can end up with a system that contains all desktops.**

![](https://arcolinux.com/wp-content/uploads/2019/11/flexible.jpg)

We install **ArcoLinuxD** and we first get the fastest Arch Linux mirrors. You can start with **any** **ArcoLinux** or even with **Arch** **Linux**.

Then we **update**.

Depending on the packages we reboot afterwards - kernels, linux-firmware, systemd, ...

**Upall** is going to check now if something has to be updated from **AUR**.

We use our cheatsheet to look up what we need.

**Option 1 :**

Long way - more learning - cheatsheet

**Option 2 :**

Fast way - git clone the ArcoLinuxD githubs

 

Then we install AWESOME on ArcoLinuxD.

Follow the steps to install awesome in the video. Do not forget to install lightdm applications.

We log out and log back in and we add in the standard awesome. Not our ArcoLinux config.

We need to go to our **TTY**.

Real metal computer = CTRL + ALT + F2, F3, ...

Virtual machine = Right CTRL + F2, F3, ...

Remember to do skel after installing packages that install into /etc/skel

We look for tools that are available and work our way up. After reboot the awesome menu has changed.

**Keyboard shortcuts are not working because the applications are not installed!!**

**That makes sense - I thought termite was behind the keyboard shortcut but it is urxvt that is behind CTRL + ALT + T.**

Go online and see what we use to create a desktop

Check

<https://github.com/arcolinuxd/>

or

<https://github.com/arcolinuxb>

Then we install bspwm on ArcoLinuxD.

We use part of the bspwm github scripts.

We use part of the bspwm github scripts.

In this part of the video **I had forgotten** to install arcolinux-bspwm-git and skel it afterwards.

We also make sure that we get the latest .bashrc in.

Then we install MATE on ArcoLinuxD.

You can keep installing any of the desktops...

Feel the ArcoVibe   
and start exploring

We gather all articles  
under the name SuperFlex  
follow the link

Video: <https://youtu.be/egZe-eQIPmo>
