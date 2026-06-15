---
title: "How to install powerline to pimp your system"
url: https://arcolinux.com/how-to-install-powerline-to-pimp-your-system/
date: 2018-04-30 07:50:33
type: post
categories: ["Terminal Design"]
tags: ["terminal", "theming"]
source_site: arcolinux.com
---

# How to install powerline to pimp your system

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-powerline.jpg)![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-terminal-powerline.jpg) If you google "linux powerline" and ask for images you will see lots of examples what can be achieved. We need first to install it and then look for a nice config. Installation of powerline. 
    
    
    sudo pacman -S powerline powerline-fonts

Open your .bashr and put this code at the bottom. 
    
    
    powerline-daemon -q
    POWERLINE_BASH_CONTINUATION=1
    POWERLINE_BASH_SELECT=1
    . /usr/lib/python3.6/site-packages/powerline/bindings/bash/powerline.sh

We did not have to load the .bashrc. But you might need to do this. Logging off and on has the same effect. 
    
    
    source .bashrc

If you are changing your config, you might need to reload powerline with 
    
    
    powerline-daemon --replace

More information here: <https://epsi-rns.github.io/desktop/2016/03/21/powerline-customizing.html> <https://powerline.readthedocs.io/en/latest/configuration.html#>

Video: <https://youtu.be/99daC8j0Iu0>
