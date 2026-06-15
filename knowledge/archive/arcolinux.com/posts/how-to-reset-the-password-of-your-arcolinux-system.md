---
title: "How to reset the password of your ArcoLinux system"
url: https://arcolinux.com/how-to-reset-the-password-of-your-arcolinux-system/
date: 2018-06-29 17:09:31
type: post
categories: ["Fixes"]
tags: ["update"]
source_site: arcolinux.com
---

# How to reset the password of your ArcoLinux system

![](https://arcolinux.com/wp-content/uploads/2018/06/reset-password.jpg) We get all the information from the Arch wiki. <https://wiki.archlinux.org/index.php/reset_root_password> **Procedure**

  * boot from the ArcoLinux iso
  * mount your root partition
  * change password
  * unmount

Commands used in the video 
    
    
    lsblk
    sudo mount /dev/sda2 /mnt
    sudo passwd --root erik
    sudo passwd --root root
    sudo umount --all

Video: <https://www.youtube.com/watch?v=BDU7RnL_t1U>
