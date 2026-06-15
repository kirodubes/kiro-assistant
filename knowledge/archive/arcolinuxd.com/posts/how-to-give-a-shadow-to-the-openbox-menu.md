---
title: "How to give a shadow to the openbox menu"
url: https://www.arcolinuxd.com/how-to-give-a-shadow-to-the-openbox-menu/
date: 2024-03-01 06:20:06
type: post
categories: ["Openbox"]
source_site: arcolinuxd.com
---

# How to give a shadow to the openbox menu

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arcolinux-openbox-compton-shadow-menu.jpg)

The compton.conf of openbox is in ~/.config/compton.conf.

Make a backup of that file and then experiment with its settings. You still have a backup in /etc/skel.

We delete a line that is holding the shadow back on the menu.

Look for the shadow-exclude part and delete this line

**"! name~=''",**

Then log out and log back in to apply the new compton settings.

We see that the conky gets a shadow too. 

Personally it looks nice but we show you how to get rid of that in the video.

Video: <https://youtu.be/wJ6EWP6mdc4>
