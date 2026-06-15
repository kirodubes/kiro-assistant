---
title: "Building and installing the future kernel from AUR"
url: https://arcolinux.com/building-and-installing-the-future-kernel-from-aur/
date: 2020-12-22 13:46:22
type: post
categories: ["Kernel"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# Building and installing the future kernel from AUR

![](https://arcolinux.com/wp-content/uploads/2020/12/newkernel.jpg)

We investigate with yay what kernels we can build from the AUR.

We visit the website <https://kernel.org>. We take a look at the PKGBUILD of the kernel. In the ~/.cache/yay folder we take a look at all the data that is required to build a kernel.

We go on a search to find some kind of list of all the nvidia cards supported in the kernel. Unfortunately I just found parts. It was my believe there used to be some kind of list in the files from kernel.org. Maybe you can find it. Maybe it is just not there. We did find a lot of links online.

We find somewhere the word '**bloated** '. [This is where we talk about it.](<https://youtu.be/LLuY3p_ptuM?t=1877>)

> Bloated (in ArcoLinux) means efficient.
> 
> Bloated (in ArcoLinux) means it is suited to our workflow and the development work we do.

We explain again the vision of ArcoLinux, ArcoLinuxD and ArcoLinuxB project.

Simply put

ArcoLinux is for the developers of ArcoLinux and anyone who likes our vision.  
ArcoLinuxD is for people who want to go for bare installation or not (calamares lets you install packages).  
ArcoLinuxB is for people who want to control what goes on their system. Build your own iso.

We pass our time by changing the look of our Xfce system. Nothing can be more fun.

Video: <https://youtu.be/LLuY3p_ptuM>

We use the **grub-customizer** to set the new kernel as the first line to boot.

Video: <https://youtu.be/6GxxH0qdlYs>

This time we do have the new kernel that boots up.

We add plank and change the theme. And we pin some applications to the panel.

Video: <https://youtu.be/ZJ3v1KdVwjU>
