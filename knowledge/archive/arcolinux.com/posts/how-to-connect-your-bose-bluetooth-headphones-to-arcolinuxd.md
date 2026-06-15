---
title: "How to connect your Bose bluetooth headphones to ArcoLinux -D -B"
url: https://arcolinux.com/how-to-connect-your-bose-bluetooth-headphones-to-arcolinuxd/
date: 2020-10-14 12:24:31
type: post
categories: ["Sound"]
tags: ["bluetooth", "music"]
source_site: arcolinux.com
---

# How to connect your Bose bluetooth headphones to ArcoLinux -D -B

![](https://arcolinux.com/wp-content/uploads/2020/10/bose.png)![](https://arcolinux.com/wp-content/uploads/2017/11/pair-with-bluetooth.png)

Bose QuietComfort 35 is a bluetooth headphone, which can be used on **ArcoLinux**. 

The extra software you need for bluetooth is already installed on **ArcoLinux** but not on ArcoLinuxD.
    
    
    sudo pacman -S pulseaudio-alsa pulseaudio-bluetooth 
    sudo pacman -S bluez bluez-libs bluez-utils bluez-firmware blueberry
    
    sudo systemctl enable bluetooth.service
    sudo systemctl start bluetooth.service
    sudo systemctl daemon-reload

Sometimes you need to switch your headset off and on again to reconnect to your machine when you reboot your computer.

Enable pairing on your headphone.

[User manual at bose.](<https://assets.bose.com/content/dam/Bose_DAM/Web/consumer_electronics/global/products/headphones/qc35/pdf/qc35_PDF_ownersguide_ML.pdf>)

[![](https://arcolinux.com/wp-content/uploads/2017/11/pair-with-bluetooth.png)](<https://arcolinux.com/wp-content/uploads/2017/11/pair-with-bluetooth.png>)

Go to the bluetooth icon, click on the bluetooth icon and connect to your device.

Go to the sound icon (bottom right) and select your device.

See that the Output profile is **High Fidelity Playback (A2DP sink)**. MUCH better sound than the other setting **Headset Head Unit (HSP/HFP).** As long as you do not see this headphone in your sound settings, you guess it, something is wrong. And in bluetooth nothing seems that simple. Then you can start googling. May I suggest the [archlinux guide](<https://wiki.archlinux.org/index.php/bluetooth>) as a start. I hope the installation was a success. A screenshot of the settings in **pavucontrol**.

[![](https://arcolinux.com/wp-content/uploads/2017/11/archlabs-pavucontrol.png)](<https://arcolinux.com/wp-content/uploads/2017/11/archlabs-pavucontrol.png>) [![](https://arcolinux.com/wp-content/uploads/2017/11/archlabs-pavucontrol-spotify.png)](<https://arcolinux.com/wp-content/uploads/2017/11/archlabs-pavucontrol-spotify.png>)

#### Tips

Use the buttons on your headphone for volume handling

Use the middle (multi-function) button for the next song (double click)

Use the middle (multi-function) button for the previous song (three clicks)

## Extra settings to check and improve the sound quality

Edit /etc/bluetooth/main.conf and see if it says 
    
    
    AutoEnable=true

  Edit /etc/pulse/default.pa and see if it says (add it) 
    
    
    load-module module-switch-on-connect

  Create a file with this name in /etc/modprobe.d/bluetooth-clear.conf Edit that file and add this to it. 
    
    
    options ath9k btcoex_enable = 1
