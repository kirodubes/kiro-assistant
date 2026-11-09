# Packages & Repositories

Kiro is Arch-based: package management is standard `pacman`, with a few extra
repositories already configured. Nothing needs adding to start installing.

## Repositories on an installed Kiro system

Active in `/etc/pacman.conf`, in this order:

- **core**, **extra** — the official Arch repositories.
- **nemesis_repo** — Kiro's own repo: the Kiro apps, configs, themes and tools
  (see [apps.md](./apps.md)). Browse it at https://erikdubois.github.io/nemesis_repo/
- **chaotic-aur** — prebuilt binaries of many popular AUR packages.

Also in the file but **switched off** after install:

- **cachyos** — the installer uses it during the driver step, then comments it
  out. Turn it back on with ATT → Pacman → "Enable CachyOS repo" if you want
  CachyOS kernels or packages.
- **multilib** (32-bit libraries, e.g. Steam) — commented out. Enable it with
  ATT → Pacman, or uncomment `[multilib]` and its `Include` line, then
  `sudo pacman -Syu`.

Options: `ParallelDownloads = 15`, `SigLevel = Required DatabaseOptional`.

> **kiro_repo** is not on an installed system: it is build-time plumbing only.
> Never add it by hand. (KiroTux systems additionally have `kirotux_repo`.)

`kiro-fix-pacman-conf` resets `/etc/pacman.conf` to this default.

## Installing software

- Update everything: `sudo pacman -Syu` — always full upgrades, never single
  packages (partial upgrades break Arch).
- Install: `sudo pacman -S <name>` · Remove: `sudo pacman -Rns <name>` ·
  Search: `pacman -Ss <term>`.
- A GUI: **pamac-aur**.

## The AUR

Kiro ships both **paru** and **yay**: `paru -S <name>` or `yay -S <name>`.
Check chaotic-aur first — it often has the program prebuilt. `kiro-set-cores`
makes AUR builds use all CPU cores.

## Package signing

nemesis_repo packages are PGP-signed with the Kiro Signing Key
(`149A BD0C 3A05 63EE`), trusted through the `kiro-keyring` package; the global
`SigLevel = Required DatabaseOptional` means pacman verifies every package.
Signature errors: `kiro-fix-pacman-keys`, then `kiro-fix-gpg-conf`.

## nemesis_repo on a non-Kiro Arch system

Append to `/etc/pacman.conf` (no per-repo SigLevel line):

```
[nemesis_repo]
Server = https://erikdubois.github.io/$repo/$arch
```

Then trust the key and install the keyring and mirrorlist:

```
sudo pacman -Sy
sudo pacman-key --recv-keys 149ABD0C3A0563EE --keyserver keyserver.ubuntu.com
sudo pacman-key --lsign-key 149ABD0C3A0563EE
sudo pacman -Sy --needed kiro-keyring kiro-mirrorlist
```

Optionally replace the `Server` line with
`Include = /etc/pacman.d/kiro-mirrorlist`, the line Kiro itself ships. Or use
ATT → Pacman → "Enable Nemesis repo".
