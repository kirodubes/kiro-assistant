# Packages & Repositories

Kiro is Arch-based, so package management is standard `pacman`, with a few
extra repositories enabled out of the box. On an installed Kiro system, all
the repos below are already configured — you don't need to add anything to
start installing software.

## Repositories on a Kiro system

These are enabled by default in `/etc/pacman.conf`:

- **core**, **extra** — the official Arch Linux repositories. The bulk of all
  software lives here.
- **nemesis_repo** — Kiro's user-facing custom repo. This is where the extra
  desktop apps, themes, and tools live that you install after a clean install.
  Already enabled; just install from it like any other repo.
- **chaotic-aur** — a large repository of prebuilt binary packages (many
  popular AUR programs, ready-built so you don't have to compile them).
- **cachyos** — provides performance-tuned packages, including the
  **linux-cachyos** kernel (Kiro's primary kernel).

**multilib** (32-bit support) is present but **disabled by default**. If you
need to run 32-bit applications, uncomment the `[multilib]` section in
`/etc/pacman.conf` and run `sudo pacman -Sy`.

> **kiro_repo** is *not* on your installed system. It is install-only
> plumbing used by the installer while building the system, and it disappears
> after the first reboot. Never add it by hand.

## Installing software

Standard `pacman` works across all the repos above:

- Update everything: `sudo pacman -Syu`
- Install a package: `sudo pacman -S <name>`
- Remove a package: `sudo pacman -Rns <name>`
- Search for a package: `pacman -Ss <term>`

Software from **nemesis_repo**, **chaotic-aur**, and **cachyos** installs
exactly the same way — no special flags. Always read a command before running
it; the assistant can't run anything on your machine.

## The AUR

The Arch User Repository (AUR) is available as on any Arch system. Kiro ships
the **paru** and **yay** AUR helpers, so you can build AUR packages with, e.g.
`paru -S <name>` or `yay -S <name>`. Many common AUR programs are also already
available prebuilt from **chaotic-aur**, which is usually faster since nothing
has to compile.

## Package signing

Packages from **nemesis_repo** are PGP-signed. The Kiro signing key ships in
the `kiro-keyring` package and is trusted in your keyring, so signature
verification just works — no manual setup needed. (Kiro's global setting is
`SigLevel = Required DatabaseOptional`, which nemesis_repo inherits.)

## Adding nemesis_repo on a non-Kiro Arch system

If you are on a Kiro install, skip this — it's already enabled. On a *plain*
Arch (or Arch-based) system you can add nemesis_repo yourself. The simplest,
safest route is to use the **ArchLinux Tweak Tool** (which can manage repos
for you) or follow the official nemesis_repo setup instructions, rather than
hand-editing `/etc/pacman.conf`. When adding it manually, set
`SigLevel = Optional` for the repo until the `kiro-keyring` package is
installed, then let it inherit the global signing level.

## Maintainer TODO

- List the notable Kiro-specific packages that ship in nemesis_repo (e.g. the
  ArchLinux Tweak Tool, themes, lockscreen/logout tools) once a verified,
  user-facing list is available.
- Link to the official nemesis_repo setup page/video for the non-Kiro
  manual-add path.
