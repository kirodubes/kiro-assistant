---
title: "How to install libreoffice the proper way"
url: https://arcolinux.com/how-to-install-libreoffice-the-proper-way/
date: 2018-06-30 06:51:26
type: post
categories: ["Editors", "Office"]
tags: ["editors"]
source_site: arcolinux.com
---

# How to install libreoffice the proper way

![](https://arcolinux.com/wp-content/uploads/2018/06/libreoffice.jpg)   


We decided not to include libreoffice on the iso. You will hear and see in the tutorial why.

It could not be any easier to install libreoffice. Libreoffice-still is the maintenance branch.
    
    
    sudo pacman -S libreoffice-fresh

Then you will need to see what package could be your language and install that as well like
    
    
    sudo pacman -S libreoffice-fresh-de libreoffice-fresh-en-gb etc

> If you can not find it with pacman. Remember to search in the AUR with trizen or yay or another [AUR helper](<https://wiki.archlinux.org/index.php/AUR_helpers>).

The [Arch Wiki should](<https://wiki.archlinux.org/index.php/LibreOffice>) always be your **first** **visit** when encountering challenges.

 

 

Keyboard Shortcuts To Remember

SUPER + T ... CTRL + ALT+ T ... Super + Enter

Launch your terminal

Video: <https://www.youtube.com/watch?v=Xqo4Mz2JZik>

 

We can also install any software package via the **gnome-software.** You have this application in all 3 desktops. But if you want to move to **phase 2, 3 and 4** , you will to get acquainted with the **terminal**.

Video: <https://www.youtube.com/watch?v=N0Z9Hwm0uuI>

 

Spelling

If you want your spelling checked you need to install hunspell.

**sudo pacman -S hunspell hunspell-de hunspell-en_US hunspell-fr etc...**

Press on Tab to find more

HYPHENATION

If you want to import the hyphenation rule install this package

**sudo pacman -S hyphen hyphen-en hyphen-fr hyphen-nl hyphen-de etc...**

Press on Tab to find more

Thesaurus

If you want to install the thesaurus you will need this

**sudo pacman -S libmythes mythes-en mythes-fr mythes-de mythes-en etc...**

Press on Tab to find more
