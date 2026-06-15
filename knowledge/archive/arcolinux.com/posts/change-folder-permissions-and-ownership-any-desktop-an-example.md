---
title: "Change folder permissions and ownership any desktop - an example"
url: https://arcolinux.com/change-folder-permissions-and-ownership-any-desktop-an-example/
date: 2018-01-21 14:44:32
type: post
categories: ["Fixes"]
tags: ["anydesktop", "fix"]
source_site: arcolinux.com
---

# Change folder permissions and ownership any desktop - an example

![](https://arcolinux.com/wp-content/uploads/2018/01/change-ownership-and-permissions.jpg)   


Sometimes you have these harddisks or ssd lying around with data. Then you connect them with your current linux distribution and you can not access them.

Often the harddisk does not get mounted automatically. In **ArcoLinux** it has been set to **automount** any connected device. One of the applications I use when investigating harddisks is **gnome-disks**. If your harddisk is not mounted, see if that application can help. **Gparted** can give you also some insight about your harddisk.

If your harddisk is **mounted** , it is sometimes mounted "**read-only"**. You do not have permission to change, delete or add anything.

I had this issue now and thought I show you how I fix this.

Two commands to use and remember are **chmod and chown.**

**Let us investigate together and see what commands I use to fix the issue.**

Video: <https://www.youtube.com/watch?v=SxIjsmuwCdE>

  


We have used the following commands
    
    
    chown -R erik:erik Data
    chmod 755 ... for the folder Muziek Erik 1

**Need more info?**  
Google for these words "linux how to change ownership and permissions"
