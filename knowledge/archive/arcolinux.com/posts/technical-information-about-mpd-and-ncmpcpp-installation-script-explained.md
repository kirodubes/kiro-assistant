---
title: "Technical information about mpd and ncmpcpp - installation script explained"
url: https://arcolinux.com/technical-information-about-mpd-and-ncmpcpp-installation-script-explained/
date: 2018-01-23 12:36:21
type: post
categories: ["Audio"]
tags: ["music"]
source_site: arcolinux.com
---

# Technical information about mpd and ncmpcpp - installation script explained

![](https://arcolinux.com/wp-content/uploads/2018/01/archmerge-mpd-ncmpcpp-explained.jpg)Open up the following resources. <https://wiki.archlinux.org/index.php/Music_Player_Daemon> <https://wiki.archlinux.org/index.php/Ncmpcpp> We have downloaded one of the githubs of ArchMergeD to find the installation script of mpd and ncmpcpp. 
    
    
    git clone https://github.com/arcolinuxd/arco-i3

Then you install the following script from the AUR folder 
    
    
    install-mpd-ncmpcpp-v1.sh

**Tip** : **Atom** \- click on the small arrow at the left middle to get rid of the sidebar. We check out all the important files installed by this script and learn how to script. Put some songs in your ~/Music folder to test it out. **If your music folder is named different** because of the language you have choosen then you will need to change that in the two config files. Use symlinks to point to your external harddrive 

Video: <https://youtu.be/Q0YefkNgsDI>

Tips 

## ncmpcpp config file

Do not display message at top right : **Volume : n/a**
    
    
    display_volume_level = no

Start up with visualizer active 
    
    
    startup_slave_screen = "visualizer"

Change the icons used for visualizer 
    
    
    #visualizer_look = ●▮

to 
    
    
    visualizer_look = 

These icons come from awesome fonts installed on your system and to be copy/pasted from [here](<http://fontawesome.io/cheatsheet/>). Change the colors of the songs displayed 
    
    
    #song_columns_list_format = (20)[]{a} (6f)[green]{NE} (50)[white]{t|f:Title} (20)[cyan]{b} (7f)[magenta]{l}

to 
    
    
    song_columns_list_format = (20)[]{a} (6f)[red]{NE} (50)[white]{t|f:Title} (20)[white]{b} (7f)[red]{l}

Current song has a yellow background when selected - change to red 
    
    
    #current_item_prefix = $(yellow)$r

to 
    
    
    current_item_prefix = $(red)$r
