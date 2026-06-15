---
title: "How to change the version number of ArcoLinux"
url: https://arcolinux.com/how-to-change-the-version-number-of-arcolinux/
date: 2020-01-11 00:27:42
type: post
categories: ["Update"]
tags: ["update"]
source_site: arcolinux.com
---

# How to change the version number of ArcoLinux

![](https://arcolinux.com/wp-content/uploads/2018/11/lsb-release.jpg)

All it takes to change the version number of ArcoLinux is changing the file /etc/lsb-release.

I always say this number is super unimportant. It does NOT say that you have updated your system correctly.

It is just a static number that any of us can change any way we want.

We show you in the video how to manually update the number to follow OUR release number.

The number is there to let the developers know **WHEN** the iso was created. We can then analyze what has changed since that time and try to analyze issues from users.

Video: <https://youtu.be/c3IzgXrqYYI>

Alternatively you can run the stay-rolling scripts in your
    
    
    .bin/stay-rolling

folder.

Choose from what release number to what release number you want to update.

![](https://arcolinux.com/wp-content/uploads/2020/01/stay-rolling-folder.jpg)

All of our update videos include the stay-rolling scripts.

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS5RJROnazR91tD1snkoN-jD>

This is the content of the latest ArcoLinux release. It will stay like this for the coming years

Edit the file /etc/lsb-release and copy/paste this in.
    
    
    LSB_VERSION=1.4
    DISTRIB_ID=ArcoLinux
    DISTRIB_RELEASE=rolling
    DISTRIB_DESCRIPTION="ArcoLinux"

We stopped using version numbers as users are **confused** by it.  
**Update** your system and you will have an up-to-date system whatever the content in /etc/lsb-release.

[More info about going rolling can be found in this release article.](<https://arcolinux.info/arcolinux-d-b-20-9/>)
