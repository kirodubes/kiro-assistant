---
title: "5 The actual installation of Arch Linux Phase 1 BIOS"
url: https://www.arcolinuxd.com/5-the-actual-installation-of-arch-linux-phase-1-bios/
date: 2020-01-01 10:29:33
type: post
categories: ["Arch Way"]
tags: ["archlinux"]
source_site: arcolinuxd.com
---

# 5 The actual installation of Arch Linux Phase 1 BIOS

Boot from USB

**Information for people who want to install Arch Linux on an SSD or harddisk**

Before booting from a USB stick, you should check your hardware settings. Boot into your hardware settings - BIOS or UEFI. Then check following settings. It can have different names and different keyboard shortcuts to reach it.

  * Disable `Secure Boot`
  * Disable `Launch CSM` or `Legacy Support`
  * Set `Boot Mode` to `UEFI`
  * Enable `USB Boot`
  * Set USB Disk as boot priority



[For more information - take a look at this page.](<https://arcolinux.com/installation/>)

[Here are all the articles where we change the settings on our motherboard to be able to boot Linux.](<https://arcolinux.com/category/arcolinux/bios-uefi/>)

Boot from the ISO in VB with BIOS![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-boot-bios.png)The image above is proof that we are booting with **BIOS**. The ISO will boot up instantly and provide you with a prompt. **MBR or EFI we end up at the same prompt.**![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-boot-bios-login.png) pre-installation Set the keyboard layout![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-keyboard.jpg)

Arch Linux standard boots into the US keyboard layout. Many of us do not have to do anything. Just check the main keyboard keys and see if they all work.

But others need to change for example from **qwerty** to **azerty**.

We follow this link on the wiki to test things out:

<https://wiki.archlinux.org/index.php/Keyboard_configuration_in_console>

We use this command to have a list of all possible keyboards out there.
    
    
    find /usr/share/kbd/keymaps/ -type f | more

Finally I will use this code to have my Belgian azerty keyboard. You choose your keyboard layout.
    
    
    loadkeys be-latin1

Video: <https://youtu.be/u9NQ3Op3mr8>

VErify the boot mode![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-efivars-BIOS.jpg)You can get confirmation with this code : 
    
    
    ls /sys/firmware/efi/efivars

or 
    
    
    efivar -l

Then you see this message "**No such file or directory** ". You booted with **BIOS**.

Video: <https://youtu.be/TTVVibkZMSw>

Connect to the internet![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-bios-ping.png)

Normally you will be connected to the internet out of the box.

On VirtualBox you will **ALWAYS** be connected **IF** your host computer is connected to the internet.

We test our internet connection via
    
    
    ping -c 4 archlinux.org

I added "-c 4". Now it will only ping 4 times.


[If you have no LAN cable present, and wifi is your only connection, check out this article.](<https://arcolinux.com/connecting-to-the-internet-via-wifi-any-desktop/>)

Video: <https://youtu.be/LTKyJdm_o8E>

UPDATE THE SYSTEM CLOCK![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/archlinux-date.png) We tell our computer to **sync** the date and time. At this point we do NOT say what timezone we are in.
    
    
    timedatectl set-ntp true

Video: <https://youtu.be/-BbIusQiw9U>

Partition the disksThis is the most dreaded part and it is also the topic of much debate online. What tool to use? What partitions to make? In what order? What size? We will use a **minimal** partition in order not to complicate things. 

  * Root partition **/dev/sda1** with 20GB, EXT4 format, primary, boot
  * Swap partition **/dev/sda2** with 2XRAM recommended size, primary, swap on

Since I made only a 30GB harddisk in my virtualbox, I will only take 10GB for my swap partition. **Rule of thumb is twice your RAM for the size of your swap.** With the commands **fdisk -l** or **lsblk** we discover that our harddisk is named **/dev/sda**. That is all we need to know to get started.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-partition-1-lsblk.jpg)

Then we start **cfdisk** to partition our harddisk. You can also use fdisk, gdisk or parted. I choose to go with this more or less graphical partitioning tool.

We have choosen to install **BIOS,** so we select **DOS**.
    
    
    cfdisk

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-dos.jpg)

In VirtualBox and on a freshly bought ssd or harddisk you will get the same image.  
However if you are reusing a harddisk, you will see lines (partitions) on there.  
Delete all the partitions till your setup is equivalent to that of the image below.

Notice the words **Label: Dos** in the third line.

If that is not the case, first type this in a terminal.
    
    
    wipefs -a /dev/sda

If that is not working for you, you can try this one as well:
    
    
    sgdisk -Z /dev/sda

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-cfdisk-empty.jpg)

