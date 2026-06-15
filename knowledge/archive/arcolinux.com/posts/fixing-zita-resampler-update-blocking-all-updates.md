---
title: "Fixing zita-resampler update blocking all updates"
url: https://arcolinux.com/fixing-zita-resampler-update-blocking-all-updates/
date: 2018-02-22 14:21:10
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fixing zita-resampler update blocking all updates

![](https://arcolinux.com/wp-content/uploads/2018/02/zita-resampler.jpg)This video is purely for educational reasons. Why? Because in a few days time this problem will not be there anymore. If you update your system and you get a message like **error: failed to commit transaction (conflicting files)** then you have 3 options. 

  1. wait until a new update comes in - typically takes 1-3 days RE-EDIT : In this case we need to intervene manually - see bottom of page - communication from Arch Linux.
  2. work around the problem with pamac (unselect the issue)
  3. analyze and solve it yourself.

**It is for option 3 that I made this article.** **How do you analyze the issue?**

Video: <https://www.youtube.com/watch?v=wXvu0zR9tN0>

# Tip 1

In case of errors always check the [Arch Linux website](<https://www.archlinux.org>). A few hours later we get the news. 

#### [zita-resampler 1.6.0-1 -> 2 update requires manual intervention](<https://www.archlinux.org/news/zita-resampler-160-1-2-update-requires-manual-intervention/> "View full article: zita-resampler 1.6.0-1 -> 2 update requires manual intervention")

2018-02-22

The zita-resampler 1.6.0-1 package was missing a library symlink that has been readded in 1.6.0-2. If you installed 1.6.0-1, ldconfig would have created this symlink at install time, and it will conflict with the one included in 1.6.0-2. In that case, remove /usr/lib/libzita-resampler.so.1 manually before updating. 

# Tip 2

 

You can also install an application that will get you this information from the net. It is called **pacmatic** and is a tip from Diëggho Oliver, a user. It will stay in your **terminal**.

Install it with
    
    
    sudo pacman -S pacmatic

and run it with
    
    
    sudo pacmatic -Syu

It will take the options from pacman.

The same text appears now in your terminal.
    
    
    The zita-resampler 1.6.0-1 package was missing a library symlink that has been readded in 1.6.0-2. If you installed 1.6.0-1, ldconfig would have created this symlink at install time, and it will conflict with the one included in 1.6.0-2. In that case, remove /usr/lib/libzita-resampler.so.1 manually before updating.
