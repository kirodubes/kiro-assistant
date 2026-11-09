# Installing Kiro

## Getting the ISO

Download from https://kiroproject.be (the Download button points to the latest
ISO on SourceForge). There are two Kiro ISOs:

- **The default ISO**: XFCE + ohmychadwm, the Calamares installer, nemesis_repo
  and the full Kiro app suite. ATT installs any other desktop afterwards.
- **The Plasma ISO**: the fully themed KDE Plasma edition, in the `Plasma/`
  folder on SourceForge.

The Wayland editions are a separate line, **KiroTux** (see
[kirotux.md](./kirotux.md)).

Only the current release stays online; older ISOs are removed. Each ISO has a
`.pkglist.txt` next to it listing every package (kernels included).

Requirements: any 64-bit (x86_64) PC; about 4 GB RAM and 20 GB disk for a
comfortable desktop. UEFI and legacy BIOS both work. There is no 32-bit
version.

## Writing the ISO to USB

- Use **MintStick**. It raw-writes the image, which is what a bootable
  installer needs.
- Do **not** use Ventoy: it chainloads instead of raw-writing, which causes
  boot failures on bare metal.
- A plain file copy onto the stick never boots.

## Before booting: Secure Boot

The Kiro ISO is not signed for Secure Boot (like most Arch ISOs). Turn Secure
Boot **off** in the firmware setup (usually `Del`, `F2` or `F12` at power-on,
under Boot or Security), save, and boot the USB.

## The boot menu

Five Kiro entries, the same on UEFI and BIOS. The first one is the default and
starts after 5 seconds. **The entry you pick decides the graphics driver of the
installed system.**

1. **open drivers: AMD / Intel - NVIDIA driver removed** — the default. Open
   mesa drivers; any NVIDIA driver is removed from the install. Right for AMD
   and Intel graphics.
2. **NVIDIA proprietary, modern - keeps nvidia** — keeps the baked-in
   `nvidia-open-dkms` driver. For Turing (RTX 20-series, GTX 16-series) and
   newer. No detection, no internet needed.
3. **NVIDIA proprietary, auto-detect - needs internet** — runs **kiro-hwd**
   during the install: it detects the card and downloads the matching driver
   (also the older 580xx branch for GTX 9xx/10xx). Falls back to the open driver
   if it fails.
4. **safe graphics, nomodeset** — kernel mode-setting off, minimal graphics.
   For black screens and hangs, to at least reach the installer.
5. **fallback kernel <name>** — boots the second kernel instead of the default
   one (see [kernels.md](./kernels.md)).

The BIOS menu also has Boot existing OS, Memtest86+, Hardware Information,
Reboot and Power Off.

## Installing with Calamares

The live session logs in automatically to XFCE. Start the installer from the
desktop. Steps:

1. **Welcome** — language and starting checks.
2. **Locale** — region and time zone.
3. **Keyboard** — layout.
4. **Partition** — where to install. Choose:
   - a file system: **ext4** (default), **btrfs** or **xfs**;
   - swap: none, small (up to 4 GB), suspend (at least RAM size, enables
     hibernation) or a swap file. zram compressed memory is always on top;
   - optional **encryption** (LUKS2).
   The EFI partition needs at least 1 GiB (2 GiB recommended). GPT is used on
   UEFI, msdos on BIOS.
5. **Users** — name, password, hostname. The root password is set to the same
   password. The user is in `wheel` (sudo).
6. **Summary** — review; nothing is written before this.

Then Calamares installs and shows **Finished**. Reboot and remove the stick.

**Bootloader:** UEFI installs get **systemd-boot**; BIOS installs get **GRUB**.
Want GRUB on UEFI (for example for `grub-btrfs` snapshots)? In the live session
open **Calamares Tweak Tool**, pick GRUB, and launch the installer from there.
Limine and rEFInd are not installer choices, and there is no tool to switch
bootloaders after install — choose at install time.

Btrfs installs get the subvolumes `@`, `@home`, `@root`, `@srv`, `@cache`,
`@log`, `@tmp`, `@snapshots`, `@swap`, mounted with zstd compression.

## After the first boot

- The system logs in through **SDDM** and preselects the ISO's default session
  (XFCE). Pick another session on the login screen.
- The default shell is **fish** (bash and zsh configs ship too; change it in ATT
  → Shells).
- Update: `sudo pacman -Syu`.
- Run `kiro-verify` for a quick health check (see [tools.md](./tools.md)).
- Open **ArchLinux Tweak Tool** for desktops, kernels, themes and services
  ([att.md](./att.md)).
- Set up **Timeshift** snapshots (it ships), or on btrfs use ATT → Btrfs.
- An "Unable to resume from device…" message at boot is harmless: it appears
  when swap with hibernation was chosen and there is no hibernation image.
