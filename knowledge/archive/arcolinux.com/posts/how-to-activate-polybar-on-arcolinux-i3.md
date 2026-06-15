---
title: "How to activate polybar on ArcoLinux i3"
url: https://arcolinux.com/how-to-activate-polybar-on-arcolinux-i3/
date: 2019-11-04 09:39:05
type: post
categories: ["Polybar"]
tags: ["i3", "openbox", "polybar"]
source_site: arcolinux.com
---

# How to activate polybar on ArcoLinux i3

![](https://arcolinux.com/wp-content/uploads/2019/11/arcolinux-xtended-i3-polybar.jpg)

If you like you can switch from one bar system to the next. There are several choices.

> Here we will switch from the i3status bar to polybar.

To start polybar we need to edit the file **~/.config/i3/config** and search (CTRL + F) for the word **polybar**.

Open the file with an editor. 

We have changed the **i3** configuration file to have an **extra** line for polybar.

This is the correct code. **Get rid of the hashtag** before the polybar line.
    
    
    #Polybar
    exec_always --no-startup-id ~/.config/polybar/launch.sh &

When we log out and log back in polybar will be launched.

But the i3status bar will be there as well.

Then we delete the bottom bar in i3. All text between bar { .... } has to be deleted. Take a backup before you do. Remember that there is also an i3 config in /etc/skel.

[Beware the skel alias.](<https://arcolinux.com/updating-your-system-with-skel-and-still-keeping-your-own-settings/>)

 

**Older video - Extra info**

We will show you how to add more functionality in Atom like **pigments** and **minimap** in one of the older video.

We show you as well how to get rid of the conky that starts up with i3 (older video).

Video: <https://youtu.be/KvUwEsRMgB8>

**Older video - Extra info**

We will show you how to add more functionality in Atom like **pigments** and **minimap** in one of the older video.

We show you as well how to get rid of the conky that starts up with i3 (older video).

Video: <https://youtu.be/Ot8-b3RC7Ew>
