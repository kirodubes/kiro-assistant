---
title: "Compton has changed into Picom - on Openbox - delete compton.conf from your system - you have a picom.conf now"
url: https://www.arcolinuxd.com/compton-has-changed-into-picom-on-openbox-delete-compton-conf-from-your-system-you-have-a-picom-conf-now/
date: 2024-03-01 06:03:40
type: post
categories: ["Openbox"]
source_site: arcolinuxd.com
---

# Compton has changed into Picom - on Openbox - delete compton.conf from your system - you have a picom.conf now

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/picom-compton.jpg)

Compton has changed into picom

**Compton** has changed into **picom**.

We work on a SSD I use for the Carli tutorials. So this is also an update video tutorial.

New alias do not exist yet like "**nmirrorlist** ".

If you analyze the package picom, it will provide compton but there is a name change. You can use pamac-aur to analyse any package.

We interrupt the download and first we check if we still got the fastest servers.

We teach you how to unlock pacman with the alias "**unlock** ".

We update our system with the alias "**update** ".

Then we get an "failed to commit transaction (invalid or corrupted package) Errors occurred, no packages were upgraded".

Easy to fix if you know how.

We clean out the **/var/cache/pacman** with the command
    
    
    sudo pacman -Scc

Then we download the proper packages.

We explain why /etc/skel is important and why the skel alias is so important.

Upall (ran after update) will get all the AUR packages. These are not from Arch Linux or from ArcoLinux.

Because of the change we need to change our arcolinux-openbox-git and arcolinux-openbox-xtended-git and also the arcolinux-pipemenus-git. 

We investigate the content of the package picom via pamac-aur.

Video: <https://youtu.be/w4qGRFsmjg8>

We logged back into Openbox and see the old standard look of Openbox. Tint2 is providing the bar.

Skel is now in order.

We need to get the new files for openbox in our own directory.

We first compare the bashrc versions and make sure we have the latest bashrc.
    
    
    cb

We copy the .bashrc over.

Skel is now making a backup of your .config. Beware the size of your .config.

Use compare to see what you want to get back.

Now we investigate the openbox matter.

We start picom in the autostart file in ~/.config/openbox

Delete the compton.conf  
and keep the picom.conf

Then we show the last standard look for openbox. Tint2 is showing a white bar now.

**Summary**

  * mirror
  * update
  * upall
  * cb
  * bupskel - is also interesting to investigate



Video: <https://youtu.be/ssjd_XPU70E>
