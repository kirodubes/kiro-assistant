---
title: "All in one Arch Linux installation - Uefi - Ext4 - Systemd-boot - Sddm - Flexi dwm"
url: https://www.arcolinuxd.com/all-in-one-arch-linux-installation-uefi-ext4-systemd-boot-sddm-flexi-dwm/
date: 2024-09-05 04:45:33
type: post
categories: ["ArchWayAllinone"]
source_site: arcolinuxd.com
---

# All in one Arch Linux installation - Uefi - Ext4 - Systemd-boot - Sddm - Flexi dwm

![](https://www.arcolinuxd.com/wp-content/uploads/2024/09/flexi.jpg)

<https://github.com/erikdubois/dwm-flexipatch>

The video is a tutorial on how to install Arch Linux, beginning with downloading the ISO from the Arch website. The presenter mentions that the size of the ISO has grown over time, not due to bloatware but because of added package options. Arch Linux releases a new ISO every month, which can be used to install the operating system. The presenter shows how to install Arch Linux in VirtualBox, highlighting various configurations such as enabling UEFI and choosing the appropriate desktop environment, XFCE in this case.

The installation process involves setting up partitions, selecting language settings, configuring mirrors, and using `archinstall`—a script that simplifies the installation. The presenter advises configuring Pacman (Arch Linux's package manager) for faster **parallel** downloads and explains how to set up **keyrings** to avoid installation issues. The video also touches on the importance of selecting the right graphics drivers and audio configurations.

The presenter emphasizes learning English technical terms for better understanding and searching for solutions. After installation, the presenter checks the XFCE environment and settings, showing how to tweak display settings, fonts, and other appearance-related options. They acknowledge that some users may face issues with hardware drivers, especially for NVIDIA graphics cards, which often require manual intervention.

The video concludes with a note on making scripts to automate post-installation setups, which would save time for future installations.

Video: <https://youtu.be/ox_CYZo--o8>

In this video, the presenter walks through the installation and setup of a customized DWM (Dynamic Window Manager) called DWM Flexi on a virtual machine running Arch Linux. The installation process begins by downloading the Arch Linux ISO, setting up XFCE as a fallback desktop, and then cloning the presenter's GitHub repository to install the DWM Flexi build. Key steps include installing necessary packages such as Git, configuring files like the power menu, and adjusting system fonts and settings for compatibility with Arch Linux.

The presenter highlights the importance of using Git to allow updates through commands like `git pull` and discusses how Arch-based systems, like ArcoLinux differ from Arch in their approach. He emphasizes that Arch is built from the ground up.

The video also covers adding custom font and adjusting system files to ensure compatibility with Arch Linux. The presenter demonstrates how to log out and reboot using the custom DWM setup and introduces tools like 'xrandr' pr 'arandr' for managing display settings. A key takeaway is learning to explore and adjust configurations manually, especially in window managers like DWM.

The presenter encourages viewers to use the terminal to install additional tools like the AUR helper (yay or paru) and emphasizes the learning process involved with understanding the C language, which is used to build and modify DWM. He also discusses various scripts for managing power menus, bars, and themes within DWM Flexi, and how to customize it further.

By the end of the video, the viewer is encouraged to explore, tweak, and learn the internal workings of DWM Flexi, read the source code, and understand how the system is built, using tools like Visual Studio Code to browse and understand the scripts used in the custom DWM environment. The presenter shares his approach to learning C by reading and analyzing the code with the help of AI and encourages viewers to do the same. The overall focus is on building a personalized, efficient desktop environment using Arch Linux and DWM Flexi, with an emphasis on learning through experimentation and customization.

Video: <https://youtu.be/ppB1STCVyIs>
