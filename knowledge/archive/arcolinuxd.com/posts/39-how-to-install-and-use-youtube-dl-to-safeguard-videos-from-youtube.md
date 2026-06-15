---
title: "39 how to install and use youtube-dl to safeguard video's from youtube"
url: https://www.arcolinuxd.com/39-how-to-install-and-use-youtube-dl-to-safeguard-videos-from-youtube/
date: 2018-11-20 19:45:47
type: post
categories: ["Plasma"]
tags: ["download"]
source_site: arcolinuxd.com
---

# 39 how to install and use youtube-dl to safeguard video's from youtube

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/youtube-dl.jpeg)

We used this [link](<https://www.youtube.com/watch?v=f_tH3qARp0U>) from youtube to do our testing with the application [youtube-dl](<https://wiki.archlinux.org/index.php/Youtube-dl>).

[Here is the list](<https://github.com/rg3/youtube-dl/blob/master/docs/supportedsites.md>) of all the websites this application supports **NOT JUST YOUTUBE**!

We analyze the code in the terminal with **youtube-dl --help**.

### Audio + Video
    
    
    youtube-dl -f bestvideo+bestaudio https://www.youtube.com/watch?v=f_tH3qARp0U

### Just Audio
    
    
    youtube-dl -x --audio-format mp3 https://www.youtube.com/watch?v=f_tH3qARp0U

You will get a video and an mp3 to play with any player of your choice.

The audio format can be in **mp3** but also **best** , **aac** , **flac** , **m4a** , **opus** , **vorbis** , **wav**.  
If we use **best** for this link, we will get **opus**. Others came in with **ogg**. So the source matters when you use best.

Video: <https://youtu.be/yfwV1QFpkr0>

Many formats are possible

![](https://www.arcolinuxd.com/wp-content/uploads/2018/11/formats.jpeg)

USE a gui to do the same job

We analyze our choices and decide to install
    
    
    yay -S youtube-dl-gui-git

Video: <https://youtu.be/0qUzhr3Yuzc>
