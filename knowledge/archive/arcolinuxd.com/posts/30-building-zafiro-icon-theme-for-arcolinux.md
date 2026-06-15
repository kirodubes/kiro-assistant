---
title: "30 building Zafiro-icon-theme for ArcoLinux"
url: https://www.arcolinuxd.com/30-building-zafiro-icon-theme-for-arcolinux/
date: 2018-11-19 21:35:13
type: post
categories: ["Plasma"]
tags: ["theming"]
source_site: arcolinuxd.com
---

# 30 building Zafiro-icon-theme for ArcoLinux

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/zafiro-icon-theme.jpeg)

We have been making tutorials about Zafiro icon theme [here](<https://arcolinux.com/install-the-zafiro-icon-theme-and-use-the-power-of-inherits/>).

We installed it with yay. Then discovered that some of the icons were missing.   
We learned how to fix that with the inherits line in index.theme. 

Then we learned how to make a PKGBUILD to fix this inherits line for us.

We will copy/paste that PKGBUILD and build it now on Plasma.
    
    
    # Maintainer: Ariel AxionL 
     
    pkgname=('zafiro-icon-theme')
    pkgver=0.7.1
    pkgrel=2
    pkgdesc="A icon pack flat with light colors."
    arch=('any')
    url="https://github.com/zayronxio/Zafiro-icons"
    license=('Artistic2.0')
    source=("https://github.com/zayronxio/Zafiro-icons/archive/v$pkgver.tar.gz")
    sha256sums=('465c10164677d1418008b0e000a649153af3973d3455cd8b5b8d3555ff0b7bfb')
     
    package() {
      install -dm 755 $pkgdir/usr/share/icons
      dir=$srcdir/Zafiro-icons-$pkgver
      install -Dm644 $dir/LICENSE.md $pkgdir/usr/share/license/$pkgname/LICENSE
      cp -dr --no-preserve='ownership' $dir $pkgdir/usr/share/icons/$pkgname
      search="Inherits=gnome,hicolor,Numix,breeze"
      replace="Inherits=Surfn,Numix-Circle,breeze,gnome,hicolor"
      sed -i s/$search/$replace/g $pkgdir/usr/share/icons/$pkgname/index.theme
    }

Video: <https://youtu.be/c6gB11-iQBA>

Video: <https://youtu.be/cRo7S2d7ds4>

## **Plasma Challenge**

You can follow our tutorials based on either of two ISO's.

**1\. ArcoLinuxB Plasma (recommended)**

We record the plasma video's on an SSD installed from the **ArcoLinuxB Plasma ISO**.  
You can either **create** your very own ArcoLinuxB Plasma ISO [following this tutorial](<https://arcolinuxb.com/byoi-on-arcolinux-plasma/>) or [download it from Sourceforge](<https://sourceforge.net/projects/arcolinux-community-editions/files/plasma/>). (ArcoLinuxB-plasma-18.11.2.ISO of 4.3 GB - games included)

**2\. ArcoLinuxD Plasma**

You can also use the ArcoLinuxD ISO and then install Plasma with the help of the github scripts. This will not be an exact copy of the ISO.

> Learn about the Plasma desktop and enjoy it.
