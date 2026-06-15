---
title: "Installing Arch Linux with a BTRFS filesystem"
url: https://www.arcolinuxd.com/installing-arch-linux-with-a-btrfs-filesystem/
date: 2022-02-02 09:19:07
type: post
categories: ["Arch Way"]
source_site: arcolinuxd.com
---

# Installing Arch Linux with a BTRFS filesystem

Format the partitions![](https://www.arcolinuxd.com/wp-content/uploads/2022/02/btrfs1.png)

We have sliced our harddisk into 3 pieces but we did **not** **format** **the root partition yet**.
    
    
    mkfs.btrfs /dev/sda3

Mount the file systems

We need to mount our created partitions into our linux hierarchy. **First** we need to mount sda3 (root) into /mnt.

We create **subvolumes** to better organize our data and to **exclude** them from btrfs snapshots.

**It may differ with older videos.**

  * @ - This is the main root subvolume /.
  * @home - This is the home directory. This consists of most of your data including Desktop and Downloads.
  * @log - Contains logs, temp. files, caches, games, etc.
  * @pkg - Contains all the pacman packages
  * @tmp - Contains certain temporory files and caches
  * @snapshots - Directory to store snapshots.



su = subvolume  
cr = create  
li = list
    
    
    mount /dev/sda3 /mnt
    
    
    btrfs su cr /mnt/@
    
    
    btrfs su cr /mnt/@home
    
    
    btrfs su cr /mnt/@root
    
    
    btrfs su cr /mnt/@srv
    
    
    btrfs su cr /mnt/@log
    
    
    btrfs su cr /mnt/@cache
    
    
    btrfs su cr /mnt/@tmp
    
    
    btrfs su li /mnt

**Now we see all the subvolumes we created.**

Let us unmount /mnt and remount all subvolumes.
    
    
    cd /
    
    
    umount /mnt
    
    
    mount -o defaults,noatime,compress=zstd,commit=120,subvol=@ /dev/sda3 /mnt
    
    
    mkdir  /mnt/home
    
    
    mkdir  /mnt/root
    
    
    mkdir  /mnt/srv
    
    
    mkdir -p /mnt/var/log
    
    
    mkdir -p /mnt/var/cache/
    
    
    mkdir /mnt/tmp

Or a one-liner
    
    
    mkdir -p /mnt/{home,root,srv,var/log,var/cache,tmp}

Type this command to check your work. 
    
    
    lsblk

Then we mount the subvolumes.
    
    
    mount -o defaults,noatime,compress=zstd,commit=120,subvol=@home /dev/sda3 /mnt/home
    
    
    mount -o defaults,noatime,compress=zstd,commit=120,subvol=@root /dev/sda3 /mnt/root
    
    
    mount -o defaults,noatime,compress=zstd,commit=120,subvol=@srv /dev/sda3 /mnt/srv
    
    
    mount -o defaults,noatime,compress=zstd,commit=120,subvol=@log /dev/sda3 /mnt/var/log
    
    
    mount -o defaults,noatime,compress=zstd,commit=120,subvol=@cache /dev/sda3 /mnt/var/cache
    
    
    mount -o defaults,noatime,compress=zstd,commit=120,subvol=@tmp /dev/sda3 /mnt/tmp

Now we continue with the "normal procedure".  
Mounting the boot partition in /boot folder
    
    
    mkdir -p /mnt/boot/**efi**
    
    
    mount /dev/sda1 /mnt/boot/**efi**

Btrfs options:

  * noatime - No access time. Improves system performace by not writing time when the file was accessed.
  * commit - Periodic interval (in sec) in which data is synchronized to permanent storage.
  * compress - Choosing the algorithm for compress. I have set zstd as it has good compression level and speed.
  * subvol - Choosing the subvol to mount.



Video: <https://youtu.be/Kc-ngqE84tQ?t=642>

Go back to the previous article.

And follow it after INSTALLATION

But REMEMBER

Install the base and base-devel packages

Remember to add any specific **Btrfs** packages in this phase of the installation or you do it later.
    
    
    pacstrap /mnt btrfs-progs

FSTAB

Check that your **fstab** is correct.
    
    
    nano /mnt/etc/fstab
