# Kiro Architecture

A short map of how Kiro is put together — useful when you want to know what
ships, where software comes from, and how the pieces fit.

## What Kiro is

Kiro is an Arch-based Linux distro. Public home: https://kiroproject.be

It is plain Arch underneath: the same packages, the same `pacman`, the same
rolling-release model. Kiro adds its own kernels, themes, configs, tools, and
an installer on top.

## How it ships: editioned ISOs

Kiro is built and distributed as an ISO (`kiro-iso` is the production
builder) and installed with the **Calamares** installer.

The ISO is **editioned**. An edition is the set of desktop/window-manager
environments baked into a given ISO and offered at the login screen. The
**default Kiro ISO ships two editions side by side**: `xfce` and `ohmychadwm`
(Kiro's customized `chadwm` tiling window manager). You choose which to use at
the login screen. Other environments are built as separate editions. (See
[desktops.md](./desktops.md) for the full environment list.)

## Kernels

- **linux-cachyos** — the primary kernel; it is what the live ISO and a normal
  install boot.
- **linux-zen** — the fallback kernel, available as a boot option if the
  primary one has trouble on your hardware.

## Custom package repos

- **nemesis_repo** — the user-facing custom repo. This is the one you add
  software from; it holds Kiro's own packages.
- **kiro_repo** — install-only plumbing used by the installer while building
  your system. It is not a user-facing repo and is not something you add by
  hand.

Everything else comes from the standard Arch repositories.

## What ships on the system

A normal install pulls in a set of Kiro packages on top of the Arch base.
The user-facing ones you are most likely to meet:

- **ArchLinux Tweak Tool** (`archlinux-tweak-tool-gtk4`) — the flagship modular
  GTK4 system tool for tweaking and maintaining your system.
- **archlinux-logout-gtk4** — the logout / power dialog.
- **alacritty-tweak-tool** — a configurator for the Alacritty terminal.
- **kiro-powermenu** — a power menu.
- **kiro-system-files** — system-level files and settings dropped into place
  (this is the package that makes the system behave like Kiro rather than
  bare Arch).
- **kiro-keybindings** — the keybindings reference material.
- **kiro-shells** and **kiro-dot-files** — shell configs and dotfiles.

Hardware detection on the live ISO is handled by **chwd**, which picks the
right graphics driver setup at boot.

## How the pieces fit

1. **kiro-iso** assembles an ISO from the Arch base plus Kiro's kernels,
   themes, configs, tools, and the chosen editions.
2. The **Calamares** installer copies that live system to disk and configures
   it. During install it can pull from `kiro_repo`; that repo is plumbing and
   does not stick around as a user-facing source.
3. On your installed system you run an edition (XFCE, ohmychadwm, or whatever
   you installed), with Kiro's tools and look already in place.
4. For software after install, you use the standard Arch repos plus
   **nemesis_repo** for Kiro's own packages.
