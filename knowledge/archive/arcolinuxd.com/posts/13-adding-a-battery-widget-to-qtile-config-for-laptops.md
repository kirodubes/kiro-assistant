---
title: "13 adding a battery widget to qtile config for laptops"
url: https://www.arcolinuxd.com/13-adding-a-battery-widget-to-qtile-config-for-laptops/
date: 2019-05-28 14:19:54
type: post
categories: ["Qtile"]
source_site: arcolinuxd.com
---

# 13 adding a battery widget to qtile config for laptops

![](https://www.arcolinuxd.com/wp-content/uploads/2019/05/arcolinuxb-qtile-battery-options.jpg)

# Choose between 4 widgets

In the configuration file for qtile ~/.config/qtile/config.py you can remove the '#' in front of the widgets you like.

In above image there are 4 ways to show you the status of your battery on a laptop.

Choose 1 and reload the config with Super + Shift + R.

One widget (horizontal battery icons) uses our own script arcobattery.py. It points to a folder/file that needs to exist on your hardware.

The battery is called **BAT0** in the script but it can have other names as well. You may need to edit this file to reflect the difference in hardware like **BAT1**...

It points to a file that is **either there or not**. It may end in not showing the widget or breaking the qtile desktop.

Check how your battery is called on your hardware in **/sys/class/power_supply**

Video: <https://www.youtube.com/watch?v=QFwbYLDalh0>
