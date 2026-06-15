---
title: "14 How to reload or fix a crashing qtile config"
url: https://www.arcolinuxd.com/14-how-to-reload-or-fix-a-crashing-qtile-config/
date: 2019-05-30 18:36:49
type: post
categories: ["Qtile"]
source_site: arcolinuxd.com
---

# 14 How to reload or fix a crashing qtile config

![](https://www.arcolinuxd.com/wp-content/uploads/2019/05/qtile-crash.jpg)

Changing your config of qtile can be fun but you may break your config and have a broken qtile as a result.

This video will tell how to get back to a working qtile.

We delete a komma in the config and qtile crashes.

At that point we get the default config of qtile and not the ArcoLinux config.

# Reloading qtile keyboard shortcuts

# ArcoLinux : Super + Shift + R 

# Standard Qtile : Super + Control + R

Video: <https://youtu.be/JNHF_yOaKnM>

Introducing a mistake to make the qtile config crash or figuring out why it crashes, is something entirely different.

Qtile can help us tell where it crashed. It is still up to us to figure out why it crashed.
    
    
    qtile -l ERROR

We need to put this command in a **terminal** or in a **TTY** in order to be able to see the **line** where qtile stopped because of the error.

Video: <https://youtu.be/ARPUrAieJ_k>

# Remember

# /etc/skel 

# contains a working qtile config

# It is kinda your backup.
