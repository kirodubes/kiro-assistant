---
title: "How to add an external music library to mpd and ncmpcpp"
url: https://arcolinux.com/how-to-add-an-external-music-library-for-mpd-and-ncmpcpp/
date: 2018-01-21 16:12:59
type: post
categories: ["Audio"]
tags: ["music"]
source_site: arcolinux.com
---

# How to add an external music library to mpd and ncmpcpp

![](https://arcolinux.com/wp-content/uploads/2018/01/external-music-library.jpg)   


Great tip for all SSD users.

**Mpd** can understand a **symbolic link** to your external harddisk.

That means we do **not** have to copy/paste your complete music library to the ssd.

Buy yourself an external harddisk with >1TB and put your collection on there.

GUI way

Right mouse click on the folder you want to point to and click on "**Send to** " and "**Desktop create link** " in XFCE. Cut and paste this link to your music folder ~/Music and WAIT - **Be patient**. Depending on your cpu and your music library it can take some time before the songs are in the library.

TERMINAL way

Go inside the music folder and make a link to your harddisk path and music folder.
    
    
    ln -s /run/media/username/... external-drive

Video: <https://youtu.be/nB5sMw-qIRk>
