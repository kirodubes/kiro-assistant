---
title: "How to fix the cursor theme on Plasma - cursor is not applied everywhere"
url: https://www.arcolinuxd.com/how-to-fix-the-cursor-theme-on-plasma-cursor-is-not-applied-everywhere/
date: 2020-01-05 21:35:20
type: post
categories: ["Plasma"]
source_site: arcolinuxd.com
---

# How to fix the cursor theme on Plasma - cursor is not applied everywhere

![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/plasma-cursors.jpg)

Moving over the screen the cursor sometimes changes from theme

Every desktop has its own way to select the cursor theme

Because we want to have a **consistent cursor theme** we have defined on all our desktops that we use breeze snow.

**Navigate to this folder /usr/share/icons/default**

You will find the file **index.theme** with this content (fix for mouse in plasma changing all the time).

Change here also to the correct cursor theme 
    
    
    [Icon Theme]  
    Inherits=Breeze_Snow

If you want an other cursor EVERYWHERE, you need to change this one too.

THE CURSOR theme IS NOT APPLIED?

DID YOU TRY  
TURNING IT OFF  
AND ON AGAIN
