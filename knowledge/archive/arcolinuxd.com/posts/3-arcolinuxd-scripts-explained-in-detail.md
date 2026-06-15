---
title: "3 -  ArcoLinuxD scripts explained in detail"
url: https://www.arcolinuxd.com/3-arcolinuxd-scripts-explained-in-detail/
date: 2017-11-10 18:32:55
type: post
categories: ["i3"]
tags: ["scripting"]
source_site: arcolinuxd.com
---

# 3 -  ArcoLinuxD scripts explained in detail

In the tutorials about ArcoLinuxD-Budgie I gave a detailed explanation about **how to make scripts**. If you want to know more about how to start from scratch on a script you can follow the tutorials of ArcoLinuxD Budgie.

In i3 we will take a look at the contents of the scripts we use to get a complete desktop.

You choose your **editor**. There is geany, sublime-text, atom and mousepad and you can install more.

I choose **Atom** in the video.

This tutorial can be interesting   
BUT IT IS NOT REQUIRED AT ALL.

We start with the [shebang](<https://en.wikipedia.org/wiki/Shebang_\(Unix\)>) or 
    
    
    #!/bin/bash

Then we have the line 
    
    
     set -e

This will end the script if it encounters errors. Type "man set" in the terminal to see what -e stands for.

**Echo** is the command to type text you want to show to others.

In the "man" of pacman you will find the **\--noconfirm --needed.**

Installing **lightdm** is documented on the [Arch wiki](<https://wiki.archlinux.org/index.php/LightDM>) and we follow the tips there.

Installing **i3wm** is documented on the [Arch wiki](<https://wiki.archlinux.org/index.php/i3>).

There is a detailed explanation of the script I use to install **AUR** packages.

You need to read about [systemctl](<https://wiki.archlinux.org/index.php/systemd>). It is the way to enable and start your services and many other things.
    
    
    [ -d $HOME"/.config/i3" ] || mkdir -p $HOME"/.config/i3"

This line will check if there is an i3 folder else it will create the directory.

Figuring out sound, [bluetooth](<https://wiki.archlinux.org/index.php/bluetooth>), [samba](<https://wiki.archlinux.org/index.php/samba>), [printers](<https://wiki.archlinux.org/index.php/CUPS>), [sharing](<https://wiki.archlinux.org/index.php/samba>), [avahi](<https://wiki.archlinux.org/index.php/avahi>) and so on. You go to the wiki of Arch and you read what you need.

To ask input from your users you can use the command "read". The -p is supplying a [prompt](<http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_08_02.html>).

We take a look at pacman.conf and tell you why we have a division between arch repo and aur repo. 

Video: <https://www.youtube.com/watch?v=MubqO4AqA4E>
