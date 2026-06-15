---
title: "Screencast your android device to ArcoLinux and/or Arch Linux"
url: https://arcolinux.com/screencast-your-android-device-to-arcolinux-and-or-arch-linux/
date: 2019-06-15 12:30:02
type: post
categories: ["Video"]
tags: ["android"]
source_site: arcolinux.com
---

# Screencast your android device to ArcoLinux and/or Arch Linux

![](https://arcolinux.com/wp-content/uploads/2019/06/scrcpy.jpg)

Many of my tutorials contain more info then the tittle suggests.

That is the case here.

Before we tackle how to screencast your android device on ArcoLinux we tell you what I did prior to this test.

  1. we build the very latest iso - [you can do this too if you follow this tutorial](<https://arcolinuxb.com/byoi-on-arcolinux-no-changes-made/>)
  2. then we burn the iso with our usb burner
  3. then we clean install ArcoLinux on a SSD
  4. we use the url <https://bit.ly/arcogetstarted3> to get my scripts in - [more info here](<https://arcolinux.com/make-your-very-own-get-started-script-to-setup-your-system-after-a-clean-install/>)
  5. I ran the bare-start-here script
  6. then I git cloned the arcolinux-nemesis github - [more info here](<https://arcolinux.com/installing-nemesis-on-any-arcolinux/>)



Now I have the script to install scrcpy on my machine and we install it.
    
    
    sudo pacman -S android-tools
    yay -S scrcpy

Then we connect our android device to our pc with an USB-C cable.

# Make sure that your Android device is on at all times.

Your android device will ask **access** to connect to your computer.

Always allow, always confirm.

Allow if you get the answer for the fingerprint and RSA.

![](https://arcolinux.com/wp-content/uploads/2019/06/allow-usb-debugging-498x1024.jpg)

You need to**change settings in your android device** in order to be able to screencast.

Let us copy/paste the explanation from the Arch Wiki.

"Enable USB Debugging on your phone or device:

  * Jelly Bean (4.2) and newer: Go to  _Settings > About Phone_ tap  _Build Number_ 7 times until you get a popup that you have become a developer. Then go to  _Settings > Developer > USB debugging_ and enable it. The device will ask to allow the computer with its fingerprint to connect. Allowing it permanently will copy `~/.android/adbkey.pub` onto the devices `/data/misc/adb/adb_keys` folder."



Source : <https://wiki.archlinux.org/index.php/Android_Debug_Bridge#Connect_device>

If you still need more info then check out [this great tutorial from howtogeek.com](<https://www.howtogeek.com/129728/how-to-access-the-developer-options-menu-and-enable-usb-debugging-on-android-4.2/>).

Here are the essential screens you need.

Go to **settings > About phone >Software information** and **tap** **7** times on **Build number** until you see the message about becoming a **developer**

![](https://arcolinux.com/wp-content/uploads/2019/06/scrcpy-build.png)

Then you move back up in the menu until you see a new menu called **Developer Options**

![](https://arcolinux.com/wp-content/uploads/2019/06/scrcpy-developer.png)

In the developer options you can then activate the **usb debugging**.

![](https://arcolinux.com/wp-content/uploads/2019/06/scrcpy-usb-debugging.png)

Here is another video to show what you need to do on your Android machine

Video: <https://youtu.be/u0UfKokqU0Y>

Links you might need

  * [scrcpy github](<https://github.com/Genymobile/scrcpy>)
  * [Android Debug Bride or ADB](<https://wiki.archlinux.org/index.php/Android_Debug_Bridge>)
  * [Android wiki](<https://wiki.archlinux.org/index.php/Android>)



Video: <https://youtu.be/0UQkZ7Wha7c>

Video: <https://youtu.be/DiDSDBDcgeE>
