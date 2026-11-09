# Kiro Apps and Packages

The user-facing Kiro apps, what each one does, and how to start it. All of them
come from **nemesis_repo**. "On the ISO" means a fresh install of the default
Kiro ISO already has it; anything else installs with
`sudo pacman -S <package>` (or through ArchLinux Tweak Tool).

## Apps you launch

| App (package) | What it does | Launch | On the ISO |
|---|---|---|---|
| **ArchLinux Tweak Tool** (`archlinux-tweak-tool`) | The flagship system tool: desktops, kernels, themes, services, pacman, locale and more. See [att.md](./att.md). | Menu "Arch Linux Tweak Tool", or `archlinux-tweak-tool` | yes |
| **ArchLinux Logout** (`archlinux-logout`) | Fullscreen transparent logout/power overlay. The menu entry "ArchLinux Logout Settings" opens its settings. X11 and Wayland. | `archlinux-logout` | yes |
| **Alacritty Tweak Tool** (`alacritty-tweak-tool`) | Edits the Alacritty terminal config: 300+ themes, fonts, opacity, cursor, a theme creator. Writes `~/.config/alacritty/alacritty.toml`. | `alacritty-tweak-tool` | yes |
| **Fastfetch Tweak Tool** (`fastfetch-tweak-tool`) | Edits fastfetch: modules and order, 500+ logos, colours, presets, live preview, shell-startup hookup. Writes `~/.config/fastfetch/config.jsonc`. | `fastfetch-tweak-tool` | yes |
| **Fish Tweak Tool** (`fish-tweak-tool`) | Configures the fish shell: prompts (Tide, Starship, Hydro, Pure), fisher plugins, colour themes, abbreviations, greeting. No sudo needed. | `fish-tweak-tool` | yes |
| **Ohmychadwm Tweak Tool** (`ohmychadwm-tweak-tool`) | One window for ohmychadwm: look (GTK/icons/cursor/font, light/dark, bar theme), bar and gaps, wallpaper, displays, mouse/touchpad, startup and default apps, key list. X11. | `Ctrl` + `Alt` + `X`, `oma`, or `ohmychadwm-tweak-tool` | yes (comes with ohmychadwm) |
| **Kiro Keybindings** (`kiro-keybindings`) | Searchable keybindings cheatsheet: detects the running tiling WM and shows its `keybindings.txt` as an overlay; type to filter, `Esc` closes. | `kiro-keybindings` | yes |
| **Kiro Power Menu** (`kiro-powermenu`) | rofi power menu (logout, shutdown, restart, lock, suspend) for window managers without one. | `kiro-powermenu` | yes (with ohmychadwm) |
| **Calamares Tweak Tool** (`kiro-calamares-tweak-tool`) | Live-ISO only, for experts: sets the installer's bootloader (e.g. GRUB instead of systemd-boot) and encryption options, then launches the installer. | `calamares-tweak-tool` in the live session | yes (live ISO) |
| **Kiro News** (`kiro-news`) | Desktop notification when Arch Linux News or Kiro's own signed feed has a new headline. Per-user systemd timer, works on every desktop. Sources in `/etc/kiro-news/sources.conf`. | `kiro-news show` | no |
| **KiroTux Drive** (`kiro-gdrive`) | Mounts shared Google Drive folders read-only under `~/GoogleDrive/<name>`; paste the share link, sign in once, it remounts at every login. Used for KiroTux downloads (see [kirotux.md](./kirotux.md)). No root. | Menu "KiroTux Drive", or `kiro-gdrive` / `kgd` | no |
| **Hyprland Tweak Tool** (`hyprland-tweak-tool`) | Setup hub for Hyprland: installs community Hyprland setups (first: ML4W) with their own installers, backing up your config first. Wayland. | `hyprland-tweak-tool` | no |

`ohmychadwm-appearance` is **superseded** by Ohmychadwm Tweak Tool: when pacman
offers the replacement on upgrade, answer `Y`. `oma` and `Ctrl` + `Alt` + `X`
open the new tool.

## Command-line: kiro-hwd (NVIDIA driver picker)

`kiro-hwd` picks and installs the right NVIDIA driver for the card:

- Turing (RTX 20-series / GTX 16-series) and newer → `nvidia-open-dkms`
- Maxwell, Pascal, Volta → `nvidia-580xx-dkms`
- Kepler and older → stay on the open `nouveau` driver
- Laptops with an integrated GPU also get `nvidia-prime` and `switcheroo-control`

```
kiro-hwd detect                 # show what it would pick
kiro-hwd install --dry-run      # show the install, change nothing
sudo kiro-hwd install           # install it
```

The installer runs it for the boot entry "NVIDIA proprietary, auto-detect". It
is on the ISO. Kiro's first-aid commands (kiro-audit, kiro-fix-mirrors, …) are
in [tools.md](./tools.md).

## Config and system packages (nothing to launch)

- **kiro-system-files** — the system layer: sysctl, modprobe, udev, systemd
  drop-ins, sudoers, X11 keymaps, and the `kiro-*` diagnostic commands
  ([tools.md](./tools.md)). Also adds the menu links "Kiro Releases" and
  "Kiro Discussions".
- **kiro-dot-files** — the `/etc/skel` snapshot new users inherit, a Plank dock
  theme library, reference configs.
- **kiro-shells** — meta package for kiro-bash-config, kiro-zsh-config and
  kiro-fish-config.
- **kiro-variety-config** — the Variety wallpaper-changer config.
- **kiro-sddm-simplicity** — the clean SDDM login theme (a Qt 6 port,
  kiro-sddm-simplicity-qt6, also exists).
- **kiro-grub-theme** — the GRUB theme (only used on GRUB installs).
- **plymouth-theme-kiro-logo** — the boot splash with the self-assembling K logo.
- **kiro-keyring** — trusts the key that signs nemesis_repo packages.
- **kiro-mirrorlist** — the Server entries for nemesis_repo.
- **kiro-wayland-dotfiles** — shared base for the Wayland editions (mako,
  hyprlock/hypridle, waybar style, screenshot script). Wayland only.
- **kiro-noctalia** — shared default config for the Noctalia shell. Wayland only.

## Theme and icon families

- **Arc** — the GTK theme family; `Arc-Dawn-Dark` is the system default
  (kiro-arc-dawn), `kiro-arc-kde` is Arc for KDE Plasma.
- **Surfn Kiro** (`surfn-kiro-icons-git`, on the ISO) — the Surfn icon theme
  tuned for light and dark, with Plasma global themes Surfn Kiro Dark/Light.
- **Neo Candy** (`neo-candy-icons-git` on the ISO, plus kiro-neo-candy-arc,
  -arc-mint-grey, -arc-mint-red, -qogir, -tela) — Beautyline + Candy icons with
  Arc/Qogir/Tela folders.
- **Papirus** (kiro-papirus-dark-tela, -dark-tela-grey) and **Vimix**
  (kiro-vimix-dark-tela) — dark icon sets with Tela folders.
- **Plasma global themes** — kiro-plasma-layan, -nord (Kiro-Nordic), -sweet,
  -whitesur, -win11: each bundles desktop theme, look-and-feel, window
  decorations, colours, Kvantum and SDDM. The other kiro-plasma-* packages
  (dolphin, konsole, keybindings, servicemenus, system-settings,
  window-management) are Plasma defaults, not themes.

Switch themes and icons from ATT's **Themes**, **Icons** or **Themer** pages.
