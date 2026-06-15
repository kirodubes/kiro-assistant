---
title: "Lets talk about systemd-boot"
url: https://arcolinux.com/lets-talk-about-systemd-boot/
date: 2024-04-22 03:46:09
type: post
categories: ["Bootloader"]
source_site: arcolinux.com
---

# Lets talk about systemd-boot

![](https://arcolinux.com/wp-content/uploads/2024/04/systemd-boot.png)

The video is a tutorial on how to change the default boot kernel in a Systemd-boot enabled system. The presenter demonstrates how to switch from the Zen kernel, which is currently the default, to the regular Arch Linux kernel. The process involves using the `bootctl` command to manage and control the boot settings.

Initially, the presenter shows that the desired change cannot be accomplished using the simple 'TAB TAB' method due to security restrictions on the EFI boot partition. To overcome this, the presenter gains root access using the `su` command, bypassing the need to use `sudo`. Once root access is secured, the command `**bootctl set-default** ` is used to set the desired kernel as the default boot option.

The tutorial highlights the importance of understanding and navigating system security settings to make changes effectively. It also emphasizes the need to be familiar with system commands and the filesystem structure, particularly the boot partition. The video concludes by showing the system rebooting with the newly set default kernel, verifying that the change has been successfully applied.

Video: <https://youtu.be/53wWWA3x5Hs>
