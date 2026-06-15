---
title: "All information regarding compton and compton.conf"
url: https://arcolinux.com/all-information-regarding-compton-and-compton-conf/
date: 2019-05-20 08:30:04
type: post
categories: ["Compton", "Fixes"]
tags: ["compton"]
source_site: arcolinux.com
---

# All information regarding compton and compton.conf

![](https://arcolinux.com/wp-content/uploads/2019/01/light-screen-compton.jpg)

End of January 2019 **compton** has received a **major** **update** from version 4 to 5.

We use it on 5 of 12 desktops at the time of writing.

  * awesome
  * bspwm
  * i3
  * openbox
  * xmonad



Needless to say it has a big impact.

Compton will provide you the following functionality :

  * **shading**
  * **transparency**
  * **fading**



Many of the old parameters in the compton.conf were abandoned and new ones were introduced.

It made us look again at the original **compton.conf** file from the official github :

<https://github.com/yshui/compton>

We then compared our own settings and mixed both together.

Next video is about the steps we took that month.

Some of the desktops have also a folder called **backup** with the old compton.confs in it. You can always go back in time and compare settings that way.

> compton.conf =ArcoLinux compton.conf
> 
> compton.conf.github = https://github.com/yshui/compton

 

Video: <https://www.youtube.com/watch?v=dtEfyIxfAZI>

Fix for dark virtualbox in full screen

Virtual Box becomes darker when you go full screen in the old compton.conf file so we added this line :

**shadow-exclude = [**  
**...**  
**"n:w:*VirtualBox*",**  
**..**  
**];**

This ensures us that VirtualBox will not get any shading and become darker than it is supposed to be.

ArcoLinux users just need to update and skel to get this in. Other linux users should add the line to their compton.conf file.

Before adding code line

![](https://arcolinux.com/wp-content/uploads/2019/01/dark-screen-compton.jpg)

After adding code line

![](https://arcolinux.com/wp-content/uploads/2019/01/light-screen-compton.jpg)

Video: <https://www.youtube.com/watch?v=VEbcUKB5zkM>

There is NOT just ONE compton.conf for ALL  
Backup and experiment

Try switching **xrender** with **glx**.

Experimenting with compton settings

Video: <https://youtu.be/iKbJ9kHn4yY>

[Arch Wiki Compton](<https://wiki.archlinux.org/index.php/compton>)

[Report issues](<https://github.com/yshui/compton/issues>)

Possible configs that might work for you

**backend = "glx"**  
**glx-no-stencil = true;**  
**glx-no-rebind-pixmap = true;**  
**vsync = "opengl-swc";**

Where is the compton.conf

****

****

****

**Awesome : ~/.config/awesome/compton.conf**

**Bspwm : ~/.config/bspwm/compton.conf**

**i3 : ~/.config/i3/compton.conf**

**Openbox : ~/.config/compton.conf  
**

****

**Qtile : ~/.config/qtile/scripts/compton.conf**

**Xmonad : ~/.xmonad/scripts/compton.conf  
**

**Many of your desktops have a backup of this configuration file.**
