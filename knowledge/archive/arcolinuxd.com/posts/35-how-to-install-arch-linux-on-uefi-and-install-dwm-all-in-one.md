---
title: "All in one Arch Linux installation UEFI with Dwm"
url: https://www.arcolinuxd.com/35-how-to-install-arch-linux-on-uefi-and-install-dwm-all-in-one/
date: 2020-11-14 18:33:43
type: post
categories: ["ArchWayAllinone", "ArchWayDesktop", "ArchWaySpices"]
source_site: arcolinuxd.com
---

# All in one Arch Linux installation UEFI with Dwm

![](https://www.arcolinuxd.com/wp-content/uploads/2020/11/archlinux-dwm-border.jpg)

Another example how to install Arch Linux from A till Z.

This time we use **ext4** as formatting system.

**efi** (fat32), **swap** and **root** as partitions and we use **uefi** on our VirtualBox. 

Later we install **dwm**.

We have seen many **archISO** releases in the last months. Many things have been changed and deleted. You can learn more about the changes of archISO on [arcolinux.com](<https://arcolinuxISO.com/category/carli7/>).

Video: <https://youtu.be/q3bQO5qJR2g>

Now we install [Dwm](<https://wiki.archlinux.org/index.php/dwm>) on our Arch Linux system.

We use the functionality of cloning virtual machines in VirtualBox.

First we install **yay** and then we have an **AUR** helper to install **dwm**.

If we later on want to change dwm we have to go to the folder where Yay created his Dwm application and we need to rebuild it again with makepkg.

We install **pacman-contrib** because we would like to have **updpkgsums** as application.

 

Video: <https://www.youtube.com/watch?v=DM5fzlePKPQ>

Adding the **ArcoLinux** Spices  
Getting Dwm of ArcoLinux and more

![](https://www.arcolinuxd.com/wp-content/uploads/2020/11/archlinux-dwm-spices.png)

In previous video we installed Dwm from the Aur with yay.

In this video we get the [ArcoLinux spices application](<https://arcolinux.info/download-applications/>) and we run the scripts manually since we have NO graphical environment yet.

There are many videos about the **ArcoLinux spices**. You can see them all in a [playlist on Youtube](<https://www.youtube.com/playlist?list=PLlloYVGq5pS4oAp187sR78hKZww-aICNK>).

We get the source code from github with a command.
    
    
    git clone https://github.com/arcolinux/arcolinux-spices

When you press a button the ArcoLinux spices application runs a script. We will run these scripts ourselves.

We first **install** the package **git** to be able to git clone our application.

Then we run the scripts in the same sequence of our GUI.

Follow the video to learn more.

Video: <https://youtu.be/E6sGdOFMJ8w>
