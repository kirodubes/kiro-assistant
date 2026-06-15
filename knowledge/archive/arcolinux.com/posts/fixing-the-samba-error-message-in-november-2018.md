---
title: "Fixing the Samba error message in November 2018"
url: https://arcolinux.com/fixing-the-samba-error-message-in-november-2018/
date: 2018-11-27 12:08:53
type: post
categories: ["Fixes", "Samba"]
tags: ["fix", "samba"]
source_site: arcolinux.com
---

# Fixing the Samba error message in November 2018

![](https://arcolinux.com/wp-content/uploads/2018/11/samba-update-1-1.jpeg)   


The first picture shows you the samba status before the updates come in.Right terminal says **smb service is active and running and is colored in green.**

Just recently we get an **Samba** **error** after updating to version **4.9.2-1**. We only see the message when we shutdown and it does not intervene in our work or pose any problems. The message disappears quite quickly and can easily be missed. Check the next image.

> Bottom-line samba is not working.

![](https://arcolinux.com/wp-content/uploads/2018/11/samba-error-1.jpg)   


Updating samba to the most recent version will result in breaking samba.

 

## Recommended solution

**Disabling** the winbind service will fix samba for now. We will have to wait for an update from the developers.
    
    
    sudo systemctl disable winbind.service

Video: <https://www.youtube.com/watch?v=s2c0MLkXFfs>

  


activate WINBIND only if you need it

If you do need **winbind** to be enabled for some reason then we can implement the solution that Marco Obaid found. Meet him on Discord. You can read about the [solution here](<https://wiki.samba.org/index.php/Idmap_config_ad>).

Our smb.conf has been adapted to include these lines.
    
    
    idmap config * : backend = tdb
    idmap config * : range = 3000-7999

When you run script 140 from any [ArcoLinuxD github](<https://github.com/arcolinuxd>) you will get the new smb.conf.

All you need to do is enable it.
    
    
    sudo systemctl enable winbind.service

 

More info about [Active Directory](<https://wiki.archlinux.org/index.php/Active_Directory_Integration>) and [winbind](<https://wiki.archlinux.org/index.php/samba>) here or from [samba.org](<https://www.samba.org/samba/docs/current/man-html/winbindd.8.html>).

Video: <https://youtu.be/LVkkEHMNsY0>
