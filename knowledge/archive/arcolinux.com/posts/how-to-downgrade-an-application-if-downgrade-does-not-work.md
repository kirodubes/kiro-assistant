---
title: "How to downgrade an application if downgrade does not work"
url: https://arcolinux.com/how-to-downgrade-an-application-if-downgrade-does-not-work/
date: 2018-02-03 12:26:42
type: post
categories: ["Fixes", "Pacman", "Update"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to downgrade an application if downgrade does not work

![](https://arcolinux.com/wp-content/uploads/2018/02/downgrade-does-not-work.jpg) In [this article](<../fix-for-updated-applications-or-how-to-downgrade-an-application/>) we have learned that there is a powerful tool installed on ArchMerge i.e. **downgrade**. With this application you can downgrade an application in an **easy** **way**. You can see the picture at the bottom page how to downgrade firefox. BUT when you do a **clean** **install** and you want to downgrade a package from **AUR** you will **NOT** have a cache file on your system and downgrade cannot provide support for AUR. 
    
    
    /var/cache/pacman/pkg

Then here is another solution for you to solve this issue. Normally I would explain to build the package but in this instance (pamac-aur) that will not work. I will explain an even easier solution. **Download** the package from our **github** **repo**. <https://github.com/arcolinux/arcolinux_repo_iso> Go and look for the version you need i.e. [pamac-aur-6.2.2-1-x86_64.pkg.tar.xz](<https://github.com/arcolinux/arcolinux_repo_iso/tree/master/x86_64> "pamac-aur-6.2.2-1-x86_64.pkg.tar.xz") or a later version if you need it. and install it afterwards with 
    
    
    sudo pacman -U pamac-aur-6.2.2-1-x86_64.pkg.tar.xz

Then we will have to tell **pamac** and **pacman** NOT to update pamac-aur. We need to edit following file and the following line 
    
    
    /etc/pacman.conf
    
    
    IgnorePkg = pamac-aur

Video: <https://youtu.be/fFHdl8b_jYU>

Downgrading packages NOT coming from THE AUR will give you much more choice example firefox![](https://arcolinux.com/wp-content/uploads/2018/02/downgrade-firefox.jpg)
