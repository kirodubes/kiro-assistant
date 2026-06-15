---
title: "In order to use redshift you need to know 3 tips"
url: https://arcolinux.com/in-order-to-use-redshift-you-need-to-know-2-tips/
date: 2019-04-06 08:10:17
type: post
categories: ["Utilities"]
source_site: arcolinux.com
---

# In order to use redshift you need to know 3 tips

![](https://arcolinux.com/wp-content/uploads/2019/03/redshift.jpg)

Redshift had been deleted from the iso in the past because it did not work. As of 19.03 version it is back on the iso and it includes a fix.

People who stay rolling install it like this
    
    
    sudo pacman -S redshift

## Tip 1 :

Make sure /etc/geoclue/geoclue.conf contains these lines at the bottom (starting from 19.03 it is present)

**[redshift]**  
**allowed=true**  
**system=false**  
**users=**

 

## Tip 2 :

Launch redshift the first time in a terminal. **This applies to all users!**

**You hardly see the effect of redshift in the video if at all.  
**

Check your own systems at daybreak, nightfall and at night.

## Tip 3 :

**If you use HBLOCK** then remember to check if you deleted the hashtag in front of

**/etc/hblockd/whitelist.list**

**location.services.mozilla.com**

![](https://arcolinux.com/wp-content/uploads/2019/03/redshift-1.jpg)

Video: <https://youtu.be/YkDg68rQbqk>
