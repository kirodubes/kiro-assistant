---
title: "Fix your ArcoLinux or Arch Linux computer with these 2 tips"
url: https://arcolinux.com/fix-your-arcolinux-or-arch-linux-computer-with-these-2-tips/
date: 2020-08-19 10:13:05
type: post
categories: ["Fixes", "Lightdm", "Update"]
tags: ["fix", "update"]
source_site: arcolinux.com
---

# Fix your ArcoLinux or Arch Linux computer with these 2 tips

We refer you also to our arch-chroot information in this website.

<https://www.arcolinuxd.com/arch-linux-utils/>

There we also cover BTRFS.

![](https://arcolinux.com/wp-content/uploads/2019/01/tty2-fix.jpg)

If you recognize these symptoms then this article can help you : 

  * black screen at bootup
  * bootup starts but halts
  * bootup starts but halts and you see why - error message
  * lightdm shows but is unresponsive
  * lightdm shows - desktop is unreachable
  * ...



# Solution 1

When your system crashes, you might still be able to go into a **TTY**.   **CTRL + ALT + F2, F3, F4, F5 and F6** **Virtualbox : RIGHT-CTRL +F2, F3, F4, F5 and F6**

> TTY = TeleTYpewriter

Then **retrace your steps.**

Did you install something wrong? Did you change the config? Do you need to update or downgrade?

Use the alias **rip** to see what you installed last.

# Solution 2

Use the power of **arch-chroot.**

If you can not use TTY to change your computer, this will be your last resort procedure.

It will get you back up and running. [Tutorial is here](<https://arcolinuxd.com/10-use-the-power-of-arch-chroot-when-your-computer-crashes>).

Video: <https://www.youtube.com/watch?v=PJqq9tFCmQM>
