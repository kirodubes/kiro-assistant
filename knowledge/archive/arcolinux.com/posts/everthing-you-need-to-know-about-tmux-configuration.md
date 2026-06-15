---
title: "Everything you need to know about tmux – Configuration"
url: https://arcolinux.com/everthing-you-need-to-know-about-tmux-configuration/
date: 2020-02-23 16:33:23
type: post
categories: ["Terminal", "Terminal Design"]
tags: ["terminal", "tmux"]
source_site: arcolinux.com
---

# Everything you need to know about tmux – Configuration

One of the beauties of tmux is its simplicity, in terms of configuration, right out-of-the-box. By default, tmux is fully functional and requires zero-configuration. However, most users eventually break away from the default settings and will begin to adjust and tweak tmux settings to personalize the tmux experience. These settings include key-bindings, prefix key, themes, among many other settings. Some changes can be made on the fly using the command line within tmux. However, such changes will be reset to default, the next time tmux is started. To make changes persistent, configuration changes should be placed in a tmux configuration file located in the user home folder.
    
    
    ~/.tmux.conf

To make a global tmux config file, place the config file in /etc.
    
    
    /etc/tmux.conf

 

> The content of the tmux config are tmux commands

Settings in the config file are read by the tmux server when it is initialized or reloaded using "source-file". For example:
    
    
    $ tmux source-file ~/.tmux.conf

Alternatively, you can use the command mode of tmux, as follows:
    
    
    **Prefix + :** _(will open the tmux prompt, then type:)_ :**source /path/to/config.conf**

And hit return.

> Advanced Tip!

Most saavy users bind a key to the command "**source-file ~/.tmux.conf** ". You can do this by putting the following line in the tmux config:
    
    
    bind r source ~/.tmux.conf\\; display "~/.tmux.conf sourced!"

The latter part of the line above will give you a visual confirmation that the config file was sourced. With this, all you have to do is **Prefix + r** to reload the config file!!!

How tmux Processes Config

tmux processes the configuration file line-by-line, similar to run commands in .bashrc or .zshrc. **_A line in the configuration file can be run in the shell within tmux._** The only caveat is that you must prefix the line with the word "tmux" before executing the command from the shell.

For example, to set the **default-terminal** variable in new panes to **screen-256color** , you can:

Put the following line in the ~/.tmux.conf:
    
    
    set -g default-terminal "screen-256color"

Or, you can set it by executing the command below from the shell within tmux:
    
    
    $ tmux set -g default-terminal "screen-256color"

