---
title: "Are you typing iso in the terminal and nothing happens - dev-rel and lsb-release"
url: https://arcolinux.com/are-you-typing-iso-in-the-terminal-and-nothing-happens-dev-rel-and-lsb-release/
date: 2020-11-22 11:54:39
type: post
categories: ["Update"]
source_site: arcolinux.com
---

# Are you typing iso in the terminal and nothing happens - dev-rel and lsb-release

![](https://arcolinux.com/wp-content/uploads/2020/11/iso.jpg)

Starting from the [September](<https://arcolinux.info/arcolinux-d-b-20-9/>) release of 2020 we went rolling and stopped using 'versions'.

Users mistakenly thought that the version was THE indicator to know if the operating system was up-to-date.

The version number is arbitrary. It is just a text file anyone can change to any version they like.

So the new 'version' is now **rolling** like Arch Linux.

At the same time we introduced some kind of reference for ourselves.

Knowing what **iso** a user starts with can help us analyze what issue a user has and find a solution.

A new file **/etc/dev-rel** and a new **alias** 'iso' were created for that reason.

Video: <https://youtu.be/Kp0Wx1Qj37U>

Possible text for the /etc/dev-rel file
    
    
    ISO_RELEASE=v20.7.6  
    ISO_CODENAME=ArcoLinux  
    ISO_BUILD=Wed 15 Jul 2020 01:23:01 PM CEST
