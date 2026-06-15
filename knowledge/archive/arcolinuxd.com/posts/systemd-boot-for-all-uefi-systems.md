---
title: "Systemd-boot for all UEFI systems"
url: https://www.arcolinuxd.com/systemd-boot-for-all-uefi-systems/
date: 2022-02-14 14:07:58
type: post
categories: ["Arch Way"]
source_site: arcolinuxd.com
---

# Systemd-boot for all UEFI systems

Instead of booting up with grub or Refind we can use **systemd-boot**.

<https://wiki.archlinux.org/title/Systemd-boot>

We will however mount our /dev/sda1 into /boot and not /boot/efi.  
That is the only difference with the tutorial.

At the beginning we should have mounted /dev/sda1(uefi) in /mnt/boot.
    
    
    mount /dev/sda1 /mnt/boot
    
    
    bootctl install
    
    
    nano /boot/loader/loader.conf
    
    
    default  arch
    timeout  5
    editor   no
    
    
    nano /boot/loader/entries/arch.conf
    
    
    title Arch Linux
    linux /vmlinuz-linux
    initrd /initramfs-linux.img
    options root=/dev/sda3 rw

BTRFS 
    
    
    title Arch Linux
    linux /vmlinuz-linux
    initrd /initramfs-linux.img
    options initrd=/initramfs-linux.img root=/dev/sda3 rw rootflags=subvol=@

Possible additions if you have the package installed:
    
    
    initrd  /intel-ucode.img
    
    
    initrd  /amd-ucode.img
    
    
    cp /boot/loader/entries/arch.conf /boot/loader/entries/arch-fallback.conf
    
    
    nano /boot/loader/entries/arch-fallback.conf

Change the text - compare with what is written here
    
    
    title Arch Linux Fallback  
    linux /vmlinuz-linux  
    initrd /initramfs-linux-fallback.img  
    options root=/dev/sda3 rw
    
    
    cp /boot/loader/entries/arch.conf /boot/loader/entries/arch-terminal.conf

Change the text - compare with what is written here
    
    
    title Arch Linux Terminal  
    linux /vmlinuz-linux  
    initrd /initramfs-linux.img  
    options root=/dev/sda3 rw systemd.unit=multi-user.target
    
    
    systemctl enable systemd-boot-update.service

We can check our work with this command. 
    
    
    bootctl list

![](https://www.arcolinuxd.com/wp-content/uploads/2022/02/systemd-boot.png)

[What happens if you set timeout to zero or just delete the line?](<https://youtu.be/DsUeRY80Gik>)

Go back to the main tutorial.
