---
title: "How to safeguard videos from youtube"
url: https://arcolinux.com/how-to-safeguard-videos-from-youtube/
date: 2018-11-20 18:04:11
type: post
categories: ["Audio", "Video"]
tags: ["help"]
source_site: arcolinux.com
---

# How to safeguard videos from youtube

![](https://arcolinux.com/wp-content/uploads/2018/11/youtube-dl.jpeg)   


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

![](https://arcolinux.com/wp-content/uploads/2018/11/formats.jpeg)   


USE a gui to do the same job

We analyze our choices and decide to install
    
    
    yay -S youtube-dl-gui-git

Video: <https://youtu.be/0qUzhr3Yuzc>

  


Creation of aliases

**Youtube-dl** is a command line way to download and safeguard video and audio.  
Install with pacman if not present.

  * alias yta-aac="youtube-dl --extract-audio --audio-format aac "
  * alias yta-best="youtube-dl --extract-audio --audio-format best "
  * alias yta-flac="youtube-dl --extract-audio --audio-format flac "
  * alias yta-m4a="youtube-dl --extract-audio --audio-format m4a "
  * alias yta-mp3="youtube-dl --extract-audio --audio-format mp3 "
  * alias yta-opus="youtube-dl --extract-audio --audio-format opus "
  * alias yta-vorbis="youtube-dl --extract-audio --audio-format vorbis "
  * alias yta-wav="youtube-dl --extract-audio --audio-format wav "
  * alias ytv-best="youtube-dl -f bestvideo+bestaudio "
