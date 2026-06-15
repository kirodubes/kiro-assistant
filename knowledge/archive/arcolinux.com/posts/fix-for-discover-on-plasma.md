---
title: "Fix for discover on Plasma"
url: https://arcolinux.com/fix-for-discover-on-plasma/
date: 2019-07-23 22:32:11
type: post
categories: ["Fixes"]
source_site: arcolinux.com
---

# Fix for discover on Plasma

![](https://arcolinux.com/wp-content/uploads/2019/07/plasma-discover-back-end.jpg)

In the video we show you how to find the solution on your own.

Use pamac-aur to get more info about the package that reports an error.

Are there dependencies missing?

Knowing **how** to find the answer yourself is as important as finding the answer.
    
    
    sudo pacman -S packagekit-qt5

Discover was missing a back-end. It was after all not that optional.

**Extra**

We explain also how to encrypt plasma to boot up fast - around 8 seconds. Unencrypted is also 8 seconds.

Video: <https://youtu.be/v1W8en4O0iw>
