---
title: "EFISTUB as bootloader"
url: https://www.arcolinuxd.com/efistub-as-bootloader/
date: 2024-03-23 09:49:26
type: post
categories: ["Arch Way"]
source_site: arcolinuxd.com
---

# EFISTUB as bootloader

> <https://wiki.archlinux.org/title/EFISTUB>

EFI Stub is a method of booting a Linux system directly from the UEFI firmware without the need for an additional bootloader like GRUB or Systemd-boot. This method takes advantage of the UEFI boot manager, simplifying the boot process by loading the Linux kernel as an EFI executable. Here's a deeper dive into EFI Stub, including its prerequisites, advantages, disadvantages, and a code abstract for setting it up.

### Prerequisites

  1. **EFI System Partition (ESP) Mounted in /boot** : The ESP should be mounted directly to `/boot` rather than `/boot/EFI`. This configuration ensures that when Pacman updates the kernel, the EFI firmware can directly read these updates, as they are placed in the same partition where the UEFI boot manager expects bootloaders.
  2. **Installation of efibootmgr** : `efibootmgr` is a tool that allows you to interact with the UEFI firmware's boot manager from within Linux. It's necessary for creating new boot entries for EFI Stub. Make sure this tool is installed on your system to execute the EFI Stub setup commands.



### Advantages of Using EFI Stub

  1. **Simplicity** : By removing the need for a separate bootloader, the EFI Stub method simplifies the boot process. There are fewer components involved, which can reduce boot times and decrease the likelihood of boot-related issues.
  2. **Direct Kernel Updates** : With the ESP mounted in `/boot`, kernel updates applied by Pacman are immediately available for the UEFI firmware to read, streamlining the update process and ensuring that your system is always running the latest kernel version.
  3. **Enhanced Security** : EFI Stub allows for a more secure booting process, as it reduces the attack surface by eliminating additional software components that could be targeted by malicious actors.
  4. **Customization** : Advanced users can benefit from the high degree of customization that EFI Stub provides, allowing for tailored boot parameters and kernel options directly managed through the UEFI firmware.



### Disadvantages of Using EFI Stub

  1. **Complex Setup for Beginners** : The initial setup process can be more complex and less intuitive than traditional bootloader configurations, potentially posing a challenge for less experienced users.
  2. **Limited Multiboot Capability** : Users who need to dual-boot multiple operating systems might find EFI Stub less convenient, as managing multiple boot entries directly through the UEFI firmware is less user-friendly than using a graphical bootloader.
  3. **Troubleshooting Difficulty** : Troubleshooting boot issues can be more challenging without a traditional bootloader, as errors need to be diagnosed through UEFI firmware settings or by using external tools.



### Code Abstract for Setting Up EFI Stub

To set up EFI Stub, use the `efibootmgr` command with the necessary parameters to create a new UEFI boot entry. The command syntax is as follows:

bashCopy code

`efibootmgr --create --disk /dev/sdX --part Y --label "Arch Linux" --loader /vmlinuz-linux --unicode 'root=UUID=block_device_identifier rw initrd=\initramfs-linux.img'  
  
`

  * `/dev/sdX` and `Y` refer to the disk and partition number of the EFI System Partition, respectively.
  * `block_device_identifier` should be replaced with the UUID of the root (`/`) partition, which can be found in `/etc/fstab`.



This command effectively registers the Linux kernel itself as a bootable EFI application with the UEFI firmware, allowing the system to boot directly into Linux without an intermediate bootloader.

Code example
    
    
    efibootmgr -c -d _/dev/sda_ -p 1 -L "Arch Linux" -l /vmlinuz-linux -u 'root=_block_device_identifier_ rw initrd=\initramfs-linux.img'

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/code-efistub.png)

Video: <https://youtu.be/NC6ee_A-90k?t=1684>

More resources:

  * [gentoo](<https://wiki.gentoo.org/wiki/Efibootmgr>)
  * [linuxconfig.org](<https://linuxconfig.org/how-to-manage-efi-boot-manager-entries-on-linux>)
  * [linuxbabe](<https://www.linuxbabe.com/command-line/how-to-use-linux-efibootmgr-examples>)
