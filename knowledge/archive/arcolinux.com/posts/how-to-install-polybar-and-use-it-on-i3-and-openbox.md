---
title: "How to install polybar and use it on i3 and openbox"
url: https://arcolinux.com/how-to-install-polybar-and-use-it-on-i3-and-openbox/
date: 2018-01-19 16:13:10
type: post
categories: ["Polybar"]
tags: ["i3", "openbox", "polybar"]
source_site: arcolinux.com
---

# How to install polybar and use it on i3 and openbox

![](https://arcolinux.com/wp-content/uploads/2018/01/archmerge-polybar-installation.jpg)   


Very often I refer to the wiki of Arch Linux but in this case this will be our link to get to know **polybar**.

<https://github.com/jaagr/polybar>

Polybar is an alternative panel or bar to use instead of the bars of i3 or tint2 in Openbox. It provides us with an alternative bar to show information about our system like temperature, cpu usage, ram usage and so on.

On the website of polybar you can see some images what can be achieved but just google **polybar** and ask for the images. Lots of very creative people make stunning desktops for this bar. Now it is up to you.

Polybar can become a good base for the coming [window tiling managers](<https://wiki.archlinux.org/index.php/Comparison_of_tiling_window_managers>) we will explore in the future like **bspwm** or **xmonad** and many others out there.

For now we are going to use it for **i3** and **openbox**.

Installation of the application

Install polybar with your terminal
    
    
    packer polybar

**You need to build it yourself**. It will **never** be included on the **iso**.

[You can build it faster if you follow this article first.](<https://arcolinux.com/use-all-your-cores-during-build-or-installation-of-packages/>)

We have provided a module in polybar for mpd and ncmpcpp BUT this software is not installed yet.

Together we will install **mpd** and **ncmpcpp AFTER** the installation of polybar. This means that **y****ou will need to reinstall polybar in order for these applications (mpd and ncmpcpp) to work in polybar.**

Installation of the configuration

The polybar configuration comes from our standard **ArcoLinux** repo. Let us install it via
    
    
    sudo pacman -S arcolinux-polybar-git

The version of this package will change over time.

The configuration of polybar is installed in **/etc/skel/.config/polybar**. Now it is up to you to copy/paste this folder **polybar** to your home folder like /home/erik/.config/**polybar**. If it is your **first** **time** , you can just **copy/paste**. If you have worked already on your configuration of polybar, I recommend you use **meld** to compare the differences.

Installation of polybar  
takes a while  
be patient

Video: <https://youtu.be/Sbtm6ZNZ1Ws>
