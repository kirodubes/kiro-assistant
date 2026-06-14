# Installing Kiro

## Getting the ISO

- Download the latest Kiro ISO from https://kiroproject.be

## Writing the ISO to USB

- Use **MintStick** to write the ISO to a USB stick. MintStick raw-writes the
  image, which is what a bootable installer needs.
- Do **not** use Ventoy — it chainloads rather than raw-writing the image,
  which causes boot failures on bare metal.

## Booting the USB

Boot from the USB stick (you may need to pick it from your firmware's boot
menu). Kiro's boot menu offers five entries — pick the one that matches your
graphics hardware:

- **open source: AMD / Intel** — the default. Boots the `linux-cachyos`
  kernel with open-source graphics drivers. Use this on AMD or Intel
  graphics, or if you're not sure.
- **NVIDIA proprietary, modern** — `linux-cachyos` with NVIDIA's proprietary
  driver loaded directly.
- **NVIDIA proprietary, auto-detect** — `linux-cachyos` with the proprietary
  NVIDIA driver, selected by hardware auto-detection (chwd).
- **safe graphics, nomodeset** — `linux-cachyos` with kernel mode-setting
  disabled. Use this if the other entries give you a black screen or fail to
  reach the desktop.
- **fallback kernel linux-zen** — boots the `linux-zen` kernel instead of
  `linux-cachyos`. Use this if `linux-cachyos` won't boot on your machine.

All entries boot into the same live environment, where the Calamares
installer is available.

## Installing with Calamares

Launch the Calamares installer from the live desktop. It walks you through
these steps:

1. **Welcome** — language and a few starting checks.
2. **Locale** — your region and time zone.
3. **Keyboard** — keyboard layout.
4. **Partition** — choose where to install Kiro.
5. **Users** — your username, password, and hostname.
6. **Summary** — review everything before any changes are written.

After the summary, Calamares installs the system (copying files, installing
the kernel and bootloader, creating your user) and then shows a **finished**
screen. Reboot and remove the USB stick when it's done.

## Maintainer TODO

- Document the **Partition** page options (erase disk / install alongside /
  manual / replace partition) — only the existence of the page is verified
  here, not its choices.
- Add verified post-install first steps (e.g. updating the system, using
  ArchLinux Tweak Tool, enabling **nemesis_repo** for extra software). See
  also `att.md` and `packages.md`.
