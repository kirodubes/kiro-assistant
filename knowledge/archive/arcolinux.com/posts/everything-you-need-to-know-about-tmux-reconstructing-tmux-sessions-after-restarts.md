---
title: "EVERYTHING YOU NEED TO KNOW ABOUT TMUX – Reconstructing Tmux Sessions After Restarts"
url: https://arcolinux.com/everything-you-need-to-know-about-tmux-reconstructing-tmux-sessions-after-restarts/
date: 2020-03-16 23:15:41
type: post
categories: ["Terminal", "Terminal Design"]
tags: ["terminal", "tmux"]
source_site: arcolinux.com
---

# EVERYTHING YOU NEED TO KNOW ABOUT TMUX – Reconstructing Tmux Sessions After Restarts

By default, if the tmux server is terminated (gracefully or not), all the pane layouts, running programs, working directories are lost. This can cause frustration and loss of productivity for users who happen to be running multiple sessions, windows, panes, and running programs. There are helpful management tools out there, but they require initial configuration and continuous updates as your workflow evolves or you start new projects. In this article, we discuss two tmux plugins that work in tandem and will help us overcome this challenge in an easy and fun way, with a very minimal configuration. These two plugins are:

  * [`tmux-resurrect`](<https://github.com/tmux-plugins/tmux-resurrect>)\- a plugin that allows to easily **save and restore tmux environment** after system restarts.
  * [tmux-continuum](<https://github.com/tmux-plugins/tmux-continuum>)\- a plugin that **automates** the saving and restoring of the tmux environment.



Saving and Restoring tmux environment 

[`tmux-resurrect`](<https://github.com/tmux-plugins/tmux-resurrect>) saves all the little details from your tmux environment so it can be completely restored after a system restart (or when you feel like it). No configuration is required. You should feel like you never quit tmux. It even (optionally) restores vim and neovim sessions. This plugin goes to great lengths to save and restore all the details from your `tmux` environment. Here's what's been taken care of:

  * all sessions, windows, panes and their order
  * current working directory for each pane
  * **exact pane layouts** within windows (even when zoomed)
  * active and alternative session
  * active and alternative window for each session
  * windows with focus
  * active pane for each window
  * "grouped sessions" (useful feature when using tmux with multiple monitors)
  * programs running within a pane! More details in the [restoring programs doc](<https://github.com/tmux-plugins/tmux-resurrect/blob/master/docs/restoring_programs.md>).



### Installation with [Tmux Plugin Manager](<https://github.com/tmux-plugins/tpm>)

Add plugin to the list of TPM plugins in `.tmux.conf`:
    
    
    set -g @plugin 'tmux-plugins/tmux-resurrect'
    

Hit **`prefix + I`** to fetch the plugin and source it. You should now be able to use the plugin.

### 

### Saving and Restoring tmux environment

To save an restore the tmux environment, following the key combination below.

  * `**Save** - **prefix + Ctrl-s**`
  * `**Restore** - **prefix + Ctrl-r**`

![](https://arcolinux.com/wp-content/uploads/2020/03/save.png)

Automating Saving and Restoring tmux environment

[tmux-continuum ](<https://github.com/tmux-plugins/tmux-continuum>)works in tandem with tmux-resurrect plugin to automate the saving and restoration of tmux environment. It provides the following features:

  * continuous saving of tmux environment
  * automatic tmux start when computer/server is turned on
  * automatic restore when tmux is started



Together these features enable uninterrupted tmux usage. No matter the computer or server restarts, if the machine is on, tmux will be there how you left it off the last time it was used.

#### [](<https://github.com/tmux-plugins/tmux-continuum#continuous-saving>)Continuous saving

Tmux environment will be saved at the interval of 15 minutes. All the saving happens in the background without the impact to your workflow. This action starts automatically when the plugin is installed.

#### [](<https://github.com/tmux-plugins/tmux-continuum#automatic-tmux-start>)Automatic tmux start

Tmux is automatically started after the computer/server is turned on. See the [instructions](<https://github.com/tmux-plugins/tmux-continuum/blob/master/docs/automatic_start.md>) how to enable this for your system.

#### [](<https://github.com/tmux-plugins/tmux-continuum#automatic-restore>)Automatic restore

Last saved environment is automatically restored when tmux is started. To enable this, put the following in the .tmux.conf:
    
    
    set -g @continuum-restore 'on'

_Note: automatic restore happens**exclusively** on tmux server start. No other action (e.g. sourcing `.tmux.conf`) triggers this._

### Installation with [Tmux Plugin Manager](<https://github.com/tmux-plugins/tpm>)

Please make sure you have [tmux-resurrect](<https://github.com/tmux-plugins/tmux-resurrect>) installed.

Add plugin to the list of TPM plugins in `.tmux.conf`:
    
    
    set -g @plugin 'tmux-plugins/tmux-resurrect'
    set -g @plugin 'tmux-plugins/tmux-continuum'
    

Hit **`prefix + I`** to fetch the plugin and source it. _The plugin will automatically start "working" in the background, no action required._

![](https://arcolinux.com/wp-content/uploads/2020/03/restore.png)

Video: <https://youtu.be/dyUapvV0FmA>
