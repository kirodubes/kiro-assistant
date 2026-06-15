---
title: "Lets talk about Grub"
url: https://arcolinux.com/lets-talk-about-grub/
date: 2024-04-22 03:45:17
type: post
categories: ["Bootloader"]
source_site: arcolinux.com
---

# Lets talk about Grub

![](https://arcolinux.com/wp-content/uploads/2024/04/grub.png)

This video tutorial focuses on configuring the GRUB bootloader on Linux systems, specifically on how to manage boot options and the default kernel selection using GRUB settings. The presenter starts by discussing the GRUB menu, highlighting the use of the 'e' key to modify boot options and the advanced options available.

The tutorial covers the use of GRUB Customizer, a tool with mixed reviews—some recommend it for simplifying GRUB configurations, while others prefer manual adjustments. The presenter opts to demonstrate the manual process, emphasizing the educational value in understanding how GRUB works.

Key points of the tutorial include navigating to the `/etc/default/grub` file, where kernel boot priorities are set. The video explains the importance of numbering in GRUB, where entries start at zero. The presenter shows how to adjust settings to make a non-default kernel (like the Linux Zen kernel) the default by changing the entry order and removing submenus to simplify the boot process.

The process concludes with instructions on updating GRUB configurations using the `**update-grub** ` command and verifying changes by rebooting. The presenter reassures that these modifications allow for control over which kernel boots by default while retaining other kernels as options.

Video: <https://youtu.be/AwqRwQYgoZA>
