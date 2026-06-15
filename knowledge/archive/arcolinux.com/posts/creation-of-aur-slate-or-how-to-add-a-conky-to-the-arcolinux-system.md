---
title: "Creation of Aur-Slate or how to add a conky to the ArcoLinux system"
url: https://arcolinux.com/creation-of-aur-slate-or-how-to-add-a-conky-to-the-arcolinux-system/
date: 2019-04-29 08:58:04
type: post
categories: ["Conky"]
tags: ["conky"]
source_site: arcolinux.com
---

# Creation of Aur-Slate or how to add a conky to the ArcoLinux system

![](https://arcolinux.com/wp-content/uploads/2019/04/Aur-slate-website.jpg)![](https://arcolinux.com/wp-content/uploads/2019/04/AUR-Slate.jpg)

Thanks to the fact that we have the package **conky-lua-archers** installed we can use conky and its LUA files (not needed here).

> You can add your own conkies to the system.

There are hundreds of them out there. Many are very similar since they all fall back on the possible parameters you can display like disk space, memory usage etc.

Some of them are super nice and graphical but you know taste is personal.

> So here is how YOU can add a conky to the ArcoLinux system.

We looked for a nice conky online and found one here :

<https://github.com/debianmain1/Conky-Debian-Slate/blob/master/Conky%20Debian-Slate-2/conkyrc_debian-slate>

Then we download the file. It says DEBIAN so we need to see if there are specific debian commands in there and replace them with Arch Linux commands.

We rename it and are sure they have the extension **.conkyrc** so conkyzen will pick it up.

The font was a bit tricky. I had to tell the conky to use **dejavu** **sans** **mono** to show the lines.

If the conky is not working, you need to start it from the terminal like this

conky -c ~/.config/conky/xxxxx.conkyrc

Then you need to analyze the errors it throws at you.  
Some errors are ok since there is an old conky configuration and a new conky configuration. See other articles about that.

Video: <https://youtu.be/JD6TeJeAyRc>
