---
title: "Compact installation guide for ArcoLinux"
url: https://arcolinux.com/the-7-step-installation-guide-for-arcolinux/
date: 2019-11-29 14:06:07
type: post
categories: ["Must read", "Post-installation"]
tags: ["nemesis", "pkgbuild", "script"]
source_site: arcolinux.com
---

# Compact installation guide for ArcoLinux

![](https://arcolinux.com/wp-content/uploads/2018/05/archlinux-xfce-theming.jpg)

This is a step by step guide what I typically  
would do on my computer system.

Step 1 : install arcolinux

![](https://arcolinux.com/wp-content/uploads/2019/11/calamares-3.2.16.jpg)

Step 2 : update ARCH and arcolinux

Make sure you have the fastest servers to download from with. We type this alias in the terminal.
    
    
    mirror

Then we update in the terminal with
    
    
    update

**Some** of the **ArcoLinux** packages will be updated in **/etc/skel**. We want them in our home directory.
    
    
    skel

Sometimes we create new aliases in our bashrc.
    
    
    cb

Step 3 : update AUR

We will now update the packages coming from AUR.
    
    
    upall

Step 4 : hblock

We ban all ads, tracking and malware websites with our **adblock**.

You can find Adblock in the xfce settings and other desktops.

Run
    
    
    hblock

in terminal for example in tiling window managers.

Step 5 : hardcode fixer for icons

In the Xfce system settings there is an icon to launch the "Fix Hardcoded Icons".

Use this code in the terminal to fix some of the applications that still use hardcoded paths to their icons on tiling window managers for example.
    
    
    sudo hardcode-fixer

![](https://arcolinux.com/wp-content/uploads/2019/11/xfce-settings.png)

Step 6 : Arcolinux nemesis

Type this in your terminal or copy/paste with ctrl + shift + v.
    
    
    git clone https://github.com/erikdubois/arcolinux-nemesis.git

I will run almost all scripts.

**Discord** is our channel for ArcoLinux relates issues.

**Telegram** is our channel for more casual conversations

**Insync** is there to sync files to **google** **drive** (paid).

**Virtualbox** will be installed.

**Spotify** will be installed.

**This github changes constantly and will differ from what you see.**

Step 7 : Arcolinux nemesis PERSONAL

Now we go inside the Personal folder of the same github: <https://github.com/erikdubois/arcolinux-nemesis>.

See what you can use from it and rewrite the codes any way you see fit.

**Bookmarks** can be interesting.  
**Firefox** is sometimes not quite readable with dark themes depending on what websites you visit. Css fix for that.

We have added a "**FUN** " **script** to the collection. It will install many interesting applications that you can use for your screenshots like bash-pipes, cmatrix, cool-retro-term, cmatrix and many more. [More info here](<https://arcolinux.com/installing-fun-stuff-for-the-terminal-on-arcolinux/>).

**This github changes constantly and will differ from what you see.**

Video: <https://youtu.be/QW8cZLzaLbM>

Video: <https://youtu.be/6vgncnhLtCs>

A workflow is something very personal

**arcogetstarted** may be something  
you can use and change to your needs

Most recent download link is  
on discord - official channel

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS6o5snF1_oPN9BMH2XaTvfZ>
