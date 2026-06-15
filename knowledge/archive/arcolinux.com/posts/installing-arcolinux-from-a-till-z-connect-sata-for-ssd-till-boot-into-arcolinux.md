---
title: "Installing ArcoLinux from A till Z - connect sata for SSD till boot into ArcoLinux"
url: https://arcolinux.com/installing-arcolinux-from-a-till-z-connect-sata-for-ssd-till-boot-into-arcolinux/
date: 2018-04-27 10:00:20
type: post
categories: ["Pre-installation"]
tags: ["bios"]
source_site: arcolinux.com
---

# Installing ArcoLinux from A till Z - connect sata for SSD till boot into ArcoLinux

![](https://arcolinux.com/wp-content/uploads/2018/04/motherboard-sata.jpg)In this video we show you what to do from A till Z. Let us assume you have also a Windows computer and you want to keep that one for work/gaming but you do want to try out Linux systems. The connections that go from the motherboard to your harddisk or sata need to be unplugged from the motherboard so it can not be found. You will not be able to overwrite or break your windows system. Then you need to have a spare sata cable (red one) or reuse one of the others and plugin the sata cable in a freshly bought ssd. Plugin also the powersupply in the sata. Then you are ready to boot. Every system has a different way to boot into the setup or bios or Uefi setup... whatever the name is... In my case I have to press F8. Other viable options are often F2, Escape and delete. ![](https://arcolinux.com/wp-content/uploads/2018/04/setup-boot.jpg)

 

We go first to the **setup** to check if the settings are ok for linux.

We are on an **Asus P8Z77-V LE** motherboard.

We need to check the following elements:

CPU configuration - **Intel Virtualization Technology** must be enabled to have Virtual Box or Vmware working on your system. 

![](https://arcolinux.com/wp-content/uploads/2018/04/intel-virtualization-technology.jpg)

CSM - Compatibility Support Module should be **enabled** and Boot device control is set to **UEFI and Legacy OpROM**

If you want to know more about csm and such then [here I found a great article.](<https://neosmart.net/wiki/enable-uefi-boot/>) I will copy/paste some of the paragraphs to be sure the information stays available. 

![](https://arcolinux.com/wp-content/uploads/2018/04/csm.jpg)

## What is Legacy Boot Mode

With newer Windows 8 PCs that are designed with UEFI support, the BIOS or firmware often has an option that specifies if the computer can boot into regular operating systems and recovery tools, or if it can boot exclusively into newer UEFI operating systems and environments. The regular way of booting into software and operating systems is called “Legacy Boot” and must sometimes be explicitly enabled/allowed in the BIOS settings. Legacy boot mode does not normally support partitions greater than 2TB in size, and can cause data loss or other problems if you try to use it normally.

## Enabling UEFI Boot Mode

On PCs and laptops from most manufacturers, including Dell, HP, Asus, Acer, Toshiba, Lenovo, and more, Legacy Boot can be disabled or turned off from the EFI setup/configuration feature, available immediately after turning on your PC. If legacy boot mode (also known as “CSM boot”) is enabled, UEFI boot mode is automatically disabled or de-prioritized.

Below are instructions for turning off Legacy Boot on most PCs and laptops, as well as specific instructions for certain brands of laptops. On most EFI computers, you’ll need to access EFI setup immediately after turning on your PC in order to see the option of enabling UEFI boot, usually as an option under the boot options section of the BIOS configuration.

### Entering the UEFI setup

Immediately after powering up your PC, as soon as the manufacturer logo (e.g. Dell, Lenovo, HP, Toshiba, Samsung, ASUS, Acer, Gateway, etc.) shows up on your BIOS splash screen, you will have the option of pressing a special key. **This key changes from PC to PC** , it all depends on your PC’s make and model.

Typically, you will see a brief note at the bottom or top of the screen indicating what the key is. One such screen is visible to the right, note the legend in the top-right corner indicating F2 will start the BIOS setup and F12 will present the boot selection menu.

Some common options include the F2, F8, F12, and Del keys. However, it could be any of the dozens of other keys on your keyboard.

Check out the website to have **more info** and **MORE BIOS/UEFI PICTURES** to compare with your hardware.  
Source : <https://neosmart.net/wiki/enable-uefi-boot/>

Next thing we need to check is **Secure boot** \- it needs to be set to include linux so **Other OS**.

![](https://arcolinux.com/wp-content/uploads/2018/04/secure-boot.jpg)

Then we need to save it. Check your system.

I have to press **F10.**

Then we reboot and I need to press **F8** to get into the boot menu to boot from the usb and we select UEFI boot to boot into the ArcoLinux iso and do a regular installation.

Video: <https://www.youtube.com/watch?v=lOOici0UU48>
