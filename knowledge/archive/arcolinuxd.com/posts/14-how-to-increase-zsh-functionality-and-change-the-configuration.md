---
title: "14 How to increase zsh's functionality and change the configuration - any desktop"
url: https://www.arcolinuxd.com/14-how-to-increase-zsh-functionality-and-change-the-configuration/
date: 2018-02-11 09:39:52
type: post
categories: ["AnyDesktop"]
tags: ["anydesktop"]
source_site: arcolinuxd.com
---

# 14 How to increase zsh's functionality and change the configuration - any desktop

![](https://www.arcolinuxd.com/wp-content/uploads/2018/02/ArchMerge_zsh.jpg) We can use a different shell in your system. The standard shell is bash. You can read more about [bash](<https://wiki.archlinux.org/index.php/bash>) or Bourne-again Shell here. But you can also use Zsh. Read more about zsh [here](<https://wiki.archlinux.org/index.php/zsh>). Zsh is already installed but not activated. And there are other packages you might miss if working with zsh. We will install the extra functionality for zsh with a script. I particularly like zsh because of **oh-my-zsh**. You can follow[ this link](<https://github.com/robbyrussell/oh-my-zsh>) to read more about this package. It will provide you with tons of new themes. With the script we change the theme to **random**. Every new terminal will have a new theme. After running the script you need to change the shell manually - my username is erik 
    
    
    sudo chsh erik -s /bin/zsh

Then you need to **logout** or **reboot** and zsh will be activated in your terminal. Changing back to bash then type 
    
    
    sudo chsh erik -s /bin/bash

Then we get our **.bashrc** settings and copy/paste it into **.zshrc** because we do not have **neofetch** in zsh or our **aliasses**. 

Video: <https://youtu.be/XafxEUn_Wn8>
