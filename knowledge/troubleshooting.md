# Troubleshooting

Before specific advice, ask the user:

1. **Which desktop / WM**, and **X11 or Wayland** session. See
   [desktops.md](./desktops.md).
2. **Which boot entry** they used on the ISO (it decides the graphics driver).
3. For anything non-trivial: the output of `kiro-report` (a public-safe log,
   made for pasting into Discussions). See [tools.md](./tools.md).

You have no access to the user's machine. Hand them safe commands and tell them
to read before running.

## The live ISO won't boot

- **Nothing boots from the USB** → Secure Boot is the most common cause: turn it
  off in the firmware. Check the stick was written with MintStick (raw image),
  not copied as files.
- **Black screen, hang or blinking cursor (AMD/Intel)** → reboot and pick
  **safe graphics, nomodeset**.
- **NVIDIA machine shows nothing** → try **NVIDIA proprietary, modern** (Turing
  / RTX 20-series and newer). Older card → **auto-detect** (needs internet).
  Still broken → **safe graphics, nomodeset** to reach the installer.
- **Kernel panic or no boot at all** → the **fallback kernel** entry.

If every entry fails on real hardware, it is a bug: send the user to
Discussions with their hardware and the entries they tried.

## The installed system won't boot

- systemd-boot (UEFI) and GRUB (BIOS) list every installed kernel: pick the
  other kernel. That is why Kiro installs two. See [kernels.md](./kernels.md).
- Rolled back an update? **Timeshift** ships; on btrfs ATT's Btrfs page sets up
  snapper snapshots. Arch can also downgrade a package from the local cache
  (`/var/cache/pacman/pkg`).
- "Unable to resume from device…" at boot is harmless (no hibernation image);
  remove `resume=` from the kernel command line if they never hibernate.

## Graphics / NVIDIA

- Installed with the open-drivers entry and want NVIDIA now? No reinstall:
  `kiro-hwd detect`, then `sudo kiro-hwd install`. It picks
  `nvidia-open-dkms` (Turing+), `nvidia-580xx-dkms` (Maxwell/Pascal/Volta), or
  keeps nouveau (Kepler and older), plus `nvidia-prime` on hybrid laptops.
- Black screen after a NVIDIA install, from a TTY (`Ctrl` + `Alt` + `F3`) or the
  fallback kernel:
  - kernel headers installed for every kernel (`linux-headers`,
    `linux-lts-headers`, … matching `uname -r`);
  - `dkms status` must say `installed`, not `added`;
  - `nvidia-smi` should see the card;
  - re-run `sudo kiro-hwd install`.
- `kiro-which-vga` shows the active driver; an OpenGL renderer of "llvmpipe"
  means the GPU driver isn't working (software rendering).
- Settings in `/etc/modprobe.d/` only take effect after
  `sudo mkinitcpio -P` and a reboot.

## Desktop looks wrong

- **"Xfce Session (Wayland)" gives a black screen** → not a Kiro setting; it is
  XFCE's experimental Wayland mode. Pick the plain **Xfce Session** at login.
- **Plasma installed through ATT looks black** → comment out the
  `QT_QPA_PLATFORMTHEME`, `QT_STYLE_OVERRIDE` and `GTK_THEME` lines in
  `/etc/environment`, then log out. See [faq.md](./faq.md).
- **Want a light theme** → change `GTK_THEME=Arc-Dawn-Dark` to `GTK_THEME=Arc`
  in `/etc/environment`, log out and in.
- **A desktop config is broken, or new defaults didn't arrive after an update**
  → `kiro-skell` restores the defaults from `/etc/skel`, with a backup.
  Updates change `/etc/skel`, never the user's home.

## pacman problems

- PGP / "invalid or corrupted package" → `kiro-fix-pacman-keys`, then
  `kiro-fix-gpg-conf` if it persists.
- Slow or failing mirrors → `kiro-fix-mirrors`.
- Broken `/etc/pacman.conf` → `kiro-fix-pacman-conf`.
- Always full upgrades (`sudo pacman -Syu`), never single-package upgrades.

## Screen turns off

On XFCE the screen blanks after 15 minutes idle by default and there is **no
automatic lock** (change it in XFCE's Power Manager). Other desktops have their
own idle settings — ask which one.

## Where to send users

Kiro GitHub Discussions: https://github.com/kirodubes/kiro-discussions/discussions.
Ask them to include the `kiro-report` output, their hardware (GPU/CPU, laptop or
desktop), the boot entry they used, and the desktop they run. A short
description plus that report beats a wall of log output.
