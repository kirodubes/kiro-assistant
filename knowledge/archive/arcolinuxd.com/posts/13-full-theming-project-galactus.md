---
title: "13 Full theming project Galactus"
url: https://www.arcolinuxd.com/13-full-theming-project-galactus/
date: 2018-03-07 18:58:07
type: post
categories: ["Awesome"]
tags: ["theming"]
source_site: arcolinuxd.com
---

# 13 Full theming project Galactus

![](https://www.arcolinuxd.com/wp-content/uploads/2018/03/pimping-pink-1.jpg)

The wallpaper "Galactus" comes in and we will use it to change our desktop accordingly.

We choose a new icon theme and kill the conky.

Atom is going to be my editor because of the lua syntax highlighting.

We first copy/paste powerarrow-blue and rename it to powerarrow-froly. Just to be safe.

Then we change the tag color. We have the idea to use a dark and light pink to make the bar at the top and use gpick to find the RGB colors.

At the bottom we do a find/replace. We replace the blue colors with the pink colors.

When we open termite, we see a blue logo of ArcoLinux. We also make a pink logo and make sure it opens up in Neofetch. Then the pink logo does not load and we need to investigate why the pink logo does not show.

## Great tip neofetch

I learned during the tutorial that Neofetch is keeping a **cache** file in the following folder that you need to delete if you want to see the new (pink) logo.
    
    
    ~/.cache/thumbnails/neofetch

Finally we change the color from the conky.

Video: <https://www.youtube.com/watch?v=MS0Wc_RVOaA>
