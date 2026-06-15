---
title: "How to fix could not satisfy dependencies"
url: https://arcolinux.com/how-to-fix-could-not-satisfy-dependencies/
date: 2017-11-14 13:54:48
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to fix could not satisfy dependencies

![](https://arcolinux.com/wp-content/uploads/2017/11/couldnotsatisfydenpendencies.jpg)

On November 2017 **teamviewer 12** could still be installed on Arch Linux. Soon the 32 bit support will fall away and we will see then what this means for this application that relies on 32 bits packages.

After writing a script to install teamviewer you might get this answer

**error: failed to prepare transaction (could not satisfy dependencies)**

Why?

Because teamviewer wanted a package from an earlier version. It wanted to downgrade this package **lib32-freetype2**.

Downgrade is actually an application that is installed on ArcoLinux and you can use it when required.

Teamviewer was starting and everything went fine. But then the updates come back in and pacman sees that an old version of the packages is used and wants to update. But teamviewer requires the old version and then you are stuck with above error.

There are two solutions to this problem.

  1. manual one
  2. automatic one



Check it out.

Video: <https://www.youtube.com/watch?v=ANbXMbhE2Xo>

![](https://arcolinux.com/wp-content/uploads/2017/11/skippackageupgrade.jpg)
