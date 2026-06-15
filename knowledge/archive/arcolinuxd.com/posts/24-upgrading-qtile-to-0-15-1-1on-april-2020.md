---
title: "24 upgrading qtile to 0.15.1-1on April 2020"
url: https://www.arcolinuxd.com/24-upgrading-qtile-to-0-15-1-1on-april-2020/
date: 2020-04-16 12:48:27
type: post
categories: ["Qtile"]
source_site: arcolinuxd.com
---

# 24 upgrading qtile to 0.15.1-1on April 2020

![](https://www.arcolinuxd.com/wp-content/uploads/2020/04/qtile-update.jpg)

> Short version : remove arcomemory.py from your Qtile folder

Mid April 2020 Qtile gets a new version on Arch Linux. We move from 0.14 to 0.15 and we needed to adjust our config accordingly.

This video contains a lot more than "delete the one file and never use it again" advice.

We start by opening up picom.conf and make sure we have transparency in VirtualBox.

#vsync = true

We install screenkey. It helps you to show what keys are pressed if you want to make tutorials.

Then we fix the nss error we were all faced with. [See Arch Linux for news](<https://www.archlinux.org/news/nss3511-1-and-lib32-nss3511-1-updates-require-manual-intervention/>).

There is also a new feature on your computer. ArcoLinux-system-config will update your Arch Linux mirrorlist at every boot.

We show you that skel will always make a backup of your .config. We put back our picom.conf setting to get transparency back.

We never delete anything in your home directory. That is up to you.

**Remove arcomemory.py in your qtile folder.**

We show you what config we will use in the next release - config-future.py.

We install arcolinux-logout-git in order to show how Qtile will look in the future.

We show you our lock screen.

You can also delete **compton-toggle.sh** as it is replaced with picom-toggle.sh.

Video: <https://youtu.be/zQ0pt6Zjw2U>
