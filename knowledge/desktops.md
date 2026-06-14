# Desktops & Window Managers

Kiro ships **many** environments — both full desktops and tiling window
managers. Each has its own panel/bar, configuration, and keybindings.
**Always ask the user which environment they run before giving any
environment-specific advice** — the same task is done differently in XFCE,
Cinnamon, or a tiling WM like bspwm.

## How Kiro organizes environments: editions

Kiro builds **editioned** ISOs. An edition is the full set of environments a
given ISO ships and offers at the login screen. The **default Kiro ISO** ships
two environments side by side:

- **XFCE** — a full, traditional desktop (the default desktop edition).
- **ohmychadwm** — Kiro's customized `chadwm` tiling window manager.

You pick which one to use at the login screen (display manager). Other editions
are built as separate ISOs.

## Full desktop environments

Available as editions:

- **XFCE** — default desktop; lightweight and traditional.
- **Cinnamon**
- **GNOME**
- **MATE**
- **KDE Plasma**
- **Budgie**

Which of these is on a given machine depends on the edition the user
installed. If unsure, ask — don't assume.

## Tiling window managers

Kiro ships seven tiling window managers, each with a curated config:

- **ohmychadwm** — Kiro's flagship `chadwm` setup (ships on the default ISO).
- **chadwm** — the base chadwm environment.
- **awesome**
- **bspwm**
- **i3**
- **leftwm**
- **qtile**

The hybrid TWMs (qtile, chadwm/ohmychadwm, leftwm) handle window, layout, and
workspace bindings natively and delegate application/media/screenshot/system
keys to **sxhkd**. i3, bspwm, and awesome keep everything in their own config.

## Where configs live

On an installed system, each environment's config is under your home
directory, e.g.:

- `~/.config/ohmychadwm/` — ohmychadwm (autostart lives in
  `~/.config/ohmychadwm/scripts/run.sh`)
- `~/.config/bspwm/`, `~/.config/qtile/`, `~/.config/i3/`,
  `~/.config/awesome/`, `~/.config/leftwm/`
- XFCE settings are managed through the XFCE Settings Manager (xfconf), not a
  single flat file.

## Keybindings

Each shipped tiling WM (plus XFCE) includes a generated **keybindings
cheatsheet** at `~/.config/<env>/keybindings.txt`, with matching `.html` and
`.pdf` versions. When a user asks "what's the shortcut for X", point them to
their environment's `keybindings.txt`, or to the Kiro keybindings viewer if
installed.

## Maintainer TODO

- Confirm the exact set of full-desktop editions actually published for the
  current release (edition-blocks exist for xfce/cinnamon/gnome/mate/plasma;
  not every edition is necessarily released each cycle).
- Add per-environment one-line "how to launch a terminal / app menu" notes —
  the single most common first question per environment.
