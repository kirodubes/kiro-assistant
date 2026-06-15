---
title: "All you need to know about BTRFS"
url: https://arcolinux.com/all-you-need-to-know-about-btrfs/
date: 2022-02-04 06:38:31
type: post
categories: ["Btrfs"]
source_site: arcolinux.com
---

# All you need to know about BTRFS

![](https://arcolinux.com/wp-content/uploads/2022/02/btrfs.jpg)

Butterfs or btrfs is a filesystem. First read the [Arch Linux wiki](<https://wiki.archlinux.org/title/Btrfs>) for more background information.

> You can choose Btrfs to be able to roll-back in time   
> to a system "where everything still worked".

There are two ways I would suggest.

Either use **timeshift** or **snapper**.   
In any case you choose **BTRFS** as filesystem during **Calamares**.

TIMESHIFT

It is best to choose the following packages in the **Calamares** installer.

  * timeshift (core application)
  * timeshift-autosnap (create snapshot)
  * grub-btrfs (snapshots available in grub



 

 

After rebooting run **Timeshift** and use the **wizard** to set it up and create your first snapshot.

 

If you **forgot** to **select** **the packages** in **Calamares** then click to see what you have to do manually.
    
    
    sudo pacman -S timeshift timeshift-autosnap grub-btrfs

SNAPPER

It is best to choose the following packages in the **Calamares** installer. Doing so will allow Calamares to set the snapper settings **automatically**.

Read more about Snapper on the [Arch Linux wiki](<https://wiki.archlinux.org/title/Snapper>).

  * snapper (core application)
  * btrfs-assistant (gui to restore)
  * grub-btrfs (snapshots in grub)
  * snap-pac (pacman hook - pre and post install)
  * snap-support (snapshots available in grub - extra help)



If you **forgot** to **select** **the packages** in **Calamares** then click to see what you have to do manually.

 
    
    
    sudo pacman -S snapper btrfs-assistant grub-btrfs snap-pac snapper-support
    
    
    sudo snapper -c _root_ create --description "_initial snapshot"_
    
    
    sudo chmod a+rx /.snapshots
    
    
    sudo chown :users /.snapshots

# Sources used

Some more reading material. 

 

  * [Install Arch Linux in Minimal Setup using BTRFS filesystem and Legacy BIOS mode](<https://gitlab.com/-/snippets/1965021>)
  * https://www.hiteshpaul.com/posts/14829/
  * <https://www.brunoparmentier.be/blog/how-to-install-arch-linux-on-an-encrypted-btrfs-partition/>
  * <https://www.nishantnadkarni.tech/posts/arch_installation/>
  * <https://www.ordinatechnic.com/distribution-specific-guides/Arch/an-arch-linux-installation-on-a-btrfs-filesystem-with-snapper-for-system-snapshots-and-rollbacks>
  * <https://www.nerdstuff.org/posts/2021/2021-001_arch_linux_btrfs_systemd-boot/>
  * <https://github.com/asus-zephyrus/archinstall>
  * <https://github.com/Deebble/arch-btrfs-install-guide>
  * <https://www.vultr.com/docs/install-arch-linux-with-btrfs-snapshotting>
  * <https://kb.adamsdesk.com/operating_system/arch_linux_install_file_system_btrfs/>
  * <https://github.com/picodotdev/alis/>
  * Garuda and EndeavourOs settings and isos



BTRFS PLAYLIST - ARCOLINUX VIDEOS

I will add the more interesting videos to this playlist as my study continues the coming months and years.

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS4YQJFYX_rz8ZgnXeKMlLAC>

BTRFS PLAYLIST - 3th PARTY 

I will add the more interesting videos to this playlist as my study continues the coming months and years.

Video: [https://www.youtube.com/watch?v=iwNg_fusT9A&list;=PLlloYVGq5pS4R2ixs9fi8jkiZTdsrwqub](<https://www.youtube.com/watch?v=iwNg_fusT9A&list=PLlloYVGq5pS4R2ixs9fi8jkiZTdsrwqub>)

BTRFS PLAYLIST - PURE ARCH LINUX

These videos are focused on the Arch Linux iso and the Arch Linux way of installing an operating system.

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS6cX425icnVlrkFqPJWx0QB>
