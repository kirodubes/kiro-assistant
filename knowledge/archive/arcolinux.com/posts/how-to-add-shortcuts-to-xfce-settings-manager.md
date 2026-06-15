---
title: "How to add shortcuts to xfce settings manager"
url: https://arcolinux.com/how-to-add-shortcuts-to-xfce-settings-manager/
date: 2018-01-20 07:47:31
type: post
categories: ["System settings"]
tags: ["xfce"]
source_site: arcolinux.com
---

# How to add shortcuts to xfce settings manager

This looked like a cool idea.  
It has been implemented in the current ArcoLinux.

BEFORE - NO CONKYZEN ![](https://arcolinux.com/wp-content/uploads/2018/01/xfce-settings-no-conkyzen.png)AFTER - CONKYZEN PRESENT ![](https://arcolinux.com/wp-content/uploads/2018/01/xfce-settings-conkyzen.png)We analyze together why some of the applications get a 'place' in the XFCE settings panel and others do not. It is because of the settings the software engineers give their applications. We need to navigate to **/usr/share/applications** and open one of the **.desktop** files in there to see why they are included or excluded from xfce settings. Experiment using sublime text. It will let you save with a popup to fill out your root password. **Now you can add any application to your xfce settings manager.** The categories line in the .desktop files decides if your icon (shortcut) will show up or not. 
    
    
    Categories=XFCE;GTK;Settings;DesktopSettings;X-XFCE-SettingsDialog;X-XFCE-HardwareSettings;

 

Video: <https://youtu.be/DVtktarMR5Y>
