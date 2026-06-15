---
title: "How to fix the logo of neofetch after a lsb-release update"
url: https://arcolinux.com/how-to-fix-the-logo-of-neofetch-after-a-lsb-release-update/
date: 2019-12-04 19:25:13
type: post
categories: ["Neofetch"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to fix the logo of neofetch after a lsb-release update

![](https://arcolinux.com/wp-content/uploads/2018/06/lsb_release.jpg)

Every now and again we receive an update from the application **lsb-release**. It will overwrite the code that is written on your system in the file **/etc/lsb-release** with its own.

**Neofetch** uses this file to determine on what system it has been installed and will show the appropriate ascii logo. In this case we get an **Arch** logo.

Change the code back to the **original** code with a copy/paste.

In the video we show you where you can find the code on the github.

Copy/paste this code in /etc/lsb-release.

Check manually if the **release** and **codename** are updated in the future. Written June 2018 and updated in Nov 2019.

Distrubtion release is the current number the iso carries like 20.1.1 aka year 2020 , month January, release 1.
    
    
    LSB_VERSION=1.4
    DISTRIB_ID=Arcolinux
    DISTRIB_RELEASE=vxx.x.x
    DISTRIB_CODENAME=ArcoLinux
    DISTRIB_DESCRIPTION=ArcoLinux

Video: <https://www.youtube.com/watch?v=gcT2yZbB65M>
