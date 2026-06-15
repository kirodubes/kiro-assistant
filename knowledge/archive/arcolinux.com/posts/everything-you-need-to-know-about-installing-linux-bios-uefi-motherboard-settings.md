---
title: "Everything you need to know about installing linux - bios uefi motherboard settings"
url: https://arcolinux.com/everything-you-need-to-know-about-installing-linux-bios-uefi-motherboard-settings/
date: 2019-12-28 12:16:36
type: post
categories: ["Pre-installation"]
source_site: arcolinux.com
---

# Everything you need to know about installing linux - bios uefi motherboard settings

![](https://arcolinux.com/wp-content/uploads/2021/01/bios.jpg)![](https://arcolinux.com/wp-content/uploads/2021/01/uefi.jpg)

BIOS  
OLDER PCS

UEFI  
NEWER PCS

basic input output system

unified extensible firmware interface

runs first at boot

runs first at boot

legacy/older

newer

most computers support both BIOS and UEFI mode

you may need to update the firmware

It checks to see what hardware components the computer has, wakes the components up and hands them over to the operating system. **UEFI addresses several limitations of BIOS** , including restrictions on **hard disk partition size** and CPU independent architecture and drivers.

Because UEFI is programmable, original equipment manufacturer (OEM) developers can add applications and drivers, allowing UEFI to function as a lightweight operating system.

The specification is most often pronounced by naming the letters U-E-F-I.

 

take care of the preliminaries

go into your firmware

Many computers display (sometimes rather quickly) how to open up the BIOS or SETTINGS or Enter Setup or ...

It is generally necessary to press a key during PC startup like F8 or F10 or Delete or ...

Make sure that **Quickboot/Fastboot** is **disabled**.  
Make sure that Intel Smart Response Technology (**SRT**) is **disabled**.  
Make sure that OS Type of**Secure Boot** is set to Other OS or disable it entirely.  
Make sure you can boot from the USB first.

Recent computers let you setup your computer to boot either in UEFI mode or in BIOS/CSM/LEGACY mode. Some computers will use the term "Compatibility Support Module" rather than CSM.  
**Choose legacy mode**.  
You can now choose to boot up with BIOS or UEFI.

Sometimes the bootloader works better with BIOS than with UEFI. You will have to test that on your hardware.

If you are installing ArcoLinux as the sole OS on a computer, either mode is likely to work. Again test out on your hardware.

what mode to choose  
bios or uefi

If you are dual-booting with Windows (W8 or later) the two OSs' boot modes should match. This configuration dictates the use of **UEFI** mode when installing ArcoLinux with Windows.

Some hardware just works better with one mode or the other. Usually BIOS is better supported. It has been around longer. This is becoming less common. UEFI is the successor of BIOS.

Sometimes the bootloader works better with BIOS then with UEFI. You will have to test that on your hardware.

If you are installing ArcoLinux as the sole OS on a computer, either mode is likely to work. Again test out on your hardware.

having troubles booting or installing

You can boot up ArcoLinux with BIOS or UEFI, if legacy mode is enabled on your computer. The choice is yours. Choose the correct line when you boot from your usb.  
Choose BIOS when UEFI was unsuccessful.

BIOS  
OLDER PCS

![](https://arcolinux.com/wp-content/uploads/2021/01/grub-arcolinux.png)

UEFI  
NEWER PCS

![](https://arcolinux.com/wp-content/uploads/2021/01/uefi-arcolinux.png)

calamares will take care of the partitioning

it will create an EFI system partition if required

But if you are manually partitioning your disk in the Calamares installer, you need to make sure you have an EFI system partition or ESP set up. This partition holds EFI-mode boot loaders and related files.

If your disk already contains an ESP (Windows is installed), it can be used for ArcoLinux too. Do not format it. It is best to have 1 ESP per disk.

You can create a partition with calamares.

  1. mount point : /boot/efi
  2. size : 500MB is more then enough
  3. type : FAT32
  4. needs a BOOT flag



identifying if ArcoLinux has been installed in UEFI

Open up your **/etc/fstab** with an editor. If it contains a line to the /boot/efi mountpoint, you have installed ArcoLinux with UEFI.

You can copy/paste this line in your terminal as well.
    
    
    [ -d /sys/firmware/efi ] && echo "Installed in UEFI mode" || echo "Installed in Legacy mode"

[LOTS OF VIDEOS HAVE BEEN CREATED](<https://arcolinux.com/bios-uefi/>)  
[ ABOUT SETTING YOUR FIRMWARE](<https://arcolinux.com/bios-uefi/>)  
[ FOR LINUX](<https://arcolinux.com/bios-uefi/>)
