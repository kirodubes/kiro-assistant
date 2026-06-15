---
title: "Updating your system with skel and still keeping your own settings"
url: https://arcolinux.com/updating-your-system-with-skel-and-still-keeping-your-own-settings/
date: 2020-03-10 14:30:50
type: post
categories: ["Cleanup", "Must read", "System settings", "Tips", "Update"]
tags: ["skel"]
source_site: arcolinux.com
---

# Updating your system with skel and still keeping your own settings

"SKEL" CAN BE A BLESSING OR A CURSE

When a **Linux** system is **installed** all the files and folders located in the folder **/etc/skel will be transferred to the home directory of the user**.

**Skel** stands for skeleton.

It is the developers intention that you have these files and folders. That is for example very important for **Tiling** **Window Managers (TWM)**. Without the configuration files of a TWM nothing would work.

### But what if you stay rolling?   
Meaning: you do not do a clean install.

The updates will be installed in**/etc/skel** and these updates are **invisible** for the user and will **never** be **used** by the system.

As a rule we do not write in your home directory.

In order to have the latest configurations we used to **manually** copy all files/folders from /etc/skel to your home directory.

Since this is quite **tedious** we created an alias.

> The alias called skel was created

Typing "**skel** " in the terminal results in :

  * a backup of your current .config folder to save your settings
  * copy all the files/folders from /etc/skel to your home directory
  * only files that exist in /etc/skel will be overwritten in your home directory



> **"Skel"** has been created for **developers** and **betatesters**.

It is a quick and easy way to copy the new configurations we need in order to try them out.

**Before** we had the alias skel, we actually compared folders with the application **Meld**.

> You can do a skel once a week or once a month or **never**.

 

# How to quickly restore your settings after a skel?

Set the computer the way you want.

Then go to your **.config** folder and also **.local** folder and just make a **copy** of these two.  
Then do a **skel**.  
Then compare your .config and .config copy with each other with **Meld**.

This does not take very long and you learn the code in this manner.

Watch the video to analyze the new code coming in.

SKEL became a script in May 2022

Video: <https://youtu.be/j-p_m03K0tQ>

Video: <https://youtu.be/R2tQ2tjQX8M>

Still not clear?

Here is the Playlist of skel on Youtube

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS5YJwFj0rBgwPWibQDqWXAx>
