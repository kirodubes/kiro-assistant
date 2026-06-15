---
title: "2 Where is the configuration of leftwm"
url: https://www.arcolinuxd.com/2-where-is-the-configuration-of-leftwm/
date: 2021-10-06 14:08:08
type: post
categories: ["Leftwm"]
source_site: arcolinuxd.com
---

# 2 Where is the configuration of leftwm

![](https://www.arcolinuxd.com/wp-content/uploads/2021/10/leftwm-1.jpg)

**Leftwm** is a tiling window manager. The source code can be found on [this github](<https://github.com/leftwm>). You can get more information on the [Arch Wiki](<https://wiki.archlinux.org/title/LeftWM>).

The **conky** is there to help you learn the keyboard shortcuts, when you first boot into Leftwm. Conkies in tiling window managers are not required.

We need to know just one folder

  * ~/.config/leftwm



Read any and all files in this folder to learn what you can change, theme or tweak.

**Polybar** is going to be our menu at the top. [You can read all the articles about polybar here](<https://arcolinux.com/category/arcolinux/design/theming/polybar/>).

The polybar configuration is unique **per** **theme** as is the picom configuration.

The bulk of the keybindings are in **sxhkdrc** but there are also keys in the **config.toml**.  
You can not have doubles are else it will not work.

picom.conf

Picom has 3 big parts in its file.

  * Shadow
  * Opacity
  * Fading



We have an [Arch Wiki page](<https://wiki.archlinux.org/index.php/picom>) to learn even more.

Choose **glx, xr_glx_hybrid** or **xrender as backend**.  
Only if you have trouble with your graphical hardware.

Video: <https://youtu.be/iQYrbfYu2vU>
