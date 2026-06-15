---
title: "How to update any ArcoLinux or how to stay rolling"
url: https://arcolinux.com/how-to-update-any-arcolinux-or-stay-rolling/
date: 2018-12-02 14:30:16
type: post
categories: ["Update", "Utilities"]
tags: ["update"]
source_site: arcolinux.com
---

# How to update any ArcoLinux or how to stay rolling

Long procedure to update

![](https://arcolinux.com/wp-content/uploads/2018/11/long-proc-update.jpeg)

If you want to **learn** more about your system and **keep** **track** of what changed then this procedure is for you.

**1 - bupskel**

Will create a backup folder of /etc/skel prior to your updates

**2 - update**

Will download and install all **Arch** Linux and **ArcoLinux** packages

**3 - bupskel**

Will create a backup folder of /etc/skel after your updates

**4 - meld**

Compare both backup folders of /etc/skel to see what changed (see video)

**5 - skel**

Will copy/paste all config files from /etc/skel to your home directory

**6 - upall is currently used instead of pksyua  
**

Now we update the rest - Only **AUR** packages will now be updated.

short procedure to update

![](https://arcolinux.com/wp-content/uploads/2018/11/short-proc-update.jpeg)

If you want to quickly and gradually update your system then this procedure is for you.

**1 - update**

Will download and install all **Arch** Linux and **ArcoLinux** packages

**2 - skel**

Will copy/paste all config files from /etc/skel to your home directory

**3 - upall or pksyua**

Now we update the rest - Only **AUR** packages will now be updated.

Video: <https://www.youtube.com/watch?v=ZC2Xr5h0Lms>

FASTEST procedure to update

![](https://arcolinux.com/wp-content/uploads/2018/11/fastest-proc-update.jpeg)

You can also type "**pksyua** " (Arch Linux, ArcoLinux and AUR will be updated in one go)  
**+**  
**skel**

Check with meld if   
.bashrc   
and  
.bashrc-latest  
are the same  
There may be new aliases

or say never mind   
and use the alias

cb

## New alias - cb or copy bash

 

We always compare 2 files after a **skel**. 

The working .**bashrc** and the newest **.bashrc-latest** are being compared and we get the new lines in.

There is now an alias to just copy/paste the one over the other.

After typing **skel** , you type **cb** and the .bashrc will be **overwritten** with the .bashrc-latest.

Video: <https://youtu.be/pQ8J-mVe9S4>

If you have personal aliases then you can add those to a personal file so they will never be overwritten when you update.

[Check out this article for more info.](<https://arcolinux.com/add-your-personal-aliases-to-bashrc-the-smart-way/>)

Playlist on Youtube - how to update ArcoLinux

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS5RJROnazR91tD1snkoN-jD>