What you change depends on your preference and use-case. We recommend that you begin with reviewing the available options in the [online documentation](<https://man.openbsd.org/tmux>). Once you identify an option that interests you, try it through the command line. If you decide to make it persistent, transfer it to your ~/.tmux.conf.

Types of tmux Configuration Options

The appearance and behaviour of `tmux` may be modified by changing the value of various options. **There are four types of option:_server options_ , _session options,_ _window options,_ and _pane options_.**

**Server and Session Options**

The `tmux` server has a set of global server options which do not apply to any particular window or session or pane. These are altered with the **`set-option` `-s`** command, or displayed with the **`show-options` `-s`** command.

In addition, each individual session may have a set of session options, and there is a separate set of global session options. Sessions which do not have a particular option configured inherit the value from the global session options. Session options are set or unset with the **`set-option`** command and may be listed with the **`show-options`** command. The available server and session options are listed under the **`set-option`** command.

**Window and Pane Options**

Similarly, a set of window options is attached to each window and a set of pane options to each pane. Pane options inherit from window options. This means any pane option may be set as a window option to apply the option to all panes in the window without the option set, for example these commands will set the background color to red for all panes except pane 0:
    
    
    set -w window-style bg=red
    set -pt:.0 window-style bg=blue
    

There is also a set of global window options from which any unset window or pane options are inherited. Window and pane options are altered with **`set-option` `-w`** and **`-p`** commands and displayed with **`show-``option` `-w`** and **`-p`**

**User Options**

`tmux` also supports user options which are prefixed with a ‘`@`’. User options may have any name, so long as they are prefixed with ‘`@`’, and be set to any string. For example:
    
    
    $ tmux setw -q @foo "abc123"
    $ tmux showw -v @foo
    abc123

_For a list of all available options, consult the tmux[online documentation](<https://man.openbsd.org/tmux>)._

 

> If `-g` is given to set-option, the global session or window option is set.

Examples

Below are some examples of how to set various options. It takes some time to get comfortable with which switch to use with which option. We recommend that you review the "available options" section in the[ online documentation](<https://man.openbsd.org/tmux#exit-empty>) and review the various options that pertain to its respective type.

**Server Options**

  * Tweak timing between key sequences


    
    
    set -s escape-time 0

  * If you’re having an issue with color detail in tmux, it may help to set **`default-terminal`** to **`screen-256color.`**`This sets the TERM variable in new panes.`


    
    
    set -g default-terminal "screen-256color"

  * Change the default server behavior and keep it running when there are no active sessions.


    
    
    set -s exit-empty off

 

**Session Options**

  * Start counting window number (base-index) at _1_ , rather than the default, _0_.


    
    
    set -g base-index 1

  * Set the prefix to `<Ctrl-a>`, like GNU Screen, rather than default `<Ctrl-b>`. _This requires that we unbind Ctrl-b key_.


    
    
    set-option -g prefix C-a
    unbind-key C-b
    bind-key a send-prefix
    

 

**Window Options**

  * Automatically name the window based on its active pane. _Automatic renaming will be disabled for the window if you rename it manually._


    
    
    set-window-option -g automatic-rename

  * To switch off automatic-rename globally:


    
    
    set-option -wg automatic-rename off

  * Synchronize input of any pane to all other panes in the same window. _Default is off_.


    
    
    set-option -w synchronize-panes on

 

**Pane Options**

Change the background of the current pane to black.
    
    
    set-option -p window-active-style bg=black

 

**User Options**

`tmux` also supports user options which are prefixed with a ‘`@`’. User options may have any name, so long as they are prefixed with ‘`@`’, and be set to any string. For example:
    
    
    $ tmux setw -q @foo "abc123"
    $ tmux showw -v @foo
    abc123
    

 

**Important Notes**

  * To unset any option, use the **-u** flag in the set-option line. For example, the line below will unset the black background that we set in the Pane Options section.


    
    
    set-option -pu window-active-style bg=black

  * To list the current set options, you can always use the show-option tmux command. For example, to show the set options for the current windows:


    
    
    show-option -w 

Or, the following for the global window set options:
    
    
    show-option -wg 

  * You can configure tmux to prompt for window name upon creating a new window, `Prefix` \+ `C` (capital C):


    
    
    bind-key C command-prompt -p "Name of new window: " "new-window -n '%%'"

``

Video: [https://www.youtube.com/watch?v=Q6SxWLaBVpw&t;=306s](<https://www.youtube.com/watch?v=Q6SxWLaBVpw&t=306s>)

vi-Style Copy/Paste Mode

tmux offers an option to turn the navigation of the window buffer into a vi-like functionality. By binding few keys, you can navigate through the current buffer and search all the output generated on the screen thus far. Furthermore, you can select, copy, and paste to other windows in the tmux session, using vi keys. By default, tmux uses emacs style and this can be changed using the tmux set command as follows:
    
    
    set-window-option -g mode-keys vi

You can confirm this is working by pressing **Ctrl+B** and then**:** in a tmux session to bring up the command line, and typing:
    
    
    list-keys -T copy-mode-vi
    

This will bring up a complete list of the vi-like functionality available to you in this mode.

When vi-style is configured in tmux, you can enter the "copy mode" using the sequence:
    
    
    Prefix  _(Ctrl + B by default)_ and then the symbol [

You can leave the copy mode by press the **Enter** key. Or, you can start a selection by pressing **Space** on a character, moving to another, and then pressing **Enter**. If you have text copied like this you can paste it into any tmux window in that session by pressing **Ctrl+B** and then `**]**`.

However, you can bind few keys to make the experience even more vi-like. This will entail binding keys to select, copy, and paste using vi-style. This is accomplish by putting the following lines inside your ~/.tmux.conf:
    
    
    # Setup vi-style copy/paste
    set-window-option -g mode-keys vi 
    bind P paste-buffer 
    bind-key -T copy-mode-vi v send-keys -X begin-selection 
    bind-key -T copy-mode-vi y send-keys -X copy-selection 
    bind-key -T copy-mode-vi r send-keys -X rectangle-toggle

Now you can use v to select (visual-mode in vi), y to yank (copy), P to paste the buffer, and r to select multiple line!

Video: [https://www.youtube.com/watch?v=rhNiNuyGKPk&t;=4s](<https://www.youtube.com/watch?v=rhNiNuyGKPk&t=4s>)
