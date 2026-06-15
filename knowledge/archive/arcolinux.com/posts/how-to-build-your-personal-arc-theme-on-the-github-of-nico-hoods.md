---
title: "How to build your personal Arc theme on the github of Nico Hoods"
url: https://arcolinux.com/how-to-build-your-personal-arc-theme-on-the-github-of-nico-hoods/
date: 2019-03-06 19:50:46
type: post
categories: ["Themes"]
tags: ["theming"]
source_site: arcolinux.com
---

# How to build your personal Arc theme on the github of Nico Hoods

![](https://arcolinux.com/wp-content/uploads/2019/03/arc-aqua-theming.jpg)

Install the new Arc themes based on Nico Hoods github with

sudo pacman -S arcolinux-arc-gtk-theme-nico-git

Long version

Originally the Arc theme comes from the github of [Horst3180](<https://github.com/horst3180/Arc-theme>). Some time ago development stopped and Nico Hood (and others) stepped in and took over on the github of [Nico Hood](<https://github.com/NicoHood/arc-theme>).

In the **past** I had a script created to change the blue color of the Arc theme to any color I like - choose one color out of 16.000.000 colors. The script is called [Arc-Theme-Colora](<https://github.com/erikdubois/Arc-Theme-Colora>). It takes you by the hand and guides you till you have a new Arc theme. We do not need the old script.

**We created a new github for the maintenance of the Arc themes on ArcoLinux.**

 

<https://github.com/erikdubois/ArcoLinux-Arc-Themes>

 

 

There are **two major projects** :

One is for ArcoLinux **users** and Arch Linux users aka folder "use-this-for-just-one-theme"

One is for ArcoLinux **maintainers** \- "2-make-all-themes-for-arcolinux.sh" - all themes in 1 go

The scripts in the folder "use-this-for-just-one-theme" was just for warming up.

I wanted to build a script that will create all 23 icon themes. Aqua and Pink are 2 new ones.

We will run this script at a certain interval and we will update our package that way.

Follow the video and the script to get your personal Arc theme.

Remark: rewatching the video it seems I mistyped at the end of the video - I did pacman -S instead of pacman -R and was wondering why Arc theme was still there... It happened. Never mind.

Video: <https://youtu.be/wf4iaL74YQY>

Short version

Procedure to make a personal Arc Theme

  1. Get the scripts from <https://github.com/erikdubois/ArcoLinux-Arc-Themes>
  2. Choose a color - example Sardi-Mint-Y-Pink
  3. script 1 install the software
  4. script 2 change the color - copy/paste from gpick in the video
  5. script 3 we use the make install from Nico Hood
  6. script 4 rename and move the themes
  7. script 5 reinstall the original Arc theme or just sudo pacman -S arc-gtk-theme



Video: <https://youtu.be/YBxo1i7fIa8>

Because we need **gnome-shell** to build the Arc-theme you will see at your login screen **GNOME**.

After creation of the Arc themes you can delete gnome-shell again with
    
    
    sudo pacman -Rs gnome-shell
