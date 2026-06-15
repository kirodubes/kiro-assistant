---
title: "Installing ArcoLinux on MacBookPro5,4"
url: https://arcolinux.com/installing-arcolinux-on-macbookpro54/
date: 2018-04-09 14:24:41
type: post
categories: ["Apple", "Nvidia"]
tags: ["mac", "nvidia"]
source_site: arcolinux.com
---

# Installing ArcoLinux on MacBookPro5,4

![](https://arcolinux.com/wp-content/uploads/2018/04/arcolinux-macbookpro54.jpg)

Let me first start with a video with all the settings of your laptop that you should remember BEFORE installing any Linux distro on your mac laptop.

Write it down, or like I did, film it and keep it safe. We can now check later what hardware is in there. We can try to find it online but we do not need to now. We have this video.

Video: <https://www.youtube.com/watch?v=AA2LLfaEO5M>

We have build our own iso from the github and have now ArcoLinux 6.6.4. It has been changed to be able to see the wireless networks out of the box. You can **build** the latest iso any time you want. [Check out these tutorials.](<https://arcolinuxb.com/category/arcolinux/byoi/>) Or download them from sourceforge.

We burn the iso to the usb with **mintstick**. It is in accessories and is called **Usb image writer**.

Then we need to be able to boot up from an usb. The trick is to keep pressing the option or Alt key when you start the laptop.

Video: <https://youtu.be/EeFGTivJnbE>

Since I want to make video tutorials I first need to get my build-in webcam and microphone working.

This is where your study starts : <https://wiki.archlinux.org/index.php/mac>.

There is also this link that can be useful : <https://wiki.archlinux.org/index.php/Laptop/Apple>

This link tells me that my laptop MacBookPro5,4 mid 2009 - everything seems to work out of the box EXCEPT **isight**.  
**Powermanagement** is **unknown** however on this page. I do not have the feeling it works.

**List of elements working out of the box after ArcoLinux installation**

  * Wireless works - Broadcom BCM4322 - all wireless networks display in networkmanager
  * Ethernet works - Nvidia MCP79
  * Xbacklight (light of keyboard) works. Keyboard keys work.
  * Sound works. Buttons for play/pause, next, previous and sound adjustment.
  * Bluetooth works. Tested with Bose Quietcomfort 35.
  * Video works. Nouveau and Nvidia work both fine.



**Fixing Isight**

First I installed this application
    
    
    trizen isight-firmware-tools

Then I rebooted and tested the webcam (guvcview) and microphone (simplescreenrecorder).

No settings changed. They worked after reboot. Needed that to make video tutorials with simplescreenrecorder.

Video: <https://youtu.be/Mh-NiE4Yj5k>

We end up with an almost 100% functionAl system.

![](https://arcolinux.com/wp-content/uploads/2018/04/ArcoLinux_macbookpro.jpg)

NVidia drivers installed

THERE IS NO NEED TO INSTALL NVIDIA  
JUST FOR EDUCATIONAL PURPOSE

In this video we analyze what driver I need to install with the help of <https://wiki.archlinux.org/index.php/NVIDIA>  
The wiki is using a nice code to find out what graphical hardware you have AND what driver you are using nouveau or nvidia.
    
    
     lspci -k | grep -A 2 -E "(VGA|3D)"

Often I tend to rely on the information provided on [nvidia.com](<http://www.nvidia.com/Download/index.aspx?lang=en-us>) to figure out what driver I need for my hardware. Install and then reboot.
    
    
    sudo pacman -S nvidia-340xx

Video: <https://www.youtube.com/watch?v=QBF0MO21IYg>

Then we **REBOOT** and check if we are using the nvidia driver. In my case I can not miss it as Nvidia's logo is filling up my screen when I reboot.

Video: <https://www.youtube.com/watch?v=0RxYm4REdpo>

ARCOLINUX NEMESIS

INSTALLING FONTS FOR CONKIES

Video: <https://www.youtube.com/watch?v=o41uNIPIKgI>

General tips

I am working on an Azerty Belgian keyboard. It might differ on yours. Just keep trying out combinations.

Fn + backspace = delete

ALT(right) + " is @ here in Azerty keyboard.

context menu opens with two fingers click on touchpad.

super + F1 launches your browser... this time you need to add the **Fn** key with that to launch your Fx-Key applications.

TO DO

If I am ever in the mood and have the time, these things are still open.

  * Close lid of laptop and go to sleep. (fixed in September 2018)
  * Brightness keys F1 and F2 ... can they work?



Do you find the solutions... Help a guy out.

They are not deal-breakers in my book.  
For a 9-year old duo-core with a new ssd it is good enough for me to be my third testing laptop.

![](https://arcolinux.com/wp-content/uploads/2019/01/macbookphoto.jpg)
