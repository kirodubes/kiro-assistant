---
title: "How to make sure you can play videos from youtube and videos from netflix on vivaldi or other browsers"
url: https://arcolinux.com/how-to-make-sure-you-can-play-videos-from-youtube-and-videos-from-netflix-on-vivaldi-or-other-browsers/
date: 2020-01-21 22:06:59
type: post
categories: ["Audio", "Video"]
source_site: arcolinux.com
---

# How to make sure you can play videos from youtube and videos from netflix on vivaldi or other browsers

![](https://arcolinux.com/wp-content/uploads/2020/01/vivaldi.jpg)

You need to remember two names

  * widevine
  * ffmpeg codecs



Then you figure out where to get the packages from<. You can always find them on AUR. But in our case we can install them from our ArcoLinux repository.

In the video we discover that other browsers have similar packages. Best is to choose the browser you prefer and install the packages for that one.
    
    
    sudo pacman -S vivaldi-widevine
    sudo pacman -S vivaldi-codecs-ffmeg-extra-bin

Video: <https://youtu.be/eBCC1LqD0lI>
