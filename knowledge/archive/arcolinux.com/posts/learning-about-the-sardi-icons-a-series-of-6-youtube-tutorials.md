---
title: "Learning about the Sardi icons - a series of 6 youtube tutorials"
url: https://arcolinux.com/learning-about-the-sardi-icons-a-series-of-6-youtube-tutorials/
date: 2018-02-16 15:52:09
type: post
categories: ["Icons"]
tags: ["gpick"]
source_site: arcolinux.com
---

# Learning about the Sardi icons - a series of 6 youtube tutorials

Sardi icons has 20 icon themes Sardi Extra icons has 106 icon themes In total 126 icon themes Create your own icon theme Inherits is a magical word 

# 1\. Showcase of the Sardi icons

Video: <https://www.youtube.com/watch?v=45N4XAxogvo>

In this video we show you all the variations of the standard Sardi icons. **There are 6 (not 5) important icon themes.** I will use the term "**engine** " from now on to point out that that theme pulls the rest of the "wagons". An example would be Sardi Flat Colora. It is a wagon. It only contains icons for places and nothing more. The rest of the icons are coming from our "engine" called Sardi Flat. The inherits line in the index.theme takes care of that. 

  * **Sardi** is the **most** **important**
  * Sardi Flat
  * Sardi Flexible
  * Sardi Ghost Flexible
  * Sardi Mono
  * Sardi Orb Colora

Sardi Orb Colora was added as the last one. It is the flat icon theme with an inner circle. 

# 2\. Installation of the Sardi icons

Video: <https://www.youtube.com/watch?v=XXpltliaxPs>

# Option 1 : sourceforge

You can download the sardi icons from [sourceforge](<https://sourceforge.net/projects/sardi/>).

Then you extract the downloaded package and copy/paste them to your home folder in this folder
    
    
    ~/.icons

 

# Option 2 : AUR

Arch users like Arch Linux, Antergos, Manjaro, ArcoLinux, ArchMerge, ArchLabs, and more can use the AUR.
    
    
    yaourt -S sardi-icons

or
    
    
    packer sardi-icons

or use other AUR helpers.

# 3\. Flexibility of the Sardi icons - run scripts

Video: <https://www.youtube.com/watch?v=bVswaGHpKm8>

When we start this video I realise that on this "Fun" ssd I had already installed the Sardi Extra icons, which will be covered in the last video.

Therefor I am going to delete these icons.

Skip to 3:20 if you are not on an Arch based distro.

This information is only relevant for people using an **ARCH** BASED DISTRO.

It is quite an important tip that is why it is in there.

**Installing icons is one thing but uninstalling can be even more important.**

You can find these script on the [ArcoLinux Nemesis github](<https://github.com/erikdubois/Arcolinux-Nemesis>).

Sardi should be in ~/.icons We explain in this video how important the "engines" are and how the icon themes know where to get the rest of their icons via the inherits line like Sardi-Arc. Then we explain what a **.sh** file is. We can run these scripts. If we forget to make a script executable, you can do it yourself via right mouse click and make it executable or via command **chmod +x** ... Procedure to follow 

  1. copy/paste icon folder and rename it
  2. change index.theme to the correct name
  3. run script
  4. change to newly created theme



# 4\. Flexibility of the Sardi icons - edit scripts

Video: <https://www.youtube.com/watch?v=ENCHcy7m3_A>

In previous video we ran the scripts present in the folders. This time we are going to use colors from a wallpaper, we like, to make our own new theme. We will have to choose a name for that new theme. **Gpick** is our tool to figure out the hexadecimal color code. Every desktop out there has its own **color** **picker**. The first "**Halloween** " icon theme had just **one** **color** to change. There are other icons in there that are build up out of **3 or 4 colors**. I like to use **inkscape** as my creation tool "my canvas" to see if colors are a match or not. Use the CTRL key to select the color in inkscape. Procedure to follow 

  1. copy/paste icon folder and rename it
  2. change index.theme to the correct name
  3. copy/paste change-color.sh and rename it
  4. look for matching colors in inkscape
  5. change color in the new script
  6. run script
  7. change to newly created theme



# 5\. Modularity of the Sardi icons

Video: <https://www.youtube.com/watch?v=lFl4phYbKSk>

In this video we will use the **inherits** line to put our "wagon" behind an other "engine". In the video series Sardi-Mono-Numix-Colora-**Pokemon** had been created in previous video and we want to have **Sardi** icons rather than **Sardi Mono** icons. Change the Inherits line in the index.theme and you can have that. **That is the modularity of Sardi.** **Putting your wagon behind an other engine.** You can use the modularity between the Sardi folders or Surfn folders. 

## **You can also mix icons like Sardi and Halo.**

To follow the tutorial you can download the Halo icons from [here.](<https://github.com/erikdubois/Halo-icons>) ArchMerge users have it installed on their system. **2 projects for you to try** Procedure to follow 

  1. copy/paste icon folder and rename it
  2. change index.theme to the correct name
  3. change the inherits line
  4. run the create icon cache script
  5. change to newly created theme



# 6\. Sardi Extra icons

# We will show you 126 created icon themes so far

Video: <https://www.youtube.com/watch?v=33wwbQtfCdE>

If you have followed the series about Sardi you know Sardi provides us **flexibility** and **modularity**.

If you start running all the scripts and start mixing icon themes, you get a lot of icon themes.

We store those created icon themes on the Sardi Extra github.

[Download all the created icon themes from the github.](<https://github.com/erikdubois/Sardi-Extra>)

People that are working on an **Arch Linux** based distribution can use the **AUR** and install any of the packages from there via **packer** or **yaourt** or any other **AUR** helper.

I will use my personal scripts on my [ArcoLinux Nemesis github](<https://github.com/erikdubois/arcolinux-Nemesis>) to easily install and uninstall all the Sardi Extra icons.

# Tip FOR ARCH USERS : Use ARCOLINUX Nemesis github  
<https://github.com/erikdubois/arcolinux-Nemesis>

Video: <https://www.youtube.com/watch?v=7I5RfR2iiAQ>

### All Arch Linux, ArcOLINUX, Antergos, Manjaro, ArchLabs, ... USERS can use this tip as well.
