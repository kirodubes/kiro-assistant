---
title: "Everything you need to know about tmux – Panes"
url: https://arcolinux.com/everthing-you-need-to-know-about-tmux-panes/
date: 2020-02-20 02:34:31
type: post
categories: ["Terminal", "Terminal Design"]
tags: ["terminal", "tmux"]
source_site: arcolinux.com
---

# Everything you need to know about tmux – Panes

What are tmux Panes?

A tmux pane is the entity that we actually use to run commands, scripts, and processes, such as ssh, backup, vim, htop, and what have you. Technically, they are [pseudoterminals](<https://en.wikipedia.org/wiki/Pseudoterminal>) encapsulating shells, like Zsh or Bash. In other words, they are terminals within a terminal. Panes are used to allow the user to organize their workflow by splitting the tmux window into vertical and horizontal panes, each running a process or a program. The layout of the panes are managed by the tmux window they reside in. By default, when tmux server is initialized, a session is started. Within this session a single window is created. This window will contain one pane, by default.

> Servers hold one or more Sessions. A Session holds one or more Windows. A Window holds one or more Panes. 

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-server.png)

Panes are created by splitting the window they reside in. Splitting can be performed vertically or horizontally using tmux shortcuts or using tmux commands (good when scripting). On an average, a tmux window can have several panes open. The terminal dimension is the limiting factor on how many panes you can split further.

_Prefix = Ctrl + b (default)_

Shortcut | Action  
---|---  
`Prefix` \+ `%` | `split-window -h` (split horizontally)  
`Prefix` \+ `"` | `split-window -v` (split vertically)  
  
 

When using Prefix + w , tmux will display the list of windows and their associated panes. In the example below, we see that there is 1 window in the current session 0. The window has a name of "1" and it contains 2 panes. The active pane in window 1 is the pane with name "bash". By default, tmux assigns the name of the running process as the pane's name.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-panes.png)

> When the last pane in a window is closed, the tmux window will be terminated by tmux.

To create a new pane by splitting the window vertically with 75% height
    
    
    tmux split-window -p 75

_You can experiment withe**split-window** command by using **-v** and **-h** switches (vertical and horizontal respectively). The**-p** switch signifies the percentage._

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-panes-01.png)

**Common tmux Shortcuts for Panes**

_Prefix = Ctrl + b (default)_

Shortcut | Action  
---|---  
`Prefix` \+ `%` | `split-window -h` (split horizontally)  
`Prefix` \+ `"` | `split-window -v` (split vertically)  
`Prefix` \+ { |  Move the current pane left  
`Prefix` \+ { |  Move the current pane right  
`Prefix` \+ (↑ ↓ ← →) |  Switch to pane to the direction  
`Prefix` \+ q |  Show pane numbers  
`Prefix` \+ 0 ... 9 |  Switch/select pane by number  
`Prefix` \+ z |  Toggle pane zoom  
`Prefix` \+ ! |  Convert pane into a window  
`Prefix` Ctrl + (↑ ↓) |  Resize current pane height _(after Prefix, hold down the Ctrl key while tapping the up or down key)_  
`Prefix` Ctrl + (← →) |  Resize current pane width _(after Prefix, hold down the Ctrl key while tapping the right or left key)_  
`Prefix` \+ x |  Close current pane  
`Prefix` \+ Spacebar |  Toggle between pane layouts  
`Prefix` \+ o  |  Switch to next pane  
  
 

**Zooming/Unzooming**

There are times when you want to work on a process or a program inside one pane and you need to enlarge it to take the entire terminal space. This can be accomplished by using the shortcut:
    
    
    Prefix + z

You can press the same shortcut to unzoom and return the pane to its previous state. If you like to create a custom key binding, you can follow the example below and enter it in your ~/.tmux.conf. This will bind Ctrl+y to zoom in and out.
    
    
    bind -n C-y resize-pane -Z

**Advanced Tip!**

You can navigate the tmux panes in a vim-like style, using the letters (h j k l). To accomplish this, bind these keys in your ~/.tmux.conf file, as follows:
    
    
    bind h select-pane -L   
    bind j select-pane -D   
    bind k select-pane -U   
    bind l select-pane -R

Video: [https://www.youtube.com/watch?v=_lYyXM_XqdI&t;=4s](<https://www.youtube.com/watch?v=_lYyXM_XqdI&t=4s>)
