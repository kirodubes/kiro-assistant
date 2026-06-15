---
title: "Add your personal aliases to zsh the smart way"
url: https://arcolinux.com/add-your-personal-aliases-to-zsh-the-smart-way/
date: 2022-03-15 10:13:40
type: post
categories: ["Shell", "Terminal"]
source_site: arcolinux.com
---

# Add your personal aliases to zsh the smart way

![](https://arcolinux.com/wp-content/uploads/2022/03/zsh-personal.jpg)

Since we always use **skel** to copy/paste the files from **/etc/skel** to your home directory, the .zshrc is overwritten every time.

We have included the following lines to the .bashrc.
    
    
    [[ -f ~/.zshrc-personal ]] && . ~/.zshrc-personal

If you create a file on your home directory with the name **.zshrc-personal** and add your personal aliases to that file, these aliases will be added.

So update your system in order to have the latest **arcolinux-zsh-git package**.

Then type **skel**.

You will get the new **.zshrc** in.

Your **own** .zshrc gets **overwritten**.

You can now logout or reboot or **use the alias cz** to **source** the new **.zshrc** and by consequence the .zshrc-personal.

> Your .zshrc-personal file will never be overwritten by ArcoLinux scripts

The use of **.bashrc-latest** was abandoned. You may still see them in old videos and/or images.

It does not exist anymore.

Video: <https://youtu.be/kA0GJAgfuIo>

Video: <https://youtu.be/XVeeuA9c8uk>
