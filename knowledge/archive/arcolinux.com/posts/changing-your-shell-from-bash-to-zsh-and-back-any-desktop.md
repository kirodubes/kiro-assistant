---
title: "Changing your shell from bash to zsh and back - any desktop"
url: https://arcolinux.com/changing-your-shell-from-bash-to-zsh-and-back-any-desktop/
date: 2021-02-12 10:39:37
type: post
categories: ["Post-installation", "Terminal", "Terminal Design", "Update"]
source_site: arcolinux.com
---

# Changing your shell from bash to zsh and back - any desktop

![](https://arcolinux.com/wp-content/uploads/2020/01/tobash-tozsh.jpg)

Our systems have [Bash](<https://wiki.archlinux.org/index.php/bash>) as our standard shell.

We could change to [Zsh](<https://wiki.archlinux.org/index.php/Zsh>) as shell. You can find the [Zsh website here](<https://ohmyz.sh/>), the [github here ](<https://github.com/ohmyzsh/>)and the [themes](<https://github.com/ohmyzsh/ohmyzsh/wiki/Themes>) here.

# What do you install to have zsh?

It all depends on the iso you start with Arch Linux, ArcoLinux, ArcoLinuxD or ArcoLinuxB.

ArcoLinux and ArcoLinuxB users can skip all the installations and just start using our aliases tobash and tozsh to switch.

If you have started with **ArcoLinuxD** or **Arch** **Linux** you are missing packages and aliases.
    
    
    sudo pacman -S zsh
    sudo pacman -S zsh-completions
    sudo pacman -S zsh-syntax-highlighting 
    sudo pacman -S arcolinux-zsh-git
    sudo pacman -S oh-my-zsh-git

The content of the package **arcolinux-zsh-git** will be installed in **/etc/skel**. In that folder you will find the file**.zshrc**.

Make sure you copy that to your homefolder.

After installing all these packages you are set to switch to **Zsh**. These things are needed on **ArcoLinuxD** or **Arch** **Linux**.

> Switching to Zsh is done via the alias "**tozsh** ".  
>  In the same way we can switch back to Bash with "**tobash** ".

And then you log out and you will see a different shell in neofetch.

The prompt will be changing because of the package [oh-my-zsh-git](<https://github.com/ohmyzsh/ohmyzsh>) that is coming from the AUR.

We show you how Zsh reacts if you want to install packages such as **zsh-completions**.

We show you how the syntax highlighting works.

> cb is not present in Zsh  
>  cz is present in Zsh

**alias tozsh**
    
    
    alias tozsh="sudo chsh $USER -s /bin/zsh && echo 'Now log out.'"

**alias tobash**
    
    
    alias tobash="sudo chsh $USER -s /bin/bash && echo 'Now log out.'"

Video: <https://youtu.be/s3x1HrLsCUA>

Complete git commands and learn

![](https://arcolinux.com/wp-content/uploads/2020/01/git-completion.jpg)

Complete pacman commands and learn

![](https://arcolinux.com/wp-content/uploads/2020/01/pacman-s.jpg)

Complete pacman commands and learn

![](https://arcolinux.com/wp-content/uploads/2020/01/pacman-r.jpg)

Complete pacman commands and learn

![](https://arcolinux.com/wp-content/uploads/2020/01/pacman-q.jpg)

Interesting sources

**[Why Zsh is Cooler than Your Shell](<//www.slideshare.net/jaguardesignstudio/why-zsh-is-cooler-than-your-shell-16194692> "Why Zsh is Cooler than Your Shell") ** from **[jaguardesignstudio](<https://www.slideshare.net/jaguardesignstudio>)**

The Zsh theme is set to random.  
Everytime a surprise or change it to one specific one

Video: <https://www.youtube.com/watch?v=9pMc_TcAyJE>

OUR YOUTUBE PLAYLIST OF ZSH

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS5ML6bno-l-yNQMBUwbQYd0>

Interesting links to learn more

[Useful tips to master your z shell](<https://reasoniamhere.com/2014/01/11/outrageously-useful-tips-to-master-your-z-shell/>)

[Practical differences between bash and zsh](<https://apple.stackexchange.com/questions/361870/what-are-the-practical-differences-between-bash-and-zsh>)

[Zsh Sourceforge book](<http://zsh.sourceforge.net/Doc/Release/zsh_toc.html>)
