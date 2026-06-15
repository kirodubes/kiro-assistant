---
title: "Build the software yourself just because you can or install it from AUR"
url: https://arcolinux.com/build-the-software-yourself-just-because-you-can-or-install-it-from-aur/
date: 2019-01-25 18:57:48
type: post
categories: ["Manage software"]
tags: ["pkgbuild", "software"]
source_site: arcolinux.com
---

# Build the software yourself just because you can or install it from AUR

![](https://arcolinux.com/wp-content/uploads/2019/01/arcolinux-openbox-pocillo.jpg)

Following up a **tip** of an **ArcoLinux** **user** we take a look at Pocillo-gtk-theme.

<https://github.com/UbuntuBudgie/pocillo-gtk-theme>

This theme seems to be developed by the UbuntuBudgie team is, who build it on the pop-os theme

<https://github.com/pop-os/gtk-theme>

who build it on the materia theme

<https://github.com/nana-4/materia-theme>

So here you have 3 different themes to take a look at.

We will stay with pocillo.

We see that you can install it via AUR
    
    
    trizen -S pocillo-gtk-theme-git

## BUT you can also build the pocillo theme yourself.

This will come in handy IF the pkgbuild from AUR breaks for example.

We are just doing it to make an educational tutorial about building.

You see that on the github they used **sudo apt install.**

That means it will work on a debian/ubuntu based system BUT not on an Arch Linux.

With some common sense and a lot of patience you can make the translation between Ubuntu and Arch Linux.

That is exactly what we will do together in the video and install this theme as an end-result.

Here you can learn how to make a **script**

with the **knowledge** we acquired and

make sure we can install it **quickly** after next clean install.

<https://arcolinux.com/how-to-make-a-script-to-build-the-pocillo-gtk-theme-to-be-able-to-re-install-it-later/>

Video: <https://youtu.be/U7hNozOCwjA>

## Download the script for Pocillo-gtk-theme here (AUR folder)

<https://github.com/erikdubois/arcolinux-nemesis>
