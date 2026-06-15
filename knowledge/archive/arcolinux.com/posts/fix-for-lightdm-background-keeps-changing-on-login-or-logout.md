---
title: "Fix for lightdm background keeps changing on login or logout"
url: https://arcolinux.com/fix-for-lightdm-background-keeps-changing-on-login-or-logout/
date: 2020-04-01 07:07:34
type: post
categories: ["Fixes", "Lightdm", "Login"]
source_site: arcolinux.com
---

# Fix for lightdm background keeps changing on login or logout

![](https://arcolinux.com/wp-content/uploads/2019/04/overwritten-background.jpg)![](https://arcolinux.com/wp-content/uploads/2019/04/login-lightdm.gif)

At this point in time, April 2019, we see a strange behavior on our XFCE desktop.

> IF you have set your wallpaper with a wallpaper coming from /usr/share/backgrounds, you will see that the background of your lightdm login screen will change to the wallpaper of your XFCE background.

Basically take a look at the gif. 

You can set whatever wallpaper via lightdm settings and it will always be overwritten.

In the video we explain why accountsservice and mugshot are in there.

## How do we solve it?

Make sure you use a wallpaper that is **NOT coming from /usr/share/backgrounds**.

Use your **own** **personal** **wallpapers** to set the background from XFCE and lightdm background will NOT be overwritten.

You can change the wallpaper with **variety** or with **Desktop** **settings**.

 

You can also solve by uninstalling accountsservice. You will notice that mugshot will not work anymore.

Video: <https://youtu.be/vBXnvwSYP_s>

Video: <https://youtu.be/oP4QVnMVRQI>

## Want to investigate it further. 

Then know that accountsservice has a file with the wallpaper in /var/lib/AccountsService/users/erik.

See image

Anything to report : [lightdm](<https://github.com/CanonicalLtd/lightdm>)

Anything to report : [accountsservice](<https://gitlab.freedesktop.org/accountsservice/accountsservice>)

![](https://arcolinux.com/wp-content/uploads/2019/04/accountsservice-file.jpg)
