---
title: "Using pywall and transparency in Bspwm in urxvt terminal"
url: https://arcolinux.com/using-pywall-and-transparency-in-bspwm-in-urxvt-terminal/
date: 2018-10-08 16:57:35
type: post
categories: ["Terminal Design"]
tags: ["theming"]
source_site: arcolinux.com
---

# Using pywall and transparency in Bspwm in urxvt terminal

![](https://arcolinux.com/wp-content/uploads/2018/10/transparency-urxvt.jpg)   


When working on BSPWM and using URxvt as terminal and using python-pywal to color your terminal content THAN you need to change two lines in .Xresources

From this
    
    
    !URxvt*transparent: true
    !URxvt*shading: 30

to this
    
    
    URxvt*transparent: true
    URxvt*shading: 30

Video: <https://youtu.be/0EM_gufrETY>
