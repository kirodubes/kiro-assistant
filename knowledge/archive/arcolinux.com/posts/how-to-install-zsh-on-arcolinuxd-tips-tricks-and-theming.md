---
title: "How to install zsh on ArcoLinux(D) tips tricks and theming"
url: https://arcolinux.com/how-to-install-zsh-on-arcolinuxd-tips-tricks-and-theming/
date: 2019-04-06 11:32:27
type: post
categories: ["Terminal", "Terminal Design"]
tags: ["theming"]
source_site: arcolinux.com
---

# How to install zsh on ArcoLinux(D) tips tricks and theming

Zsh is an alternative to bash. Check out the [Arch wiki first](<https://wiki.archlinux.org/index.php/zsh>).

We have a script to install zsh. But not only zsh also other features that are need to have like

  * zsh-completions
  * oh-my-zsh
  * zsh-syntax-hightlighting



Command not found has been abandoned in Feb 2018.

You will find it on all githubs : <https://github.com/arcolinuxd>.

After running the script you need to change the shell with this command
    
    
    sudo chsh erik -s /bin/zsh

Change erik to your loginname.

 

Video: <https://youtu.be/9z3LD68PU2A>

Then we reboot and check out our terminal.

We need to get the aliases from our .bashrc and copy/paste them into .zshrc.

We reload the .zshrc with the command source.

Video: <https://youtu.be/ljSDPq81k0c>

# Making sure the latest bashrc aliases are in your zshrc too

Video: <https://youtu.be/uFNRSe8pdW0>

Getting back to bash if you are tired of using zsh is done like this
    
    
    sudo chsh erik -s /bin/bash
