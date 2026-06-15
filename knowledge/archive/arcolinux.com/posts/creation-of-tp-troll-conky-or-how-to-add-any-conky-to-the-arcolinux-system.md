---
title: "Creation of TP-Troll conky or how to add any conky to the ArcoLinux system"
url: https://arcolinux.com/creation-of-tp-troll-conky-or-how-to-add-any-conky-to-the-arcolinux-system/
date: 2019-03-06 12:29:28
type: post
categories: ["Conky"]
tags: ["conky"]
source_site: arcolinux.com
---

# Creation of TP-Troll conky or how to add any conky to the ArcoLinux system

![](https://arcolinux.com/wp-content/uploads/2019/03/troll-deepin.jpg)

Thanks to the fact that we have the package **conky-lua-archers** installed we can use conky and its LUA files.

> You can add your own conkies to the system.

There are hundreds of them out there. Many are very similar since they all fall back on the possible parameters you can display like disk space, memory usage etc.

Some of them are super nice and graphical but you know taste is personal.

> So here is how YOU can add a conky to the ArcoLinux system.

We looked for a nice conky online and found one here :

<https://www.deviantart.com/trollpunny/art/Conky-Rings-Revamped-591137228>

Then we download the files and inspect them one by one.

We rename it and are sure they have the extension **.conkyrc** so conkyzen will pick it up.

We put the LUA file in the LUA folder.

We download the fonts from the net. Most of the fonts are free for personal use. As it turned out **Santana** font was free to use so we have included it in our fonts package.

We download fonts if we need and install them by double-clicking on them.

Now we need to change the path(s) that are used in the file.

Our path is :

~/.config/conky  
~/.config/conky/lua  
~/.config/conky/images

If the conky is not working, you need to start it from the terminal like this

conky -c ~/.config/conky/testconky.conkyrc

Then you need to analyze the errors it throws at you.   
Some errors are ok since there is an old conky configuration and a new conky configuration. See other articles about that.

Video: <https://www.youtube.com/watch?v=k04JlwN7_nU>

how to analyze issues and look for solutions

Video: <https://youtu.be/YtrOqMXiENk>
