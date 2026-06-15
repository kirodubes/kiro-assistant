---
title: "Arc-gtk-theme supplies support for Openbox - coming from Nico Hood - fix error"
url: https://arcolinux.com/arc-gtk-theme-supplies-support-for-openbox-coming-from-nico-hood-fix-error/
date: 2018-07-16 07:40:50
type: post
categories: ["Fixes"]
tags: ["fix", "openbox"]
source_site: arcolinux.com
---

# Arc-gtk-theme supplies support for Openbox - coming from Nico Hood - fix error

![](https://arcolinux.com/wp-content/uploads/2018/07/arc-theme-supports-openbox.jpg) Arc-gtk-theme source on [Arch repo](<https://www.archlinux.org/packages/community/any/arc-gtk-theme/>) has changed from [horst3180](<https://github.com/horst3180/arc-theme>) to [nicohood](<https://github.com/nicohood/arc-theme>). Nico provides us with Openbox support out-of-the-box. Horst did not. We can delete this package for the installation to continue. We do not need it anymore now. Thank you Nico for supporting Openbox in the arc-gtk-theme package. 
    
    
    sudo pacman -R openbox-arc-git
