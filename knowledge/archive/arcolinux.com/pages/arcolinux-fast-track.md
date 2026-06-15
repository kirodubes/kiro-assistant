---
title: "ArcoLinux Fast Track"
url: https://arcolinux.com/arcolinux-fast-track/
date: 2024-03-02 08:13:59
type: page
source_site: arcolinux.com
---

# ArcoLinux Fast Track

Pre-installation

Writing an iso is explained thoroughly in this article.

We start either from

  * Windows
  * macOS
  * Linux



We can also burn an iso with dd (linux) from the terminal.

[Follow the link to know more.](<https://arcolinux.com/everything-you-need-to-know-about-burning-an-iso-to-usb/>)

We provide you with different ways to see if an iso is corrupted or not.

  * sha1
  * sha256
  * md5sum



You will find the checksums on Sourceforge and on Seedhost then you need to check them locally with the information that is supplied online.  
The checksums should match.

[![](https://arcolinux.com/wp-content/uploads/2021/08/checks.jpg)](<https://arcolinux.com/wp-content/uploads/2021/08/checks.jpg>)

https://youtu.be/RC3IN1EuE6o

**Checking the signature or .sig**

This is a more complex thing because of the keyservers not being "up-to-specs" lately.

See that you have **gnupg** installed.

See that you have a **.gnupg** folder.

See that you have a file called gpg.conf in .gnupg with this keyserver in it (just that one) keyserver hkp://keys.openpgp.org:80

Then you can get the key.
    
    
    gpg --recv-keys 74F5DE85A506BF64
    

Then you can verify a download with the sig file.
    
    
    gpg --verify arcolinuxl-v22.03.06-x86_64.iso.sha256.sig
    
    gpg: assuming signed data in 'arcolinuxl-v22.03.06-x86_64.iso.sha256'
    gpg: Signature made Wed 23 Feb 2022 01:36:26 PM CET
    gpg: using RSA key 93D1CCB2B2421F4B1CD0489774F5DE85A506BF64
    gpg: Good signature from "Erik Dubois <erik.dubois@gmail.com>" [ultimate]

We have create an extensive but clear article what you should know about installing linux on your computer.

Once everything is set correctly, you can install any Linux operating system.

[Follow the link to know everything about installing linux - BIOS - UEFI - LEGACY - QUICKBOOT - SECURE BOOT](<https://arcolinux.com/everything-you-need-to-know-about-installing-linux-bios-uefi-motherboard-settings/>)

These days the linux kernel is so far evolved that it will support a wide range of graphical drivers out of the box.

If, however, you really need the proprietary driver of Nvidia then this can be installed. The [Arch Wiki](<https://wiki.archlinux.org/index.php/NVIDIA>) will provide you with a lot of answers.

During the installation process you can choose what nvidia package you would like to install. [See the installation video to see what you can choose.](<https://arcolinux.com/installation/>)

[Follow the link to many nvidia and display related articles.](<https://arcolinux.com/category/arcolinux/general/peripherals/display/>)

We communicate via a [diversity of social media](<http://www.arcolinux.info/arcolinux-editions/>) but we also communicate via Youtube.

We use **playlists** on Youtube to be able to focus on a topic.

[Here is the "ArcoLinux News playlist".](<https://www.youtube.com/playlist?list=PLlloYVGq5pS4c7QXtqCG3ZW0BT7tg_lp0>)

As an ArcoLinux user you need to follow the news on the Arch Linux website.

[This website will provide the latest news from Arch Linux.](<https://www.archlinux.org>)

installation

Calamares is free and is an universal installer framework. That means you can install many Linux distros with it.

You can visit the website [here](<https://calamares.io>).

You can visit the github and report issues [here](<https://github.com/calamares/calamares>).

Calamares is NOT from ArcoLinux.

ArcoLinux believes in and endorses Calamares. We improve the installer by posting issues on the github.

We have an extensive article (30+ videos) just about Calamares called

[All you ever need to know about Calamares - it contains also tutorials about dual-booting and encryption.](<https://arcolinux.com/the-calamares-series-all-you-ever-need-to-know-about-calamares/>)

If you are a **beginner** in Linux we would **advise** **against** dual booting. We often get frustrated people on our forum with problems concerning dual booting.

We recommend installing **just one operating system on a hard disk** or **SSD**. [You can buy a ssd bay and switch ssds that way like in this project](<https://arcolinuxd.com/how-to-mount-an-ssd-bay-in-your-desktop-to-easily-switch-between-windows-and-linux/>). This can help you on a desktop computer but not on a laptop.

However we have many articles about dual-booting if you really need it.

[Follow the link to see our articles about dual-booting.](<https://arcolinux.com/category/arcolinux/general/dual-boot/>)

We have an extensive article (30+ videos) just about Calamares where you learn more about dual-booting.

[All you ever need to know about calamares - it contains also tutorials about dual-booting and encryption.](<https://arcolinux.com/the-calamares-series-all-you-ever-need-to-know-about-calamares/>)

[Check out the Arch Linux Wiki for more information.](<https://wiki.archlinux.org/index.php/Dual_boot_with_Windows>)

[](<https://arcolinux.com/the-calamares-series-all-you-ever-need-to-know-about-calamares/>)

We have an extensive article (30+ videos) just about Calamares. Part of the videos will cover encryption.

[All you ever need to know about calamares - it contains also tutorials about dual-booting and encryption.](<https://arcolinux.com/the-calamares-series-all-you-ever-need-to-know-about-calamares/>)

With every new Calamares we will make a new "**How to install ArcoLinux** " and "**How to install ArcoLinuxD** " on YouTube. The ArcoLinuxB are derivatives of ArcoLinux and the installation procedure is the same. Even those installation videos are created for the users.

[Follow the link to see our article about installing the latest version of ArcoLinux.](<https://arcolinux.com/installation/>)

[Follow the link to see our article about installing the latest version of ArcoLinuxD.](<https://arcolinuxd.com/installation/>)

[Use our forum to solve issues or post your questions.](<http://arcolinuxforum.com>)

[Use our YouTube channel and the search button to find solutions.](<https://youtube.com/erikdubois>)

[Use the playlists of our YouTube channel to find solutions and focus on the topic of the moment.](<https://www.youtube.com/user/maclover696/playlists?view=1&flow=grid>)

Join us on the forum, Discord, Telegram, Facebook, Mewe, YouTube and never miss anything.

Make it possible to help you.

Often language, the lack of technical terms, etc. make it difficult to help users.

This is how you can help us help you. [We have written several articles on how to report effectively.](<https://arcolinux.com/category/arcolinux/help/>)

post-installation

Updating is inherent to all OSs. We recommend you update via the **terminal**. You can also update via graphical GUI applications like pamac-aur or discover.

Updating via terminal has some advantages

  * you get to know the commands and their aliases
  * you see the same texts developers can
  * you see the messages pacman sends
  * you see the warnings, errors or all clear messages
  * you learn how pacman and yay work
  * you learn to know the name of the packages
  * you learn which packages matter
  * you know what you installed



We provide many video's on how to update in order to stay rolling and to never re-install ever again.

[Follow this link to see the current collection of update videos.](<https://arcolinux.com/category/arcolinux/general/update/>)

Every other month there is a release of the iso and every month there is a "**what is new video** " and a "**how to stay rolling video** ". These videos are very educational to watch.

We have a [playlist on YouTube](<https://www.youtube.com/playlist?list=PLlloYVGq5pS5RJROnazR91tD1snkoN-jD>) only about updating or how to stay rolling.

[Here you can find everything you need to know about updating your system - educational version.](<https://arcolinux.com/how-to-update-arcolinux-long-procedure-learn-and-analyze/>)

[Here you can find everything you need to know about updating your system - superfast version.](<https://arcolinux.com/superfast-update-of-arcolinux/>)

We have gathered all the possible things to do after a clean installation in this article.

It will also include the nemesis scripts and the arcogetstarted scripts.

[Follow this link to get more information on what to do after a clean install.](<https://arcolinux.com/things-to-do-after-arcolinux-installation/>)

As a rule the latest linux kernel will always work. Hardware is however very diverse. Sometimes you need to choose a different kernel like linux-lts or linux-zen or linux-hardened or kernels from the AUR. You can also downgrade kernels.

During the ArcoLinux installation Calamares lets you choose between **linux** and **linux-lts** kernel.

[Follow this link to find all our information about kernels.](<https://arcolinux.com/category/arcolinux/general/kernel/>)

Bluetooth is available on ArcoLinux. If you are missing the hardware, you can expand your computer with a bluetooth dongle with a small investment.

[Follow this link to find all articles about bluetooth.](<https://arcolinux.com/tag/bluetooth/>)

For tiling window managers I would like to give you the tip to search our websites for the words **arandr, xrandr and lxrandr** to set your display resolution. Other desktops often have tools available to set your display.

[ Follow this link to see the current articles about resolution.](<https://arcolinux.com/tag/resolution/>)

We have an application called variety. You can use it to set your wallpaper or to change it automatically after a period of time.

[Follow this link to find all articles in the category wallpaper.](<https://arcolinux.com/category/arcolinux/design/wallpaper/>)

Samba is all about sharing data with others. In order to do so you need to set up a samba server. This can be quite complex because it is used in the context of enterprises but on ArcoLinux we keep it simple for the home users, who would like to share data between computers.

[Follow the link to see all your samba related articles.](<https://arcolinux.com/category/arcolinux/applications/samba/>)

pacman is our package manager

The goal is to sync the pacman databases with the command
    
    
    sudo pacman -Sy

Pacman stores the databases locally in /var/lib/pacman/sync/.

The goal is to **sync** the pacman databases with the online databases **with force this time**.

We sync the databases with the command
    
    
    sudo pacman -Syy

Pacman stores the databases locally in /var/lib/pacman/sync/.

The goal is to **sync** the pacman databases with the online databases **and update our system**. ****

We sync the databases with the command
    
    
    sudo pacman -Syu

Pacman stores the databases locally in /var/lib/pacman/sync/.

The goal is to **sync** the pacman databases with the online databases **with force** **and update our system**. ****

We sync the databases with the command
    
    
    sudo pacman -Syyu

Pacman stores the databases locally in /var/lib/pacman/sync/.

> We use this command as our alias for update.

The goal is to install packages.

**Foobar is a fictive package.**
    
    
    sudo pacman -S foobar

In both cases the goal is to install a **bunch** of packages.

GROUP PACKAGES

There are actually **several** packages in one **group**.

Here you can find the list of all package groups.

<https://www.archlinux.org/groups/>

Many of the **desktops** will have a **group** **package** to install a complete desktop. Follow the url and find mate, plasma, xfce4 and xfce4-goodies and so many more.

These are the ones we also use in our [cheatsheet](<http://www.arcolinux.info/documents-arcolinux/>) on ArcoLinux.

You can not uninstall a group package.

 

META PACKAGES

If you do an Arch Way installation one of the first meta packages you will install are
    
    
    pacman -S base

[Read on the Arch Wiki about the difference between group and meta package.](<https://wiki.archlinux.org/index.php/Meta_package_and_package_group>)

Simply put, meta-packages are packages that do nothing but depend on other packages. The result of this is that you can install a group of packages at once by installing a single meta-package. Now, Arch Linux has a similar concept: package groups, and while they serve a similar purpose they are suitably different. The difference is when you add or remove dependencies - groups will not install/remove additional dependencies whereas meta packages will. When a dependency is added our system will install it automatically.

You can uninstall a metapackage.

Removing packages you no longer need can be done with 
    
    
    sudo pacman -R foobar

[The Arch Wiki will show you a summary of the possibilities.](<https://wiki.archlinux.org/index.php/pacman#Removing_packages>)

Removing packages and the dependencies, **which are not required by any other installed package** , can be done with
    
    
    sudo pacman -Rs foobar

[The Arch Wiki will show you a summary of the possibilities.](<https://wiki.archlinux.org/index.php/pacman#Removing_packages>)

To query means to ask. You are asking questions and pacman will respond.

There are more flags possible here but remember that the Q stands for query. You can try these commands out without any harm. You are asking for info. Replace foobar with firefox for example.

sudo pacman -Q foobar  
sudo pacman -Qs foobar  
sudo pacman -Qi foobar  
sudo pacman -Ql foobar  
sudo pacman -Si foobar

[You can find the summary on the Arch Wiki.](<https://wiki.archlinux.org/index.php/pacman#Querying_package_databases>)

If you found a file and you wonder what packages have actually delivered this file then type this
    
    
    sudo pacman -Qo /path/to/file_name

Arch Linux has a way of determining if a package is authentic. [The packages are signed](<https://wiki.archlinux.org/index.php/Pacman/Package_signing>).

In the Arch Linux community developers come and go and with them keys will be deleted and added.

The only thing you have to remember is a package to install if you see a message about the keys.
    
    
    sudo pacman -S archlinux-keyring

This keyring is stored in this folder.
    
    
    /usr/share/pacman/keyrings/

[Here is an example of how to fix issues of this kind.](<https://arcolinux.com/fix-for-key-could-not-be-looked-up-remotely-update-your-archlinux-keyring-first/>)

[Here is another example for "key could not be looked up remotely".](<https://arcolinux.com/fix-for-key-could-not-be-looked-up-remotely/>)

Sometimes you need **one specific key** from a **developer** and the **archlinux-keyring** will not provide you this one. So installing archlinux-keyring
    
    
    sudo pacman -S archlinux-keyring

did not work.

Pacman will mention the key that is missing when updating or installing in the terminal. Use the key to complete the command

I have taken a key as an example. It will look similar to this one.
    
    
    gpg2 --keyserver-options auto-key-retrieve --receive-keys A6234074498E9CEE

After receiving the key (and that can take a while), you can try to update or install again.

![](https://arcolinux.com/wp-content/uploads/2021/08/gpg-key.jpg)

The information to help you with this can be found on this [Arch Linux wiki page](<https://wiki.archlinux.org/index.php/Pacman>).
    
    
    sudo rm -r /etc/pacman.d/gnupg/
    
    
    sudo pacman-key --init
    
    
    sudo pacman-key --populate archlinux
    
    
    sudo pacman-key --populate arcolinux
    
    
    sudo pacman-key --lsign-key 74F5DE85A506BF64

We locally sign to trust the key of ArcoLinux.

We have a script to fix the keys - type the following command in a terminal

> fixkey

When you download packages pacman is going to store it somewhere. You will find them in this folder.
    
    
    /var/cache/pacman/pkg/

The size of this folder can grow over time (if you keep rolling) as it is not automatically cleaned out. The advantage is that you can downgrade a package later.

You can clean up the cache folder and gain a few GB with this command. If we build an iso, it is a good practice to delete the cache as well.
    
    
    sudo pacman -Sc

[Visit the Arch Wiki to learn more about the possibilities.](<https://wiki.archlinux.org/index.php/pacman#Cleaning_the_package_cache>)

The settings for pacman are kept in 
    
    
    /etc/pacman.conf

We only go in there to activate the test repositories.

There is an alias to change the content - for advanced users and beta-testers.
    
    
    npacman

Here you can [find an article about pacman.conf](<https://arcolinux.com/how-to-get-you-submicron-wallpapers-back-and-install-the-new-mirrorlist-for-pacman-conf/>) where we add old repositories back to our pacman.conf to get our submicron wallpapers back.

Your folder /etc/pacman.d/ holds two files. Pacman needs to know where to get its files. These are the source files if you will.

  1. where can I find the packages for Arch Linux aka mirrorlist
  2. where can I find the packages for ArcoLinux aka arcolinux-mirrorlist



The content of arcolinux-mirrorlist is fixed and is now: seedhost (paid) and github (free)

The content of mirrorlist (so just Arch Linux) is fixed by our alias mirror. It will get the fastest Arch Linux servers in your neighborhood.

We have created several aliases to get the fastest Arch Linux servers in your neighborhood.

  * mirror
  * mirrora
  * mirrord
  * mirrors



They are all a little bit different and will result in a different mirrorlist in the /etc/pacman.d folder. See also topic "pacman.d".

Then you can **update** your system and see if you are downloading faster than before.

Sometimes we run out of disk space. This mostly happens on dual boot systems.

You can clean out the cache folder and gain a few GB.
    
    
    sudo pacman -Scc

Pacman stores the databases locally in **/var/lib/pacman/sync/**.

The pacman databases will occasionally get corrupted. Removing the files in this folder and updating your system will create new databases.
    
    
    sudo rm /var/lib/pacman/sync/*
    update

Type in the terminal this command
    
    
    pacman -Suv

You will get all the important places pacman is going to use.
    
    
    Conf File : /etc/pacman.conf
    DB Path : /var/lib/pacman/
    Cache Dirs: /var/cache/pacman/pkg/ 
    Hook Dirs : /usr/share/libalpm/hooks/ /etc/pacman.d/hooks/ 
    Lock File : /var/lib/pacman/db.lck
    Log File : /var/log/pacman.log
    GPG Dir : /etc/pacman.d/gnupg/

[![](https://arcolinux.com/wp-content/uploads/2021/01/pacman-suv.jpg)](<https://arcolinux.com/wp-content/uploads/2021/01/pacman-suv.jpg>)

This a a collection of interesting links

<https://wiki.archlinux.org/index.php/pacman>

<https://wiki.archlinux.org/index.php/Pacman/Tips_and_tricks>

<https://wiki.archlinux.org/index.php/System_maintenance>

 

 

pamac is our graphical package manager

Pamac is a graphical application coming from **Manjaro**. We can install it from the AUR. These days we have it on our repository.

On most ArcoLinux desktops we will include this package.

It has many functionalities

  * install packages
  * remove packages
  * update packages
  * analyze packages on content
  * analyze packages on dependencies
  * AUR packages can be included



We advise you to update your system via the terminal. On this page we explain a way but ultimately it does not matter if you update via a graphical application or via a terminal. The result will be the same.

AUR HELPERS

Yay is what they call an [AUR-helper](<https://wiki.archlinux.org/index.php/AUR_helpers>). It literally helps you install packages from the [AUR](<https://aur.archlinux.org/>).

> Installed by default.

Yay works as a pass-through for pacman. Packages from Arch Linux repositories can also be installed (or removed) that way.
    
    
    sudo pacman -S firefox
    yay -S firefox

But packages that are originate from AUR have to be installed with **yay**. Foobar is a fictive package.
    
    
    yay -S foobar

ArcoLinux wants to have 2 AUR helpers. If one breaks down, we can use the other.

Paru is what they call an [AUR-helper](<https://wiki.archlinux.org/index.php/AUR_helpers>). It literally helps you install packages from the [AUR](<https://aur.archlinux.org/>).

> Installed by default

Paru works as a pass-through for pacman. Packages from Arch Linux repositories can also be installed (or removed) that way.
    
    
    sudo pacman -S firefox
    paru -S firefox

But packages that are originate from AUR have to be installed with **paru**. Foobar is a fictive package.
    
    
    paru -S foobar

ArcoLinux wants to have 2 AUR helpers. If one breaks down, we can use the other.

Trizen is what they call an [AUR-helper](<https://wiki.archlinux.org/index.php/AUR_helpers>). It literally helps you install packages from [AUR](<https://aur.archlinux.org/>).

Trizen also works a pass-through for pacman. Packages from Arch Linux repositories can also be installed (or removed) that way.
    
    
    sudo pacman -S firefox
    trizen -S firefox

But packages that are coming from AUR, they need to be installed with **trizen**. Foobar is a fictive package.
    
    
    trizen -S foobar

ArcoLinux wants to have 2 AUR helpers. If one breaks down, we can use the other.
