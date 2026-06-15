---
title: "Fix for cannot stat no such file or directory"
url: https://arcolinux.com/fix-for-cannot-stat-no-such-file-or-directory/
date: 2018-01-28 11:13:21
type: post
categories: ["Fixes"]
tags: ["fix", "pkgbuild"]
source_site: arcolinux.com
---

# Fix for cannot stat no such file or directory

![](https://arcolinux.com/wp-content/uploads/2018/01/conky-lua-archers-fix.jpg)   


An application coming from AUR will always have a **PKGBUILD** you can read and edit. Normally there is no need for that. Just in some odd occasions you will need to edit it to overcome an **installation** **problem**.

Jan 2018 **conky-lua-archers** is a great example how to solve an installation issue yourself.

We are missing a file and that is why we can not install it.

After analysis my guess is that 'they' have renamed the file from LICENSE to LICENSE.GPL The PKGBUILD does not reflect that change. Hence the installation stops.

**Let us fix it together.**

**To be fair : I do not think this is the fault of the maintainer of the package on the AUR website.**
    
    
     install -D -m644 LICENSE.GPL ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.GPL

Video: <https://youtu.be/1BdOESsi5bA>
