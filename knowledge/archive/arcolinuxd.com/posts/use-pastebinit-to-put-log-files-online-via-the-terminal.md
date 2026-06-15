---
title: "Use pastebinit to put log files online via the terminal"
url: https://www.arcolinuxd.com/use-pastebinit-to-put-log-files-online-via-the-terminal/
date: 2019-06-24 22:16:37
type: post
categories: ["Help"]
source_site: arcolinuxd.com
---

# Use pastebinit to put log files online via the terminal

![](https://www.arcolinuxd.com/wp-content/uploads/2019/06/pastebinit.jpg)

Starting from a question on Discord

> How do I send information from a live-dvd like ArcoLinuxD to the internet without browser?

The answer is install 
    
    
    sudo pacman -S pastebinit

To know any application in linux you type two things
    
    
    man pastebinit
    
    
    pastebinit --help or -h

This will give you all the info you require.

Navigate to the log or file you want to put on the net and type
    
    
    pastebinit -i README -b http://pastebin.com

NOT HTTPS.

Then you get a link where your data is.

Video: <https://youtu.be/1CnmNN9uOxM>
