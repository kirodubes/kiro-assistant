---
title: "5 How to autologin into your plasma desktop"
url: https://www.arcolinuxd.com/5-how-to-autologin-into-your-plasma-desktop/
date: 2018-11-07 22:45:42
type: post
categories: ["Plasma"]
tags: ["autologin"]
source_site: arcolinuxd.com
---

# 5 How to autologin into your plasma desktop

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/lightdm.jpeg)

Since Plasma works on lightdm now as login or display manager we need to edit the lightdm configuration file. [More technical info at Arch Wiki](<https://wiki.archlinux.org/index.php/LightDM>).

Let us open up /**etc/lightdm/lightdm.conf** and change one word from **xfce** to **plasma** and **save** it.

You can see what I changed the above picture. (blue line)

That is all it takes.

Change 

**autologin-session=xfce**

to

**autologin-session=plasma**

Video: <https://www.youtube.com/watch?v=Kjvpb2EhWdI>

## **Plasma Challenge**

You can follow our tutorials based on either of two ISO's.

**1\. ArcoLinuxB Plasma (recommended)**

We record the plasma video's on an SSD installed from the **ArcoLinuxB Plasma ISO**.  
You can either **create** your very own ArcoLinuxB Plasma ISO [following this tutorial](<https://arcolinuxb.com/byoi-on-arcolinux-plasma/>) or [download it from Sourceforge](<https://sourceforge.net/projects/arcolinux-community-editions/files/plasma/>). (ArcoLinuxB-plasma-18.11.2.ISO of 4.3 GB - games included)

**2\. ArcoLinuxD Plasma**

You can also use the ArcoLinuxD ISO and then install Plasma with the help of the github scripts. This will not be an exact copy of the ISO.

> Learn about the Plasma desktop and enjoy it.
