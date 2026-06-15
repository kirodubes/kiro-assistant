---
title: "How to uninstall Samba and its components"
url: https://arcolinux.com/how-to-uninstall-samba-and-its-components/
date: 2018-11-27 12:38:51
type: post
categories: ["Samba", "Utilities"]
tags: ["samba"]
source_site: arcolinux.com
---

# How to uninstall Samba and its components

![](https://arcolinux.com/wp-content/uploads/2018/11/samba-update-1-1.jpeg)   
![](https://arcolinux.com/wp-content/uploads/2018/11/samba-error-1.jpg)   


Until ArcoLinux 18.11 Samba was installed on the iso.  
All ArcoLinux 18.12+ editions will no longer have samba and samba related software.

Since we had **issues** with **Samba** **end** of **November** we investigated Samba and decided not to include it anymore on the iso.

**If you do want** **samba** in the **future** then we have 2 scripts on any of the [ArcoLinuxD githubs](<https://github.com/arcolinuxd>) to install it. **Scripts 140 and 150** will take care of that.

Not including samba will result in a faster and more secure setup and will be less prone to future errors.

We have added a **script** to your **~/.bin/main** to **delete** **samba** and related software from your system and keep **rolling**.

> Delete samba with the script and keep rolling

You may have more packages installed that are samba related.

Depending on the desktop you may have installed helpers for the smb shares. I let you find them and delete them e.g. caja-share, nemo-share, ...

Video: <https://youtu.be/O2SwCMc5pRk>
