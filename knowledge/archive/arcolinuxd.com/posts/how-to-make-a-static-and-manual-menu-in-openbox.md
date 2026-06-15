---
title: "How to make a static and manual menu in openbox"
url: https://www.arcolinuxd.com/how-to-make-a-static-and-manual-menu-in-openbox/
date: 2024-03-01 06:38:14
type: post
categories: ["Openbox"]
source_site: arcolinuxd.com
---

# How to make a static and manual menu in openbox

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/archmerge-theming-openbox-manual-menu.jpg)ArcoLinux has a **generated** menu out of the box. Any application, that you install or uninstall, will show up or disappear from the menu. The menu is generated with the tool obmenu-generator. **What if you wanted to have the original menu.xml back that comes with openbox in a vanilla installation.** You can have a regular menu.xml file that you can edit manually and change any way you see fit. You can find it here : **~/.config/openbox** Change the following files from name 

  * menu.xml to menu.xml.orginal
  * menu-make-it-yourself.xml to menu.xml

Restart the openbox via menu or via keyboard shortcut. We will change the text in the menu and will talk about the xml structure and what can go wrong.Keyboard Shortcuts To RememberSupER + SPACEBARget obmenuKeyboard Shortcuts To RememberCTRL + SHIFT + BACKSPACERestart openbox

Video: <https://www.youtube.com/watch?v=_Iqom5gAJm0>
