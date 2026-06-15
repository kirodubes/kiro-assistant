---
title: "Update your system using pamac"
url: https://arcolinux.com/update-your-system-using-pamac/
date: 2017-09-28 18:16:14
type: post
categories: ["Pamac", "Update"]
tags: ["pamac", "software", "update"]
source_site: arcolinux.com
---

# Update your system using pamac

**This applies to all desktop environments.** **Pamac** is our standard updater in ArcoLinux. You can update your system also in the terminal. That is for another article. Pamac provides us a **tray-icon** (assuming you did not change the icon theme) that is **white**. This means that your system is **up-to-date**. When the pamac icon turns **red** , it means you can do **updates**. There is no must to do it straight away. You can do that when you shutdown. Always take a look at the names that are in the list. You need to learn these names. By following this up, you will learn package by package, what is installed on ArcoLinux and you will understand why we install packages in [phase 2](<https://arcolinux.com/tutorials/>). Oktober 2017 we are using version 6. It gives us as an overview of all **possible** **packages** you can install. You can check there what software is coming from the **ArcoLinux** **repositories**. A repository is a place on the net, where the Arch packages/software are kept. You can then install them from there. The video will show you the old ArchMerge repo's. 

Video: <https://www.youtube.com/watch?v=ZQJPFIOq3PA>

## These are the ArcoLinx repositories:

 
    
    
    #[arcolinux_repo_testing]
    #SigLevel = Required DatabaseOptional
    #Server = https://arcolinux.github.io/arcolinux_repo_testing/$arch
    
    [arcolinux_repo]
    SigLevel = Required DatabaseOptional
    Server = https://arcolinux.github.io/arcolinux_repo/$arch
