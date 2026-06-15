---
title: "Reduce your shutdown time from 90 seconds to 30 seconds"
url: https://arcolinux.com/reduce-your-shutdown-time-from-90-seconds-to-30-seconds/
date: 2019-03-14 22:52:25
type: post
categories: ["Fixes"]
source_site: arcolinux.com
---

# Reduce your shutdown time from 90 seconds to 30 seconds

![](https://arcolinux.com/wp-content/uploads/2019/03/shutdown-time.jpg)

Only if your computer shuts down after 90 seconds

some of our computers have it but not all

Change one line in one file on your system and reboot and reboot again to see a shutdown time of 30 seconds.

**/etc/systemd/system.conf**

Change this line
    
    
    #DefaultTimeoutStopSec=90s

to this line
    
    
    DefaultTimeoutStopSec=30s

Video: <https://youtu.be/Lrw1zlUz05E>
