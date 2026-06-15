---
title: "Connecting to the internet via wifi - any desktop"
url: https://arcolinux.com/connecting-to-the-internet-via-wifi-any-desktop/
date: 2019-11-26 08:30:59
type: post
categories: ["Post-installation", "Pre-installation"]
source_site: arcolinux.com
---

# Connecting to the internet via wifi - any desktop

![](https://arcolinux.com/wp-content/uploads/2019/07/nmtui.jpg)

never mind wifi

use a lan cable

do wifi when you have a desktop

but some laptops only have wifi 

Option 1

nmtui

Video: <https://youtu.be/rfdG9hqaK20>

Option 2

nmcli

Video: <https://youtu.be/8gRpvPHq5RY>

Still not on internet  
than use this information  
to get there

We have the wiki as our guide open: 

<https://wiki.archlinux.org/index.php/Wireless_network_configuration>

<https://wiki.archlinux.org/index.php/Network_configuration>

<https://wiki.archlinux.org/index.php/Network_configuration#Network_managers>

<https://wiki.archlinux.org/index.php/NetworkManager>

We follow the wiki and type in the commands we read on the wiki.

We need to know the name of our network interface card or NIC.

**ip link** provided us the name aka **wlp4s0**

All applications to connect to the wifi are installed on ArcoLinux, ArcoLinuxD and ArcoLinuxB like wpa_supplicant, wifi-menu, iw, wireless_tools, ...

Then we need to set the link to **up**
    
    
    sudo ip link set wlp4s0

Then we need to connect to an access point.
    
    
    sudo wifi-menu

Select the correct wifi and type your password.

Now we should still contact the wifi - it know what to contact and how to contact but there is no connection to it yet.
    
    
    nmtui

On ArcoLinux we have always networkmanager installed so we have also this **nmtui** installed.

Video: <https://youtu.be/hJA2thCRxrY>
