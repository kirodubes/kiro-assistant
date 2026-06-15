---
title: "Installing the spigot server for minecraft on any Arch Linux based system"
url: https://arcolinux.com/installing-the-spigot-server-for-minecraft-on-any-arch-linux-based-system/
date: 2019-07-15 12:25:11
type: post
categories: ["Fun"]
source_site: arcolinux.com
---

# Installing the spigot server for minecraft on any Arch Linux based system

![](https://arcolinux.com/wp-content/uploads/2019/07/spigeot-server.jpg)

We are going to install the spigot server but first we take a look at the minecraft server settings in ([see former video](<https://arcolinux.com/installing-the-official-minecraft-server-on-any-arch-linux-based-system/>)) in /etc/conf.d/minecraft.
    
    
    yay -S spigot

and choose nr 4 for java 8.

After installation you first need to change the /srv/craftbukkit/eula.txt and set it to true.
    
    
    sudo nano /srv/craftbukkit/eula.txt

then you can start the server with
    
    
    spigot start

Video: <https://youtu.be/mT3z_IcUX2A>
