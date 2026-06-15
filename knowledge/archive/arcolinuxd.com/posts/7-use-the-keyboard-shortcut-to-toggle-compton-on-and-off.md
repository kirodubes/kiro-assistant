---
title: "7 Use the keyboard shortcut to toggle compton on and off"
url: https://www.arcolinuxd.com/7-use-the-keyboard-shortcut-to-toggle-compton-on-and-off/
date: 2019-01-17 21:07:04
type: post
categories: ["Xmonad"]
source_site: arcolinuxd.com
---

# 7 Use the keyboard shortcut to toggle compton on and off

![](https://www.arcolinuxd.com/wp-content/uploads/2019/01/arcolinuxb-compton-toggle-on-off.jpg)

> CTRL + ALT + O

We have created a shortcut to quickly toggle compton on and off. At some point in time you would like to do that. We take a look at the script, that will toggle compton on and off and show for the first time where in xmonad.hs the keyboard shortcut is. If compton is turned **off** , there will be **no** more **transparency**. Termite will have a **black** background. The conky will have a **black** background. Urxvt is an exception as we have set urxvt in .Xresources to be transparent (lines 56-57). We may change this setting in the future. 
    
    
    URxvt*transparent: true
    URxvt*shading: 30

Video: <https://www.youtube.com/watch?v=fnV_NQi0GTk>
