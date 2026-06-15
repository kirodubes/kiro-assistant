---
title: "How to make a script - example is template for stayrolling script"
url: https://arcolinux.com/how-to-make-a-script-example-is-template-for-stayrolling-script/
date: 2020-01-07 18:19:04
type: post
categories: ["Scripting"]
source_site: arcolinux.com
---

# How to make a script - example is template for stayrolling script

![](https://arcolinux.com/wp-content/uploads/2020/01/script-tutorial.jpg)

We have created a template for the future stayrolling scripts.

It is a good occasion to explain how to create your own scripts.

1\. Create a file and name it somename.sh  
2\. Make it executable.
    
    
    chmod +x somename.sh

3\. Add the [shebang](<https://en.wikipedia.org/wiki/Shebang_\(Unix\)>) to the file.
    
    
    #!/bin/bash

4\. Then you start scripting.

 

We learn about pacman -R, pacman -S, --noconfirm, --needed.

We create our script and test it out.

Next up we analyze the template we will use in the future.

**The goal is to avoid people saying there is an error when pacman is trying to remove something that is already removed.**

For this reason we have created a function that gives us some **information** with some **coloring** for the user.

**A function is always defined at the top of your script.** When you call the function bash should already know it.

We give examples of how the function works and speficically how '**if then'** works.

[Information about functions in bash.](<https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php>)

[Information about if then else fi in bash.](<https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php>)

[Sed command is not explained](<https://www.geeksforgeeks.org/sed-command-in-linux-unix-with-examples/>) in the video. Maybe later I will explain it.

Video: <https://youtu.be/EUQSgQmNG5g>
