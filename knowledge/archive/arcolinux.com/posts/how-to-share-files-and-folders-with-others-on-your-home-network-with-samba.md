---
title: "How to share files and folders with others on your home network with Samba"
url: https://arcolinux.com/how-to-share-files-and-folders-with-others-on-your-home-network-with-samba/
date: 2018-06-21 18:10:53
type: post
categories: ["Post-installation", "Samba", "Utilities", "Virtual Machines"]
tags: ["samba"]
source_site: arcolinux.com
---

# How to share files and folders with others on your home network with Samba

![](https://arcolinux.com/wp-content/uploads/2018/06/samba2.png)

In the context of this tutorial we use Samba if we want to **share** **files** and **folders** with other computers in our **private** network.

One computer becomes the **Samba** **Server**. It will give the **service** to **share data on that computer** with others on the network.

Samba is already **activated** on **ArcoLinux** and **ArcoLinuxB**. But not on ArcoLinuxD until you run the scripts.

As a consequence any computer with ArcoLinux **CAN BECOME** a Samba Server.

> This **short** and **quick** **procedure** will change your computer into a Samba Server.

**Goals**

  * It is the aim of this article to be **NON** **technical**
  * It is the aim of this article to provide an **easy** procedure
  * Created for people at **home** wanting to share data between computers
  * One folder is created for all purposes with **read** **and** **write** **access**
  * Give one person access to the folder with password
  * We do **not** make a new user account for Samba



# Procedure on Your SAMBA SERVER

  1. Create a directory in your home directory with the name "**SHARED** "
  2. Delete all the **semi-colons** at bottom of /etc/samba/**smb.conf**
  3. Add yourself as user to Samba and set a password for access (change username)


    
    
    sudo smbpasswd -a erik

In case you need to restart Samba for some reason then this is the command:
    
    
    sudo systemctl restart smb.service nmb.service

# Video setup

**ArcoLinuxB** **Plasma** is becoming the **Samba** **Server**.

**ArcoLinux** on Vmware is a **desktop** connection to **get** the **files** from the Samba Server aka ArcoLinuxB Plasma.

Video: <https://www.youtube.com/watch?v=uxSf8W_t890>

More technical info can be found [on the Arch wiki](<https://wiki.archlinux.org/index.php/samba>).

## More information about the **setup in the video**.

[I had just completed this article](<https://arcolinux.com/how-to-share-files-and-folders-between-guest-and-host-on-vmware/>) on how to share a folder on the host computer with the guest computer on vmware (without samba). As a result I had this virtual machine of ArcoLinux standing by. If you want to be able to share with your whole network from within the operating system running on vmware you need to choose for a **bridged** network connection.

![](https://arcolinux.com/wp-content/uploads/2018/06/ArcoLinuxB-Plasma_vmware-bridged.png)
