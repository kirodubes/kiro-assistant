---
title: "Polybar configuration in more detail - general and i3 module"
url: https://arcolinux.com/polybar-configuration-in-more-detail-general-and-i3-module/
date: 2018-01-19 18:29:55
type: post
categories: ["Polybar"]
tags: ["i3", "polybar"]
source_site: arcolinux.com
---

# Polybar configuration in more detail - general and i3 module

![](https://arcolinux.com/wp-content/uploads/2018/01/archmerge-polybar-general-i3.jpg)

First we are going to take a look at the **launch.sh** file to start polybar.

If you are on ArchMerge 6.3.1 awesome font is installed. You only need to install **polybar**.

If you are on ArchMergeD you need to install them both
    
    
    yaourt -S polybar awesome-terminal-fonts

You can find nice awesome font icons for your configuration on this website.

<http://fontawesome.io/cheatsheet/>

Note : **killall -q** \-- **q** does not stand for **quit** but **quiet**. A quick 'man killall' in the terminal tells us that.

We explain what happens in the launch.sh and why it is there and what it does.

Then we take a look at the config file and advice you to go and read/bookmark this website for more info about your polybar configuration: <https://github.com/jaagr/polybar/wiki>

We go into the general settings and into the mainbar-i3 and discuss some of the more interesting elements.

Modules-left, modules-center and modules-right will be edited the most. You define what modules you want to see in those lines

Video: <https://youtu.be/YZ5VkdR2c7Q>

Video: <https://youtu.be/QkmDpV3JbtA>
