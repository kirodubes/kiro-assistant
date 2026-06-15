---
title: "How to fix the \"ugly\" lines when you shutdown"
url: https://arcolinux.com/how-to-fix-the-ugly-lines-when-you-shutdown/
date: 2018-04-05 12:21:52
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to fix the "ugly" lines when you shutdown

![](https://arcolinux.com/wp-content/uploads/2018/04/systemd.jpg)   


Somewhere in March we got an update in that makes our shutdown look different.  
We see now a lot of strange lines.

**Nick** **Petrov** went to look for a solution and found a way to hide these messages.

**Follow his procedure:**

Edit the file**/etc/mkinitcipo.conf** with sublime-text and add **"shutdown"** to the hooks. Then save it.

Then run the following code in the terminal
    
    
    sudo mkinitcpio -p linux

When you have rebooted, you will see less lines when you shutdown.

There is **no** **need** to do this. It is just for **cosmetic** reasons.

Video: <https://youtu.be/JKvIzv8wxHM>
