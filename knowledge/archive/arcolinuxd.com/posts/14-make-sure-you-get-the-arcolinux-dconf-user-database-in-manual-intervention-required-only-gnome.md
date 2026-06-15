---
title: "14 make sure you get the ArcoLinux dconf/user database in - manual intervention required - only Gnome"
url: https://www.arcolinuxd.com/14-make-sure-you-get-the-arcolinux-dconf-user-database-in-manual-intervention-required-only-gnome/
date: 2019-07-11 16:20:42
type: post
categories: ["Fixes", "Gnome"]
source_site: arcolinuxd.com
---

# 14 make sure you get the ArcoLinux dconf/user database in - manual intervention required - only Gnome

![](https://www.arcolinuxd.com/wp-content/uploads/2019/07/dconf-gnome.jpg)

When developing Gnome in July 2019 it came to my attention that the settings I had created and saved in ~/.config/dconf/user were not applied into the system.

Updates came in /etc/skel/.config/dconf/user.

We did the skel command (check your aliases) but the new settings like icon, wallpaper, themes, ...

Dconf is a kind of database that keeps track of all the settings of Gnome. You can only edit it via dconf-editor.

# Tip 

> Copy/paste the /etc/skel/.config/dconf/user manually over to ~/.config/dconf/user
> 
> and check and recheck
> 
> then reboot

Video: <https://www.youtube.com/watch?v=r6OZTwjC7BQ>
