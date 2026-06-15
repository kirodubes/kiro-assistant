---
title: "How to update ArcoLinux 18.10 to ArcoLinux 18.12"
url: https://arcolinux.com/how-to-update-arcolinux-18-10-to-arcolinux-18-12/
date: 2018-12-04 13:14:53
type: post
categories: ["Update"]
tags: ["samba", "update"]
source_site: arcolinux.com
---

# How to update ArcoLinux 18.10 to ArcoLinux 18.12

![](https://arcolinux.com/wp-content/uploads/2018/12/arcolinux-rolling.jpg)   


Every video about updating your system to the latest edition will learn you something.  
The video will always contain more information than the title suggests. That applies to all the videos.

> Staying rolling is the focus point in this article.

Here is the more detailed article just about updating.

<https://arcolinux.com/how-to-update-any-arcolinux-or-stay-rolling/>

We go over the elements that have changed these last weeks but surely not all of them.

The main focus is **how** to **update** and use the new **aliases** in your **.bashrc**.

We start with an **update** in the terminal to get the Arch Linux and ArcoLinux packages in.

Then we update the AUR packages with **pksyua**.

Then we use the alias skel to copy/paste the contents of /etc/skel to the home directory.

We compare the bashrc with the bashrc-latest.

We talked about making a .bashrc-personal. [More info is here](<https://arcolinux.com/add-your-personal-aliases-to-bashrc-the-smart-way/>). You will love it if you have your own aliases.

New alias of cb. [Here is a video just about cb](<https://www.youtube.com/watch?v=pQ8J-mVe9S4>).

Yayskip and trizenskip have an article [here](<https://arcolinux.com/how-to-install-a-package-by-skipping-the-validity-check/>).

We created 4 mirror aliases more info [here](<https://arcolinux.com/how-to-get-the-best-arch-linux-servers-to-update-your-system/>).

We have to install 2 new packages for the alias rip and ytv-best and others.
    
    
    sudo pacman -S expac youtube-dl

 

We will **uninstall** **samba** via the scripts provided in ~/.bin.

**~/.bin/stay-rolling/18.11-to-18.12/delete-all-samba-related-services-and-apps-error-message-vx.sh**

****

**Stay-rolling** script is there to be able to manage the files with our package manager called pacman.

**~/.bin/stay-rolling/18.11-to-18.12/stay-rolling-vx.sh**

****

If you want to have an exact copy of 18.12 release then you should disable and uninstall tlp. It is an application that is useful for laptops but not for desktops. It concerns the battery of the laptop.
    
    
    sudo systemctl disable tlp.service
    sudo systemctl disable tlp-sleep.service
    sudo pacman -R tlp

Video: <https://youtu.be/UfTGy8NrPM8>

  


# Now you can change your release number to 18.12.7.

# Use the power of the video to do it.

Video: <https://www.youtube.com/watch?v=c3IzgXrqYYI>
