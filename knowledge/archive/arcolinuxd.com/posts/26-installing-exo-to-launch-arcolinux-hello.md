---
title: "26 installing exo to launch ArcoLinux Hello"
url: https://www.arcolinuxd.com/26-installing-exo-to-launch-arcolinux-hello/
date: 2018-11-11 12:08:00
type: post
categories: ["Plasma"]
source_site: arcolinuxd.com
---

# 26 installing exo to launch ArcoLinux Hello

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/exo-open.jpeg)

We have created a link on the ArcoLinux ISO (xfce, openbox and i3) that points to the most important page on arcolinux.info :

<https://arcolinux.info/arcolinux-editions/>

When you type "**hello** " in the menu of **xfce** or **plasma** you will get a menu item. Behind this menu is an application that will guide you to this specific url on the **browser of your choice**.

Since **exo** is an **xfce** application it was **NOT** **installed** on **Plasma.**

****

# **What are your options now?**

## Option 1 :

Whatever and never click the link. Do not install anything.

## Option 2 :

Git rid of this menu altogether and not install anything 
    
    
    sudo rm /usr/share/applications/arcolinux-hello.desktop

## Option 3 :

Install the package this menu requires (option of the video and future ArcoLinuxB)
    
    
    sudo pacman -S exo

We explain the power of pamac and investigate this application exo.  
After the installation you can use pamac to investigate what is installed on your machine.
    
    
    exo-open --help

Since exo is an XFCE application it will never go look into the default application settings of Plasma.   
You can set the preferred applications in exo with this command in the terminal.
    
    
    exo-preferred-applications

Video: <https://youtu.be/IsoSJ71mQ5k>

## **Plasma Challenge**

You can follow our tutorials based on either of two ISO's.

**1\. ArcoLinuxB Plasma (recommended)**

We record the plasma video's on an SSD installed from the **ArcoLinuxB Plasma ISO**.  
You can either **create** your very own ArcoLinuxB Plasma ISO [following this tutorial](<https://arcolinuxb.com/byoi-on-arcolinux-plasma/>) or [download it from Sourceforge](<https://sourceforge.net/projects/arcolinux-community-editions/files/plasma/>). (ArcoLinuxB-plasma-18.11.2.ISO of 4.3 GB - games included)

**2\. ArcoLinuxD Plasma**

You can also use the ArcoLinuxD ISO and then install Plasma with the help of the github scripts. This will not be an exact copy of the ISO.

> Learn about the Plasma desktop and enjoy it.
