---
title: "Fix for One or more PGP signatures could not be verified!"
url: https://arcolinux.com/fix-for-one-or-more-pgp-signatures-could-not-be-verified/
date: 2018-12-08 14:05:51
type: post
categories: ["Fixes"]
tags: ["fix"]
source_site: arcolinux.com
---

# Fix for One or more PGP signatures could not be verified!

![](https://arcolinux.com/wp-content/uploads/2018/02/One-or-more-PGP-signatures-could-not-be-verified.jpg)   


In the meantime we have changed our aur helper to **trizen** / **yay** and we will change it probably in future again. Aur helpers have a tendency to come and go.

trizen --skipinteg package-to-install

yay -S --mflags --skipinteg package-to-install

When the installation of an application halts with the error "One or more PGP signatures could not be verified!" and you trust this application, you can bypass this check via the extra options **\--skipinteg**.

We have also two aliases you can try out :

**yayskip**

**trizenskip**

> **Type 'alias' in your terminal to see ALL aliases.**

You can find such information in your local "man".
    
    
    yay ncurses5-compat-libs--mflags --skipinteg

![](https://arcolinux.com/wp-content/uploads/2018/02/vmware.jpg)   


Video: <https://youtu.be/M1-vEgyAfFQ>

  


# SUMMARY

trizen --skipinteg package-to-install

yay -S --mflags --skipinteg package-to-install

 

**Use the aliases**

yayskip

trizenskip
