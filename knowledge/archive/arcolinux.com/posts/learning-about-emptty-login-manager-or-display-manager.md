---
title: "Learning about Emptty - login manager or display manager"
url: https://arcolinux.com/learning-about-emptty-login-manager-or-display-manager/
date: 2025-01-25 07:44:18
type: post
categories: ["Login"]
source_site: arcolinux.com
---

# Learning about Emptty - login manager or display manager

EMPTTY

**Emptty: A Minimalistic TTY Login Manager**

Emptty is a lightweight, minimalistic login manager designed for use with terminal-based environments. Unlike traditional graphical login managers, which rely on a graphical user interface (GUI), Emptty operates in a text-based mode, providing a simple and efficient way to log into a system directly from the TTY (teletypewriter) console.

### Key Features

  1. **Text-based Interface** : Emptty uses a terminal-only interface, making it ideal for users who prefer a command-line environment or want to save system resources by avoiding a full-fledged graphical interface.
  2. **Minimal Footprint** : It is designed to have a small resource footprint, perfect for users running lightweight Linux distributions or those working in environments where efficiency and simplicity are paramount.
  3. **Simple Authentication** : Emptty handles user authentication via standard UNIX login methods, such as verifying user credentials and ensuring secure access to the system.
  4. **Customizable** : Users can configure the login prompt and other settings to suit their personal preferences, adding flexibility for those who need specific customization options.
  5. **Ideal for Headless Systems** : Emptty is well-suited for headless setups or systems that don't require a GUI, such as servers or embedded systems, where minimal system overhead is critical.



### Use Cases

  * **Servers** : Emptty provides a quick, no-nonsense way to log into servers where a GUI is unnecessary and unwanted.
  * **Minimalistic Desktop Environments** : For users building ultra-lightweight desktop environments or window managers, Emptty offers an ideal login solution.
  * **Embedded Systems** : Emptty can be useful for embedded Linux systems, where system resources are limited, and a graphical login manager would be too heavy.



### Conclusion

Emptty is an excellent choice for users who value simplicity, performance, and efficiency in terminal-based login management. Its minimalistic design ensures that the system remains lean while providing the core functionality needed for secure user authentication. Whether for servers, headless systems, or minimal desktops, Emptty is an effective and unobtrusive login solution.

### 

**Aliases**

  * toemptty - switch to emptty
  * nemptty - edit /etc/emptty/conf



> <https://github.com/tvrzna/emptty>

![](https://arcolinux.com/wp-content/uploads/2021/08/emptty.png)![](https://arcolinux.com/wp-content/uploads/2021/08/emptty-vert.png)

> How to autologin

> Do not forget to add yourself to a new group
> 
> sudo usermod -aG nopasswdlogin erik
> 
> Change erik into your username
> 
> Edit the configuration file to your liking

![](https://arcolinux.com/wp-content/uploads/2021/08/emptty-autologin.jpg)

Video: <https://youtu.be/v4bFkW-OvL8>

Video: <https://youtu.be/7PILWGuzuL8>

> To enable autologin **without** seeing the emptty screen during login, adjust the following parameters and/or add the specified lines:

![](https://arcolinux.com/wp-content/uploads/2025/01/emppty.jpg)

Video: <https://youtu.be/l1_pRyofYfg>
