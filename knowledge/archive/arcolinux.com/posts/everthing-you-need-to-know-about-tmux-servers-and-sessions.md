---
title: "Everything you need to know about tmux - Servers and Sessions"
url: https://arcolinux.com/everthing-you-need-to-know-about-tmux-servers-and-sessions/
date: 2020-02-15 00:15:05
type: post
categories: ["Terminal", "Terminal Design"]
tags: ["terminal", "tmux"]
source_site: arcolinux.com
---

# Everything you need to know about tmux - Servers and Sessions

How Does tmux Work?

tmux is a clien-server implementation. When we start tmux, we are essentially connected to a server instance via a socket connection. What is presented in the terminal in our screen is a client connection to the tmux server. tmux server manages all aspects of tmux operations. You can think of the server as the engine in your vehicle. The server runs in the background and ensures that sessions, windows, panes, other aspects of tmux are operating, even when the tmux client is detached. This is the magic of tmux!

Unlike Web or database servers, the tmux server does not require administration or specialized skill set. The tmux developers designed the server to run transparently in the background with nearly zero setup or configuration needed. It runs perfectly, out-of-the-box! We could write the entire tutorial and not mention the tmux server. However, it is beneficial to understand how tmux works, in order to make it work for you and your specific use-case. The main points to remember about tmux servers are:

  *     *       * Servers hold one or more sessions.
      * Servers ensure that sessions remain alive, even after detaching the client.
      * Servers are terminated when the last remaining running session is closed.
      * When we start a new instance of tmux, while a server is running, a new session is created inside the running server.
      * _(For Advanced users)_ You can run multiple tmux servers. _See -L flag in the[documentation](<http://man.openbsd.org/tmux>)._
      * By default, the tmux server is named "**default** " and the socket is stored in /tmp. You can override it using **TMUX_TMPDIR** environmental variable.
      * Servers have clients. When we launch tmux and are attached to a session, we have a client connection to the tmux server.



> Servers hold one or more Sessions. A Session holds one or more Windows. A Window holds one or more panes.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-server.png)

To query tmux Server for a list of active clients that are connected, you can run the following command:
    
    
    $ tmux list-clients

_For a list of various options that can be applied to the tmux server, consult the tmux[documentation](<http://man.openbsd.org/tmux>). _

 

> Once all sessions are killed, `tmux` exits

 

Video: [https://www.youtube.com/watch?v=Y-CBtHIKnPw&t;=252s](<https://www.youtube.com/watch?v=Y-CBtHIKnPw&t=252s>)

tmux Sessions

A session is nothing but a collection of [pseudo terminals](<https://en.wikipedia.org/wiki/Pseudoterminal>) that are managed by the tmux server. When a tmux server is started, it creates a new session that has one window that will occupy the entire terminal screen and may be split horizentally and/or vertically into rectangular panes, each is a separate pseudo terminal. A tmux session holds one or more windows. When all tmux sessions are terminated, tmux server exits.

> A session holds one of more windows.

Think of sessions in tmux as workspaces in Tiling Windows Managers, or virtual desktops in Virtualbox. Sessions help organize your work by managing the windows and their associated panes. The magic of tmux is that sessions are persistent and can survive accidental disconnection (such as SSH timeout), or intentionally detaching the session, closing the terminal, and later on re-attaching the session, all while processes are running. By default, tmux sessions will not survive a system reboot. In other words, detached sessions will be lost when the system is rebooted. However, there are plugins to tmux that allow the running tmux session to survive and be reconstructed after a system reboot. We will discuss advanced topics, such as recovering tmux sessions after a system reboot, in a later article.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-session2.png)

By default, tmux names sessions numerically starting with number zero "0". The session name can be changed using the key combination:
    
    
    prefix + $ _(while holding Ctrl + b press $)_

Or, from the command line while in tmux:
    
    
    $ tmux rename-session -t old_session_name new_session_name

If creating a new session, you can use the new command to name the session while creating it:
    
    
    $ tmux new-session -s 'my Arco Project'

Now, to list all your active session:
    
    
    Prefix + s

or
    
    
    $ tmux list-sessions

 

tmux commands can be executed from the tmux "command mode." To enter the tmux command-mode, use " **Prefix \+ : **". When in command-mode, you should not proceed the command with the word "tmux". For example, **$ tmux list-sessions** is **:list-sessions** in the command mode. When in the command-mode, the status line will turn **yellow**.

![](https://arcolinux.com/wp-content/uploads/2020/02/tmux-command-mode.png)

**Some common tmux shortcuts pertaining to sessions are:**

_Prefix = Ctrl + b (default)_

__

Shortcut | Action  
---|---  
`Prefix` \+ `(` | Switch the attached client to the previous session.  
`Prefix` \+ `)` | Switch the attached client to the next session.  
`Prefix` \+ `L` | Switch the attached client back to the last session.  
`Prefix` \+ `s` | Select a new session for the attached client interactively  
`Prefix` \+ d |  Detach from session  
`Prefix` \+ $ |  Rename session  
  
 

 

Video: [https://www.youtube.com/watch?v=x16LUmCwv7E&t;=1s](<https://www.youtube.com/watch?v=x16LUmCwv7E&t=1s>)
