---
title: "Everything you need to know about keys"
url: https://arcolinux.com/everything-you-need-to-know-about-keys/
date: 2022-10-02 14:47:55
type: post
categories: ["Pacman", "Pamac", "Post-installation", "Terminal"]
source_site: arcolinux.com
---

# Everything you need to know about keys

The package manager from Arch Linux aka **pacman** works with signed packages. To sign a package you need key. To be able to install a package you need a key.

There is the "**archlinux-keyring** " package that will need an update from time to time and there is the "**arcolinux-keyring** ".
    
    
    sudo pacman -Sy archlinux-keyring

Depending on your situation you often have to **FIRST install the archlinux-keyring BEFORE you can update**.

If the erik.dubois key is forgotten, deleted, obliterated or anything else we type one of the following aliases in a terminal.
    
    
    alias keyfix="/usr/local/bin/arcolinux-fix-pacman-databases-and-keys"
    alias key-fix="/usr/local/bin/arcolinux-fix-pacman-databases-and-keys"
    alias keys-fix="/usr/local/bin/arcolinux-fix-pacman-databases-and-keys"
    alias fixkey="/usr/local/bin/arcolinux-fix-pacman-databases-and-keys"
    alias fixkeys="/usr/local/bin/arcolinux-fix-pacman-databases-and-keys"
    alias fix-key="/usr/local/bin/arcolinux-fix-pacman-databases-and-keys"
    alias fix-keys="/usr/local/bin/arcolinux-fix-pacman-databases-and-keys"

You can find all these aliases in the bashrc or zshrc of fish config.

They all point to one file with **this content** (09/2022).

echo "###############################################################################"  
echo "Removing the pacman databases at /var/lib/pacman/sync/*"  
echo "###############################################################################"  
echo  
sudo rm /var/lib/pacman/sync/*  
echo

echo "###############################################################################"  
echo "Removing /etc/pacman.d/gnupg folder"  
echo "###############################################################################"  
echo  
sudo rm -rf /etc/pacman.d/gnupg/*  
echo

echo "###############################################################################"  
echo "Initialize pacman keys with pacman-key --init"  
echo "###############################################################################"  
echo  
sudo pacman-key --init  
echo

echo "###############################################################################"  
echo "Populating keyring with pacman-key --populate"  
echo "###############################################################################"  
echo  
sudo pacman-key --populate  
echo

echo "###############################################################################"  
echo "Getting new databasesw with pacman -Sy"  
echo "###############################################################################"  
echo  
sudo pacman -Sy  
echo

echo "###############################################################################"  
echo "### DONE - YOU CAN CLOSE THIS WINDOW ####"  
echo "###############################################################################"

After running these commands you will be able to download and update again.

**You will have fixed any and all keys like the chaotics and endeavouros keys as well.**

 

Video: <https://youtu.be/lPVDxVs_9Qg>

In case everything turns south you always have the ArchLinux Tweak Tool or ATT to install the ArchLinux keyring or fix the keys.

> The ATT to the rescue

![](https://arcolinux.com/wp-content/uploads/2022/10/fixkey.jpg)

If you do not have the script to fix the keys then type the commands yourself in a terminal.

Video: <https://youtu.be/KYyk1_Iz69g>

ARCOLINUX KEY IS UNKNOWN MESSAGE  
remove pacman-init.service  
FIXKEY  
ADD KEYSERVERS

Possible keyservers - test out and remove the hashtag 
    
    
    #keyserver hkp://keys.openpgp.org
    #keyserver hkp://keys.openpgp.org:80
    #keyserver hkps://keys.openpgp.org
    #keyserver hkps://keys.openpgp.org:443
    #keyserver hkps://keyserver.ubuntu.com:443
    keyserver hkp://keyserver.ubuntu.com:80
    #keyserver hkp://pool.sks-keyservers.net:80
    #keyserver hkps://hkps.pool.sks-keyservers.net:443
    #keyserver hkp://ipv4.pool.sks-keyservers.net:11371

Check out these two aliases to help with keys.

**fix-keyserver**
    
    
    alias fix-keyserver='[ -d ~/.gnupg ] || mkdir ~/.gnupg ; cp /etc/pacman.d/gnupg/gpg.conf ~/.gnupg/ ; echo '\''done'\'''

**fix-pacman-keyserver**
    
    
    alias fix-pacman-keyserver='/usr/local/bin/arcolinux-fix-pacman-gpg-conf'

Video: <https://youtu.be/ROLVePGlKuU>

when updating an Arch Linux system  
you may need the knowledge of the keys

Video: <https://youtu.be/p-fET96yewg>

playlist of all update videos  
on youtube

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS5RJROnazR91tD1snkoN-jD>
