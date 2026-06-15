---
title: "Setting the bios in HP Pavilion HPE-315be"
url: https://arcolinux.com/setting-the-bios-in-hp-pavilion-hpe-315be/
date: 2018-04-28 20:30:51
type: post
categories: ["Bios &amp; Uefi"]
tags: ["bios"]
source_site: arcolinux.com
---

# Setting the bios in HP Pavilion HPE-315be

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-bios-vritualization-technology.jpg)

We investigate how to get inside the bios of this HP computer. It might be a different in every computer. I think it is [this](<https://support.hp.com/us-en/product/hp-pavilion-elite-hpe-300-desktop-pc-series/4162190/model/4270211/drivers>) computer: HP Pavilion HPE-315be. It is an 8-9 year old computer. ArcoLinux works fine on it.

In our case **F10** is what we need to get into the **bios**.

We check 2 things:

  * can we boot from usb
  * is virtualization enabled to be able to have virtualbox later



You need to set the boot priority so it actually will boot from your usb. You can sometimes also call for a bootmenu to choose to boot from usb rather than harddisk. Once booted from usb you have full control over the system and can install arcolinux.

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-boot-device-priority.jpg)

Video: <https://youtu.be/kHkwHwL0db4>
