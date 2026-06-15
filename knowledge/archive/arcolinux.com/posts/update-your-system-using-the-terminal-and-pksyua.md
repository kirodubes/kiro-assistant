---
title: "Update your system using the terminal and upall or pksyua"
url: https://arcolinux.com/update-your-system-using-the-terminal-and-pksyua/
date: 2018-04-28 08:32:56
type: post
categories: ["Terminal", "Update"]
tags: ["terminal", "update"]
source_site: arcolinux.com
---

# Update your system using the terminal and upall or pksyua

![](https://arcolinux.com/wp-content/uploads/2018/04/update-pksyua.jpg)

**This applies to all desktop environments.**

**Pamac** is our graphical updater in ArcoLinux. You can find [more info about updating via pamac in this article.](<https://arcolinux.com/update-your-system-using-pamac/>)

But you can also update in the **terminal**.

Personally I start the day with a command in the terminal and read what will be updated. Trying to learn the names of all these applications.
    
    
    pksyua

or
    
    
    upall

When there is an update coming in from ArcoLinux packages we check if there are updates that go into **/etc/skel**.

Then I will navigate with my file manager to **/etc/skel** and **copy/paste** the hidden content (CTRL + H to show it) to my own home directory.

> After that I am 100% rolling and 100% up-to-date.

We also show you in the video an other approach. Use **meld** to compare the folders in /etc/skel with your own. This is a great way to learn. What did ArcoLinux change and why? You can learn the why also on our githubs. When we change elements, we try to be 'descriptive' what we changed.

Video: <https://www.youtube.com/watch?v=0d33UfyT7Ec>
