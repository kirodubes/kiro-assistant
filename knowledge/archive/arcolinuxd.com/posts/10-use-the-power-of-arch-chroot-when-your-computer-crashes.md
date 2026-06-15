---
title: "arch-chroot and ext4 - use the power of arch-chroot when your computer crashes"
url: https://www.arcolinuxd.com/10-use-the-power-of-arch-chroot-when-your-computer-crashes/
date: 2022-02-26 16:00:39
type: post
categories: ["arch-chroot", "ArchWayUtils", "Fixes"]
tags: ["archlinux", "help"]
source_site: arcolinuxd.com
---

# arch-chroot and ext4 - use the power of arch-chroot when your computer crashes

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-arch-chroot.jpg)

Changing root is commonly done for performing system maintenance on systems where booting and/or logging in is no longer possible. Common examples are:

  * Reinstalling the [bootloader](<https://wiki.archlinux.org/index.php/Bootloader> "Bootloader").
  * Rebuilding the [initramfs image](<https://wiki.archlinux.org/index.php/Mkinitcpio> "Mkinitcpio").
  * Upgrading or [downgrading packages](<https://wiki.archlinux.org/index.php/Downgrading_packages> "Downgrading packages").
  * Resetting a [forgotten password](<https://wiki.archlinux.org/index.php/Password_recovery> "Password recovery").
  * or just when you broke your system and can no longer boot.



Then we mount the partitions we need and undo whatever broke your system.

Get yourself the latest Arch Linux ISO

or ArcoLinux

and keep it around

These commands will be used IF

  * you installed ArcoLinux with UEFI 
  * you installed [Arch Linux with UEFI](<https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-uefi/>)


    
    
    loadkeys be-latin1

or you use **setxbmap** and the keyboard
    
    
    setxkbmap be
    
    
    mount /dev/sda3 /mnt
    
    
    mount /dev/sda1 /mnt/boot/efi
    
    
    arch-chroot /mnt

You can add **swapon /dev/sda2** but I rarely do out of laziness and there is no issue.

Then you are in your actual computer - install, uninstall, change configs and repair your computer.

Video: <https://youtu.be/zkGzNVV4l7Q>

BIOS

These commands will be used IF

  * you installed ArcoLinux with BIOS
  * you installed [Arch Linux with BIOS](<https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-bios/>)

![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/archlinux-mount.jpg)
    
    
    loadkeys be-latin1

or you use **setxbmap** and the language
    
    
    setxkbmap be
    
    
    mount /dev/sda1 /mnt
    
    
    arch-chroot /mnt

You can add **swapon /dev/sda2** but I rarely do out of laziness and there is no issue.

Then you are in your actual computer - install, uninstall, change configs and repair your computer.

WHAT IF ...

If you did something completely different, you will need to analyze what are your partitions.

Use **lsblk** for that.

Let us analyze the following partitioning.

![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/lsblk.png)
    
    
    loadkeys be-latin1

or you use **setxbmap** and the keyboard
    
    
    setxkbmap be
    
    
    mount /dev/sda2 /mnt
    
    
    mount /dev/sda1 /mnt/boot/efi
    
    
    arch-chroot /mnt

You can add **swapon /dev/sda3** but I rarely do out of laziness and there is no issue.

How to fix a kernel not booting or is it the grub?

Video: <https://youtu.be/oK8k0hAqyiU>

PUT your data on an USB stick  
or external harddisk

Video: <https://youtu.be/GiCaBVsq0hU>

/boot/vmlinuz-linux can not be found

Solution : reinstall the kernel - update-grub
    
    
    sudo su (no password if you use ArcoLinux ISO to become root)

Video: <https://youtu.be/CC9Www6sgDM>

Blinking cursor in the top left and black background

patient : ArcoLinuxB Plasma

We check all elements. Where can it can go wrong? In what phase of the [boot process](<https://wiki.archlinux.org/index.php/Arch_boot_process>)?

  * linux kernel - other kernels
  * amd-ucode or intel-ucode
  * grub
  * nvidia
  * rip in the terminal to see the last updates
  * what did you do?



You need to think back and **analyze** what can be the reason.

Here the solution was one simple line.
    
    
    sudo systemctl enable sddm -f

That was the solution IN MY CASE. **Lightdm** is not working then we switch to **sddm** and wait for the updates.

It is all about trial and error.

Video: <https://youtu.be/s9MZcVGPl24>

> May these images help you analyze your issue

Fixing an installation of a "bad self-build" linux kernel

/boot/vmlinuz-linux not found

/boot/vmlinuz-linux-lts not found

/boot/vmlinuz-linux-zen not found

/boot/vmlinuz-linux-hardened not found

Video: <https://youtu.be/22s4E00Ct1c>

ALL YOUTUBE VIDEOS ABOUT ARCH-CHROOT

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS5a1nMSuPJS0MDslM1zLCEd>
