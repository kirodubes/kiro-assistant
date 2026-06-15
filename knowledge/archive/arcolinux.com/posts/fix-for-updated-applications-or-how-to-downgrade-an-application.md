---
title: "Fix for updated applications or how to downgrade an application"
url: https://arcolinux.com/fix-for-updated-applications-or-how-to-downgrade-an-application/
date: 2018-12-07 13:05:29
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fix for updated applications or how to downgrade an application

![](https://arcolinux.com/wp-content/uploads/2018/02/pamac-aur-preferences.jpg)

Pamac-aur (February 2018)

You can Downgrade pamac-AUR  
BUT IT IS NOT A MUST

February 8th 2018 an update from **pamac-aur** (6.2.3) comes in and gives us an issue. We do **not** seem to be able to open **preferences** in this new version. What makes it more strange is that some of our computers do open with the newer version.

Let us use it to make a tutorial how to **downgrade** an application to its previous version.

To be fair to the pamac developers, this can happen to **ANY** **application** out there.

> It is up to us to manage our systems until the fix comes or until we fix it.

If you want to keep the new version, you can set the preferences of the missing popup always in
    
    
    /pamac.conf

We will downgrade with the following command
    
    
    downgrade pamac-aur

The older version is located at
    
    
    /var/cache/pacman/pkg/

This folder is your **pacman** **cache** and will keep your **older** versions.

The **pacman.conf** will be changed if you say **ignore** package. Great tip to check out.
    
    
    # Pacman won't upgrade packages listed in IgnorePkg and members of IgnoreGroup
    IgnorePkg = pamac-aur
    #IgnoreGroup =

 

**This means you can add applications to this IgnorePkg line as well and prevent software from being updated!**

**Keep track of what you put in there and delete it again later.**

Video: <https://youtu.be/vM8Zt5z_Bsc>

[NEED More info click here](<https://wiki.archlinux.org/index.php/downgrading_packages>)

Downgrading packages NOT coming from THE AUR will give you much more choice   
example firefox

![](https://arcolinux.com/wp-content/uploads/2018/02/downgrade-firefox.jpg)

Obsstudio and qt 5.12 dependency (December 2018)

Video: <https://www.youtube.com/watch?v=8xsFrWzr38E>

One mail and one day later obs-studio has been build against our version of qt and this video is no longer of consequence.
