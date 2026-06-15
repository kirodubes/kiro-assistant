---
title: "All in one Arch Linux installation Uefi, Ext4, Efistub, Sddm and Plasma"
url: https://www.arcolinuxd.com/all-in-one-arch-linux-installation-uefi-ext4-efistub-sddm-and-plasma/
date: 2024-03-23 11:04:13
type: post
categories: ["ArchWayAllinone", "ArchWayDesktop"]
source_site: arcolinuxd.com
---

# All in one Arch Linux installation Uefi, Ext4, Efistub, Sddm and Plasma

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-plasma.jpg)

This video serves as a comprehensive tutorial on installing Arch Linux, specifically focusing on the "Arch Linux way" during Phase 7 of the Arcolinux University series. It highlights the complexities newcomers might face, such as dealing with a black screen upon first booting into Linux, and guides viewers through overcoming these challenges.

Key Points:

  1. **Boot Loaders** : The tutorial discusses different boot loaders suitable for old and new computers, including GRUB, Refind, Systemd-boot, and introduces **EfiStub** as a fourth option, specifically for new computers with **UEFI** firmware. This segment emphasizes the importance of choosing the appropriate boot loader based on the computer's hardware and firmware capabilities.
  2. **Installation Guide** : The instructor walks through the installation process, from downloading the Arch ISO to configuring the system. This includes: 
     * Preparing the disk with GPT and creating partitions (EFI and root).
     * Formatting the partitions and setting up the file system.
     * Mounting the root filesystem and EFI partition correctly, with detailed instructions on ensuring the ESP (EFI System Partition) is mounted to `/boot` for direct kernel updates by Pacman.
  3. **System Configuration** : Various system configurations are addressed, such as setting the timezone, locale, hostname, and enabling Network Manager for internet connectivity. Additionally, the tutorial covers setting up a root password and creating a new user with sudo privileges.
  4. **Boot Loader Installation** : The tutorial provides a step-by-step guide on setting up **EFISTUB** as the boot loader, including creating boot entries using the EFI Boot Manager. It emphasizes the criticality of correctly entering commands to avoid boot issues.
  5. **Troubleshooting** : A segment is dedicated to troubleshooting and fixing boot issues, highlighting the importance of precise command execution and how to recover from errors by remounting partitions and chrooting into the installation.
  6. **Graphical Environment Setup** : Lastly, the tutorial covers the installation of a graphical environment (Plasma Desktop) on the newly installed Arch system, showcasing how to install additional software and manage system settings for a user-friendly experience.



The video concludes with the successful installation of Arch Linux using the EFI Stub method, demonstrating the boot process and the operational Plasma Desktop environment. This tutorial is intended for users familiar with Linux basics but new to the Arch Linux installation process, providing them with the knowledge to install Arch Linux confidently.

Video: <https://youtu.be/NC6ee_A-90k>
