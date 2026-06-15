---
title: "arch-chroot and btrfs - use the power of arch-chroot when your computer crashes"
url: https://www.arcolinuxd.com/arch-chroot-and-btrfs-use-the-power-of-arch-chroot-when-your-computer-crashes/
date: 2024-03-23 16:04:07
type: post
categories: ["arch-chroot", "ArchWayUtils"]
source_site: arcolinuxd.com
---

# arch-chroot and btrfs - use the power of arch-chroot when your computer crashes

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/btrfs-xl-vol.jpg)

> <https://wiki.archlinux.org/title/Chroot#Running_on_Btrfs>

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-chroot-btrfs.png)

ArcoLinux, based on Arch Linux, offers a rolling release system with the advanced filesystem, Btrfs. This setup provides snapshots, rollbacks, and efficient disk management. However, system issues may arise from failed updates or misconfigurations. This guide explains how to access and repair your system using `arch-chroot` and Btrfs subvolumes, without direct code snippets for easier WordPress formatting.

## Prerequisites

  * A bootable **ArchLinux** media (USB/CD).
  * A basic understanding of the Linux command line.



## Step 1: Identify Your Disk Partitions

Start by booting from the ArcoLinux media and opening a terminal. Use the `lsblk` command to list all block devices, focusing on the root partition, typically `/dev/sda2` on a single-disk system.

## Step 2: Mount Btrfs Subvolumes

Btrfs's subvolumes feature allows for accessible and manageable filesystem parts. The mounting process is essential for system repair and involves several steps:

  1. **Mount the root subvolume** : Begin with the root subvolume, usually identified with an `@` symbol.
  2. **Mount other subvolumes** : Continue by mounting additional subvolumes like `@root`, `@home`, `@log`, `@cache`, `@tmp`, and `@srv` at their respective directories within `/mnt`. This approach reflects your system's structure for the `arch-chroot` operation.
  3. **Mount the EFI system partition** : This is crucial for EFI systems, typically involving the partition `/dev/sda1`.



Each mounting step involves specifying the device and the mount point, tailored to your system's setup.

## Step 3: Accessing the System with arch-chroot

With the subvolumes properly mounted, use `arch-chroot` to access your system in a chroot environment. This command shifts you into your system's root environment, enabling repairs, updates, or configuration changes as if directly booted into it.

## Repairing Your System

Inside the chroot environment, you can perform various system repairs:

  * **Update the system** : Run the system update command to ensure all packages are current.
  * **Reinstall the bootloader** : For EFI systems, reinstalling the bootloader may be necessary. This involves specifying the target, EFI directory, and bootloader ID.
  * **Troubleshoot and modify configurations** : This may include editing system files like `/etc/fstab` or others, according to the issues faced.



## Conclusion

This guide provides a structured method for recovering an ArcoLinux system using `arch-chroot` and Btrfs subvolumes. By following these steps, most boot issues can be addressed efficiently, minimizing data loss. Regular backups are recommended to aid in recovery from irreversible damage.

## Practice
    
    
    lsblk
    
    mount /dev/sda2 /mnt -o subvol=@
    mount /dev/sda2 /mnt/root -o subvol=@root
    mount /dev/sda2 /mnt/home -o subvol=@home
    mount /dev/sda2 /mnt/var/log -o subvol=@log
    mount /dev/sda2 /mnt/var/cache -o subvol=@cache
    mount /dev/sda2 /mnt/var/tmp -o subvol=@tmp
    mount /dev/sda2 /mnt/srv -o subvol=@srv
    
    mount /dev/sda1 /mnt/boot/efi
    
    arch-chroot /mnt
    

Video: <https://youtu.be/xSaG307pnTE>
