---
title: "5 The actual installation of Arch Linux Phase 1 UEFI"
url: https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-uefi/
date: 2020-01-01 10:48:59
type: post
categories: ["Arch Way"]
tags: ["archlinux"]
source_site: arcolinuxd.com
---

# 5 The actual installation of Arch Linux Phase 1 UEFI

Boot from an usb

**Information for people who want to install Arch Linux on an SSD or harddisk**

Before booting from an usb stick you better check your hardware settings. Boot into your hardware settings or BIOS or UEFI settings. Then check following settings. It can have different names and different keyboard shortcuts to reach it.

  * Disable `Secure Boot`
  * Disable `Launch CSM` or `Legacy Support`
  * Set `Boot Mode` to `UEFI`
  * Enable `USB Boot`
  * Set USB Disk as boot priority



[Need more information - take a look at this page.](<https://arcolinux.com/installation/>)

[Here are all the articles where we change the settings on our motherboard to be able to boot Linux.](<https://arcolinux.com/category/arcolinux/bios-uefi/>)

Boot from the ISO in VB![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/archuefi.png)

The image above is proof that we are booting with EFI - set it correctly in the virtual machines.

Then we have to wait quite a long time before Arch Linux kicks in and boots up. That is normal.

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-uefi.png)pre-installationSet the keyboard layout![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-keyboard.jpg)Arch Linux standard boots into an US keyboard layout. Many of us do not have to do anything. Just check the main keyboard keys and see if they all work. But others need to change for example from **qwerty** to **azerty**. We follow this link on the wiki to test things out: <https://wiki.archlinux.org/index.php/Keyboard_configuration_in_console> We have used this command to have a list of all possible keyboards out there. 
    
    
    find /usr/share/kbd/keymaps/ -type f | more

Finally I will use this code to have my Belgian azerty keyboard. You choose your keyboard layout.
    
    
    loadkeys be-latin1

Video: <https://youtu.be/u9NQ3Op3mr8>

VErify the boot mode![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/confirmation-efi.jpg)It is **not really necessary** **IF** you saw the first image on this page. It tells you the Arch Linux usb stick is booting into **UEFI**. You can get confirmation with this code : 
    
    
    ls /sys/firmware/efi/efivars

or 
    
    
    efivar -l

If you get a bunch of lines, all is well.

Video: <https://youtu.be/vBOTdZ8Nvjo>

Connect to the internet![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-internet.jpg)Normally you will be connected to the internet out of the box. On virtualbox you will **ALWAYS** be connected **IF** your host computer has internet. We test our internet connection via 
    
    
    ping -c 4 archlinux.org

I added "-c 4". Now it will only ping 4 times. We can ask also some more information about our interface with 
    
    
    ifconfig

The name of your ethernet (or wifi) interface is important to know. In my case **enp0s3**. You will need it later in conkies etc. Your [DHCP](<https://wiki.archlinux.org/index.php/Dhcpcd>) server (mostly a router) has provided you with all the information you need to go on the net : 

  * Ipaddress for your pc
  * Subnetmask
  * Gateway ipaddress
  * Nameserver to resolve the names into an ipaddress



[No lan cable present and wifi is the only thing you have, check out this article.](<https://arcolinux.com/connecting-to-the-internet-via-wifi-any-desktop/>)

Video: <https://youtu.be/LTKyJdm_o8E>

UPDATE THE SYSTEM CLOCK![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/archlinux-date.png)We tell our computer to **sync** the date and time. At this point we do NOT say what timezone we are in.
    
    
    timedatectl set-ntp true

Video: <https://youtu.be/-BbIusQiw9U>

Partition the disksThis is the most dreaded part and it is also the topic of much debate online. What tool to use? What partitions to make? In what order? What size? We will use a **minimal** partition in order not to complicate things. 

  * EFI System partition **/dev/sda1** with 550MB, FAT32 format
  * Swap partition **/dev/sda2** with 2XRAM recommended size, swap on
  * Root partition **/dev/sda3** with at least 20GB or the rest of the space in ext4 format

Since I made only a 30GB harddisk in my virtualbox, I will only take 10GB for my swap partition. **Rule of thumb is twice your RAM for the size of your swap.** With the commands **fdisk -l** or **lsblk** we discover that our harddisk is named **/dev/sda**. That is all we need to know to get started.
    
    
    cfdisk

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-1-lsblk.jpg)Then we start **cfdisk** to partition our harddisk. You can also use fdisk, gdisk or parted. I choose to go with this more or less graphical partitioning tool. We have choosen to install UEFI or EFI so we choose now **GPT**.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-2-gpt.jpg)

On a virtualbox and on a freshly bought ssd or harddisk you will get the same image.  
However if you are reusing a harddisk, you will see lines (partitions) on there.  
Delete all the partitions untill you have the same view like image beneath.

Notice the words **Label: gpt** in the third line.

If that is not the case, first type this in a terminal.
    
    
    wipefs -a /dev/sda

If that is not working for you, you can try this one as well:
    
    
    sgdisk -Z /dev/sda

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-1.jpg)Use the arrow keys to move around cfdisk. Press enter on the **New** menu and type **550MB** and press Enter. Select the type from the bottom menu and choose **EFI SYSTEM** partition type.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-3.jpg)That will result in this layout.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-4.jpg)Now that the EFI partition is created. Let us create the **swap** partition. As a rule of thumb it must be twice the RAM. In my case that would be 32 GB and I have only 30GB in my virtualbox. I will take 10GB for SWAP in this exercise.Move the selection to Free space. Move the selection to New and press Enter. Type in the amount of Swap you want to use - 10 GB in this case and press enter![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-5.jpg)Move the selection to **Type** and choose **Linux swap**.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-6.jpg)We will stick to 3 partitions. We can make more partitions if you want. [More info about partitions here.](<https://wiki.archlinux.org/index.php/Partitioning>)Move the selection to Free space. Move the selection to New and press Enter. Take the rest of the amount for your root partition or / and press enter![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-8.jpg)Move the selection to **Type** and choose **Linux filesystem**. (already a Linux filesystem)![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-8-bis.jpg)![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-9.jpg)Move the selection to **Write**. And type "**yes** " and press enter.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-10.jpg)When you typed **yes** and confirmed it with an **Enter** you can select **quit**. When typing **lsblk** things must be changed. We have now 3 partitions.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-3-cfdisk-11.jpg)

Video: <https://youtu.be/jYbGyHvx7EQ>

The partitioning information in the video about either 

  * 4 primary partitions or
  * 3 primary partitions and one extended partion with many logical partitions

applies on an **MBR** setup. It might seem out of place here but I thought I pass that knowledge along here already. In regards to **EFI** I find information that we can go till **128 primary partitions** not that we will need as much ever. [Link for more info](<https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-and-gpt-faq>).Format the partitions![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/format-partitions.png)

We have sliced our harddisk into 3 pieces but we did **not** **format** **them** **yet**.  
That is what we will do now with these commands.

Formatting the **EFI** partition
    
    
    mkfs.fat -F32 /dev/sda1

Formatting the **swap** partition and activating it
    
    
    mkswap /dev/sda2  
    swapon /dev/sda2

Formatting the **root** partition.
    
    
    mkfs.ext4 /dev/sda3
    
    
    mkfs.fat -F32 /dev/sda1
    
    
    mkswap /dev/sda2  
    swapon /dev/sda2

[Follow this article if you want to format as BTRFS instead of EXT4.](<https://www.arcolinuxd.com/installing-arch-linux-with-a-btrfs-filesystem/>)
    
    
    mkfs.ext4 /dev/sda3

****

**Xfs** , **Reiserfs** , **F2fs** , **Jfs** is not complex.  
You can learn about those in the all-in-one articles.

Instead of mkfs.ext4 you use ...

  * mkfs.reiserfs
  * mkfs.xfs
  * mkfs.f2fs
  * mkfs.jfs



Video: <https://youtu.be/31ou1hFtHx0>

Mount the file systems![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/mount-part.png)

We need to mount our created partitions into our linux hierarchy. **First** we need to mount sda3 (root) into /mnt.

Then we create **/mnt/boot/efi** in which we will mount **/dev/sda1**.

**This may differ with older videos.**
    
    
    mount /dev/sda3 /mnt
    
    
    mkdir /mnt/boot

If you plan to use **systemd-boot** instead of Grub or anything else then first read this [article](<https://www.arcolinuxd.com/systemd-boot-for-all-uefi-systems/>).  
If you plan to use **efistub** instead of Grub or anything else then first read this [article](<https://www.arcolinuxd.com/efistub-as-bootloader/>).
    
    
    mkdir /mnt/boot/**efi**
    
    
    mount /dev/sda1 /mnt/boot/**efi**

Video: <https://youtu.be/vdmGgctJbW4>

INSTALLATIONSelect the mirrors![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-mirrorlist.png)You can select the mirrors that are closest to you geographically BUT it does not mean they will be the fastest. Normally I will change nothing until the speed is not satisfactory. As an example I changed some of the settings with nano and showed you how to save it then. Read the info about mirror servers as this is quite important.

In nano use**left shift** and **arrows** to select lines (white background and black letters) and then delete those lines with**left alt** and **delete** button.
    
    
    nano /etc/pacman.d/mirrorlist

Video: <https://www.youtube.com/watch?v=TI0l3w2g1rc>

Video: <https://youtu.be/zCMEkrUc-tY>

Use parallel downloads in pacman

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-parallel-downloads.png)

Use the possibility to download in parallel. If you have a fast internet then it will save you minutes in installation time.
    
    
    nano /etc/pacman.conf

I will remove the '#' and change the 5 into 20. You decide the number best for you.

Install the base and base-devel packages![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-pacstrap.jpg)

We are going to install the base and base-devel packages on our mounted partition in /mnt now. This will become our Linux system later on. Content of base package changed 10/2019.

**Vi** is available by default. We will need to edit files later on with nano.

**visudo** is needed later on. Installing**base-devel** will install the **sudo** package to be able edit visudo later on.
    
    
    pacstrap -K /mnt base base-devel linux linux-firmware nano

Video: <https://youtu.be/4MgiXta704c>

[Remember that Arch Linux split the linux-firmware package.](<https://archlinux.org/news/linux-firmware-202201190c6a7b3-2-requires-kernel-53-and-package-splitting/>)  
If you recognize any names, your computer system may need it.

![](https://www.arcolinuxd.com/wp-content/uploads/2022/02/firmware.png)

**Remember to add additional packages for filesystems.**

  * btrfs - btrfs-progs
  * reiserfs - reiserfsprogs
  * jfs - jfsutils
  * f2fs - f2fs-tools
  * xfs - xfsprogs

CONFIGURE THE SYTEMFstab![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/fstab.png)

Let us use the script **genfstab** to generate a fstab file so linux will know what partitions we have like root and swap.

If the text underneath shows "**& gt;**" again we actually mean "**>** ".
    
    
    genfstab -U /mnt >> /mnt/etc/fstab

Open fstab to check that it is all correct.
    
    
    nano /mnt/etc/fstab

Video: <https://youtu.be/Ag1Vdod5_dg>

CHROOT![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-chroot.jpg)Let us now move inside your future linux system and change elements there. With **exit** you can exit this chroot environment should you want it. I can only recommend you read the article about [chroot](<https://wiki.archlinux.org/index.php/Change_root>). It helped me fix a broken Arch Linux system in the past.
    
    
    arch-chroot /mnt

Video: <https://youtu.be/-BvnD2XeDjI>

Time zone![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-timezone.jpg)

Here we are going to set our timezone aka where do you live according to Linux.

We investigate all the possibilities by navigating to the folder zoneinfo.
    
    
    ln -sf /usr/share/zoneinfo/RegionCity /etc/localtime

In my case I used
    
    
    ln -sf /usr/share/zoneinfo/Europe/Brussels /etc/localtime

Then we set the hardware clock from the systemclock with this command.
    
    
    hwclock --systohc

Video: <https://youtu.be/TZY0ZH6ZtBY>

LOCALE![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-locale.jpg)

In the locale we are going to set your localization.

What language do you want the system to be in?

You can investigate by using this command and uncomment the language or languages you prefer.

In my case I used **en_US.UTF-8** and deleted the hashtag in front of it. Use the Page up and Page down key to navigate throught the list. You need to find out your language.

Belgium -Dutch would be **nl_BE.UTF-8**.
    
    
    nano /etc/locale.gen

Then we save the file and generate the locale by running this command
    
    
    locale-gen

We will also set the variable **LANG** or language to reflect the same choice.

**We will use the shorter version at the bottom.**
    
    
    nano /etc/locale.conf

And type in this file
    
    
    LANG=en_US.UTF-8

and save it.

IF you changed the keyboard layout like me you should do this too.  
Let us make sure Arch Linux remembers to use my azerty keyboard after rebooting.
    
    
    nano /etc/vconsole.conf

and add this line to it and save it afterwards
    
    
    KEYMAP=be-latin1

If the text underneath shows "**& gt;**" again we actually mean "**>** ".

## Shorter alternative
    
    
    echo LANG=en_US.UTF-8 > /etc/locale.conf
    
    
    echo KEYMAP=be-latin1 > /etc/vconsole.conf

Video: <https://youtu.be/ZurF9p6WA4Q>

HOSTNAME![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-hostname.jpg)

We need to give our computer a name. Best is to choose one with no special characters and no spaces.

There is the longer way where you use nano and the shorter way. Up to you to decide. The result will be the same
    
    
    nano /etc/hostname

Write the name you have choosen for your computer.

Then we save the file with CTRL + X.

We did the shorter alternative in the video this time.

Ps. I mixed up the hostname file between tutorials Arch Linux, Archlinux and ArchErik. Just take one unique name.

If the text underneath shows "**& gt;**" again we actually mean "**>** ".

## Shorter alternative
    
    
    echo Archlinux > /etc/hostname

Then we edit our /etc/hosts file so it reflects this code. Use the TAB to align them.
    
    
    nano /etc/hosts
    
    
    127.0.0.1	localhost
    ::1	       localhost
    127.0.0.1	Archlinux.localdomain	Archlinux

Video: <https://youtu.be/QbGUmpnHUn8>

NETWORK CONFIGURATION![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-networkmanager.jpg)We will use the application NetworkManager afterwards in any of our desktops we would like to install. Therefore it makes sense to install and activate this application right now.

Make sure you type **NetworkManager** in the second line. It is case sensitve.You will get **3 symlink lines** as a result. When we boot we will have internet on board.
    
    
    pacman -S networkmanager
    
    
    systemctl enable NetworkManager

**Watch out for typos - capital letters are a must in "NetworkManager"  
Do not get 3 lines - you made an error  
**

Video: <https://youtu.be/lhhA9KsoyT4>

Root Password![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-root-password.jpg)We add a password to our root account with this command. Choose your password wisely.
    
    
    passwd

Video: <https://youtu.be/1RT-y5bwqV0>

4 Boot loaders

Grub (bios and uefi)  
Refind (uefi)  
Systemd-boot (uefi)  
EFISTUB (uefi)

Scroll down to find the links for Refind, Systemd-boot and Efistub.

1\. GRUB

![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/grub.png)

To install grub to our system in order to be able to boot later on we need to pass these commands (you can add **os-prober** to the installation line if you multi-boot):

**This may differ from the videos.**

**We have create a directory /boot/efi and mounted /dev/sda1 in it. So we need to refer now to that directory.  
**
    
    
    pacman -S grub efibootmgr
    
    
    grub-install --target=x86_64-efi --efi-directory=/boot/**efi**

Sometimes you see people add **\--recheck** as extra check. It does not seem necessary.  
We still need to make the grub configuration file with this command in order to be able to boot.
    
    
    grub-mkconfig -o /boot/grub/grub.cfg

Video: <https://youtu.be/dRVODxz95kA>

> NOT a part of the standard installation

**[What if you are planning to switch ssds with a ssd bay like in this article?](<https://www.arcolinuxd.com/how-to-mount-an-ssd-bay-in-your-desktop-to-easily-switch-between-windows-and-linux/>)  
**

This may be different on other hardware.  
I need to create an extra directory and copy and rename a file in order to pop out one ssd and reboot another.

> Only do if you need this.
    
    
    mkdir /boot/efi/EFI/boot
    
    
    cp /boot/efi/EFI/arch/grubx64.efi /boot/efi/EFI/boot/bootx64.efi

If I do not do this and still switch ssd, I will get this message

> Reboot and Select proper Boot device  
> or Insert Boot Media in selected Boot device and press a key

What if you now see this message from above?

Arch Linux can ALWAYS be repaired. [That is what this article is trying to tell you.](<https://www.arcolinuxd.com/10-use-the-power-of-arch-chroot-when-your-computer-crashes/>)

2\. [rEFInd as alternative to grub](<https://www.arcolinuxd.com/refind>)

3\. [Systemd-boot as alternative to grub](<https://www.arcolinuxd.com/systemd-boot-for-all-uefi-systems/>)

4\. [EFISTUB as bootloader](<https://www.arcolinuxd.com/efistub-as-bootloader/>)

RebootRebooting![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-reboot.png)

Now we can think about rebooting the system.  
Type exit to get out of the chroot environment.
    
    
    exit

We can optionally unmount our disks with
    
    
    umount -R /mnt

Then we can reboot with
    
    
    reboot

And log back in with **root** as user and his/hers **password**.

The image beneath is proof that grub has been installed correcly.
    
    
    exit
    
    
    umount -R /mnt
    
    
    reboot

If you choose Grub, you will see the screen underneath.

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-grub.png)

Video: <https://youtu.be/BM1HboGlx2g>

Reboot after shutdown of virtualbox

We assume you have Arch Linux installed on Virtual Box and that you **shutdown** the virtual machine.

When you restart Virtual Box you will be presented with this screen underneath.  
Select **storage** and make sure the **ISO** of Arch Linux is **deselected** from IDE Secondary Master.

![](https://www.arcolinuxd.com/wp-content/uploads/2020/01/virtualbox-ISO-gone.jpg)Then we start our Arch Linux and we will boot into grub.

Video: <https://youtu.be/TTorFSKyEV0>

[NEXT STEP](<https://www.arcolinuxd.com/6-the-actual-installation-of-arch-linux-phase-2>)
