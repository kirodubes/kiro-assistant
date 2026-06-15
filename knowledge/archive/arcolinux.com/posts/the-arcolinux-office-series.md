---
title: "The ArcoLinux Office Series"
url: https://arcolinux.com/the-arcolinux-office-series/
date: 2019-12-10 10:03:18
type: post
categories: ["Office"]
tags: ["office"]
source_site: arcolinux.com
---

# The ArcoLinux Office Series

![](https://arcolinux.com/wp-content/uploads/2019/03/wallpaperoffice.jpg)

## Contents

  * Libreoffice
  * WPS Office
  * Openoffice
  * Onlyoffice
  * msoffice-online



Where to find the information/software

Video: <https://youtu.be/XhpOJ50zRqY>

Let us use scripts for our next installation 

<https://github.com/erikdubois/arcolinux-nemesis>

Video: <https://youtu.be/DU1MhUNnz6I>

Video: <https://youtu.be/I4qBKg2-9Gw>

Libreoffice German  
skel, bupskel and cb

Video: <https://youtu.be/5pD90IC6440>

theming of libreoffice

![](https://arcolinux.com/wp-content/uploads/2019/03/original-writer.jpg)![](https://arcolinux.com/wp-content/uploads/2019/03/writer-theme-papirus.jpg)

Video: <https://youtu.be/M1BSAmTd0cw>

grammar check

![](https://arcolinux.com/wp-content/uploads/2019/03/writer-theme-papirus.jpg)

Video: <https://youtu.be/BHz4aSqVe1A>

change script to your language

Video: <https://youtu.be/I9P1yXsRu10>

Libreoffice extensions

When you type **yay libreoffice** or **yay libreoffice extensions** you will notice that there is a lot of support for this package.

Here we list what users give us as tips: 

**papirus-libreoffice-theme**

Papirus theme for LibreOffice

Got more tips, let us know.

![](https://arcolinux.com/wp-content/uploads/2019/04/archlinux-wps-office.jpg)

A learning process can be very personal. Here is what I do with any new application out there.

  1. [visit the Arch Wiki](<https://wiki.archlinux.org/index.php/WPS_Office>)
  2. check AUR with yay
  3. google the package name
  4. watch some youtube videos
  5. google tips and tricks for that package
  6. google archlinux and the package name
  7. ...



All that I have learned about the installation packages will go inside a script so that next time my accumulated knowledge can be put to good use AGAIN.

<https://github.com/erikdubois/arcolinux-nemesis>

That is where I keep my scripts.  
  
We have installed **WPS Office** on an Arch Linux **Qtile**. Because of **Qtile** the application will feel and look different from the non-window tiling managers like xfce. In this case we needed to know what the applications were called. They will be present in your start menu in other desktops.

This is another example of thinking out of the box. You can install it on ArcoLinux, ArcoLinuxD, ArcoLinuxB and any Arch based system. 

## Starting from December 2019 wps-office is on our repo

Install it with
    
    
    sudo pacman -S wps-office wps-office-mime ttf-wps-fonts

If for some reason our package is broken then you can still install it from AUR
    
    
    yay -S wps-office ttf-wps-fonts 

There is also a stable version of wps office
    
    
    yay -S wps-office-stable

There is also a bin version of wps office (bin version tends to install faster)
    
    
    yay -S wps-office-bin

# TIP:

If you select **Arc theme** instead of **Arc-Dark** the popup to save and open documents will look all white.

![](https://arcolinux.com/wp-content/uploads/2019/04/wps-arc-dark.jpg)![](https://arcolinux.com/wp-content/uploads/2019/04/wps-arc.jpg)![](https://arcolinux.com/wp-content/uploads/2019/04/wps-office-xfce.jpg)

Video: <https://www.youtube.com/watch?v=z_HXZ9QOJqk>

Video: <https://youtu.be/bsMXTCbO4sY>

fixing the icons of wps office

# Tips in this video

  1. hide the category in the xfce menu
  2. use the **Fix Hardcoded Icons** application to fix icons
  3. fix hardcoded path manually and refresh your cache
  4. report hardcoded paths on the foggalong github : <https://github.com/Foggalong/hardcode-fixer>



Video: <https://youtu.be/WdEDyjVxHLg>

fixing the pkgbuild so we can install it

# Tips in this video

  1. yay has a hidden folder where it builds packages
  2. you can edit a **pkgbuild**
  3. use common sense to guess the url
  4. use **updpkgsums** to update the md5sums in the pkgbuild



Video: <https://youtu.be/MWQ-J1qrUcI>

Showing the writer and presentation

We show you how to change the theme in Herbstluftwm. It will affect the look in Openoffice.

We change the colors of writer via the options and appearance.

Video: <https://www.youtube.com/watch?v=8x38yN8lNNo>

installation and overview

# INstallation

As always we rely on the AUR and yay to install a packages
    
    
    yay -S onlyoffice-bin

Video: <https://youtu.be/Q_ukqTw6gTI>

installation and overview

# Installation

As always we rely on the AUR and yay to install a packages
    
    
    yay -S msoffice-online

Video: <https://youtu.be/Rhgc8iO4hi0>
