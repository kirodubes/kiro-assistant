---
title: "Installing the official minecraft server on any Arch Linux based system"
url: https://arcolinux.com/installing-the-official-minecraft-server-on-any-arch-linux-based-system/
date: 2019-07-15 12:20:54
type: post
categories: ["Fun"]
source_site: arcolinux.com
---

# Installing the official minecraft server on any Arch Linux based system

![](https://arcolinux.com/wp-content/uploads/2019/07/minecraftd.jpg)

You can host your own server at home and share the minecraft world with others at home or on the internet.

Install it with 
    
    
    yay -S minecraft-server

There is no gui ... nor is it necessary you see in the image what can do with it - start, stop, status, console, ...

A gui will only consume even more memory and our memory needs to go to the game hence no gui.

We see all the commands when we type the command minecraftd in the terminal.

**BUT FIRST we need to edit a file.**

sudo nano /srv/minecraft/eula.txt 

and change it to true.

You can change the environment inside your world - you are in control - weather, time, teleport, ...

In the video we change the weather in the server and the game changes.

The number of the port is important. Standard it is 25565. You can change it in the /etc/config.d/minecraft file if you need to.

You can put it behind an ip like this to connect to a ip :

192.168.0.5:25565

Connecting issues think about firewall application, antivirus application, ports on the router, ... that can potentially block your communication to other minecraft servers.

Video: <https://youtu.be/tPrUwGZlEog>
