---
title: "28 How to open a folder as root on Plasma"
url: https://www.arcolinuxd.com/28-how-to-open-a-folder-as-root-on-plasma/
date: 2021-01-18 11:45:49
type: post
categories: ["Plasma"]
tags: ["dolphin", "thunar"]
source_site: arcolinuxd.com
---

# 28 How to open a folder as root on Plasma

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/open-folder-as-root.jpeg)

Solution : install thunar

**Dolphin** is under constant development and their software engineers have a vision how a file manager should work. At some point in time they decided that security wise it is not opportune to open up a file manager -- **dolphin as root**. The potential harm, a user can do, is huge.

The developers have hard-coded into Dolphin that it can not be run as root.

Our best solution for now is to install **thunar** and use the **custom** **actions** from ArcoLinux to open up a **folder as root**.

See the image above.

Install **thunar** with
    
    
    sudo pacman -S thunar thunar-volman thunar-archive-plugin

In the video you will see a new folder in dolphin called "root actions". [We installed that in this article](<https://www.arcolinuxd.com/27-how-to-add-root-services-to-dolphin-on-plasma/>).

Video: <https://youtu.be/BmpNsm8ywsI>

To get the very last updates for **Xfce-Thunar** you need to install this package and run the **skel** command afterwards.

It all depends with what ISO you started out whether you need to do this.  
This package will install "open folder as root" in thunar.
    
    
    sudo pacman -S arcolinux-xfce-git

Video: <https://youtu.be/smc9jtcCkKA>

Open thunar as root starting from Dolphin

![](https://www.arcolinuxd.com/wp-content/uploads/2021/01/openthunarasroot.jpg)

Video: <https://youtu.be/e9AY-IXVZkE>
