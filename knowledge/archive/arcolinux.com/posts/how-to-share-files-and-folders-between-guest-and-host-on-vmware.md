---
title: "How to share files and folders between guest and host on vmware"
url: https://arcolinux.com/how-to-share-files-and-folders-between-guest-and-host-on-vmware/
date: 2018-06-21 14:52:21
type: post
categories: ["Virtual Machines"]
tags: ["virtual machines"]
source_site: arcolinux.com
---

# How to share files and folders between guest and host on vmware

![](https://arcolinux.com/wp-content/uploads/2018/06/ArcoLinuxB-Plasma_vmware-share-public.jpg)   


Like in [Virtualbox](<https://arcolinux.com/how-to-install-virtualbox-from-a-till-z/> "https://arcolinux.com/how-to-install-virtualbox-from-a-till-z/") we can also have the need to share files and folders between the host system (in video plasma) and the guest system (in video arcolinux).

Alternatives are usb’s and cloud services.

We have already installed vmware [following this article](<https://arcolinux.com/how-to-install-the-latest-vmware-workstation-on-arcolinux/>).

And we have already installed ArcoLinux in this vmware machine [following this article](<https://arcolinux.com/installing-arcolinux-on-the-latest-vmware-workstation-on-arcolinux/>).

**Host** is the operating system (OS) that is running on your computer.

**Guest** is the OS that is running inside virtualbox.

# **Procedure**

  1. Share **Public** folder in the settings of vmware - point to Public folder on your host
  2. Install **open-vm-tools** inside the guest OS
  3. mount the shared folder with this command inside the guest OS


    
    
    sudo vmhgfs-fuse -o allow_other -o auto_unmount .host:/Public /home/$USER/Public

You are ready to test it out.

Video: <https://youtu.be/-vqM8eVnWDo>

  


More information can be found on the [Arch wiki](<https://wiki.archlinux.org/index.php/VMware>).
