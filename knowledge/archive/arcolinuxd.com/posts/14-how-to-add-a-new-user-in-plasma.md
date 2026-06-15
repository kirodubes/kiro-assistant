---
title: "14 how to add a new user in Plasma"
url: https://www.arcolinuxd.com/14-how-to-add-a-new-user-in-plasma/
date: 2018-11-09 16:45:01
type: post
categories: ["Plasma"]
tags: ["user"]
source_site: arcolinuxd.com
---

# 14 how to add a new user in Plasma

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/john-doe.jpeg)

Adding a new user can always be done via the terminal like this how to on the forum.

But does Plasma come with an gui or graphical user interface to do just the same. 

Type **user** in the menu and you will soon find an application **User Manager**.

Video: <https://youtu.be/ilvLxYW0HE4>

In previous video we had the possibility to "**Enable administrator privileges for this user** " and we did **not**.

If John Doe tries to update the system this is the message he will get this message.

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/nosudo.png)

You could use this option in the situation where you want to give a computer to a child or you want to share your computer with a child and you do not want him or her to have any administrator rights. I have never done is on Linux and do not know what problems you may encounter but I have tried in on Windows (standard user) with very disappointing results. It just took a week or so before I made my son administrator.

> Let us give John Doe administrator privileges and try again.

Check the box like in the picture and save again.

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/userasadministrator.png)

As I imagined the "Log in automatically" is not working if you have lightdm as loginmanager. When we change to [**SDDM**](<https://wiki.archlinux.org/index.php/SDDM>) that will change.

Lightdm is here because it is the standard displaymanager in ALL OUR DESKTOPS.

## **Plasma Challenge**

You can follow our tutorials based on either of two ISO's.

**1\. ArcoLinuxB Plasma (recommended)**

We record the plasma video's on an SSD installed from the **ArcoLinuxB Plasma ISO**.  
You can either **create** your very own ArcoLinuxB Plasma ISO [following this tutorial](<https://arcolinuxb.com/byoi-on-arcolinux-plasma/>) or [download it from Sourceforge](<https://sourceforge.net/projects/arcolinux-community-editions/files/plasma/>). (ArcoLinuxB-plasma-18.11.2.ISO of 4.3 GB - games included)

**2\. ArcoLinuxD Plasma**

You can also use the ArcoLinuxD ISO and then install Plasma with the help of the github scripts. This will not be an exact copy of the ISO.

> Learn about the Plasma desktop and enjoy it.