Use the arrow keys to navigate **cfdisk,** and create the **root** partition.  
Press enter on the **New** menu and type **20GB** , choose **primary** and press Enter.  
The type is set to **Linux** and that is correct. However do not forget to select **Bootable** for this partition. You will see an **asterisk** in the column Boot.

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-cfdisk-sda1.jpg)Now that the **ROOT** partition is created. Let us create the **swap** partition. As a rule of thumb it must be twice the RAM. In my case that would be 32 GB and I have only 30GB in my virtualbox. I will take 10GB for SWAP in this exercise.Move the selection to Free space. Move the selection to New and press Enter. Choose **Primary**. We take all the space that is **left** for **Swap** and press enter.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-cfdisk-sda1.jpg) Move the selection to **Type** and choose **Linux swap**.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-linux-swap.jpg)

We will stick to 2 partitions.

Although we are only creating the two partitions, you can make more if you like.  
[More info about partitions here.](<https://wiki.archlinux.org/index.php/Partitioning>)

This should be the result.![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-bios-result.jpg)

Then we choose **Write**.   
Type **yes** and confirm with **Enter,** then select **quit**.

Type **lsblk** to see the changes to the harddisk. We have now 2 partitions.

![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-cfdisk.jpg)

Video: <https://youtu.be/3iesq_ep5Wo>

Format the partitions![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-cfdisk.jpg)

We have sliced our harddisk into 2 pieces but **we have not formatted them yet**.  
That is what we will do now with these commands.

Formatting the **ROOT** partition
    
    
    mkfs.ext4 /dev/sda1

Formatting the **swap** partition and activating it
    
    
    mkswap /dev/sda2  
    swapon /dev/sda2

Video: <https://youtu.be/buDO6OwT0Rk>

Mount the file system BIOS![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-mount.jpg)

We need to mount our created root partition into our Linux hierarchy.
    
    
    mount /dev/sda1 /mnt

Video: <https://youtu.be/54GBZbhvEto>

INSTALLATION Select the mirrors![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-mirrorlist.png)

You can select the mirrors that are closest to you geographically BUT it does not mean they will be the fastest. Normally I will change nothing until the speed is not satisfactory. As an example I changed some settings with nano and showed you how to save it.

Read the info about mirror servers as this is quite important.
    
    
    nano /etc/pacman.d/mirrorlist

Video: <https://www.youtube.com/watch?v=TI0l3w2g1rc>

Video: <https://youtu.be/zCMEkrUc-tY>

Use parallel downloads in pacman

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-parallel-downloads.png)

Use the possibility to download in parallel. If you have a fast internet then it will save you minutes in installation time.
    
    
    nano /etc/pacman.conf

I will remove the '#' and change the 5 into 20. You decide the number best for you.

Install the base and base-devel packages![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-pacstrap.jpg)

We are going to install the base and base-devel packages on our mounted partition in /mnt now. This will become our Linux system. 

**Vi** is available by default. We will need to edit files with nano.

**visudo** is needed. Installing **base-devel** will install the **sudo** package to be able edit visudo.
    
    
    pacstrap -K /mnt base base-devel linux linux-firmware nano

[Remember that Arch Linux split the linux-firmware package.](<https://archlinux.org/news/linux-firmware-202201190c6a7b3-2-requires-kernel-53-and-package-splitting/>)  
If you recognize any names, your computer system may need it.

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-linux-firmware.png)

Video: <https://youtu.be/4MgiXta704c>

CONFIGURE THE SYTEMFstab BIOS![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-fstab-bios.jpg)

Use the **genfstab** script to generate a fstab file so linux will know what partitions we have like root and swap.

