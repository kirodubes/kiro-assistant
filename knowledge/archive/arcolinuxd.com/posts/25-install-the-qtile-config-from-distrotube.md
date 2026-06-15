---
title: "25 Install the Qtile config from DistroTube"
url: https://www.arcolinuxd.com/25-install-the-qtile-config-from-distrotube/
date: 2024-03-02 07:41:38
type: post
categories: ["Qtile"]
source_site: arcolinuxd.com
---

# 25 Install the Qtile config from DistroTube

![](https://www.arcolinuxd.com/wp-content/uploads/2024/03/qtile-distrotube.jpg)

> sudo pacman -S arcolinux-qtile-distrotube-git

> we do use the ArcoLinux keybindings

The video starts with the presenter expressing their admiration for ArcoLinux, an Arch-based Linux distribution, and sharing the news that ArcoLinux has included their qtile configuration file in their repositories, which can be installed via the Pacman package manager. The presenter is flattered by this gesture and decides to explore how ArcoLinux has integrated their qtile configuration by setting up a virtual machine with ArcoLinuxB Qtile Edition.

The presenter guides viewers through the installation process and advises selecting the X11 version of qtile over the experimental Wayland version for stability. After logging into ArcoLinux, they demonstrate how to update the system and install their qtile configuration package from the ArcoLinux repositories. The process involves replacing the standard Qtile package with the presenter's version.

The video then covers how to navigate the Linux file system to locate and understand the purpose of the **/etc/skel** directory, which serves as a template for new user home directories. The presenter copies their Qtile configuration files from /etc/skel to their home directory to apply their customizations.

Further, the presenter tweaks the virtual machine's screen resolution for optimal display and restarts Qtile to apply the changes, encountering and resolving a minor issue with the screen resolution setting.

The presenter also attempts to set up their Emacs configuration in the new system but faces some challenges with package installation and config file locations. They demonstrate troubleshooting steps, including removing conflicting directories and restarting Emacs to apply their custom configuration.

Throughout the video, the presenter emphasizes the community aspect of free and open-source software, expressing gratitude to the ArcoLinux team for recognizing their work and sharing it with the community.

Video: <https://youtu.be/WkTgIN3qJno>
