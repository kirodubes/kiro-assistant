---
title: "Fix for vivaldi-codecs-ffmpeg-extra-bin not updated and vivaldi is updated"
url: https://arcolinux.com/fix-for-vivaldi-codecs-ffmpeg-extra-bin-not-updated-and-vivaldi-is-updated/
date: 2018-02-01 13:48:09
type: post
categories: ["Fixes"]
tags: ["fix", "pkgbuild"]
source_site: arcolinux.com
---

# Fix for vivaldi-codecs-ffmpeg-extra-bin not updated and vivaldi is updated

![](https://arcolinux.com/wp-content/uploads/2018/02/vivaldi-dead-bird.png)In the video I am looking at the **ffmpeg** file while I should have been looking at the **ffmpeg-extra** file In this article we are going to become a little more technical. It is not necessary to follow along since updates in Arch Linux take about 3-5 days and then your application is working again. **In this case I uploaded the created package into the ArcoLinux repo. You will get the working update in.** **Current situation on February 1st 2018** Vivaldi is update to version 1.14.1077.41 via AUR updates but the ffmpeg support file to see HD movies on youtube, open gmail, hangouts and so on is NOT updated and remains version 63.0.3239.132. Some of the sites we go to end up with this screen you see above - the dead bird image. **You can wait for the updates to come in but for me this is an opportunity to teach something about PKGBUILD.** Analysis We take a look at the [AUR](<https://aur.archlinux.org/packages/?O=0&SeB=nd&K=vivaldi&outdated=&SB=n&SO=a&PP=50&do_Search=Go>) and search for the package **vivaldi**. We found out that the package had been just updated on the day we launched ArchMerge 6.4.1. The latest version is 1.14.1077.41. The package vivaldi-codecs-ffmpeg-extra-bin (63.0.3239) has **NOT** been updated on the AUR to follow the new Vivaldi update and that results in a **mismatch** and some of the sites show us a **dead bird image**. SOLUTION 1 Wait for the maintainer to update the pkgbuild. SOLUTION 2 

**Let us write the PKGBUILD ourselves.**

We download the snapshot of the latest **vivaldi-codecs-ffmpeg-extra-bin.**

We extract it and this will be our 'playground'. We will change the pkgbuild here.

Then we go and surf to the source to see what is there. We need to find a**NEW VERSION**.

We analyze and change the PKGBUILD and try to run it with : **makepkg**

I did not see the word "extra" in the name of the file therefor I need to make a new md5sum. After looking at the video that is quite clear now.

Then we install the build package with
    
    
    sudo pacman -U ....

SOLUTION 3 The package has been added now to ArcoLinux repo. You will get it in via 
    
    
    sudo pacman -Syyu

Once the package is updated on the AUR, I will delete the one on our repo. 

Video: <https://youtu.be/KQciv4Ozrpw>
