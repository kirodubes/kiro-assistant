# Kernels

Every Kiro ISO ships **two kernels**: one boots by default, the other is
installed alongside as a **fallback**. If a kernel update ever leaves the
machine unable to boot, the user picks the other entry from the boot menu
instead of reaching for a rescue USB.

## The pair changes per release

The pair is chosen per release and deliberately changes from month to month, so
the stock, LTS, Zen, CachyOS and hardened kernels all get real use on real
installs. Examples so far:

- v26.09: `linux-cachyos` (default) + `linux-zen` (fallback)
- v26.10 and later builds: `linux` (default) + `linux-lts` (fallback), both from
  Arch's `[core]` repo

**Never state "the" Kiro kernel as a fact for the user's machine.** Ask instead:

- `uname -r` shows the running kernel.
- The boot menu shows both: the fallback entry is titled
  "fallback kernel <name>".
- Each release card on the release notes page
  (https://kiroproject.be/releases.html) lists the kernels that ISO shipped, and
  the `.pkglist.txt` next to each ISO on SourceForge lists every package.

Kiro is **kernel-agnostic by design**: its sysctl, udev, systemd and tmpfile
settings never hard-code a kernel name, so any Arch kernel keeps the tuning and
the audit checks working. The shipped pair is the default, not a lock-in.

## Picking the fallback at boot

On the live ISO, the last Kiro boot entry is **fallback kernel <name>**. If the
machine won't boot the default kernel (kernel panic, no boot, very new or
unusual hardware), reboot and pick it. On an installed system, systemd-boot (or
GRUB) lists both installed kernels; pick the other one. See
[install.md](./install.md) and [troubleshooting.md](./troubleshooting.md).

## Switching kernels on an installed system

- **ArchLinux Tweak Tool → Kernels** installs or removes kernels from a list of
  33 kernels plus the CachyOS repo list. See [att.md](./att.md).
- Terminal: install the kernel **and its headers**, e.g.
  `sudo pacman -S linux-zen linux-zen-headers`. Headers matter: DKMS modules
  such as the NVIDIA driver are built against them.
- Keep at least two kernels installed, so there is always a fallback.
- systemd-boot picks up a new kernel automatically through a pacman hook.

## Building your own pair

The **Kiro ISO Builder** (https://kiroproject.be/byoi.html) builds a Kiro ISO
with any kernel combination you pick (for example CachyOS or Zen).

## Liquorix

Kiro once shipped Liquorix (`linux-lqx`). It is no longer a default, but it can
be installed and booted any time, like any other Arch kernel.
