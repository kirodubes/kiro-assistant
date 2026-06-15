---
title: "What you need to know about the scripts"
url: https://www.arcolinuxd.com/what-you-need-to-know-about-the-scripts/
date: 2019-12-29 12:34:56
type: page
source_site: arcolinuxd.com
---

# What you need to know about the scripts

When you install software on your computer, you type in the terminal
    
    
    sudo pacman -S ...   
    yay -S ...

When you write these commands in a **file** and make it **executable** , you get a **script**.

Scripts are there to **assist** us when we re-install **ArcoLinuxD** or **Arch Linux**.

They get the job done while we do something else.

need to know

The **numbering** of the scripts will change over time.

The **content** of the scripts will change over time.

The scripts in the **video** will differ from the scripts on the github.

Applications from **AUR** will **fail**. Nothing to do with ArcoLinux.

Applications from **AUR** can be edited in order to get them installed OR wait for a few days. Check the [AUR website](<https://aur.archlinux.org/packages/>) for more information from the maintainer and/or users.

Scripts are there to give you **freedom**. Change them to **your** **liking**. **Add** more applications. **Hashtag** out other lines.

Use **github** or other services to **back** **up** your personal scripts to be reused at a later time.

Script will HALT if there is a problem. Put a hashtag **(#)** before this code "**set -e** " and it will skip the problem and install the rest. Then analyze the problem.
