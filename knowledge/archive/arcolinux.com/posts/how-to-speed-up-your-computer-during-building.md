---
title: "How to speed up your computer during building"
url: https://arcolinux.com/how-to-speed-up-your-computer-during-building/
date: 2018-02-04 23:06:00
type: post
categories: ["Fixes", "Manage software", "Post-installation", "Update"]
tags: ["fix"]
source_site: arcolinux.com
---

# How to speed up your computer during building

The file **/etc/makepkg.conf** can be edited so that it will use **all available cores when you are building packages coming from the AUR.**

**The more cores, you have, the more you have to gain with these settings**.

Use "**lscpu** " to see how many cores your system has. That is important for our settings.

[![](https://arcolinux.com/wp-content/uploads/2018/02/lscpu.png)](<https://arcolinux.com/wp-content/uploads/2018/02/lscpu.png>)

You can see in the white line that I have 8 cores.

Then you can start editing the **/etc/makepkg.conf** file with **Sublime-text**.

I have in my system 8 cores so I will change the **j2** to **j9**.  
**Rule of thumb is one more than the number of cores.**

**Tip 1**

Change this line
    
    
    #MAKEFLAGS="-j2"

into
    
    
    MAKEFLAGS="-j9"

[Read on the wiki for more info.](<https://wiki.archlinux.org/index.php/Makepkg#Improving_compile_times>)

In the wiki they give an other solution. You can also use the following line - you do not need to know the number of cores. Arch linux will fill the number of cores.
    
    
    MAKEFLAGS="-j$(nproc)"

**Be aware** that on some computers nproc has been known to report the wrong number of cpu's. Always check.

**Tip 2**

Here we actually give in the number of cores so **-T 8**

Change this line
    
    
    COMPRESSXZ=(xz -c -z -)

into
    
    
    COMPRESSXZ=(xz -c -T 8 -z -)

If we follow [this link to the Arch wiki](<https://wiki.archlinux.org/index.php/Makepkg#Utilizing_multiple_cores_on_compression>) and read the text we can also use the following code to compress using all our cores
    
    
    COMPRESSXZ=(xz -c -z - --threads=0)

or
    
    
    COMPRESSXZ=(xz -c -T 0 -z -)

****

**Tip 3**  
As of **ArchMerge 6.5.1** we have included a **script** to automatically set your makepkg.conf to the correct number of cores. You can find it in
    
    
    ~/.config/openbox/scripts

Video: <https://www.youtube.com/watch?v=VkAC0Tqascw>

Join us in testing the speed of your computer Setting up test environment We will test with the application **polybar** and we will install "**termdown** " to have a timer in the terminal with packer. 
    
    
    packer termdown

The timer can be reset with R and spacebar pauses the counter and numbers turn green. Start it in the terminal with "termdown". Desktop Computer test ![](https://arcolinux.com/wp-content/uploads/2018/02/inxi-desktop.png)Before the tweaks ![](https://arcolinux.com/wp-content/uploads/2018/02/desktop-polybar-cpu2.jpg)After the tweaks ![](https://arcolinux.com/wp-content/uploads/2018/02/desktop-polybar-cpu8.jpg)Conclusion **We have gained 170 seconds - 55 seconds = 115 seconds or almost 2 minutes.** Notice the **conky** that shows we have used the full 100% of the cpu in the last picture BUT not in the previous picture. Join us in testing the speed of your computer Setting up test environment We will test with the application **polybar** and we will install "**termdown** " to have a timer in the terminal with packer. 
    
    
    packer termdown

The timer can be reset with R and spacebar pauses the counter and numbers turn green. Start it in the terminal with "termdown". LAPTOP Computer test ![](https://arcolinux.com/wp-content/uploads/2018/02/laptop-inxi.jpg)Before the tweaks ![](https://arcolinux.com/wp-content/uploads/2018/02/cpu2.jpg)After the tweaks ![](https://arcolinux.com/wp-content/uploads/2018/02/laptop-polybar-cpu4.jpg)Conclusion **We have gained 321 seconds - 168 seconds = 153 seconds or 2 and half minutes.** Tip : **Htop** confirms that I have indeed 8 cores at the top. ![](https://arcolinux.com/wp-content/uploads/2018/02/htop-8cores.png)
