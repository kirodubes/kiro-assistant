---
title: "16 How to add a locking mechanism to Gnome - archlinux-logout"
url: https://www.arcolinuxd.com/16-how-to-add-a-locking-mechanism-to-gnome-archlinux-logout/
date: 2022-10-23 09:19:50
type: post
categories: ["Gnome"]
source_site: arcolinuxd.com
---

# 16 How to add a locking mechanism to Gnome - archlinux-logout

Just install archlinux-logout-git and add a keyboard shortcut.

Sleep and autolock will not work correctly on Gnome until you active this service via a terminal.
    
    
    sudo systemctl enable betterlockscreen@$USER

You may want to check the powersaving options in the gnome settings.

Video: <https://youtu.be/-8xMlb5n9kc>
