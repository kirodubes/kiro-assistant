---
title: "How to downgrade to an older Linux-lts kernel"
url: https://arcolinux.com/how-to-downgrade-to-an-older-linux-lts-kernel/
date: 2020-12-31 17:14:48
type: post
categories: ["Kernel"]
source_site: arcolinux.com
---

# How to downgrade to an older Linux-lts kernel

![](https://arcolinux.com/wp-content/uploads/2020/12/downgrade-to-linux-lts.jpg)

Downgrading any package including the kernel is done for a reason.

Most of the time we downgrade the package because the **new update** is **malfunctioning** with other **software** or with our **hardware**.

We have an application already pre-installed called : **downgrade**.

You can use this application to get an older version back of the needed software. You need to know the package name to do so.

In the video we downgrade the linux-lts kernel although we do not have the linux-lts kernel installed. We are working on the linux kernel.

It does not change anything. Just do not forget to update your grub with the alias '**update-grub** '.
    
    
    sudo downgrade linux-lts  
    update-grub

Your packages are coming from the archive : <https://archive.archlinux.org>

There are at least 4 linux kernels to try out

  * linux
  * linux-lts
  * linux-zen
  * linux-hardened



and the many kernels on the AUR.

Video: <https://www.youtube.com/watch?v=NyDy3PRb7Kc>
