---
title: "How to install and set any cursor theme"
url: https://arcolinux.com/how-to-install-any-cursor-theme/
date: 2020-10-02 06:55:33
type: post
categories: ["Cursors", "Must read"]
tags: ["pkgbuild", "theming"]
source_site: arcolinux.com
---

# How to install and set any cursor theme

![](https://arcolinux.com/wp-content/uploads/2018/06/oxy-neon.jpg)

Where to download cursor themes?

The **AUR** or Arch User Repository includes already the best of cursor themes out there.

Type the following text in your terminal
    
    
    yay cursor  
    paru cusor  
    trizen cursor

Choose a number and install it.

It will be installed in **/usr/share/icons**.

**Or** you find yourself another source like <https://www.gnome-look.org>.

In the video we are going to test out this cursor **Oxygen Neon**.  
<https://www.gnome-look.org/p/999997/>

You need to extract the file and put it into your**~/.icons** or create the folder, if you do not have it. There must be a **dot** in front of the word **icons**.

Where to set your cursor

Depending on the desktop you are using, you need to set your cursor via different applications.

We are on **Xfce** and there is an icon in Xfce settings to set your cursor : **mouse and touchpad**

![](https://arcolinux.com/wp-content/uploads/2018/06/mouseandtouchpad.jpg)

 

But there are also other applications and many other desktops including Tiling Window Managers.

They will often change the settings in two files

**~/.gtkrc-2.0**

**~/.config/gtk-3.0/settings.ini**

**~/.icons/default**

and there is also an icon theme set as **default** in **ArcoLinux**.

**Check this folder /usr/share/icons/default**

You will find the file index.theme with this content (fix for mouse in plasma changing all the time)
    
    
    [Icon Theme]
    Inherits=Bibata-Modern-Ice

Standard it is set to **Bibata-Modern-Ice**. If you want an other cursor **EVERYWHERE** , you need to change this one too.

**On 05/10/2020 the developer changed the name of Bibata_Ice to Bibata-Modern-Ice.**

Depending on the desktop you look for applications to change the cursor. Check the files mentioned above and change the settings manually, if needed.

Check also **lxappearance** to set the cursor.

Other systems like for example **Gnome** , **Budgie** , **Cinnamon** and **Mate** store the setting in the **~/.config/dconf** folder. Set the cursor via the settings of the desktop.

**Plasma** saves it settings in the **~/.local** folder. You will find a icons folder in there.

Sometimes we set the cursor theme within the **configuration** file of a **Tiling** **Window** **Manager**.

THE CURSOR theme IS NOT APPLIED?

DID YOU TRY  
TURNING IT OFF  
AND ON AGAIN

At some point we changed our default cursor from  
Breeze_Snow  
to  
Bibata_Ice

Video: <https://www.youtube.com/watch?v=-IQd_Qt4CJ8>

WHAT IF ...

I create a pkgbuild for the Arch Linux Community

Manjaro, antergos, ... all can use it

### [Here is a complete list of all the distros that are based on Arch Linux.](<https://wiki.archlinux.org/index.php/Arch-based_distributions>)

AUR = Arch **User** Repository - User is someone like **you** and **me**. We show you **what** to read and what to do if you want to make your own recipe to install a **cursor theme oxy-neon**. I do not show how to put this pkgbuild on the AUR. That will be for later.

  * <https://wiki.archlinux.org/index.php/creating_packages>
  * <https://wiki.archlinux.org/index.php/Arch_packaging_standards>
  * <https://wiki.archlinux.org/index.php/PKGBUILD>
  * <https://wiki.archlinux.org/index.php/makepkg>



This cursor theme can now be installed via  
YAY OXY-NEON

Since the **downlink** from the **video** is never going to be a static one, I will host this file and any future files on my personal github: <https://github.com/erikdubois/gnome-look>.

Using the download link from github the source will remain stable to be used in the pkgbuild.

Read the final pkgbuild here : https://aur.archlinux.org/packages/oxy-neon/

Video: <https://www.youtube.com/watch?v=8YlkUxG8kLw>

Name change from Bibata_Ice to Bibata-Modern-Ice

Video: <https://youtu.be/-eVFrHyTy5A>

Sometimes your cursor is set via the local ~/.icons folder

change it also there or remove it

Video: <https://youtu.be/xGHdpT_VOGw>

TIP : remove all the cursors you do not want
