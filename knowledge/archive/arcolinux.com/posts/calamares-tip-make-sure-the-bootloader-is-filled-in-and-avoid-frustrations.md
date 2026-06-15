---
title: "Calamares tip - make sure the bootloader is filled in and avoid frustrations"
url: https://arcolinux.com/calamares-tip-make-sure-the-bootloader-is-filled-in-and-avoid-frustrations/
date: 2019-05-18 12:09:20
type: post
categories: ["Fixes"]
source_site: arcolinux.com
---

# Calamares tip - make sure the bootloader is filled in and avoid frustrations

![](https://arcolinux.com/wp-content/uploads/2019/05/bootloaderfilled.jpg)![](https://arcolinux.com/wp-content/uploads/2019/05/bootloadempty.jpg)

Compare the bottom line of both images.  
**It should never be empty.**

This tip for calamares (our installer) only concerns people 

  * that have older hardware and use **MBR** to install ArcoLinux
  * that use **Virtual** **Box** and use **MBR** to install ArcoLinux.



**EFI** or **UEFI** people are **NOT** **affected** and do not see the bottom line about the boatloader in Calamares.

**If you do not change anything, then the installation will go fine.**

If you **change** the settings in Erase disk from no swap to anything else then Calamares (may 2019) will have forgotten the last line and you will have to add it **manually** yourself.

See images and video.

Video: <https://youtu.be/gadbE7pMrnQ>
