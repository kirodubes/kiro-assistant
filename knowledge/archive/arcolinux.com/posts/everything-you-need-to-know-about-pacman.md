---
title: "Everything you need to know about pacman"
url: https://arcolinux.com/everything-you-need-to-know-about-pacman/
date: 2020-11-26 09:22:17
type: post
categories: ["Manage software", "Pacman", "Post-installation"]
source_site: arcolinux.com
---

# Everything you need to know about pacman

Pacman is   
our package manager

We have applications like **pamac** , **discover** or **gnome-software** to install software but there are also **commands** to do the same.

We urge you to **learn** the **commands** that are behind all the GUIs.

Installing Firefox is super simple.
    
    
    sudo pacman -S firefox

Removing Firefox is super simple including dependencies if possible.
    
    
    sudo pacman -Rs firefox

> But you can do so much more with pacman.

![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-s-1.jpg)

Pacman operation : sync

**command** | **example** | **description**  
---|---|---  
sudo pacman -S | sudo pacman -S firefox | Installs the package  
sudo pacman -Sy | sudo pacman -Sy | Sync the pacman database  
sudo pacman -Syy | sudo pacman -Syy | Sync the pacman database with force  
**sudo pacman -Syu** | **sudo pacman -Syu** | Sync the pacman database and update  
sudo pacman -Syyu | sudo pacman -Syyu | Sync the pacman database with force and update or update alias  
sudo pacman -S ... --noconfirm | sudo pacman -S --noconfirm firefox | Installs firefox - if confirmation is needed, always yes  
sudo pacman -S ... --needed | sudo pacman -S --needed firefox | Installs firefox if not yet installed - scripts  
sudo pacman -Sc | sudo pacman -Sc | Cache clean - remove packages no longer installed  
sudo pacman -Scc | sudo pacman -Scc | Cache clean - remove all files from cache  
sudo pacman -Sg | sudo pacman -Sg xfce4 | Show content of group package  
sudo pacman -Si | sudo pacman -Si | Show info of package  
sudo pacman -Sl | sudo pacman -Sl arcolinux_repo | Shows all packages in a repo  
sudo pacman -Ss | sudo pacman -Ss awesome | Search in name and description anywhere  
  
 

![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-si.jpg)![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-Sl.jpg)![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-ss.jpg)

Pacman operation : query

To **query** means to ask.

There are more flags possible here but remember that the Q stands for query. You can try these commands out **without** **any** **harm**. Replace foobar with Firefox for example.

sudo pacman -Q foobar  
sudo pacman -Qs foobar  
sudo pacman -Qi foobar  
sudo pacman -Ql foobar  
sudo pacman -Si foobar

### TIP

If you found a file and you wonder what package has actually delivered this file then type this

sudo pacman -Qo /path/to/file_name

![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-q.jpg)

Pacman operation : File

There are more flags possible here but remember that the F stands for file. You can try these commands out **without** **any** **harm**. Replace foobar with Firefox for example.

sudo pacman -F foobar  
sudo pacman -Fl foobar

 

![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-f.jpg)

Pacman configuration

The settings for pacman are kept in
    
    
    /etc/pacman.conf

We go in there to activate the test repositories for example.

There is an alias to change the content of this configuration file.
    
    
    npacman

Your folder **/etc/pacman.d/** holds two files.

Pacman needs to know where to get its files. These are the source files if you will.

  * where can I find the packages for Arch Linux aka mirrorlist
  * where can I find the packages for ArcoLinux aka arcolinux-mirrorlist



The content of **arcolinux-mirrorlist** is managed by ArcoLinux.

The content of **mirrorlist** is managed by our alias mirror and others.   
It will get the fastest **Arch** **Linux** servers in your neighborhood.

Pacman management

Sometimes we run out of disk space. This mostly happens on dual boot systems.

You can clean out the cache folder and gain a few GB.
    
    
    sudo pacman -Scc

Pacman stores the databases locally in **/var/lib/pacman/sync/**.

The pacman databases will occasionally get **corrupted**. Removing the files in this folder and updating your system will create new databases.
    
    
    sudo rm /var/lib/pacman/sync/*  
    update

Type in the terminal this command

pacman -Suv

You will get all the important places pacman is going to use.
    
    
    Root : /  
    Conf File : /etc/pacman.conf  
    DB Path : /var/lib/pacman/  
    Cache Dirs: /var/cache/pacman/pkg/   
    Hook Dirs : /usr/share/libalpm/hooks/ /etc/pacman.d/hooks/   
    Lock File : /var/lib/pacman/db.lck  
    Log File : /var/log/pacman.log  
    GPG Dir : /etc/pacman.d/gnupg/

![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-suv.jpg)

Pacman and mirror

We have created several aliases to get the fastest Arch Linux servers in your neighborhood.

Pacman will download the packages from these servers.

  * mirror
  * mirrora
  * mirrord
  * mirrors
  * mirrox



They are all a little bit different and will result in a different mirrorlist in the /etc/pacman.d folder.

Then you can **update** your system and see if you are downloading faster than before.

Group and meta packages

In both cases the goal is to install a **list** of **packages**.

**GROUP PACKAGES**

There are actually several packages in one group.

Example:
    
    
    sudo pacman -S xfce4 xfce4-goodies

That is all that is needed to have a complete Xfce4 desktop.

Here you can find the list of all package groups.

<https://www.archlinux.org/groups/>

Many of the desktops will have a group package to install a list of packages.   
Follow the link above and find mate, mate-extra, plasma, xfce4 and xfce4-goodies and so many more.

These are the ones we also use in our cheatsheet on ArcoLinux.

You can **not** **uninstall** a group package.

 

**META PACKAGES**

If you do an Arch Way installation one of the first meta packages you will install are
    
    
    pacman -S base

Read on the Arch Wiki about the difference between group and meta package.

Simply put, meta-packages are packages that do nothing but depend on other packages. The result of this is that you can install a group of packages at once by installing a single meta-package. Now, Arch Linux has a similar concept: package groups, and while they serve a similar purpose they are suitably different. The difference is when you add or remove dependencies - groups will not install/remove additional dependencies whereas meta packages will. When a dependency is added our system will install it automatically.

You **can** **uninstall** a metapackage.

Following code may remove too much so reinstall what you need. 
    
    
    sudo pacman -Rscn gnome

will remove this group package. You can also try this one 
    
    
    sudo pacman -Runs gnome

I do sometimes the same with Kodi.![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-Sg.jpg)

Local help : read your "man pacman"

Type this command in the terminal
    
    
    man pacman

![](https://arcolinux.com/wp-content/uploads/2021/01/manpacman.jpg)

Online help 

<https://wiki.archlinux.org/index.php/pacman>

<https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks>

<https://wiki.archlinux.org/index.php/System_maintenance>
