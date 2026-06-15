---
title: "How to get the fastest Arch Linux servers"
url: https://arcolinux.com/how-to-get-the-fastest-arch-linux-servers/
date: 2020-04-16 14:18:32
type: post
categories: ["Pacman", "Update"]
source_site: arcolinux.com
---

# How to get the fastest Arch Linux servers

![](https://arcolinux.com/wp-content/uploads/2020/04/mate-update.jpg)

It started with the wish to have an up-to-date mirrorlist **during the installation of ArcoLinux**.

**Calamares** provides us a great variety of **applications** to **download**. It is now more than ever important to get the best Arch Linux servers for your country. The alias **mirror** would update the mirrorlist. But we wanted an **automated** **service** for it so users can focus on Calamares.

> The faster the Arch Linux servers, the faster ArcoLinux will be installed.

We created an extra service in the package **arcolinux-system-config-git** that will quietly check **during boot-time** which Arch Linux servers are the fastest today. This happens **automatically** in the **background** and you will never see it. We see the result in /etc/pacman.d/mirrorlist.

Randomly during the day an **/etc/cron.daily** task is requesting the best Arch Linux servers. This cron job has been working for months already. We will decide later if we keep this cron job or not (arcolinux-cron-git).

**Practical example**

If you start working at 6.00AM you get a new mirrorlist from arcolinux-system-config-git and during the day you will get an update of the mirrorlist from the cron service.

You may at any time use our aliases **mirror** , **mirrors** , **mirrord** and **mirrora** to possibly the improve connection speed.

LAPTOP USERS  
During calamares installation

During the **installation** of **ArcoLinux** (Calamares) make sure you have **internet**.

**First** advice is plug in a **lan** **cable** and stay connected then everything goes **automatically**.  
**Second** advice is use the **networkmanager** icon in the bottom right to connect to wifi.  
**Third** advice is [use **nmtui** to connect](<https://arcolinux.com/connecting-to-the-internet-via-wifi-any-desktop/>) to wifi via terminal.

Then you need to update the Arch Linux servers.

Type in a terminal
    
    
    sudo update-mirrors

or

one of the aliases

mirror

mirrora

mirrors

mirrord

Now you are ready to install the packages provided in Calamares.

Video: <https://youtu.be/DLKLEeil1AY>
