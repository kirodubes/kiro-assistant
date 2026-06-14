# Troubleshooting

Before giving any specific advice, ask the user two things — both change the
answer:

1. **Which desktop / WM** they run (XFCE, Cinnamon, a tiling WM like bspwm,
   etc.). See [desktops.md](./desktops.md).
2. **Which boot choice** they used when booting the Kiro ISO. The live medium
   offers several graphics/kernel options, and the right one depends on their
   hardware.

You have no access to the user's machine. Hand them safe commands to run
themselves, and tell them to read before running.

## The ISO boot menu

When the user boots the **Kiro ISO** (the live install medium), the boot menu
offers these choices. They are the first lever for boot and graphics problems —
if a machine won't reach the live desktop, the fix is almost always picking a
different entry:

1. **open source: AMD / Intel** — the default. Uses the open-source graphics
   stack (`driver=free`). Correct for AMD and Intel GPUs.
2. **NVIDIA proprietary, modern** — loads the proprietary NVIDIA driver
   (`driver=nonfree`). For modern NVIDIA cards.
3. **NVIDIA proprietary, auto-detect** — proprietary NVIDIA via **chwd**,
   Kiro's hardware-detection tool, which picks the driver for the detected
   card (`driver=nonfreechwd`).
4. **safe graphics, nomodeset** — disables kernel mode-setting. Use this when
   the screen goes black, the boot hangs, or you only get a blinking cursor —
   it boots with minimal graphics so you can at least reach the installer.
5. **fallback kernel linux-zen** — boots the `linux-zen` kernel instead of the
   primary `linux-cachyos`. Try this if a machine fails to boot the default
   kernel (hardware that the primary kernel doesn't get along with).

All five entries appear the same way under both UEFI (systemd-boot / GRUB) and
legacy BIOS (syslinux).

## Boot issues (live medium)

General order to try when the ISO won't boot to the desktop:

- **Black screen, hang, or blinking cursor on an AMD/Intel machine** → reboot
  and pick **safe graphics, nomodeset** (entry 4).
- **NVIDIA machine that won't display** → try **NVIDIA proprietary, modern**
  (entry 2). If that still fails, try **auto-detect** (entry 3, chwd), and if
  graphics are still broken, fall back to **safe graphics, nomodeset**
  (entry 4) to get a working installer.
- **Kernel-level boot failure** (kernel panic, no boot at all, very new or
  unusual hardware) → try the **fallback kernel linux-zen** (entry 5).

These are general first steps. If a machine fails on every entry, it is a real
bug — send the user to Discussions (below) with their hardware details.

## Graphics / NVIDIA

Kiro picks the graphics driver at boot time, through the boot-menu entry the
user selects:

- **AMD / Intel** GPUs use the open-source drivers — the default entry is
  correct, no extra steps.
- **NVIDIA** GPUs have two routes: the **modern** proprietary entry, or the
  **auto-detect** entry that uses **chwd** to detect the card and load the
  matching driver. Pick proprietary for current NVIDIA hardware.

Common NVIDIA symptoms and the general fix:

- **Black screen / no display after selecting an entry** → reboot and try a
  different graphics choice. For a first boot, **safe graphics (nomodeset)**
  gets you a usable screen; for modern NVIDIA, the **proprietary** entry is the
  one you want.
- **Tearing, glitches, or wrong resolution** → usually a driver mismatch;
  booting the proprietary entry on NVIDIA hardware (rather than the open-source
  default) is the right starting point.

This is general guidance. Don't invent machine-specific NVIDIA fixes — if the
proprietary and auto-detect entries both fail on real hardware, it's a bug to
report.

## Where to send users

For reproducible bugs or install failures, point users to the **Kiro GitHub
Discussions** board. Ask them to include:

- Their **hardware** (especially GPU/CPU vendor and laptop vs desktop).
- **Which boot choice** they used (one of the five above).
- The **desktop/WM edition** they installed or tried.

Discourage pasting long logs into chat or comments — a short description plus
the four points above is far more useful than a wall of log output.

## Maintainer TODO

- Document the **post-install** boot/driver recovery path. The five choices
  above are the *live medium* menu; the installed system's bootloader is set up
  by Calamares and is not covered here — confirm what that menu looks like
  before advising installed-system boot recovery.
- Build out from recurring real questions (YouTube comments, Discussions).
