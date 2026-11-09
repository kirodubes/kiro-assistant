# Desktops & Window Managers

**Always ask which environment the user runs, and whether it is an X11 or a
Wayland session, before giving environment-specific advice.** The same task is
done differently in XFCE, Plasma or a tiling window manager.

## What the ISO ships

The default Kiro ISO ships **two** environments, both X11:

- **XFCE** — the full desktop; the live session and a fresh install log into it.
- **ohmychadwm** — Kiro's flagship tiling window manager (a customised chadwm),
  with its own Ohmychadwm Tweak Tool (`Ctrl` + `Alt` + `X`).

Pick between them on the **SDDM** login screen; SDDM remembers the last
session. A separate **Plasma ISO** ships the fully themed KDE Plasma edition.
Kiro boots **X11 by default**; Wayland is optional (see
[wayland.md](./wayland.md)), and the KiroTux line has a Wayland ISO per
desktop (see [kirotux.md](./kirotux.md)).

## Everything else comes through ATT

ArchLinux Tweak Tool installs the other environments on demand. In total ATT
offers **29** (the two on the ISO plus **27 more**).

**ATT → Desktop** (15, chosen from a dropdown):

- Full desktops: **XFCE**, **Plasma**, **GNOME**, **Cinnamon**, **MATE**,
  **Budgie**
- X11 tiling WMs: **ohmychadwm**, **chadwm**, **awesome**, **bspwm**,
  **dusk**, **hlwm** (herbstluftwm), **i3**, **leftwm**, **qtile**

Most install with a Kiro config package (`kiro-<name>`); Plasma, GNOME and
Budgie install without one (after Plasma, ATT suggests the optional
`kiro-plasma-meta`). **Plasma and GNOME are one-way installs**: removing them
cleanly needs a reinstall, and ATT warns first. There are also
"Install all desktops" and "Install all twms" buttons.

**ATT → Desktop - Wayland** (14): see [wayland.md](./wayland.md).

## Known quirks

- **Plasma installed on top of XFCE looks black**: Kiro's `/etc/environment`
  theming variables override Plasma's theme. Comment out
  `QT_QPA_PLATFORMTHEME`, `QT_STYLE_OVERRIDE` and `GTK_THEME`, log out.
- **"Xfce Session (Wayland)" gives a black screen**: XFCE's own experimental
  Wayland mode, not a Kiro session. Pick the plain **Xfce Session**.
- **Dark everywhere**: deliberate (`GTK_THEME=Arc-Dawn-Dark` in
  `/etc/environment`); `GTK_THEME=Arc` is the light sibling.

## Where configs live

- `~/.config/ohmychadwm/` — ohmychadwm (autostart:
  `~/.config/ohmychadwm/scripts/run.sh`)
- `~/.config/<wm>/` — bspwm, qtile, i3, awesome, leftwm, …
- XFCE settings live in xfconf (XFCE Settings Manager), not one flat file.
- New defaults arrive in `/etc/skel`; `kiro-skell` copies them into the home
  folder with a backup (see [tools.md](./tools.md)).

The hybrid tiling WMs (qtile, chadwm/ohmychadwm, leftwm) handle window, layout
and workspace keys natively and leave application, media, screenshot and
system keys to **sxhkd**. i3, bspwm and awesome keep everything in their own
config.

## Keybindings

Each shipped tiling WM (plus XFCE) has a generated cheatsheet at
`~/.config/<env>/keybindings.txt`, with `.html` and `.pdf` versions. The
**Kiro Keybindings** app (`kiro-keybindings`) shows it as a searchable overlay
for the running WM. Point "what's the shortcut for X" questions there.
