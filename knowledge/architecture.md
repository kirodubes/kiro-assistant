# Kiro Architecture

A short map of how Kiro is put together. Public home: https://kiroproject.be

## What Kiro is

An Arch-based distro: plain Arch underneath (same packages, same `pacman`, same
rolling release), with Kiro's configs, tools, themes and an installer on top.
Built by Erik Dubois (creator of ArcoLinux) with Claude AI as development
partner. No telemetry of any kind.

## How it ships

- **kiro-iso** builds the ISO; the **Calamares** installer puts it on disk.
- Two Kiro ISOs: the **default ISO** (XFCE + ohmychadwm, X11) and the
  **Plasma ISO**. Every other desktop comes through ArchLinux Tweak Tool
  afterwards (see [desktops.md](./desktops.md)).
- **KiroTux** is the Wayland line: one ISO per Wayland desktop (see
  [kirotux.md](./kirotux.md)).
- Monthly releases. Each ISO ships **two kernels** (default + fallback), and the
  pair changes per release (see [kernels.md](./kernels.md)).
- The **Kiro ISO Builder** (https://kiroproject.be/byoi.html) builds your own
  Kiro ISO with the desktops and kernels you pick.

## Repositories

- **nemesis_repo** — the user-facing Kiro repo (signed).
- **chaotic-aur** — prebuilt AUR packages.
- **cachyos** — present but switched off after install.
- **kiro_repo** — build-time plumbing only; never on an installed system.
See [packages.md](./packages.md).

## What an install looks like

- **Bootloader:** systemd-boot on UEFI (GRUB on request via Calamares Tweak
  Tool), GRUB on BIOS.
- **Login:** SDDM with the Kiro Simplicity theme.
- **Graphics:** chosen by the boot entry; **kiro-hwd** detects NVIDIA cards and
  installs the matching driver (see [install.md](./install.md)).
- **Microcode:** the installer keeps only the CPU's microcode package; it is
  embedded in the initramfs (no separate microcode line in the boot entry).
- **Shell:** fish by default (bash and zsh configs ship).
- **Services on by default:** firewalld, tuned (power profiles), NetworkManager,
  Bluetooth, CUPS printing, ananicy-cpp, systemd-oomd. SSH is **off**
  (`kiro-enable-ssh`).
- **Memory:** zram compressed swap (up to 8 GB); zswap off.
- **Snapshots:** Timeshift ships; btrfs installs get snapper through ATT.
- **Idle (XFCE):** the screen blanks after 15 minutes; there is no automatic
  lock.
- **Look:** dark by default (`GTK_THEME=Arc-Dawn-Dark` in `/etc/environment`).

## The Kiro tools

- **ArchLinux Tweak Tool** — the system tool ([att.md](./att.md)).
- The other apps (logout, tweak tools, keybindings, news, KiroTux Drive) —
  [apps.md](./apps.md).
- **kiro-system-files** — the system layer (sysctl, udev, systemd drop-ins) and
  the `kiro-*` first-aid commands ([tools.md](./tools.md)).
- **kiro-dot-files** / `/etc/skel` — the default user configs; `kiro-skell`
  restores them.

Kiro is kernel-agnostic: none of its tuning hard-codes a kernel name.
