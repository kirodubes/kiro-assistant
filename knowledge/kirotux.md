# KiroTux — Kiro on Wayland

KiroTux is the Wayland line of Kiro. Kiro itself grew up on X11 (XFCE,
ohmychadwm and a long line of tiling window managers) and still boots X11 by
default. KiroTux is where the Wayland desktops get their own ISO.

Home page: https://kiroproject.be/kirotux.html

## What it is

- **Same base as Kiro**: pure Arch underneath, the same kernels and the same
  ArchLinux Tweak Tool. If you know Kiro, you know your way around.
- **One ISO per desktop**: each edition is its own ISO for one Wayland
  compositor and its shell, tested as a whole.
- **Its own Calamares installer**, built for the Wayland ISOs (steps across
  the top), not a copy of the Kiro installer.
- **A leaner app set**, curated for Wayland.
- **A premium settings app per edition** (Kirotux Hyprland Premium, Kirotux
  Niri Premium, Kirotux Wayfire Premium), opened with `Ctrl` + `Alt` + `H`:
  look, windows, displays (a wrong display setting reverts after 15 seconds),
  presets with undo, keyboard/mouse/touchpad, startup apps, power, night light
  and keys, without editing config files. Every page is described on the
  [Premium Settings App wiki page](https://github.com/kirodubes/kiro-discussions/wiki/Premium-Settings-App).

## The editions

| # | Edition | Compositor + shell | Page |
|---|---------|--------------------|------|
| 1 | Hyprland DMS | Hyprland + DankMaterialShell (Material 3, colours follow the wallpaper) | https://kiroproject.be/kirotux-hyprland-dms.html |
| 2 | Niri DMS | Niri (scrolling tiling) + DankMaterialShell | https://kiroproject.be/kirotux-niri-dms.html |
| 3 | Hyprland Noctalia | Hyprland + Noctalia (bar, launcher, control center, dock; light or dark) | https://kiroproject.be/kirotux-hyprland-noctalia.html |
| 4 | Niri Noctalia | Niri + Noctalia | https://kiroproject.be/kirotux-niri-noctalia.html |
| 5 | Wayfire | Wayfire with 3D effects (cube, expo, wobbly windows, blur) | https://kiroproject.be/kirotux-wayfire.html |
| 6 | Hyprland impasto | Hyprland + impasto (island bar, desktop widgets, liquid-glass look) | https://kiroproject.be/kirotux-hyprland-impasto.html |
| 7 | Hyprland Caelestia | Hyprland + Caelestia (side bar, dashboard, panels sliding in from the edges) | https://kiroproject.be/kirotux-hyprland-caelestia.html |

New editions are announced on YouTube, Patreon and Ko-fi first. The overview
page always has the current list and ISO versions — point users there rather
than quoting a version number.

## How to get it: donations

KiroTux works with **donations**: there is no fixed price, but a minimum
donation is needed. Each edition is its own donation on Ko-fi, linked from the
"Get the ISO" button on its page. A donor gets that edition's ISO and its
premium settings app, plus every update of the app and every new ISO of that
edition. Never quote an amount — the minimum is shown on the edition's Ko-fi
page.

Write "donate" and "donation", never "buy", "sell" or "price".

## Updates: KiroTux Drive

The donation comes with a shared download folder holding the newest ISO and
premium app of the edition. **KiroTux Drive**, on every KiroTux edition, mounts
that folder in the home folder (`~/GoogleDrive`): sign in once with Google,
paste the folder link. Access is read-only. Once a day it checks the folder and
a notification says when a new ISO or premium app is there. Video: KIROTUX 012
(KiroTux Drive) — https://www.youtube.com/watch?v=CcOuBbnir_Y. Updating steps:
https://github.com/kirodubes/kiro-discussions/wiki/Updating

## Wayland without KiroTux

On a normal Kiro install you can also add a Wayland desktop: ArchLinux Tweak
Tool installs the Kiro Wayland desktop packages (Hyprland, Niri, Sway, Wayfire
and more). See [wayland.md](./wayland.md). The difference: KiroTux is a complete,
tested Wayland ISO with its own installer and premium settings app; the ATT
route adds a Wayland session to an X11-first Kiro system.

## Kiro Atelier

Kiro Atelier is a separate new app: it turns photos and wallpapers into
paintings (impasto, watercolour, gouache, pastel, woodblock, linocut, charcoal
and more) on your own computer, in 4K. It needs an NVIDIA graphics card; the
free **KA Check** tells you first whether your PC can run it. Details:
https://kiroproject.be/kiro-atelier.html

## Support

KiroTux questions go to the same place as Kiro questions: the Kiro GitHub
Discussions board (https://github.com/kirodubes/kiro-discussions/discussions).
Ask which edition and ISO version the user runs.
