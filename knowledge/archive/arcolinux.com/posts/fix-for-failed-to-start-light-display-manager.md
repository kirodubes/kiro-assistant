---
title: "fix for failed to start light display manager"
url: https://arcolinux.com/fix-for-failed-to-start-light-display-manager/
date: 2019-06-05 08:30:55
type: post
categories: ["Fixes", "Lightdm", "Nvidia"]
tags: ["nvidia"]
source_site: arcolinux.com
---

# fix for failed to start light display manager

![](https://arcolinux.com/wp-content/uploads/2019/02/failed-to-start-light-display-manager.jpg)

Option 1 update kernel and nvidia packages

Go to **tty** with CTRL + ALT + F2

Login

Type in the terminal the following commands
    
    
    update  
    skel  
    upall

then type
    
    
    sudo update-mirrors

then again type
    
    
    update  
    skel  
    upall

This means we have updated our computer.   
The second time we first ask for different Arch Linux servers with update-mirrors  
and we update again and see if we receive newer packages.

Now reboot with
    
    
    sudo reboot

Nvidia files and linux kernel must match and sometimes the Arch Linux servers have not a matching pair. Then you download an new kernel and no nvidia packages or a new nvidia package but the kernel does not upgrade. I believe that is the main reason behind the issues people have with nvidia.

That said I do not install nvidia packages and no issues what so ever in the last 5 years.

 

Option 2 Downgrade lightdm

February 6th 2019 we get an update in that breaks our installation.

Lightdm is often NOT the reason but it will show the **error message**.

The reason of the crash is what lies behind lightdm.

Nvidia, drivers of all kind, desktop, what configuration, compton and alternatives, ...

Type "**rip** " to see what packages where installed last.

Can any of these packages be the culprit?

I had seen what packages were installed and I did notice **lightdm** in there.

LIGHTDM is one of your **major** packages - it starts out display or login manager. Other important packages to keep track off is **linux** and **systemd**.

IF you did not see the packages that came in you can use our alias **RIP** in the terminal to see the last packages.

You computer will function fine until you reboot and then lightdm throws you lots of errors.

[We have made already a video about the power of TTY here](<https://arcolinux.com/fix-your-arcolinux-or-arch-linux-computer-with-these-2-tips/>) but it can not hurt to make one specifically for this issue.

SOLUTION

Get to a TTY with CTRL + ALT + F2 or F3 or ... (Virtualbox users use RIGHT CTRL + F2

Login
    
    
    downgrade lightdm

Choose the prior version with a number

Add lightdm to IgnorePkdg : Y

reboot and have fun again

Other Arch Linux users need to install downgrade with an AUR helper like yay or trizen.

Video: <https://youtu.be/4592XVGwgIs>

A few hours later the fix comes in

A few hours later lightdm is fixed 

Bug report is here : [https://bugs.archlinux.org/task/61654?project=1&string=lightdm](<https://bugs.archlinux.org/task/61654?project=1&string=lightdm>)

You have put lightdm in the ignorepkg list in pacman.conf... 

How to update to the latest package now?

Delete the line in /etc/pacman.conf containing lightdm.

Save the file.

Update and install and reboot.

Video: <https://youtu.be/4592XVGwgIs>
