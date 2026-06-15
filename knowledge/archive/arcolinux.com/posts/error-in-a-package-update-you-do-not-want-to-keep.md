---
title: "Error in a package update you do not want to keep"
url: https://arcolinux.com/error-in-a-package-update-you-do-not-want-to-keep/
date: 2018-01-08 20:40:21
type: post
categories: ["Fixes"]
tags: ["fix", "pkgbuild"]
source_site: arcolinux.com
---

# Error in a package update you do not want to keep

![](https://arcolinux.com/wp-content/uploads/2018/01/error.jpg) Packages or applications coming from AUR can cause problems. The individuals have to maintain the pkgbuild and need to update it if the source changes, the checksum changes, and so many other variables. **January 8, 2018** we had an example with **snapd**. **Upgrading does not work and uninstalling and reinstalling does not work either.** In such a case you need to check the [aur page](<https://aur.archlinux.org/packages/snapd/>) and see what solution or what problem this package is having. In many cases you have to wait a **few** **days** until the scripts get updated. If it takes longer than a few weeks you can flag it out of date on the AUR website. In that case the maintainer will get an email alerting him that his packages has been flagged out-of-date. In this case we do not need this application and we uninstall it with 
    
    
    sudo pacman -R snapd

We can always reinstall it in a few days/weeks.
