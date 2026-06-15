---
title: "53 getting Sddm and Plasma on ArcoLinuxD"
url: https://www.arcolinuxd.com/53-getting-sddm-and-plasma-on-arcolinuxd/
date: 2019-11-05 21:06:01
type: post
categories: ["Plasma"]
source_site: arcolinuxd.com
---

# 53 getting Sddm and Plasma on ArcoLinuxD

![](https://www.arcolinuxd.com/wp-content/uploads/2019/11/plasma-arcolinuxd.png)

We install sddm and plasma on this freshly installed ArcoLinuxd.

> Force sddm with -f to overwrite the standard lightdm.service.
    
    
    sudo systemctl enable sddm.service -f

We switch to the 3 different menu's.

We check what we get in with the plasma package aka lego block.

No dolphin no konsole...

How do we get those in?

We install firefox and go the Arch Wiki. We look for the group details.

I missed the package kde-application or **kde-applications-meta** (konsole, dolphin, ...) on Arch Wiki so I go and watch on the ArcoLinuxB github to see what lego block I need to get it in.

We show you that there also other KDE packages to make a minimal installation. There are other kde- meta packages.

We change the design.  
We show the wobbly and why it is missing.  
We show you where to set your num lock on at boot.

We take a look at the **menu** again after**kde-applications-meta**.

> Then we can install more ArcoLinux packages or not.

**arcolinux-plasma-git** is the desktop related package

**arcolinux-config-plasma-git** is the **non** -desktop related package (nemesis = beta package)

Quite recently we changed our icons from Sardi-Arc to Surfn-Arc. Hence no icons.

Since there is no **surfn** icon installed we do not see an icon, ... obviously.

We learn about xfce, meld, thunar, skel, thunar, ...

We change back from Sddm to Lightdm.

**Experiment. Experiment. Experiment.**

![](https://www.arcolinuxd.com/wp-content/uploads/2019/11/found-the-missing-lego-block.png)

I totally forgot we had **not** installed  
Surfn icons

We decided to switch from   
Sardi to Surfn icons

Hence the problems with the icons  
We missed a lego block

Video: <https://youtu.be/-eVX-Lsb9aQ>
