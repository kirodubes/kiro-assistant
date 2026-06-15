---
title: "7 Changing the weather widget to your personal town"
url: https://www.arcolinuxd.com/7-changing-the-weather-widget-to-your-personal-town/
date: 2018-03-07 18:39:26
type: post
categories: ["Awesome"]
source_site: arcolinuxd.com
---

# 7 Changing the weather widget to your personal town

![](https://www.arcolinuxd.com/wp-content/uploads/2018/03/arcolinux-awesome-openweather-widget.jpg)

We will change the weather widget. It is now set to the weather of Belgium, Antwerp.

We take a look at the top of theme.lua and checkout the variables that are defined at the top.

Search for weather in the theme.lua to find the widget.

Copy/paste the weather link to any webbrowser and find out your city id and copy/paste the city id in the theme.lua then reload your system.

 

Video: <https://www.youtube.com/watch?v=uRYGPZyFP80>

From Celsius to Fahrenheit From Metric to Imperial ![](https://www.arcolinuxd.com/wp-content/uploads/2018/03/arcolinux-awesome-fahrenheit.jpg)

Some of us do not use Celsius but Fahrenheit.   
How do we change the weather widget to Fahrenheit?

We go to theme.lua, look for weather and change the settings. We can change "°C" to "°F" in that line but we need to do more.

We need to edit as well **lain/widget/weather.lua.**

## **Metric to imperial**

 

Video: <https://www.youtube.com/watch?v=1CkxBCtcVrk>
