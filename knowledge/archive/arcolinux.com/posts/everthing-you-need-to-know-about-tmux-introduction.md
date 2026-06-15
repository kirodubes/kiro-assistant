---
title: "Everything you need to know about tmux - Introduction"
url: https://arcolinux.com/everthing-you-need-to-know-about-tmux-introduction/
date: 2020-02-06 03:39:29
type: post
categories: ["Terminal", "Terminal Design"]
tags: ["terminal", "tmux"]
source_site: arcolinux.com
---

# Everything you need to know about tmux - Introduction

![](https://arcolinux.com/wp-content/uploads/2019/12/tmux.jpg)Why use tmux?tmux is a productivity tool for the terminal. It is a powerful utility that empowers terminal users to strike a fine-balance between multitasking and organization. While some gui terminals attempt to addess this challenge with splitting, tabs, and what have you, tmux separates itself with unique features that make it a must-have tool for sys admins, developers, and power users. Some of its unique features include:

  1. It behaves like a Windows Manager for the terminal. When inside tmux, you can:
     * Partition the tmux window into multiple “panes”, each would have its own command line.
     * Run multiple tmux windows with the same session.
     * Run multiple tmux sessions and switch between them, like virtual  desktops.
  2. It allows multitasking inside the terminal (run multiple processes).
  3. It allows applications and processes to run in the background, even after closing the terminals. This is achieved by “detaching” a tmux session. When tmux is started again, the tmux session(s) can be  re-attached and the running processes will not suffer any interruptions.
  4. It is scriptable, configurable, and ships with a powerful command system that allows to retrieve and manipulate information on its objects.
  5. It has a mature community-developed suite of tools to further enhance the user experience.



Video: <https://www.youtube.com/watch?v=k93pdfm9MsQ>

What is tmux?tmux is a "terminal multiplexer”: it enables a number of terminals (or windows), each running a separate program, to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached. The key elements to understanding and using tmux effectively are centered around Sessions, Windows, and Panes (using the tmux terminology). 

  * **Session** \- the entity that holds one or more Windows. Once tmux is started, it will have at _least_ one session. Sessions are like Workspaces in Tiling Windows Managers, or VMs in Virtualbox.
  * **Window** \- the entity that holds "panes" and resides within a session. All sessions start with at least one Window open. Windows have layouts and can be split into "Panes".
  * **Pane** \- is a [pseudoterminal](<https://en.wikipedia.org/wiki/Pseudoterminal>) encapsulating the shell. A tmux Window can be split into panes, each is a terminal that can run applications or processes. Think of a Pane as a "_terminal within a terminal._ " When tmux is running, you will always have at least one pane open.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-installation-02.png)

Video: [https://www.youtube.com/watch?v=0oFCYzVzWws&t;=5s](<https://www.youtube.com/watch?v=0oFCYzVzWws&t=5s>)

Installation and Basic Usage of tmux

tmux installation is very simple in Linux, and specifically in ArcoLinux. The [ArchWiki](<https://wiki.archlinux.org/index.php/tmux#Installation>) provides additional details on installing and using tmux. To install tmux on your system, simple execute the following command: 
    
    
    sudo pacman -S tmux

To start using tmux, simply type tmux in the terminal and hit the enter key. Your screen should look something like the screenshot below. _Notice the bright green status bar at the bottom of the screen_. This is your visual indicator that you are in tmux environment now.  ![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-installation-01.png)tmux is keyboard-driven. In other words, we interact with tmux by sending commands to the running tmux server. We interact with a running instance of tmux by using keyboard sequences for various command. This is similar to the concept of key-bindings in Tiling Windows Managers. The "prefix key" is the most important key in tmux. It is how we are able to interact with tmux sever, split windows, move windows, switch sessions, and many other custom commands. 

> The default prefix key in tmux is `<Ctrl-b>`.

_While holding down the`control` key, press `b`._ To learn the default key sequences for common tmux operations, use the following cheat-sheet for quick reference: <https://tmuxcheatsheet.com>

> It is very important to understand that we interact with tmux using commands. These commands are what tmux uses to set options, navigate panes, switch windows, and what have you.

There are multiple ways to sending commands to tmux: 

  1. **Keybindings** (or keyboard shortcuts) - all keybindings must start with the prefix key (Ctrl + b by default).
  2. **tmux commands** sent from the shell - tmux must be started and all tmux commands follow this format: _$ tmux <command>_
  3. **User -defined config file** \- if it exists, tmux reads the user config file when the server first starts. _The default location for the tmux user config file is: ~/.tmux.config._ The config file is a good place for settings or options that need to be persistent.

For example, let's say you would like to show all sessions actively running after tmux starts. You can accomplish this by: 
    
    
    **Ctrl + b** and then press the key**s**

Or, from the shell, type the command: 
    
    
    $ tmux list-sessions

_Consult the[tmux documentation,](<http://man.openbsd.org/tmux>) or the online[ tmux cheatsheet](<https://tmuxcheatsheet.com>) for a list of all possible commands and their associated keybindings._

Video: [https://www.youtube.com/watch?v=1hrgc6pNUgg&t;=5s](<https://www.youtube.com/watch?v=1hrgc6pNUgg&t=5s>)
