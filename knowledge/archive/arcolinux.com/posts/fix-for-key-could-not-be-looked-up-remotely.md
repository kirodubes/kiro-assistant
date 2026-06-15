---
title: "Fix for key could not be looked up remotely"
url: https://arcolinux.com/fix-for-key-could-not-be-looked-up-remotely/
date: 2021-01-06 08:25:28
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fix for key could not be looked up remotely

![](https://arcolinux.com/wp-content/uploads/2018/01/remote-key-could-not-be-looked-up-remotely.jpg)

confirmed  
IT is a port issue @ home  
Network @ work no issue

The HKP protocol uses 11371/tcp for communication. In order to get the signed keys from the servers (using  _pacman-key_), this port is required for communication.

[Arch Wiki link](<https://wiki.archlinux.org/index.php/Pacman/Package_signing>)

quick fix

Video: <https://youtu.be/z0toc92nUQ8>

LONG VERSION

This is the long video. I do not know the solution and we analyze the problem together with the help of the **Arch** **Wiki**.

We have installed ArchMerge 6.2.1 (other ArchMerge and ArchMergeD ssd's are getting the same error) after asking to update with
    
    
    sudo pacman -Syu

Then we get this error about ...

**Key "123456789" could not be looked up remotely.**

First you check the [Arch Wiki](<https://wiki.archlinux.org/index.php/pacman#Error:_key_.220123456789ABCDEF.22_could_not_be_looked_up_remotely>) and read the solution from there.

First thing we try is this
    
    
    sudo pacman-key --refresh-keys

We get an error:

**gpg: keyserver refresh failed : Server indicated a failure**

Second thing we try is to update the **archlinux-keyring** but if you have followed the video than you see that there was no recent update of this package. It is very unlikely that a reinstall will fix our issue.
    
    
    sudo pacman -Sy archlinux-keyring
    sudo pacman -Syu

 

Third attempt is to reset all pacman keys from this [link on Arch Wiki](<https://wiki.archlinux.org/index.php/Pacman/Package_signing#Resetting_all_the_keys>).
    
    
    sudo pacman-key --init
    sudo pacman-key --refresh-keys

 

On any other day this solution will work BUT then it struck me that there might be an issue in communicating with the keyservers.

This is what triggered my search to analyze my issue.

"which might not be possible e.g. behind **proxys** or **firewalls** and results in the stated error"

If you check [this wiki page about gpg](<https://wiki.archlinux.org/index.php/GnuPG>) it is suggested to put a port number behind the keyserver line.

  * If your network blocks ports used for hkp/hkps, you may need to specify port 80, i.e.`pool.sks-keyservers.net:80`



**In my personal case** I need to add a **port** to the get the keys from the keyserver.

There is **no** **communication** between my **computer** and the **keyserver**.

Can be due to a firewall on your personal computer, the firewall on your router, the firewall on your modem or the firewall of your internet service provider. I think the last one since nothing change on my end.

Edit this file and add port 80 behind the line with the keyserver information. Make a backup if you want to.  
That solved my issue. It might solve yours too.
    
    
    subl3 /etc/pacman.d/gnupg/gpg.conf
    
    
    keyserver hkp://pool.sks-keyservers.net:80

You can also use the hkps keyservers and port
    
    
    keyserver hkps://hkps.pool.sks-keyservers.net:443

Video: <https://www.youtube.com/watch?v=VteuMfDzu9w>

SHORT VERSION

We have installed ArchMergeD Awesome (other ArchMerge and ArchMergeD ssd's are getting the same error) after asking to update with
    
    
    sudo pacman -Syu

Then we get this error about ...

**Key "123456789" could not be looked up remotely.**

First you check the [Arch Wiki](<https://wiki.archlinux.org/index.php/pacman#Error:_key_.220123456789ABCDEF.22_could_not_be_looked_up_remotely>) and read the solution from there.

**In my personal case** I need to add a **port** to the get the keys from the keyserver.

There is no communication between my computers and the keyserver.

Can be due to a firewall on your personal computer, the firewall on your router, the firewall on your modem or the firewall of your internet service provider. I think the last one since nothing changed on my end.

Edit this file and **add port 80** behind the line with the **keyserver** information. Make a backup if you want to.  
That solved my issue. It might solve yours too.
    
    
    subl3 /etc/pacman.d/gnupg/gpg.conf
    
    
    keyserver hkp://pool.sks-keyservers.net:80

Video: <https://www.youtube.com/watch?v=4JWrEnjaubM>

**Jansson** package was the reason I could not update that day.

You can always look online which applications need this package.

https://www.archlinux.org/packages/community/x86_64/jansson/

Quite a few important ones in there. So we need to keep it and update it.

Alternative solution

There is also an alternative fix. In the **testing** repositories there is a new **archlinux-keyring** waiting to be added to the core repo (08/01/2018). [Check that information online](<https://www.archlinux.org/packages/?sort=&q=archlinux-keyring&maintainer=&flagged=>). I wondered if installing that package **now** would solve my missing key problem and it did.

**So here is what I did.**
    
    
    subl3 /etc/pacman.conf

Then add the testing repo by deleting the hashtag in front of these lines.
    
    
    #[testing]
    #Include = /etc/pacman.d/mirrorlist

Then get in sync with this new repo.
    
    
    sudo pacman -Sy

Then install this new package. You should notice an higher version number.
    
    
    sudo pacman -S archlinux-keyring

Then put the hastag back in /etc/pacman.conf and sync with the repo's again.
    
    
    sudo pacman -Syu

That solved my issue with the keyserver since there was no need any more to get info from the keyserver. The archlinux-keyring provided the new key for jannson package now and the updates went ahead as usual.

Alternative solution

Use the scripts from ArcoLinuxD to add the keyservers to your system.

You will find it on any desktop. Here is the one from plasma.

[https://github.com/arcolinuxd/arco-plasma/](<https://github.com/arcolinuxd/arco-plasma>)

bottom line

This issue will be fixed once the archlinux-keyring moves  
from testing to core repo.  
No need to add a port then.
