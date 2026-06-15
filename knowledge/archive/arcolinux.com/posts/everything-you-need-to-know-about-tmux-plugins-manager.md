---
title: "Everything you need to know about tmux - Plugins Manager"
url: https://arcolinux.com/everything-you-need-to-know-about-tmux-plugins-manager/
date: 2020-03-10 04:44:31
type: post
categories: ["Terminal", "Terminal Design"]
tags: ["terminal", "tmux"]
source_site: arcolinux.com
---

# Everything you need to know about tmux - Plugins Manager

Like vi, emacs, and other mature Linux programs, tmux is extensible and allows third-party code (or plugins) to extend its features and capabilities. The plugins can be installed manually, or managed through a "plugin manager." [Tmux Plugin Manger](<https://github.com/tmux-plugins/tpm>) (also known as "tpm") is designed to automatically manage the tmux plugins. By adding few lines into your ~/.tmux.conf you can easily activate plugins and extend the power of tmux beyond its default offering.

**Install tpm**

1\. First, we will [clone](<https://github.com/tmux-plugins/tpm.git>) tpm into ~/.tmux folder under the home folder
    
    
    $ git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

2\. We add the following lines at the bottom of our ~/.tmux.conf
    
    
    # List of plugins
    set -g @plugin 'tmux-plugins/tpm'
    set -g @plugin 'tmux-plugins/tmux-sensible'
    
    # Other examples:
    # set -g @plugin 'github_username/plugin_name'
    # set -g @plugin 'git@github.com/user/plugin'
    # set -g @plugin 'git@bitbucket.com/user/plugin'
    
    # Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
    run -b '~/.tmux/plugins/tpm/tpm'

3\. Finally, we reload tmux (_also knows as "sourcing tmux"_). If tmux is already running, type the following:
    
    
    $ tmux source ~/.tmux.conf

That's it!

[](<https://github.com/tmux-plugins/tpm#installing-plugins>)**Installing Plugins**

  1. Add new plugin to `~/.tmux.conf` with **`set -g @plugin '...'`**
  2. Press **`prefix` \+ `I`** (capital i, as in **I** nstall) to fetch the plugin.



You're good to go! The plugin was cloned to `~/.tmux/plugins/` dir and sourced.

[](<https://github.com/tmux-plugins/tpm#uninstalling-plugins>)**Uninstalling Plugins**

  1. Remove (or comment out) plugin from the list.
  2. Press **`prefix` \+ `alt` \+ `u`** (lowercase u as in **u** ninstall) to remove the plugin.



All the plugins are installed to `~/.tmux/plugins/. A`lternatively you can find plugin directory there and remove it.

Example - Prefix highlighting plugin

The tmux plugin [tmux-prefix-highlight](<https://github.com/tmux-plugins/tmux-prefix-highlight>) provides a visual indicator in the tmux status bar when the tmux prefix key is pressed. The installation is extremely simple using the [tmux Plugin Manager (TPM)](<https://github.com/tmux-plugins/tpm>).

**Installation**

Add plugin to the list of TPM plugins by simply adding the line below to ~/.tmux.conf:
    
    
    set -g @plugin 'tmux-plugins/tmux-prefix-highlight'
    

Finally, press **prefix + I** to install it.

**Usage**

Just add **`#{prefix_highlight}`** to your left/right status bar by adding the line below to ~/.tmux.conf
    
    
    set -g status-right '#{prefix_highlight} | %a %Y-%m-%d %H:%M'
    

The plugin can also be configured to show when copy mode is active; see the **[Configurations](<https://github.com/tmux-plugins/tmux-prefix-highlight>)** section of the online documentation.

![](https://arcolinux.com/wp-content/uploads/2020/03/tmux-prefix-001.png)

Example - Nordify tmux

[Nord](<https://www.nordtheme.com>) is a theme that comes with a total of sixteen, carefully selected, dimmed pastel colors for a eye-comfortable, but yet colorful ambiance. It is inspired by the beauty of the arctic, the colors reflect the cold, yet harmonious world of ice and the colorfulness of the Aurora Borealis. [Nord](<https://www.nordtheme.com>) consists of four named [color palettes](<https://www.nordtheme.com/docs/colors-and-palettes>) providing different syntactic meanings and color effects for dark & bright ambiance designs.

Nord tmux is an arctic, north-bluish clean and elegant [tmux](<https://tmux.github.io/>) theme. It is part of the ports that Nord offers to unify the appearance of your favorite applications.

![](https://arcolinux.com/wp-content/uploads/2020/03/tmux-nord-001.png)![](https://arcolinux.com/wp-content/uploads/2020/03/tmux-nord-003.png)

**Installation and Activation**

Nord uses tmux plugins manager (tpm) to automatically download and activate Nord tmux. Once tpm is installed:

  1. add **`set -g @plugin "arcticicestudio/nord-tmux"`** to your [`tmux.conf `](<http://man.openbsd.org/OpenBSD-current/man1/tmux.1#FILES>)(by default `.tmux.conf` located in your home directory)
  2. press the default key binding **`prefix` \+ `I` **to fetch- and install the plugin

![](https://arcolinux.com/wp-content/uploads/2020/03/tmux-nord-004.png)

Video: <https://youtu.be/Jdw716CrTDg>
