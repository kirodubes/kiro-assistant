---
title: "4 Downloading the ISO and setting up virtual box"
url: https://www.arcolinuxd.com/4-downloading-the-ISO-and-setting-up-virtual-box/
date: 2021-01-16 10:15:21
type: post
categories: ["ArchWayStart"]
tags: ["archlinux"]
source_site: arcolinuxd.com
---

# 4 Downloading the ISO and setting up virtual box

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-ISO-download.jpg)

We use our standard torrent application Qbittorrent or Transmission or Ktorrent to download the ISO of Arch Linux.

Each month there will be a new release. It is only to keep the updates to a minimum.

You will install a minimal base installation and build everything up from there.

<https://www.archlinux.org/download/>

We will also set up our VirtualBox. So I can make my articles and youtube tutorials.

[If you have followed one of these articles](<https://arcolinux.com/category/arcolinux/applications/virtual-machines/>) you will have Virtual Box or an other virtual machine installed by now. You can ofcourse install Arch Linux on an SSD or harddisk. You can use **Mintstick** on ArcoLinux to burn the Arch Linux ISO on an usb. You can also use **Etcher** to burn an ISO to the usb. [More info about burning an ISO to a usb can be found here.](<https://arcolinux.com/everything-you-need-to-know-about-burning-an-ISO-to-usb/>)

If you decide to try it out first on virtual box than this is the most important setting.

Tell virtualbox to use **EFI or UEFI** with the tick "**Enable EFI (special OSes only)** ".

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/virtualbox-efi.jpg)

Video: <https://youtu.be/HY1cW-OaA-Y>

This is an **EFI** boot screen.

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/uefi-boot.jpg)

When installing on **VirtualBox with MBR or BIOS** then you keep the setting of **Enable EFI** ticked **off**. 

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-virtualbox-mbr.jpg)

This is an MBR bootscreen.

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-mbr-bootscreen.jpg)
