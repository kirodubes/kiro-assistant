---
title: "Install the zafiro icon theme and use the power of inherits"
url: https://arcolinux.com/install-the-zafiro-icon-theme-and-use-the-power-of-inherits/
date: 2018-11-20 10:47:16
type: post
categories: ["Icons", "Utilities"]
tags: ["pkgbuild", "theming"]
source_site: arcolinux.com
---

# Install the zafiro icon theme and use the power of inherits

![](https://arcolinux.com/wp-content/uploads/2018/11/zafiro.jpg)   


I came across the **Zafiro** icon theme on the social media. The icon theme was mentioned.

As an Arch Linux user the first thing you do .... is check ... **is it on the AUR**?

It is on the AUR!

Install it with
    
    
    yay -S zafiro-icon-theme

> Let us use this icon theme to demonstrate the power of the inherits line. 

Select the **Zafiro** icon them.

Choose a theme that goes with this icon theme.

Some of your applications will not have an icon from Zafiro. It will get an icon from gnome or hicolor or numix or ... This is set in the inherits line.

First let us run the **hardcoded** icons applications in xfce settings (or in the terminal).

Let us change the **inherits** line in the **index.theme** of Zafiro and rethink the order. Let us put Surfn as the first one.

**Inherits=Surfn,Numix-Circle-Light,breeze,gnome,hicolor**

This can be an alternative you like better.

**Inherits=Surfn,breeze,Numix-Circle,gnome,hicolor**

We delete the icon-theme.cache.

We need to recreate the icon-theme.cache with gtk-update-icon-cache.

Now we can select the Zafiro icon theme again.

We combine in this video also **how to update ArcoLinux**.

> It just takes a few commands to stay roling.
    
    
    update
    skel
    pksyua

Video: <https://www.youtube.com/watch?v=A1KXkloDLNk>

  


This PKGBUILD is changed to have more support from other icon themes.
    
    
    # Maintainer: Ariel AxionL <axionl@aosc.io>
    
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

the last three lines  
have been added

Copy/paste the PKGBUILD code into a file with the name PKGBUILD.  
Open a terminal in that directory and type  
**makepkg**  
You get the resulting application in this folder with extension **tar.xz**.  
Double-click to install or pacman -U ...tar.xz.

Video: <https://youtu.be/MX2aYqkV1jc>
