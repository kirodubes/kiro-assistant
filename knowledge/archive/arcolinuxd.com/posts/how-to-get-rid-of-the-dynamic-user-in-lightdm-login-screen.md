---
title: "How to get rid of the dynamic user in lightdm login screen"
url: https://www.arcolinuxd.com/how-to-get-rid-of-the-dynamic-user-in-lightdm-login-screen/
date: 2019-03-12 11:11:03
type: post
categories: ["AnyDesktop", "Fixes"]
source_site: arcolinuxd.com
---

# How to get rid of the dynamic user in lightdm login screen

![](https://www.arcolinuxd.com/wp-content/uploads/2019/03/dynamic-user.jpg)

Depending in what learning stage you are (ArcoLinux learning phases), what ISO you are on ArcoLinuxD or Arch Linux or what distribution you are using ...

IF you are also using LIGHTDM as your login manager, you may see a "dynamic user" when logging in. See image.

Here is how we can get rid of this dynamic user on the login screen of lightdm.

Go to **/etc/lightdm/users.conf** and add

**/sbin/nologin**

to the last line so you get

**hidden-shells=/bin/false /urs/bin/nologin /sbin/nologin**

Other solutions is to install an extra package

**sudo pacman -S accountsservice**

Video: <https://youtu.be/ItXcZ8NL8eo>
