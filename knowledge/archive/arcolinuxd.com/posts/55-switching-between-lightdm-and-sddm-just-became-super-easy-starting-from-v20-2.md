---
title: "55 Switching between lightdm and sddm just became super easy starting from v20.2"
url: https://www.arcolinuxd.com/55-switching-between-lightdm-and-sddm-just-became-super-easy-starting-from-v20-2/
date: 2020-02-18 15:57:49
type: post
categories: ["Plasma"]
source_site: arcolinuxd.com
---

# 55 Switching between lightdm and sddm just became super easy starting from v20.2

![](https://www.arcolinuxd.com/wp-content/uploads/2020/02/sddm-setting.jpg)

ArcoLinux uses Lightdm as displaymanager or loginmanager on all its desktops.

Changing to **Sddm** on Plasma is **super** **easy** starting from ArcoLinux 20.2. It takes only a few seconds since Sddm is already installed just not activated yet.

Type this in your terminal and logout.
    
    
    sudo systemctl enable sddm -f

If you do not like the default look of sddm, then you navigate to the system settings and download a theme you like.

Video: <https://youtu.be/_v4sz0Ndfos>
