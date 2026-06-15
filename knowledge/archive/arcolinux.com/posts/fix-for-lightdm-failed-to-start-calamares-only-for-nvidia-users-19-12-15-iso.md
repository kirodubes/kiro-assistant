---
title: "Fix for lightdm failed to start - calamares - only for nvidia users - 19.12.15 iso"
url: https://arcolinux.com/fix-for-lightdm-failed-to-start-calamares-only-for-nvidia-users-19-12-15-iso/
date: 2019-12-12 23:15:27
type: post
categories: ["Fixes", "Lightdm", "Nvidia"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# Fix for lightdm failed to start - calamares - only for nvidia users - 19.12.15 iso

![](https://arcolinux.com/wp-content/uploads/2019/12/lightdm-nvidia-fix.png)

**This is just for people, who have a Nvidia card and need the nvidia package.**

The**isos of 19.12.15** have now the possibility to install the **nvidia** package from within the calamares installer.

During our tests every single installation worked fine as the linux kernel and the nvidia packages were a match for each other.

But after the launch we notice that lightdm could not be launched anymore.

We learned that the linux kernel was frozen in time but the nvidia package was coming straight from the internet.

It resulted in a **mismatch** between **linux** kernel and **nvidia** package.

The **calamares installer is already changed** to install the latest linux kernel if you choose to install the nvidia package.

**You can build the isos now.**

 

**People installing with a 19.12.15 iso and choosing nvidia need to apply several extra commands to get their system up and running.**

It is explained in the infographic above.

 

Video: <https://youtu.be/Q-0ZOiQLGuw>

Video: <https://www.youtube.com/watch?v=dB8byGWtFJI>