If the text underneath shows "**& gt;**" again we actually mean "**>** ".
    
    
    genfstab -U /mnt >> /mnt/etc/fstab

You should have 2 partitions when you open the file with
    
    
    nano /mnt/etc/fstab

Video: <https://youtu.be/8ppVC95Y64Q>

CHROOT![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-chroot.jpg)

Next, go inside your future linux system.

Type **exit** to leave the chroot environment again.

I can only recommend you read the article about [chroot](<https://wiki.archlinux.org/index.php/Change_root>). It helped me fix a broken Arch Linux system in the past.
    
    
    arch-chroot /mnt

Video: <https://youtu.be/-BvnD2XeDjI>

Time zone![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-timezone.jpg)

The next step is to set the timezone based on where you live.

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

In my case I used **en_US.UTF-8** and deleted the hashtag in front of it. Use the Page up and Page down key to navigate through the list. Select your language(s).

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

Give your computer a name using no special characters and spaces.

The longer way is with the editor, the short from CLI. Up to you to decide. The result will be the same
    
    
    nano /etc/hostname

Write the name you have choosen for your computer, then we save the file with CTRL + X.

We did the shorter alternative in the video this time.

**NOTE** : I mixed up the hostname file between tutorials Arch Linux, Archlinux and ArchErik. Just take one unique name.

If the text underneath shows "**& gt;**" again we actually mean "**>** ".

## Shorter alternative
    
    
    echo Archlinux > /etc/hostname

Edit /etc/hosts tabbing over to type the second and third columns.
    
    
    nano /etc/hosts
    
    
    127.0.0.1	localhost  
    ::1	        localhost  
    127.0.0.1	Archlinux.localdomain	Archlinux

Video: <https://youtu.be/QbGUmpnHUn8>

NETWORK CONFIGURATION![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-networkmanager.jpg) We will use the application NetworkManager afterwards in any of our desktops we would like to install. Therefore it makes sense to install and activate this application right now.

Make sure you type **NetworkManager** in the second line. It is **case sensitve**. You will get**3 symlink lines** as a result. When we boot we will have internet on board.
    
    
    pacman -S networkmanager
    
    
    systemctl enable NetworkManager

**Watch out for typos - capital letters are a must in "NetworkManager"  
If you do not get 3 lines, there was an error.  
**

Video: <https://youtu.be/lhhA9KsoyT4>

Root Password![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-root-password.jpg)We add a password to our root account with this command. Choose your password wisely.
    
    
    passwd

Video: <https://youtu.be/1RT-y5bwqV0>

Boot loader![](https://www.arcolinuxd.com/wp-content/uploads/2018/04/archlinux-grubloader.jpg)

In order to boot the system with Grub, execute the following commands (for multi-boot, installing **os-prober** is required).
    
    
    pacman -S grub
    
    
    grub-install --target=i386-pc /dev/sda

Some users add **\--recheck,** which is not necessary, however.  
We still need to make the grub configuration file with this command in order to be able to boot.
    
    
    grub-mkconfig -o /boot/grub/grub.cfg

Video: <https://youtu.be/y_InwyDUiRQ>

Reboot Rebooting![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-reboot.png)

Now we can think about rebooting our system.  
Type exit to get out of the chroot environment.
    
    
    exit

We can optionally unmount our disks with
    
    
    umount -R /mnt

Then we can reboot with
    
    
    reboot

Log back in as user **root** with your **password**.

The image beneath is proof that grub has been installed correcly.
    
    
    exit
    
    
    umount -R /mnt
    
    
    reboot

And log back in with **root** as user and his/hers **password**.

The image beneath is proof that grub has been installed correcly.

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/arch-grub.png)

Video: <https://youtu.be/BM1HboGlx2g>

Reboot after shutdown of virtualbox

We assume you have Arch Linux installed on VirtualBox and that you **shutdown** the virtual machine.

When you restart VirtualBox select **storage** and make sure the **ISO** of Arch Linux is **deselected** from IDE Secondary Master.

Then we start our Arch Linux and we will boot into grub. [NEXT STEP](<https://www.arcolinuxd.com/6-the-actual-installation-of-arch-linux-phase-2>)
