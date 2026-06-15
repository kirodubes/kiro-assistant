---
title: "How to fix icons that never change their look whatever theme you choose"
url: https://arcolinux.com/how-to-fix-icons-that-never-change-their-look-whatever-theme-you-choose/
date: 2018-12-09 12:52:53
type: post
categories: ["Fixes", "Icons"]
tags: ["fix", "icons"]
source_site: arcolinux.com
---

# How to fix icons that never change their look whatever theme you choose

Icons that never change their look whatever icon theme you choose are : **hardcoded** icons. At the time of the launch of Kirk 1st October 2017 there were 5 such applications present. These applications have an **absolute** path to a picture on your system. This path will never change UNLESS YOU do something about it. What is more... Every update will again break your icon theme as the application receives again a hardcoded icon. You will have to run it again. On ArcoLinu we can fix this by typing the following command in the terminal 
    
    
    sudo hardcode-fixer

This will change a hardcode path like /usr/share/icons/.../hardinfo.png to hardinfo Keyboard Shortcuts To Remember SUPER + T ... CTRL + ALT+ T ... Super + Enter Launch your terminal 

Video: <https://youtu.be/F0OAUfWvhgs>

report hardcoded icons   
and   
make linux awesome

Video: <https://youtu.be/912aY9aj8cY>
