---
title: "Checking out the aliases on your system can be quite interesting"
url: https://arcolinux.com/checking-out-the-aliases-on-your-system-can-be-quite-interesting/
date: 2018-10-09 21:24:17
type: post
categories: ["Terminal", "Utilities"]
tags: ["terminal"]
source_site: arcolinux.com
---

# Checking out the aliases on your system can be quite interesting

![](https://arcolinux.com/wp-content/uploads/2018/10/aliases.jpg) This is a command that just works on any Linux system. Type in the terminal the command **alias** and you will get the list of all possible aliases on that system. Making a new one is super easy. For example when you type **inxi** you get just 3 lines of information. If you type **inxi -b** you get a lot more. You can add an alias that will change the **inxi** command in the **inxi -b** command like this 
    
    
    alias inxi='inxi -b'

and add it to the **.bashrc**. Bashrc will be read each time you login and the aliases will be applied. **In this video you will see the 5 new aliases in action.**

  1. **skel** will copy/paste everything from /etc/skel to your home directory
  2. **hw** is an application that will give you hardware info
  3. **kc** will kill all conkies
  4. **yayskip** will skip integrity checks when installing
  5. **trizenskip** will skip integrity checks when installing

 

Video: <https://youtu.be/DftBmbRsESE>
