---
title: "How to get two polybars in Openbox, Bspwm, i3, Xmonad and others"
url: https://arcolinux.com/how-to-get-two-polybars-in-openbox-bspwm-i3-xmonad-and-others/
date: 2019-02-01 14:51:15
type: post
categories: ["Polybar"]
source_site: arcolinux.com
---

# How to get two polybars in Openbox, Bspwm, i3, Xmonad and others

![](https://arcolinux.com/wp-content/uploads/2019/02/arcolinux-openbox-polybar-two.jpg)

Polybar can be installed on different desktops. It is a personal choice.

You can use it in 

  * bspwm (standard applied)
  * i3
  * openbox
  * xmonad (standard applied)



Polybar is fun since it has so many [modules](<https://arcolinux.com/all-modules-that-are-available-for-polybar-any-desktop/>).

You can make it [transparent.](<https://arcolinux.com/how-to-make-the-polybar-transparent/>)

Before we build polybar we make sure we will use all the cores of your cpu.

We run the script in ~/.bin/main/000-... in order to use all all cores.
    
    
    yay polybar

We show you where yay builds its packages.

We go to ~/.config/openbox/autostart and tint2 will be replaced with polybar.

In ~/.config/polybar/launch.sh we make sure that the second bar is active. We delete the hashtags. 

Log out and log back in and you will have 2 bars.

Then you can start changing the modules.

Video: <https://youtu.be/OPRS7QMunUY>
