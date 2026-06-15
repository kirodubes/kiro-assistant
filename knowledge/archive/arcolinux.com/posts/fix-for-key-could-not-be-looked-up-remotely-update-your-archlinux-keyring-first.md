---
title: "Fix for key could not be looked up remotely - update your archlinux-keyring first"
url: https://arcolinux.com/fix-for-key-could-not-be-looked-up-remotely-update-your-archlinux-keyring-first/
date: 2018-01-13 08:05:54
type: post
categories: ["Fixes", "Update"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fix for key could not be looked up remotely - update your archlinux-keyring first

![](https://arcolinux.com/wp-content/uploads/2018/01/key-could-not-be-looked-up-remotely.jpg)   


UPDATE  
archlinux-keyring first  
then the rest

If there are **keys** that give an **error** when updating, you should first check if there is a new **archlinux-keyring**.

January 2018 it was this key but it can be any other in the future : **CEB167EFB5722BD6**

If there is no update then you check out this [article](<https://arcolinux.com/fix-for-key-could-not-be-looked-up-remotely/>).

If there is an **update** availabe for archlinux-keyring, then update that one first with and then the rest.
    
    
    sudo pacman -Su archlinux-keyring

Read more about this keyring on the wiki.  
<https://wiki.archlinux.org/index.php/Pacman/Package_signing>

Video: <https://youtu.be/M5cpRBuBrkU>

  


A few days later.... when you do now a clean install of ArchMerge 6.3.1 you will get the question to add the missing key from **Eli Schwartz** to your system and you will be able to update without issues.

![](https://arcolinux.com/wp-content/uploads/2018/01/keyupdate.jpg)
