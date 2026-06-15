---
title: "Analyze bash commands you find on the internet - alias cleanup"
url: https://arcolinux.com/analyze-bash-commands-you-find-on-the-internet/
date: 2018-12-06 11:59:31
type: post
categories: ["Cleanup", "Terminal", "Utilities"]
tags: ["terminal"]
source_site: arcolinux.com
---

# Analyze bash commands you find on the internet - alias cleanup

![](https://arcolinux.com/wp-content/uploads/2018/12/cleanup.jpg)

When navigating the internet you find aliases, configs, .dot files you might like to try.

Before you do try to know as much as possible about the code.

We are going to study this line of code from Nick Petrov.
    
    
    alias cleanup='sudo pacman -Rns $(pacman -Qtdq)'

Most of the commands have either a manual or a help function.
    
    
    man command
    command --help
    command -h

These are the most common ones.

We check the manual for pacman with **man pacman** and go read about all the switches.

## Definitely read about pacman in the arch wiki.

<https://wiki.archlinux.org/index.php/pacman>

Video: <https://youtu.be/_TSe41ToHl0>

This means you are cleaned up.

![](https://arcolinux.com/wp-content/uploads/2018/12/no-cleanup-needed.jpg)
