---
title: "How to install software on ArcoLinux in the terminal"
url: https://arcolinux.com/how-to-install-software-on-arcolinux-in-the-terminal/
date: 2017-09-29 13:51:30
type: post
categories: ["Manage software", "Terminal"]
tags: ["pkgbuild", "software", "terminal"]
source_site: arcolinux.com
---

# How to install software on ArcoLinux in the terminal

[**Our terminal is going to be our best friend**](<https://arcolinux.com//the-terminal-is-going-to-be-our-best-friend/>). In that article we saw that there are many more themes already available for termite on ArcoLinux. There are also many other terminals to choose from. The **terminal** is the **most** **important** part in **Linux**. You need to learn about it. We can **install** **software** using a graphical user interface or gui like **gnome-software** or**pamac**. But a gui is nothing more than an application that passes commands on to the terminal. If you are not yet comfortable with the terminal, you keep using the two alternatives. **But we better learn how to use the terminal.** In particular **how to install software in the terminal**. From time to time we will send you to the **wiki** of Arch Linux. You will find a lot of information there. It can be that, at this point in time, the information is not clear. We will get there. One of the most important commands is : [**pacman**](<https://wiki.archlinux.org/index.php/pacman>). You can remember the name with the words **Pac** kage **Man** ager. [Check out the wiki now](<https://wiki.archlinux.org/index.php/pacman>). In short pacman is a package manager that keeps your packages (aka your software)**up-to-date** , **installs** them, **removes** them... When you install a package it sometimes need **other** packages to be able to run. Those are **dependencies**. Pacman will install those as well. **Installing a specific package** Let us install the package [**Atom**](<https://atom.io/>). An interesting application to edit conky's, scripts, css or python files. 
    
    
    sudo pacman -S atom

Type the above line in a terminal and you will have atom on your system. This application is coming from a specific repository or place e.g. extra or testing. If a package is already installed, it will be reinstalled. But there are also [AUR helpers](<https://wiki.archlinux.org/index.php/AUR_helpers>) to install software from the AUR. First read [here what AUR](<https://wiki.archlinux.org/index.php/Arch_User_Repository>) exactly is. There seems to be a lot of AUR helpers and everyone seems to have their own preference. So can you. Test them out and choose. Packer is my personal preference. You will see me do it in the tutorials. The AUR seems to be interesting as it hosts many interesting 'packages'. Not really packages but the way to build or create them. A pkgbuild is a kind of recipe how to make them. [Check out all the packages you can install now](<https://aur.archlinux.org/packages/>). **ArchMerge is equipped with 3 AUR helpers**. You choose. In **ArcoLinux** we added **trizen** to test it out. 
    
    
    packer spotify
    yaourt spotify
    pacaur -S spotify
    
    trizen spotify

In the tutorial I will install two **cloud** services. I believe it is the **best** **way** to work on linux. Put all the documents you do not want to loose in the **cloud** and **experiment**. Learn and be safe at the same time. We will install **dropbox** and **insync** (google drive). Keyboard Shortcuts To Remember SUPER + T ... CTRL + ALT+ T ... Super + Enter Launch your terminal 

Video: <https://www.youtube.com/watch?v=eDmGRR6Vvuo>
