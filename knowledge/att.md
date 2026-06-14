# ArchLinux Tweak Tool (ATT)

**ArchLinux Tweak Tool** (one word; abbreviated ATT) is Kiro's modular GTK4
system-configuration tool. It puts the most common Arch system tasks — kernels,
themes, services, packages, login screen, and more — behind a single graphical
interface, so you don't have to remember the command line for each one. It will
ask for an administrator password when a change needs root.

## Launching

- **Menu:** look for **Arch Linux Tweak Tool** in your application menu.
- **Terminal:** run `archlinux-tweak-tool` (or the short alias `att`).

Don't run it as root — launch it as your normal user and let it prompt for the
password when needed.

## Pages

ATT is organized as a sidebar of pages. The main ones:

| Page            | What it does                                                       |
|-----------------|--------------------------------------------------------------------|
| **AI Tools**    | Claude AI integration for help with system tasks                   |
| **Accessibility** | Accessibility-related settings                                   |
| **Autostart**   | Manage applications that launch at login                           |
| **Backup**      | Personal-file backup tools                                         |
| **Desktop**     | Install and switch desktop environments                            |
| **Fastfetch**   | Configure the fastfetch system-info display                        |
| **Icons**       | Install and manage icon themes                                     |
| **ISO**         | Kiro ISO Builder showcase                                          |
| **Kernels**     | Install and remove kernels                                         |
| **Locale**      | Set locale, keyboard layout, and timezone                          |
| **Logging**     | Browse ATT session logs and investigate system logs               |
| **Maintenance** | Mirror ranking, orphan removal, and pacman cache cleanup           |
| **Network**     | Network tools and Samba share configuration                        |
| **Office**      | Office suites and productivity apps                                |
| **Packages**    | Export and import installed-package lists                          |
| **Pacman**      | Edit pacman settings (repos, parallel downloads, options)          |
| **Performance** | CPU governor and I/O scheduler tuning                              |
| **Plymouth**    | Install and switch boot-splash (Plymouth) themes                   |
| **Privacy**     | Privacy-focused settings, including hBlock DNS ad-blocking         |
| **Services**    | Enable and disable systemd services                                |
| **Shells**      | Switch the default shell and configure bash, zsh, and fish         |
| **Software**    | Curated installers for commonly used applications                  |
| **Support**     | Ways to help fund the project                                      |
| **System**      | System inspector — hardware info and a system overview             |
| **Themer**      | Apply coordinated theme sets in one step                           |
| **Themes**      | Manage GTK and Plasma themes                                       |
| **User**        | Create and configure user accounts                                 |
| **Wallpaper**   | Browse folders and set the desktop wallpaper                       |

Some pages only appear when relevant to your system:

- **Sddm** — login-manager configuration; shown when SDDM is in use.
- **Btrfs** — snapshot tools; shown on a Btrfs root filesystem.
- **Streamline** — remove optional apps by category; shown on Kiro.
- **Dev** — developer/diagnostic page; shown only in developer mode.

## Common tasks

- **Install or remove a kernel** — open **Kernels**, pick a kernel, install or
  remove it. (On Kiro, linux-cachyos is the primary kernel and linux-zen the
  fallback.)
- **Turn a service on or off** — open **Services** and toggle the systemd
  service you want.
- **Change your default shell** — open **Shells** and switch between bash, zsh,
  and fish.
- **Set a boot splash** — open **Plymouth** to install and switch the Plymouth
  theme.
- **Clean up the system** — open **Maintenance** to rank mirrors, remove orphan
  packages, and clear the pacman cache.
- **Tune pacman** — open **Pacman** to adjust options like parallel downloads.
- **Change the look** — use **Themes** and **Icons** for individual pieces, or
  **Themer** to apply a coordinated set at once; **Wallpaper** sets the
  background.

## Maintainer TODO

- Per-page detail (exact buttons/options) is not documented here — add as
  needed from the individual `*_gui.py` modules.
