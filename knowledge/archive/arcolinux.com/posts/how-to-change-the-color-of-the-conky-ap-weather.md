---
title: "Everything you need to know about the conky AP-Weather"
url: https://arcolinux.com/how-to-change-the-color-of-the-conky-ap-weather/
date: 2018-11-28 11:02:42
type: post
categories: ["Conky"]
tags: ["conky", "gpick", "script"]
source_site: arcolinux.com
---

# Everything you need to know about the conky AP-Weather

![](https://arcolinux.com/wp-content/uploads/2018/11/conky-ap.jpg)

We show you what **procedure** I have in my head to **change** a conky and make it my own **without** it being **overwritten** IF I use the **skel** command on a later date.

> Rename the conky before you apply changes.

We tell you why the conky will **not** **display** **any** **weather** information at **first**. The conky is just too fast.

We show you that on **second** **launch** of the conky the weather information was received from the server and now can be used.

All the weather information is stored in the **~/.cache** folder.

Conkies start with letters. They are a way to credit the donators of the conkies like Adhi Pambudi or **AP**.

Without a working **API key** you will not get any weather information... so after trying a reboot of the conky you may need to get your **personal** **API** key.

Where should I look for my personal town? What is its **number**?

We change the city code from Antwerp to **London**.

Then we forgot to **delete** the **cache**. So go in ~/.cache and delete the files from the conky.

> kc alias kills the conky.

We **compare** a working conky with the conky that is not working and look for differences. And delete one line.

Place the code and the conky next to each other to quickly analyze.

We **delete** the shortcut keys. We do not need them.

We delete the conky to show the **number** of **desktops**.

We use the **goto** command to position the elements of a conky.

The font was changed so we CTRL + Z to see where we deleted the info about the **font**.

Change the **height** of the conky.

Change the **space** from the top or the space from the right - x and y axes.

We put the conky in the **middle** of the **right**.

We change the **color** of the **bars**.

Video: <https://youtu.be/B6L4RlR4h6g>

Archived article

After writing[ this tutorial](<https://arcolinux.com/how-to-change-the-color-of-the-archmerge-logo/>) I wanted the AP-Weather conky to be red as well. We are going to change this conky to a different kind of red. The same as in the logo from the other article.

You will need inkscape and gpick to do it.

Follow the tutorial and recolor the conky to match your awesome wallpaper.

**TIP**

**Reload** the conky if you select it for the **first** time. This conky works so fast that the information about the weather is not coming fast enough from the net. Restart the conky.

![](https://arcolinux.com//wp-content/uploads/2017/09/ap-weather-red.jpg)

Video: <https://www.youtube.com/watch?v=8b_u6-8vzqE>

What if you wanted to change the color of the weather icons as well. We will explain how to change the colors of the icons. We will explain how to execute a script the easy way. Replacing the color red with the same red from the logo.

**TIP**

Sometimes file managers like thunar, nautilus, nemo, ... need to refresh their images after a script. **Press F5**.

Video: <https://www.youtube.com/watch?v=RYloDsJFAb0>

# General conky info

> A conky will NEVER EVER work on all desktops.

**There are just too much differences between all the different window managers.**

It will also depend on the software you have installed.

There are two versions of the application called 'conky'.

  1. version 1.9 and earlier - old syntax
  2. version 1.10 and higher - new syntax - LUA (and old syntax)



We install the application **conky-lua-archers (1.10)** on ArcoLinux

**Options to explore when encountering issues :**

  * own_window_type = 'desktop', # options are: normal/override/dock/desktop/panel
  * own_window_transparent = true, # options are : true and false
  * own_window_argb_visual = true, # options are : true and false
  * own_window_argb_value = 0, # options are : 0-255



#### More information about conkies can be found here :

[Arch wiki](<https://wiki.archlinux.org/index.php/conky>)

[Conky github configuration](<https://github.com/brndnmtthws/conky/wiki>)

[Conky github faq](<https://github.com/brndnmtthws/conky/wiki/FAQ>)

[Conky github user configs](<https://github.com/brndnmtthws/conky/wiki>)

[Conky configuration on sourceforge](<http://conky.sourceforge.net/config_settings.html>)

[Conky variables on sourceforge](<http://conky.sourceforge.net/variables.html>)
