---
title: "How to deactivate the transparency  in i3 and openbox"
url: https://arcolinux.com/how-to-deactivate-the-transparency-in-i3-and-openbox/
date: 2017-10-15 09:16:41
type: post
categories: ["Compton"]
tags: ["i3", "openbox", "theming"]
source_site: arcolinux.com
---

# How to deactivate the transparency  in i3 and openbox

![](https://arcolinux.com//wp-content/uploads/2017/10/archmerge-compton-deactivated.jpg)   


[Compton](<https://wiki.archlinux.org/index.php/Compton>) is a compositor for Openbox and i3. It will take care of transparency and shadows on your system. It 'beautifies' your system. But sometimes you need to take a picture and you rather not see the background coming through. How can I do this?

Openbox has a menu to deactivate the compositor (compton). That is one way of deactivating it.

You can type "killall compton" in the terminal.

Or you can set the compton file to never show any transparency ever again.

 

Tip: **i3** and **openbox** have a **separate** **compton.conf** file! Experiment with it.

 

 

  
  


Keyboard Shortcuts To Remember

Super + Keypad numbers

Tile your windows any way you want

Video: [www.youtube.com/watch?v=TXDxtVxSmMU](<www.youtube.com/watch?v=TXDxtVxSmMU>)

  


Here is a tutorial on a dual screen. I change three settings and we get a completely differen feel on i3. We will change the settings in ~/.config/i3/compton.conf.

  * menu-opacity
  * inactive-opacity
  * fading



Video: <https://www.youtube.com/watch?v=TrCWYUxfo-4>
