---
title: "Installing ArcoLinux on Samsung 970 Evo NVMe M.2"
url: https://arcolinux.com/installing-arcolinux-on-samsung-970-evo-nvme-m-2/
date: 2018-12-24 21:52:00
type: post
categories: ["Pre-installation"]
tags: ["anydesktop", "hardware"]
source_site: arcolinux.com
---

# Installing ArcoLinux on Samsung 970 Evo NVMe M.2

![](https://arcolinux.com/wp-content/uploads/2018/12/samsung-970-evo-nvmem2-front.jpg) ![](https://arcolinux.com/wp-content/uploads/2018/12/samsung-970-evo-nvmem2-back.jpg)

You can install an operating system on a **harddisk** , an **ssd** or on an **NVMe**.   
They are ordered from **slower** to **fast** to **fastest**.

![](https://arcolinux.com/wp-content/uploads/2018/12/harddisk-exposed.jpg) ![](https://arcolinux.com/wp-content/uploads/2018/12/samsung-ssd-exposed.jpg) ![](https://arcolinux.com/wp-content/uploads/2018/12/samsung-970-evo-ssd.jpg)

We start by looking at the **motherboard**. Not every motherboard can connect with an NVMe M.2.

![](https://arcolinux.com/wp-content/uploads/2018/12/inxi-strix.png)

We see it is an Asus STRIX Z270H GAMING and go look [online for more info](<https://www.asus.com/Motherboards/ROG-STRIX-Z270H-GAMING/>).

There we can see that it has a connector for M.2 on the motherboard.

We put it on the motherboard and attach it with a very small screw (not in box from Samsung).   
I detach all other ssd's or harddisks. Just to be on the safe side.

> Disconnect your power cables before opening up your case.

![](https://arcolinux.com/wp-content/uploads/2018/12/motherboard-asus-ROG-STRIX-Z270H-GAMING-with-nvme.jpg)

After adding the ssd to the motherboard and fixing it with a screw, I rebooted and installed ArcoLinux as usual without any changes.

After the installation I rebooted and started making the tutorials and benchmark tests on it.

So technically there is nothing to tell about this installation. Business as usual.

You can test the speed of the ssd with **gnome-disks** and take a look at the partitions with **gparted**.

We see the device is not**/dev/sda** but **/dev/nvme0n1** now.

This is the ssd that I have bought:

<https://www.samsung.com/us/computing/memory-storage/solid-state-drives/ssd-970-evo-nvme-m-2-250gb-mz-v7e250bw/>

![](https://arcolinux.com/wp-content/uploads/2018/12/samsung-970-evo-ssd.jpg)

Video: <https://youtu.be/ctCH5SgoFiI>

Then I connected my sata cables back for my ssd and installed ArcoLinux on the SSD.  
Watch out during Calamares install that you put ArcoLinux on /dev/sda and then you can boot into SSD or NVMe from grub.

![](https://arcolinux.com/wp-content/uploads/2018/12/grub-ssd-and-nvme.jpg)

Do not forget to select the proper harddisk when installing with calamares.

I have now reconnected an SSD to the motherboard.

![](https://arcolinux.com/wp-content/uploads/2018/12/calamares-nvme.jpg)![](https://arcolinux.com/wp-content/uploads/2018/12/gparted-nvme.jpg)![](https://arcolinux.com/wp-content/uploads/2018/12/gparted-sda.jpg)

it takes 6 seconds to boot up ArcoLinux now
