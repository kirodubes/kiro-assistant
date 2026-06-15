---
title: "Install software from the ArcoLinux Iso Repository if the pkgbuild fails"
url: https://arcolinux.com/install-software-from-the-arcolinux-iso-repository-if-the-pkgbuild-fails/
date: 2019-01-24 20:31:47
type: post
categories: ["Fixes", "Manage software"]
tags: ["fix", "pkgbuild", "software"]
source_site: arcolinux.com
---

# Install software from the ArcoLinux Iso Repository if the pkgbuild fails

![](https://arcolinux.com/wp-content/uploads/2019/01/arcolinuxb-xmonad-timeshift.jpg)

At this moment of writing Timeshift (it can be any other package) can not be build. The maintainer says to [**downgrade**](<https://arcolinux.com/?s=downgrade>) vala. You will be able to build the very latest package then.

**But let us be honest the latest version is sometimes not that important**.

As long as you can have the application, you will settle for a version from a week or a month ago. Arch Linux is pretty fast in updating anyway.

Instead of downgrading ([tutorials about that on this website](<https://arcolinux.com/?s=downgrade>)) I will show you an even faster way of installing this particular package.

> This will only work with the packages that ArcoLinux puts on its iso's

When we build an iso or when you build an iso - ArcoLinuxB project - you will install the packages we have build during the last month.

**Since we release a monthly iso you will always have the version of 1, 2, 3 and max 4 weeks ago.**

You can always install any application coming from this website : 

[https://bike.seedhost.eu/arcolinux/](<https://ant.seedhost.eu/arcolinux/>)

Navigate to the contents of this folder : 

**/arcolinux_repo_iso/x86_64/**

Look for you application (not sig) and download the package. Double-click and install it.

Pamac might say you there is a newer version after this installation.

To get rid of that message ...

Open **/etc/pacman.conf with sublime-text**

and add your package to this line (timeshift in this example)

**IgnorePkg = timeshift**

**Delete** the hashtag in front of the line or it will NOT be used. 

Video: <https://youtu.be/bXwQqrhQ2AY>
