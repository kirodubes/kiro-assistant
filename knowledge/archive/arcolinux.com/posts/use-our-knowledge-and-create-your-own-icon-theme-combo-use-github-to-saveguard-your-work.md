---
title: "Use our knowledge and create your own icon theme combo - use github to saveguard your work - create your repository"
url: https://arcolinux.com/use-our-knowledge-and-create-your-own-icon-theme-combo-use-github-to-saveguard-your-work/
date: 2022-02-23 08:34:03
type: post
categories: ["Icons"]
source_site: arcolinux.com
---

# Use our knowledge and create your own icon theme combo - use github to saveguard your work - create your repository

![](https://arcolinux.com/wp-content/uploads/2022/02/arcolinux-candy-beauty-tela.jpg)

NEWS VIDEO

  1. how to create an icon theme
  2. how to put it online on github
  3. how to get it back on another computer - manually
  4. how to get it back on another computer - scripting - automatically
  5. how to build the package so you can install it anywhere
  6. how to create a repository to host the package and install it with sudo pacman -S ...



Video: <https://youtu.be/i0mGvoPjAiE>

> this is a "possible" workflow article

In this video we show you the **workflow** how to combine different icons to have a new theme altogether.

We could have created my new themes in the video - we ended up creating **ArcoLinux-Candy-Beauty-Tela**.

<https://github.com/erikdubois/ArcoLinux-Candy-Beauty-Tela>

or
    
    
    git clone https://github.com/erikdubois/ArcoLinux-Candy-Beauty-Tela

> Use the inherits line.
> 
> Use github or others.

Video: <https://youtu.be/QFpfV0_futY>

How to install ArcoLinux-Candy-Beauty-Tela manually

Here we install the theme by using the git clone command and copy paste the content where it supposed to be.
    
    
    git clone https://github.com/erikdubois/ArcoLinux-Candy-Beauty-Tela

Video: <https://youtu.be/H1WpWnNhQRY>

How to install ArcoLinux-Candy-Beauty-Tela with scripts - arcolinux-nemesis

Here we install the theme by using a script we still have to make.
    
    
    git clone https://github.com/erikdubois/arcolinux-nemesis

Video: <https://youtu.be/ZHjCzHf427o>

How to create a pkgbuild for ArcoLinux-Candy-Beauty-Tela

Let us create a PKGBUILD for the theme . Use and re-use code.
    
    
    https://github.com/arcolinux/arcolinux-pkgbuild/tree/master/ARCOLINUX/arcolinux-candy-beauty-git

In the end this is the result.
    
    
    https://github.com/erikdubois/pkgbuild

Video: <https://youtu.be/RhJxDwZ8bcM>

How to create an Arch Linux repository to install the package with sudo pacman -S ...

Here we create a new github project that will host any and all of our created packages.
    
    
    https://github.com/erikdubois/nemesis_repo

Add the repo to your system with npacman or the ATT. (/etc/pacman.conf)
    
    
    [nemesis_repo]
    SigLevel = Optional TrustedOnly
    Server = https://erikdubois.github.io/$repo/$arch

Video: <https://youtu.be/FnPs9n4acRE>

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS6ON76mc7WE6_7pTtvbZUu4>

Let us create more pkgbuilds for more icon themes

Here we show you how easy it is to create more **pkgbuilds** if you have created already the one.

[https://github.com/erikdubois?tab=repositories&q=arcolinux-candy](<https://github.com/erikdubois?tab=repositories&q=arcolinux-candy>)
    
    
    https://github.com/erikdubois/nemesis_repo

Video: <https://youtu.be/SM9qfoHBCZU>

You can put anything on your repo

Here we show you how easy it is to add packages from the AUR to your repo
    
    
    https://github.com/erikdubois/nemesis_repo

Video: <https://youtu.be/5_4ZIdBXTDk>

How to add your own repo to /etc/pacman.conf with scripts (not manually)

We change the arcolinux-nemesis scripts to do the work for us.   
Automatically.

Use scripts and walk away.
    
    
    https://github.com/erikdubois/nemesis_repo

Video: <https://youtu.be/4cz0Zn8EAoo>

Let us test our new arcolinux-nemesis script and install the themes from that repo

Create your own repo, put the packages on their you like and install them.

Video: <https://youtu.be/mkEXQy9TlgM>

We rename our packages to edu-... - PKGBUILD tutorial

When we have a user base, we do not want them to run into issues.

We want that our newly named package will replace the old package with a simple update.

Pacman can do that. The code for that is "**Replace** ".

You have seen this before. The user gets a question to replace x with y and a **(Y/n)** at the end.

Video: <https://youtu.be/XuamB9uatGw>
