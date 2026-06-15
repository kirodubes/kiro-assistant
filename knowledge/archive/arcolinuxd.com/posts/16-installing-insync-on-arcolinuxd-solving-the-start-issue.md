---
title: "16 - Installing insync on ArcoLinux(D) - solving the start issue"
url: https://www.arcolinuxd.com/16-installing-insync-on-arcolinuxd-solving-the-start-issue/
date: 2017-11-11 18:58:04
type: post
categories: ["i3"]
tags: ["cloud"]
source_site: arcolinuxd.com
---

# 16 - Installing insync on ArcoLinux(D) - solving the start issue

First of all installing an application can be done on **any** ArcoLinux(D). No matter the desktop. I just happen to be on ArchMergeD-i3 when I wanted to make a tutorial about [insync](<https://www.insynchq.com/>). **Insync** is a tool that you can use to **synchronize** your files and folders on **google drive** to your personal computer. It works like a mirror. Anything you put in the folder on your computer will be synced to the **cloud** and vice versa. Insync however is **free** for **15** days to try it out then you should pay for it. Check out [insync](<https://www.insynchq.com/>) for pricing. Dropbox is also a cloud services and [is explained here](<https://arcolinux.com/how-to-install-dropbox-and-how-to-use-it/>). We go over all the possible ways to install it.
    
    
    sudo pacman -S insync
    packer insync
    pacaur -S insync
    yaourt insync
    pks insync

After the installation we figure out what to do with "man insync". It seems we can start it with
    
    
    insync start

Then we run into an other problem and we start **qtconfig-qt4** with our dmenu shortcut (super + shift + d). We should not select **GTK+** but change it to anything else then "insync start" will work.

We should tell insync **where** you want put the files and folders. We choose to make a folder named "Insyc" where the complete google drive will be insynced.

Video: <https://youtu.be/cgrFs17OMqo>
