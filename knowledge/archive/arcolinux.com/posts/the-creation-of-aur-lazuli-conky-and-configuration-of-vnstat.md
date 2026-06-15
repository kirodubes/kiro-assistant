---
title: "The creation of AUR-Lazuli conky and configuration of vnstat"
url: https://arcolinux.com/the-creation-of-aur-lazuli-conky-and-configuration-of-vnstat/
date: 2018-11-30 14:24:28
type: post
categories: ["Conky"]
tags: ["conky"]
source_site: arcolinux.com
---

# The creation of AUR-Lazuli conky and configuration of vnstat

![](https://arcolinux.com/wp-content/uploads/2018/11/Lazuli.jpg)

We download the Aureola conkies from [github](<https://github.com/erikdubois/aureola>). We choose to incorporate the **Lazuli** conky into ArcoLinux.

**What steps did I undertake to incorporate this particular conky into ArcoLinux?**

## **Contents of the video**

We download the Aureola conky and extract it.  
We analyze the content and see that we do not need the fonts - they are already installed.

We rename the conky to AUR-Lazuli.conkyrc.

We change the header content of the conky.

Then we start reading the config of the conky.

We delete the first line.

There is **NO NETWORK TRAFFIC** in the conky.

When you type **ifconfig** in your terminal you will know the **name** of your network card.

Change the name **enp0s31f6** into the network card name you find in **ifconfig**.

Use CTR + F and replace all.

We delete code for dropbox and spotify.

We see vnstat in the code of the conky. It is standard installed on ArcoLinux.

We change the colors of the conky : bars and titles.

Video: <https://youtu.be/VjF4cP6U7xg>

How to enable vnstat

We analyze in the video that the package vnstat is already installed.   
We only need to activate it.
    
    
    sudo systemctl enable vnstat.service

> Now just reboot

![](https://arcolinux.com/wp-content/uploads/2018/11/enable-vnstat.jpg)

How to know the name of your network card

Type this command and take the network card that has an actual ip address. In the picture that is enp0s3. The ip address is 10.0.2.15.
    
    
    ifconfig

![](https://arcolinux.com/wp-content/uploads/2018/11/ifconfig.jpg)

Video: <https://www.youtube.com/watch?v=m0ipSrCbBys>

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
