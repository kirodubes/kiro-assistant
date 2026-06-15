---
title: "How to set virtualbox the correct way - graphics controller - workflow"
url: https://arcolinux.com/how-to-set-virtualbox-6-the-correct-way-graphical-controller-workflow/
date: 2020-01-02 15:37:16
type: post
categories: ["Virtual Machines"]
tags: ["anydesktop", "virtual machines"]
source_site: arcolinux.com
---

# How to set virtualbox the correct way - graphics controller - workflow

![](https://arcolinux.com/wp-content/uploads/2020/01/virtualbox-setup.jpg)

My current settings on **January 2020**.

The settings I have been using all the time on Virtualbox 5 are all the same **EXCEPT ONE**.

I learned it the hard way and I want you to save the time with this article.

> Make sure you set the graphics controller to **VBoxSVGA**
> 
> Do not enable 3D acceleration
> 
> ****

**VMSVGA** is what Virtualbox will set as **standard**.

**VMSVGA** is VMware's SVGA II graphics adapter. **If not changed you will end up in a very small window.**

In the video I will also explain my workflow and the use of a template.

It lets you make copies or clones so you can go back at any time and restart again.

Video: <https://youtu.be/zW03Vs2CVZo>
