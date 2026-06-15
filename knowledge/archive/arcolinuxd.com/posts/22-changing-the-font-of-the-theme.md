---
title: "22 Changing the font of the theme"
url: https://www.arcolinuxd.com/22-changing-the-font-of-the-theme/
date: 2018-03-07 19:23:08
type: post
categories: ["Awesome"]
tags: ["theming"]
source_site: arcolinuxd.com
---

# 22 Changing the font of the theme

![](https://www.arcolinuxd.com/wp-content/uploads/2018/03/terminus-font-also-tagnames.jpg)

In this tutorial we are going to change the fonts. Normally we use noto fonts. But we can change the fonts as well. 

We will use the terminus fonts. Here are some terminal commands in regards with fonts
    
    
    fc-list | grep Terminus

We change it to _xos4 terminus_.

We change the font of the calendar and weather as well.

Video: <https://www.youtube.com/watch?v=o-S1TmC1QIM>

We continue to work with xos4 terminus everywhere.

We change the font in the **termite** **config**. And then we have to realign the icon. We need to move it more to the top. But we need to edit the **neofetch** **config** to do that.

yoffset and xoffset will take care of that.

The font in ncmpcpp can be changed as well. I did **not** tell you that in the **video**. Ncmpcpp is launched via urxvt meaning you need to set the font in your .Xresources.
    
    
    URxvt*font: xft:Monospace:regular:size=13

We change this file and copy/paste the terminus font over.
    
    
    ~/.gtkrc-2.0

You need also to change this file
    
    
    ~/.config/gtk-3.0/settings.ini

Video: <https://www.youtube.com/watch?v=bMbzJOpIOH8>
