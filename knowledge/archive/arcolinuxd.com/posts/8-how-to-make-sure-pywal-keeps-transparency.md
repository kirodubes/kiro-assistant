---
title: "8 how to make sure pywal keeps transparency"
url: https://www.arcolinuxd.com/8-how-to-make-sure-pywal-keeps-transparency/
date: 2018-05-04 14:16:38
type: post
categories: ["Bspwm"]
tags: ["theming"]
source_site: arcolinuxd.com
---

# 8 how to make sure pywal keeps transparency

![](https://www.arcolinuxd.com/wp-content/uploads/2018/05/arcolinuxd-pywalt-pink.jpg)

In previous article about python-pywal we installed [some extra software](<https://www.arcolinuxd.com/7-what-is-pywal-and-how-to-use-it-in-bspwm/>).

We lost our transparency and we will change it after making a backup of Xresources. That is a hidden file. Use CTRL + H to show hidden files.

We change these lines in ~/Xresources and delete the "!" sign.
    
    
    !URxvt*transparent: true
    !URxvt*shading: 30

You can always reload Xresources with this command. I like to log out to make sure all applications are loaded and give me a fresh start.
    
    
    xrdb ~/.Xresources

Video: <https://www.youtube.com/watch?v=DWZ6yyrT4qo>
