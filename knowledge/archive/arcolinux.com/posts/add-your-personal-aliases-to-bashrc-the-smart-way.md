---
title: "Add your personal aliases to bashrc the smart way"
url: https://arcolinux.com/add-your-personal-aliases-to-bashrc-the-smart-way/
date: 2022-03-15 10:03:33
type: post
categories: ["Shell", "Terminal"]
tags: ["terminal"]
source_site: arcolinux.com
---

# Add your personal aliases to bashrc the smart way

![](https://arcolinux.com/wp-content/uploads/2018/12/bashrc-personal.jpg)

Since we always use **skel** to copy/paste the files from **/etc/skel** to your home directory, the bashrc is overwritten every time.

We have now included the following lines to the .bashrc.
    
    
    [[ -f ~/.bashrc-personal ]] && . ~/.bashrc-personal

If you create a file on your home directory with the name .bashrc-personal and add your personal aliases to that file, these aliases will be added.

So update your system in order to have the latest **arcolinux-root-git package**.

Then type **skel**.

You will get the new **.bashrc** in.

Your **own** .bashrc gets **overwritten**.

You can now logout or reboot or **use the alias cb** to **source** the new **.bashrc** and by consequence the .bashrc-personal.

> Your .bash-personal file will never be overwritten by ArcoLinux scripts

The use of **.bashrc-latest** was abandoned. You may still see them in old videos and/or images.

It does not exist anymore.

Video: <https://youtu.be/B5qU_kfmHL8>

Video: <https://youtu.be/kA0GJAgfuIo>

Video: <https://youtu.be/XVeeuA9c8uk>
