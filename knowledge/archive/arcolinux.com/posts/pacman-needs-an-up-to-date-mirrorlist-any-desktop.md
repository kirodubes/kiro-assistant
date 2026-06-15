---
title: "Pacman needs an up-to-date mirrorlist - any desktop"
url: https://arcolinux.com/pacman-needs-an-up-to-date-mirrorlist-any-desktop/
date: 2018-09-11 16:50:19
type: post
categories: ["Pacman", "Update"]
tags: ["anydesktop"]
source_site: arcolinux.com
---

# Pacman needs an up-to-date mirrorlist - any desktop

Never mind the warning  
Update the mirrorlist with   
mirror   
in the terminal

![](https://arcolinux.com/wp-content/uploads/2018/09/warning-mirrorlist.jpg)   
![](https://arcolinux.com/wp-content/uploads/2017/12/mirrorlist.pacnew.png)

 

Pacman or your **PAC** kage **MAN** ager is going to get its packages from different servers over the world. Depending where you live you select the servers that our near to you in **distance** BUT they may **not** be the **fastest**.

Or you use our alias "**mirror** " and let the application "**reflector** " test what servers are**the** **fastest** in your part of the world.

I point you first to the Arch Wiki and [let you read this article about mirror](<https://wiki.archlinux.org/index.php/mirrors>) and [this article about reflector](<https://wiki.archlinux.org/index.php/reflector>).

You will learn that the **mirrorlist** is coming in via a package named **pacman-mirrorlist**.

**But it is NOT, because you get an update in, that you are using the latest mirrors from that package!**

We will show what you need to do (if you want to use the latest mirrorlist).

After the update you will now have two files in **/etc/pacman.d** folder.

  * mirrorlist
  * mirrorlist.pacnew



It is up to us to do something with it or not.

On ArcoLinux we use an alias called "**mirror** " and we are using our own mirrorlist that is created by reflector.

We check what comes in with the update **mirrorlist.pacnew**.

And we could use this list of servers for our pacman. We are adding the servers that are the closest to **Belgium**. But it does not mean they will be the "best".

Mirrorlist is the file that pacman will use NOT mirrorlist.pacnew.

We try different servers to see what happens.

Bottom-line  
I will keep using mirror or reflector to update my Arch Linux Servers or the mirrorlist.

Video: <https://youtu.be/u6JLYkkf7uc>

 

Video: <https://youtu.be/ZUmYGPcFhnE>
