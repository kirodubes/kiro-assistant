---
title: "8 getting to know the structure of xmonad.hs"
url: https://www.arcolinuxd.com/8-getting-to-know-the-structure-of-xmonad-hs/
date: 2019-01-18 12:00:04
type: post
categories: ["Xmonad"]
source_site: arcolinuxd.com
---

# 8 getting to know the structure of xmonad.hs

![](https://www.arcolinuxd.com/wp-content/uploads/2019/01/arcolinuxb-xmonad-hmonad.jpg)

Before we get into the details of xmonad.hs it is a good thing to first setup your workflow as in this [article](<https://www.arcolinuxd.com/4-setting-up-your-working-environment-for-haskell/>).

Then we analyze the parts of the file only to discover that the actual application is at the very bottom.

All the rest is importing modules and defining configs and keyboard shortcuts.

We recognize the following blocks in your xmonad.hs file

  * importing modules
  * autostart.sh script
  * coloring of borders
  * name of our primary keys like super key, alt key, ...
  * border width
  * workspaces
  * window manipulation (floating or not etc...)
  * mouse bindings
  * key bindings
  * azerty and qwerty settings
  * at the bottom xmonad actually starts - main :: IO()



> Programming tip : Never ever use TAB

Video: <https://youtu.be/C8rD2cgb1ww>
