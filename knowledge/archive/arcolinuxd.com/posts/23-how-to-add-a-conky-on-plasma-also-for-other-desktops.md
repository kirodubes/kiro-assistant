---
title: "23 How to add a conky on Plasma - also for other desktops"
url: https://www.arcolinuxd.com/23-how-to-add-a-conky-on-plasma-also-for-other-desktops/
date: 2018-11-10 16:14:00
type: post
categories: ["AnyDesktop"]
tags: ["anydesktop", "conky"]
source_site: arcolinuxd.com
---

# 23 How to add a conky on Plasma - also for other desktops

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/conky-system-wo.jpeg)

**Conkyzen** (am-conkyzen - application where you can select all the conkies), the **conkies** (arcolinux-conky-collection-git) and the **conky application** (conky-lua-archers) are already installed on your system.

**Plasma** has its own **widgets**. But if you want to have **your** **preferred** **conky** back, you can.

It is possible you need to change a few things.

> With a bit of knowledge you can run any conky on any desktop.

In this video we are going to run the conky from [Willem](<https://www.deviantart.com/wim66>).

We just need to change this line from 

_own_window_type = 'desktop',-- # options are: normal/override/dock/desktop/panel_

to

_own_window_type = 'override',-- # options are: normal/override/dock/desktop/panel_

Video: <https://youtu.be/5EKOwkk7CgU>

How to autostart a conky

**Conkyzen** (am-conkyzen - application where you can select all the conkies), the **conkies** (arcolinux-conky-collection-git) and the **conky application** (conky-lua-archers) are already installed on your system.

__

We need to know that **am-conky-session** is the application that **actually** **launches** the conkies.

If we can **autostart** that one upon boot, we will have a conky at boot. We have made already such a tutorial for the [pamac-tray icon](<https://www.arcolinuxd.com/22-adding-the-pamac-update-icon-to-the-tray-and-configuring-pamac-on-plasma/>).

**Follow the video to see how we autostart am-conky-session.**

Video: <https://youtu.be/cw52vCGwxfI>

We will also show you in above video how to add an extra custom **keyboard** **shortcut** to launch **dolphin** \- the **file manager** from Plasma.

# General conky info

> A conky will NEVER EVER work on all desktops.

**There are just too much differences between all the different window managers.**

It will also depend on the software you have installed.

There are two versions of the application called 'conky'.

  1. version 1.9 and earlier - old syntax
  2. version 1.10 and higher - new syntax - LUA (and old syntax)



We install the application **conky-lua-archers (1.10)** on ArcoLinux

**Options to explore when encountering issues :**

  * own_window_type = 'desktop', # options are: normal/override/dock/desktop/panel
  * own_window_transparent = true, # options are : true and false
  * own_window_argb_visual = true, # options are : true and false
  * own_window_argb_value = 0, # options are : 0-255



#### More information about conkies can be found here :

[Arch wiki](<https://wiki.archlinux.org/index.php/conky>)

[Conky github configuration](<https://github.com/brndnmtthws/conky/wiki>)

[Conky github faq](<https://github.com/brndnmtthws/conky/wiki/FAQ>)

[Conky github user configs](<https://github.com/brndnmtthws/conky/wiki>)

[Conky configuration on sourceforge](<http://conky.sourceforge.net/config_settings.html>)

[Conky variables on sourceforge](<http://conky.sourceforge.net/variables.html>)

## **Plasma Challenge**

You can follow our tutorials based on either of two ISO's.

**1\. ArcoLinuxB Plasma (recommended)**

We record the plasma video's on an SSD installed from the **ArcoLinuxB Plasma ISO**.  
You can either **create** your very own ArcoLinuxB Plasma ISO [following this tutorial](<https://arcolinuxb.com/byoi-on-arcolinux-plasma/>) or [download it from Sourceforge](<https://sourceforge.net/projects/arcolinux-community-editions/files/plasma/>). (ArcoLinuxB-plasma-18.11.2.ISO of 4.3 GB - games included)

**2\. ArcoLinuxD Plasma**

You can also use the ArcoLinuxD ISO and then install Plasma with the help of the github scripts. This will not be an exact copy of the ISO.

> Learn about the Plasma desktop and enjoy it.
