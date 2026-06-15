---
title: "How to fix one or more pgp signatures could not be verified libc++ and discord by adding a new repo"
url: https://arcolinux.com/how-to-fix-one-or-more-pgp-signatures-could-not-be-verified-libc-and-discord-by-adding-a-new-repo/
date: 2018-07-11 14:26:39
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to fix one or more pgp signatures could not be verified libc++ and discord by adding a new repo

![](https://arcolinux.com/wp-content/uploads/2018/07/arcolinux-repo-3party.jpg)

Add the repo and install discord in 30 seconds rather than 30 minutes.

**Only** the people that had **discord** installed before the update of libc++ will see this error. We are 11th July 2018. You will see no errors if you install discord after that date.

Discord is our communication channel between users and ArcoLinux team members and you are welcome to join our channel @ <https://discord.gg/R2amEEz>.

[In this article](<https://arcolinux.com/how-to-fix-one-or-more-pgp-signatures-could-not-be-verified-libc-and-discord/>) we told you to get a public key to be able to **build** and install the libc++ updates.

Then you can build the 3 packages required for discord but "it takes a while" to build these packages.

"Looking forward" to building these packages on all our computers we have opted to start with a **new repo** **to avoid these long builds** for this update of libc++ and for all future applications that "take the fun out of computing".

Add these lines to the bottom of your /etc/pacman.conf
    
    
    [arcolinux_repo_3party]
    SigLevel = Required DatabaseOptional
    Server = https://arcolinux.github.io/arcolinux_repo_3party/$arch

As the name suggests this is for all applications that are coming from **third parties**.

Nothing to do with ArcoLinux.

As of ArcoLinux version 6.9.1 or July 2018 this repo is standard present.

Video: <https://www.youtube.com/watch?v=g3mlXW2qGrM>
