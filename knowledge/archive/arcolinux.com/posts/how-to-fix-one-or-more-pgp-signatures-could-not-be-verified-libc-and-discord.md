---
title: "How to fix one or more pgp signatures could not be verified libc++ and discord"
url: https://arcolinux.com/how-to-fix-one-or-more-pgp-signatures-could-not-be-verified-libc-and-discord/
date: 2018-07-11 14:02:17
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to fix one or more pgp signatures could not be verified libc++ and discord

![](https://arcolinux.com/wp-content/uploads/2018/07/pgp-signatures.jpg)

**Only** the people that had **discord** installed before the update of libc++ will see this error. We are 11th July 2018. You will see no errors if you install discord after that date.

Discord is our communication channel between users and ArcoLinux team members and you are welcome to join our channel @ <https://discord.gg/R2amEEz>.

But forget about discord because it can happen to any application and here is the solution.

We need to download the key in order for the build to proceed.

Type this line in the terminal - the public key can be found in the error message.
    
    
    gpg --receive-keys A2C794A986419D8A

In an ideal world this would work. Personally I will have to do more because of firewalls, routers, internet service provider or something else.

I copy/paste the **gpg.conf** from **/etc/pacman.d/gnupg** to my own directory in **~/.gnupg** and add a keyserver to it. You can try out 4 versions to see which one works for you.

  1. keyserver hkp://pool.sks-keyservers.net
  2. keyserver hkp://pool.sks-keyservers.net:80
  3. keyserver hkps://hkps.pool.sks-keyservers.net:443
  4. keyserver hkp://ipv4.pool.sks-keyservers.net:11371



Last line was not shown in the video.  
Then you can try to receive the missing key again and build your application.

Video: <https://youtu.be/_ANJMBryemY>

Alternative way

You can use the AUR helper **yay** instead of trizen or yaourt.

**Yay will give you the possibility to import the keys automatically.**
    
    
    trizen yay
    yay discord

In an ideal world this would work. Personally I will have to do more because of firewalls, routers, internet service provider or something else.

I copy/paste the **gpg.conf** from **/etc/pacman.d/gnupg** to my own directory in **~/.gnupg** and add a keyserver to it. You can try out 4 versions to see which one works for you.

  1. keyserver hkp://pool.sks-keyservers.net
  2. keyserver hkp://pool.sks-keyservers.net:80
  3. keyserver hkps://hkps.pool.sks-keyservers.net:443
  4. keyserver hkp://ipv4.pool.sks-keyservers.net:11371



Then you can try to receive the missing key again and build your application.

![](https://arcolinux.com/wp-content/uploads/2018/07/keys-yay.png)

Another Alternative way

Use the scripts from ArcoLinuxD to add the keyservers to your system.

You will find it on any desktop. Here is the one from plasma.

<https://github.com/arcolinuxd/arco-xfce/tree/master/ArchWay>
