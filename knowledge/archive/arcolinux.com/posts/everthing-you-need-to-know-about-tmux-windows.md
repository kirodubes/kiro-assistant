---
title: "Everything you need to know about tmux – Windows"
url: https://arcolinux.com/everthing-you-need-to-know-about-tmux-windows/
date: 2020-02-17 02:02:16
type: post
categories: ["Terminal", "Terminal Design"]
tags: ["terminal", "tmux"]
source_site: arcolinux.com
---

# Everything you need to know about tmux – Windows

What are tmux Windows? 

tmux window is the entity that holds panes and resides within the tmux session. Think of a window in tmux as a tab in your notebook. Tabs (windows) help organize your work and group your individual pages (panes) based on some topic of your choice. By default, when tmux starts, a session is initialized. Within this session, tmux initializes a single window (by default) which occupies the entire area of the terminal. This window will contain one single pane (by default).

> A tmux window resides within a session and holds one or more panes

A window may be split horizontally, or vertically, into one or more rectangular areas called "panes." Each pane partitions the screen into a separate terminal ([pseudo terminal](<https://en.wikipedia.org/wiki/Pseudoterminal>)). 

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-server.png)

tmux displays one active window, at a time. The status bar (or status line) at the bottom of the screen displays the name of the current window, as a visual indicator. Please note that the symbol "*" indicates the active window.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-window.png)

When tmux session is started, at least one window will open. You create additional windows manually, or using a script, depending on the use-case of your workflow. tmux indexes windows numerically, starting with 0 (by default). The default name given to a window is its index number (default is 0), unless defined otherwise. Many users prefer to change the default index numbering in tmux to start with 1. This makes it easier to refer to the window with index 1 as window 1. To change this behavior, you can run this command:
    
    
    $ tmux set -g base-index 1

To make this change persistent, put this command in your ~/.tmux.conf :
    
    
    set -g base-index 1

## Windows shortcuts for common tasks

 _Default prefix is Ctrl + b_

 

Shortcut | Action  
---|---  
`Prefix` \+ c |  Create window  
`Prefix` \+ , |  Rename current window  
`Prefix` \+ & |  Close current window  
`Prefix` \+ p |  Navigate to previous window  
`Prefix` \+ n |  Navigate to next window  
`Prefix` \+ l |  Bring up the last selected window  
`Prefix` \+ f |  Go to a window with a match of a text string  
`Prefix` \+ 0 ... 9 |  Switch/select window by number  
  
Video: [https://www.youtube.com/watch?v=5No0X4ajZmY&t;=1s](<https://www.youtube.com/watch?v=5No0X4ajZmY&t=1s>)

## Moving (_reordering_) windows

As the number of your windows increases, you may want to reorder or move them around. This can be easily accomplished using the **move-window** tmux command. The move-window command requires two arguemtns **-s** (source or the window you want to move) and **-t** (target index number). _The target index number must not be used by another window._

For example, to move the current window to index 7:
    
    
    $ tmux move-window -t 7

To move window 3 to index 5:
    
    
    $ tmux movew -s 3 -t 5

To accomplish the same behavior using tmux shortcut, you can use **prefix + .** , which will prompt for an index to move the current window to.

 

Window Layouts

You can split a tmux window vertically or horizontally into panes. The arrangements of the panes within a window is referred to as "layout." This is a familiar concept for the Tiling Windows Managers' users. tmux comes with a number of preset layouts that may be selected with the **select-layout** command or cycled with **next-layout** command. In addition, you can cycle through the layouts using the shortcut:
    
    
    Prefix (Ctrl + b) + Space-bar

**Supported tmux Layouts:**

**1\. even-****horizontal** -Panes are spread out evenly from left to right across the window.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-layout-1.png)

**2\. even-****vertical** -Panes are spread evenly from top to bottom.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-layout-2.png)

**3\. main-horizontal** \- A large (main) pane is shown at the top of the window and the remaining panes are spread from left to right in the leftover space at the bottom. _Use the main-pane-height window option to specify the height of the top pane._

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-layout-003.png)

**4\. main-vertical** \- Similar to `main-horizontal` but the large pane is placed on the left and the others spread from top to bottom along the right. _See the**main-pane-width** window option._

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-layout-4-1.png)

**5\. tiled** \- Panes are spread out as evenly as possible over the window in both rows and columns.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-layout-5.png)

* Narlock, Tony. The Tao of tmux _,_ Leanpub, 17 Feb. 2020, [www.leanpub.com/the-tao-of-tmux/read](<http://leanpub.com/the-tao-of-tmux/read>).

The **`list-windows`** command displays the layout of each window in a form suitable for use with **`select-layout`**. For example:
    
    
    $ tmux list-windows
    0: ksh [159x48]
        layout: bb62,159x48,0,0{79x48,0,0,79x48,80,0}
    $ tmux select-layout bb62,159x48,0,0{79x48,0,0,79x48,80,0}
    

## Closing windows

When you exist (or kill) the last pane in the active window, the window will be closed (or killed). However, to close the active window along with its pane(s), use the shortcut:
    
    
    Prefix (Ctrl +b) + &

_This will destroy the current window, its panes, and all running processes within them._

To kill the current window using the tmux command, use the following inside the current window:
    
    
    $ tmux kill-window

It is possible to kill a target window from outside the current window (using a script, for example) by using the **-t** option, which specifies the index of the window to be closed. For example:
    
    
    $ tmux kill-window -t2

_This will close the window with index #2._

 

Video: [https://www.youtube.com/watch?v=vA0vtW0cYXg&t;=7s](<https://www.youtube.com/watch?v=vA0vtW0cYXg&t=7s>)
