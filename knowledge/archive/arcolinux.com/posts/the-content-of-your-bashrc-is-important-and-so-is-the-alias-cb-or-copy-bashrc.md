---
title: "The content of your bashrc is important and so is the alias cb or copy bashrc"
url: https://arcolinux.com/the-content-of-your-bashrc-is-important-and-so-is-the-alias-cb-or-copy-bashrc/
date: 2019-04-10 12:23:12
type: post
categories: ["Terminal", "Update"]
source_site: arcolinux.com
---

# The content of your bashrc is important and so is the alias cb or copy bashrc

![](https://arcolinux.com/wp-content/uploads/2019/04/alias-cb.jpg)

.bashrc is a very important file in your linux system. 

The point at the start means it is hidden. You need to press CTRL + H on many filemanagers to show the hidden files/folders.

If you want to know much more about bash, you definitely need to read up on the [Arch wiki](<https://wiki.archlinux.org/index.php/Bash>).

ArcoLinux has a specific .**bashrc-latest** file. 

It contains the very last version of our bashrc. It is that content that will be used on a new ArcoLinux build.

In order for you to use the last changes (like a new alias), you need to copy/paste the content of .bashrc-latest into .bashrc.

And if you use skel to keep up-to-date you better change it also in /etc/skel else you will overwrite your .bashrc again in your home directory and get the old .bashrc.

> The alias "cb" or copy bashrc is taking care of that. 

In the video we analyze the contents of our bashrc and show you what the alias 'cb' will do.

**Two letters to ensure your .bashrc is the latest one.**

If you have aliases of your own, put them in the .bashrc-personal. [More info about that in this article](<https://arcolinux.com/add-your-personal-aliases-to-bashrc-the-smart-way/>).

> The .bashrc-personal will never be overwritten.

Video: <https://youtu.be/jbz_uLOT4I4>
