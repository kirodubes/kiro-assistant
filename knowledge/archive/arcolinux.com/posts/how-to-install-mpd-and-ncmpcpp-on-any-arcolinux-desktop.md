---
title: "How to install mpd and ncmpcpp on any ArcoLinux desktop"
url: https://arcolinux.com/how-to-install-mpd-and-ncmpcpp-on-any-arcolinux-desktop/
date: 2022-02-14 10:36:38
type: post
categories: ["Audio"]
tags: ["anydesktop", "polybar"]
source_site: arcolinux.com
---

# How to install mpd and ncmpcpp on any ArcoLinux desktop

![](https://arcolinux.com/wp-content/uploads/2022/02/mpdncpmpcppcava.jpg) ![](https://arcolinux.com/wp-content/uploads/2018/01/mpd-ncmpcpp.jpg) 

Mpd is a music player daemon and ncmpcpp is a music client. The client ncmpcpp runs in a terminal and connects to the daemon or server side to get the music.

We start with reading [the arch wiki of MPD](<https://wiki.archlinux.org/index.php/Music_Player_Daemon>) and [the arch wiki of NCMPCPP](<https://wiki.archlinux.org/index.php/ncmpcpp>) to get a general overview of what these applications are and how they can function.

Google "ncmpcpp" and ask for images if you want to see what you can achieve in regards to the theming.

Then we install them via a script located on my personal github :
    
    
    git clone https://github.com/erikdubois/arcolinux-nemesis

Inside the AUR folder you will find the script to install **mpd** and **ncmpcpp**.

We take a look at the installation script as well in atom.

The script assumes you have a "**Music** " folder. You can put your music in there or you can make a symbolic link (ln -s) in there to point to your external harddrive where the bulk of your music is.

If ArcoLinux is installed in **another** **language** than **English** , you will need to change the settings of mpd and ncmpcpp to point to the **music** folder in your language.

Partial list of views within ncmpcpp:

  * `1` \- Current playlist
  * `2` \- Filesystem browser
  * `3` \- DB search
  * `4` \- Library
  * `5` \- Playlist editor
  * `6` \- Tag editor (very powerful!)
  * `7` \- Output selector
  * `8` \- Music visualizer
  * `=` \- Clock
  * **`F1` \- Help**



### Other UI keys

  * `q` \- Quit
  * `f` \- Seek forward
  * `b` \- Seek backward
  * `\` \- Switch between classic and alternative views
  * `#` \- Display bitrate of file
  * `i` \- Show song info
  * `I` \- Show artist info (saved in `~/.ncmpcpp/artists/ARTIST.txt`)
  * `L` \- Shuffle between available lyric databases
  * `l` \- Retrieve song lyrics for current song Show/hide lyrics
  * `>` \- Next track
  * `<` \- Previous track
  * `p` \- Play/Pause
  * `+` \- Increase volume 2%
  * `-` \- Decrease volume 2%



Test it out. Learn and have fun.

Video: <https://youtu.be/m231VFWeDRA>

 TIP : use F1 to learn the necessary shortcuts

Exchange code from playerctl to mpc to have audio buttons support

Applies to any TWM not just leftwm

Video: <https://youtu.be/5Pp6l9LLDTA>

Cava is just an extra treat

Once you get to know ncmpcpp you can also install **cava** , which is an "Console-based Audio Visualizer for Alsa (MPD and Pulseaudio)".

Read more about it [on this github](<https://github.com/karlstav/cava>).

Install it with this code
    
    
    sudo pacman -S cava

Launch it via terminal by typing '**cava** '. Everything should work out of the box **IF** mpd and ncmpcpp work. **Check out the ~/.config/cava configuration** file and see what you can change there.

![](https://arcolinux.com/wp-content/uploads/2018/01/cava.jpg) In the picture beneath I used gradient colors to display the bars. 
    
    
    gradient = 1
    gradient_color_1 = '#0099ff'
    gradient_color_2 = '#ff3399'

![](https://arcolinux.com/wp-content/uploads/2018/01/cava-config.jpg) 

Video: <https://youtu.be/2Z9uAYi9Jds>

 

OLDER VIDEOS - PLAYLIST YOUTUBE

Video: <https://www.youtube.com/playlist?list=PLlloYVGq5pS7os6NAzVjPs4a3uUhLb7ug>
