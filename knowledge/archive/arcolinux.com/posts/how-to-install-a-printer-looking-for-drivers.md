---
title: "How to install a printer - looking for drivers"
url: https://arcolinux.com/how-to-install-a-printer-looking-for-drivers/
date: 2020-12-13 13:42:01
type: post
categories: ["Printers"]
source_site: arcolinux.com
---

# How to install a printer - looking for drivers

![](https://arcolinux.com/wp-content/uploads/2020/04/printer.png)

ArcoLinux has printer support enabled by default.

If you are working on Arch Linux then you need to read up about [cups](<https://wiki.archlinux.org/index.php/CUPS>).

Cups and its packages provides support for thousands of printers but maybe not (yet) the latest printers.

Check out this page to know more [about your particular brand.](<https://wiki.archlinux.org/index.php/CUPS/Printer-specific_problems>)

Do not forget the AUR. It hosts many drivers you can install.

Watch the video to see all the options.

Remember the name to launch the printer setup. You will need to know it on a tiling window manager.

**system-config-printer**

Video: <https://youtu.be/sOjwzuUaVIU>

HP printers

Check out the Arch wiki page of your printer in this case we google "arch wiki hp printer".

[Follow this link to learn about cups and the drivers needed for you printer.](<https://wiki.archlinux.org/index.php/CUPS/Printer-specific_problems>)

And this is the direct link to the [wiki for HP](<https://wiki.archlinux.org/index.php/CUPS/Printer-specific_problems#HP>) on the same page.

Most printers use hplip so 
    
    
    sudo pacman -S hplip

and reboot.

Then set your printer in the printer manager.
