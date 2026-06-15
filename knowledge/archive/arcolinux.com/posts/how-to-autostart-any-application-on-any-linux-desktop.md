---
title: "How to autostart any application on any Linux desktop"
url: https://arcolinux.com/how-to-autostart-any-application-on-any-linux-desktop/
date: 2018-07-22 10:00:26
type: post
categories: ["Conky", "Post-installation"]
tags: ["conky"]
source_site: arcolinux.com
---

# How to autostart any application on any Linux desktop

![](https://arcolinux.com/wp-content/uploads/2018/07/ArcoLinuxB-Deepin_20180722_092549.jpg)

Many desktop environments give you a tool to set applications to autostart like xfce, cinnamon, mate, etc... but some of them do not like window tiling managers (often in the configs) or like Deepin.

We may just not have found the application on Deepin but I am going to use this desktop environment to explain how to **autostart** **any** **application** **on** **any** **Linux** **desktop**.

**2 examples in the video**

  1. create your own .desktop file
  2. copy/paste a .desktop file



**1 create your own .desktop file**

You need to have one file in your ~/.config/autostart telling the system to autostart an application.

  1. move to your ~/.config/autostart
  2. make a .desktop file
  3. copy/paste the code in - see beneath
  4. change the exec line


    
    
    [Desktop Entry]
    Type=Application
    Name=conky
    Exec=your_action
    StartupNotify=false
    Terminal=false

**2\. copy/paste a .desktop file**

Go to /usr/share/applications and copy/paste the desired application in your ~/.config/autostart

 

**3\. use the ArcoLinux Tweak Tool**

Follow some simple steps to autocreate the .desktop file via ATT.

Video: <https://youtu.be/dzyCkWUv0lY>

Video: <https://youtu.be/Mt66D_KyoEs>

Video: <https://www.youtube.com/watch?v=HOc8ZAGyJPU>
