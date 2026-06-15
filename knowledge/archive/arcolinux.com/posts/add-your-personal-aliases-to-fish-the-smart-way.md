---
title: "Add your personal aliases to fish the smart way"
url: https://arcolinux.com/add-your-personal-aliases-to-fish-the-smart-way/
date: 2022-03-15 10:14:30
type: post
categories: ["Shell", "Terminal"]
source_site: arcolinux.com
---

# Add your personal aliases to fish the smart way

![](https://arcolinux.com/wp-content/uploads/2022/03/fish.jpg)

Since we always use **skel** to copy/paste the files from **/etc/skel** to your home directory, the **config.fish** is overwritten every time.

We have included the following lines to the config.fish. There are more possibilities.
    
    
    # Aliases  
    if [ -f $HOME/.config/fish/alias.fish ]  
    source $HOME/.config/fish/alias.fish  
    end

If you create a file in your home directory in**~/.config/fish** with the name **alias.fish** and add your personal aliases to that file, these aliases will be added to fish.

So update your system in order to have the latest **arcolinux-fish-git package**.

Then type **skel**.

You will get the new**config.fish** in.

Your **own** config.fish gets **overwritten**.

> But the personal files will never be overwritten.

You can now logout or reboot or **use the alias cf** to **source** the new **settings**.

Video: <https://youtu.be/kA0GJAgfuIo>

Video: <https://youtu.be/XVeeuA9c8uk>

Want to learn about Fish

use our youtube playlist

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS7yGHbCc2WiqYeTCkLSgQPL>
