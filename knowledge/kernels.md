# Kernels

Kiro ships two kernels and lets you pick at boot or swap them later:

- **linux-cachyos** — the primary kernel. It is what the live ISO and a normal
  install boot by default. It comes from the **cachyos** repo (performance-tuned)
  and is paired with `linux-cachyos-headers`.
- **linux-zen** — the fallback kernel. Available as a boot-menu entry on the
  live ISO, and a good second option if `linux-cachyos` has trouble on a
  particular machine.

Liquorix is not used.

## Picking the fallback at boot

The Kiro ISO boot menu includes a **fallback kernel linux-zen** entry. If the
machine won't boot the default `linux-cachyos` kernel — kernel panic, no boot at
all, or very new/unusual hardware — reboot and choose that entry. See
[install.md](./install.md) for the full boot menu and [troubleshooting.md](./troubleshooting.md)
for boot triage.

## Switching kernels on an installed system

Use the **Kernels** page in ArchLinux Tweak Tool to install or remove kernels
through a graphical interface — pick a kernel and install or remove it, no
command line needed. See [att.md](./att.md).

Both kernels can be installed side by side; the bootloader then lets you choose
between them at boot.

## Which to use

- Stick with **linux-cachyos** unless you hit a problem — it is the tuned
  default Kiro is built around.
- Switch to **linux-zen** if `linux-cachyos` won't boot, misbehaves, or doesn't
  support some piece of your hardware well.
