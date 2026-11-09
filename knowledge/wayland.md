# Wayland on Kiro

Kiro boots an **X11** session by default (XFCE or ohmychadwm). Wayland is
**optional**, and there are two ways to get it:

1. **Add a Wayland session to a Kiro install** through ArchLinux Tweak Tool
   (below). No reinstall; X11 stays.
2. **Install a KiroTux ISO**: one complete Wayland desktop per ISO, with its own
   installer and premium settings app. See [kirotux.md](./kirotux.md).

## ATT → Desktop - Wayland

14 Kiro Wayland configs, each a `kiro-*` package from nemesis_repo:

- **Hyprland** — plain, and with the **Noctalia**, **Noctura** or
  **Dank Material Shell** (DMS) shells
- **Niri** — **Ohmyniri**, **Niri Noctalia**, **Niri Dank Material Shell**
- **Sway** (swayfx), **Wayfire**, **River**, **Labwc**, **Mango**, **Scroll**,
  **Dwl**

How it works:

- Tick one or more → **Install selected**. The button stays grey until an
  extra repo (nemesis_repo, chaotic-aur or cachyos) is enabled on ATT's
  **Pacman** page — on Kiro nemesis_repo is already on.
- Editions built on **different shells** (DMS, Noctalia, Noctura) can't be
  installed together; ATT warns first.
- **Remove selected** removes only the config package; the compositor and
  `~/.config` stay. ATT refuses to remove the session you are logged into.
- Log out and pick the new session on the SDDM login screen.

Shared Wayland pieces come along: **kiro-wayland-dotfiles** (notifications,
hyprlock/hypridle, waybar style, screenshot script) and **kiro-noctalia** (the
Noctalia shell defaults).

## Things to know

- Ask which compositor **and** which shell the user runs: a Hyprland + DMS
  desktop is configured differently from Hyprland + Noctalia.
- The **"Xfce Session (Wayland)"** login entry is XFCE's own experimental mode,
  not one of these, and gives a black screen on Kiro. Use the plain Xfce
  Session.
- **Hyprland Tweak Tool** (`hyprland-tweak-tool`) is a setup hub that installs
  community Hyprland setups (first: ML4W), backing up the config first.
- Kiro's ohmychadwm tools (Ohmychadwm Tweak Tool, kiro-powermenu) are X11.
  ArchLinux Tweak Tool and ArchLinux Logout work on both.
