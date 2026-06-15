---
title: "How to install the linux-mainline kernel coming from AUR"
url: https://arcolinux.com/how-to-install-the-linux-mainline-kernel-coming-from-aur/
date: 2018-10-11 16:46:06
type: post
categories: ["Kernel"]
tags: ["kernel"]
source_site: arcolinux.com
---

# How to install the linux-mainline kernel coming from AUR

![](https://arcolinux.com/wp-content/uploads/2018/10/linux-mainline.jpg)   


A question on the forum results in an other tutorial on youtube and here.

When we wrote this article my main machine has kernel 4.18.12.  
Linux-mainline kernel is 4.19rc.7.

So the idea is to test out /experiment with the newer kernels of the moment.

![](https://arcolinux.com/wp-content/uploads/2018/10/kernel.org_.jpg)   


The name **mainline** comes from **kernel.org** where we can see that is indeed the **last** **kernel** that has been released on 2018-10-07. It is now 11 October. So this particular kernel was released 4 days ago.

That package can be installed from AUR.

So you need an AUR helper.

Either **yay** or **trizen** will help you with that.

2018/10/11 there are 3 keys to be imported.
    
    
    yay -S linux-mainline

Depending on your internet service provider you either need to do something or not if you get an error importing the keys.  
If you get an error, you follow this [tutorial](<https://arcolinux.com/how-to-fix-one-or-more-pgp-signatures-could-not-be-verified-libc-and-discord/>). Included in this video as well.  
Then try again
    
    
    yay -S linux-mainline

It will take quite a while to build your kernel.

Then install it. In my case I went to work and let it compile. I installed it from ~/.cache/yay/linux-mainline with
    
    
    sudo pacman -U ...

Then we do an **update-grub** and try out the new kernel.
    
    
    update-grub

If you want to install [virtualbox](<https://arcolinux.com/how-to-install-virtualbox-on-a-computer-with-a-linux-mainline-kernel/>) later on, you can install the linux-mainline-headers now too. You will find it in ~/.cache/yay/linux-mainline folder as well.
    
    
    sudo pacman -U linux-mainline-headers...

![](https://arcolinux.com/wp-content/uploads/2018/10/yay-folder-linux-mainline.jpg)   


Video: <https://youtu.be/Ppntut_vL_U>

  


Let us remove the linux-mainline kernel again with these commands
    
    
    sudo pacman -R linux-mainline
    update-grub

Video: <https://youtu.be/N1XVLl_50Dk>

  


There are other kernels you can install.

[Check this article.](<https://arcolinux.com/installing-a-new-kernel-linux-linux-lts-linux-hardened-linux-zen/>)

Installation on SSD

8 cores enabled

Skipping pgp keys import

BUILDING TAKES 30 minutes

Video: <https://youtu.be/ObmkGaNRKcA>

  
![](https://arcolinux.com/wp-content/uploads/2018/10/kernel-new.jpg)   


4.19 kernel has been released

A tip how to read your pacman.conf the easy way.

A tip where to exclude packages from updating.

A tip how to get the keys from Linux Torvalds and others in.

Video: <https://www.youtube.com/watch?v=BJ3F0Vo2_Vg>
