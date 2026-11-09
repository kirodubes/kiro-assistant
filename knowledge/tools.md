# Kiro Command-Line Tools (first aid)

`kiro-system-files` ships these commands on every Kiro install. They are the
fastest answers to common problems. Tell the user to read what a command does
before running it; the ones that change the system ask for `sudo`.

## Asking for help

| Command | When to use it |
|---|---|
| `kiro-report` | Makes one public-safe diagnostic log to paste into Kiro Discussions when asking for help. **First thing to ask for in a support thread.** |
| `kiro-diag` | One-command snapshot: ISO version, kernel, BIOS/UEFI, display manager, session, NVIDIA status. |
| `kiro-iso-version` | Which ISO version this install came from. |
| `kiro-calamares-log` | Short readable summary of the installer log with a CLEAN or FAILED verdict. Use after a failed or odd install. |
| `kiro-which-vga` | Shows the active GPU driver and the OpenGL renderer. "llvmpipe" means software rendering: the GPU driver is not working. |

## Checking the system

| Command | When to use it |
|---|---|
| `kiro-verify` | Fast post-install sanity check. |
| `kiro-audit` | Full post-install audit (kernel, microcode, repos, SDDM, services, bootloader, …). `kiro-audit --fix` repairs known issues. |
| `kiro-lint` | Static checker for sysctl/modprobe/udev config conflicts (after hand-editing those). |
| `kiro-probe` | Uploads a hardware probe to linux-hardware.org; `kiro-probe --save` keeps it local with an HTML report. |
| `kiro-probe-report` | Opens (or builds) a colour-coded HTML hardware report. |

## Fixing pacman

| Command | When to use it |
|---|---|
| `kiro-fix-pacman-keys` | "invalid or corrupted package (PGP signature)" errors: refreshes the keyrings. |
| `kiro-fix-gpg-conf` | Key verification still fails: restores Kiro's pacman `gpg.conf`. |
| `kiro-fix-mirrors` | Slow or failing downloads: ranks mirrors with rate-mirrors. |
| `kiro-get-mirrors` | The same with reflector. |
| `kiro-fix-pacman-conf` | `/etc/pacman.conf` broken or hand-edited into trouble: resets it to the Kiro default. |

## Configs and setup

| Command | When to use it |
|---|---|
| `kiro-skell` (or `skell`) | Restores Kiro's default configs: copies `/etc/skel` into your home, backing up only the `~/.config` entries it overwrites. Use when a desktop config is broken, or to get new defaults after an update (updates change `/etc/skel`, not your home). |
| `kiro-skell-all` | The same, but backs up the whole `~/.config` first. |
| `kiro-enable-ssh` | SSH is off by default. This installs openssh, enables sshd and opens SSH in the firewall. |
| `kiro-set-cores` / `kiro-set-cores-min1` / `kiro-set-cores-min2` | Faster AUR builds: makepkg uses all cores, all minus one, or all minus two. |
| `kiro-pci-latency` | Sets a uniform PCI latency timer. Only useful on some older hardware. |
| `kiro-get-nemesis` | Clones the arcolinux-nemesis bootstrap scripts into your home (advanced users). |
| `kiro-keep-kirotux-repo` | KiroTux only: keeps `[kirotux_repo]` in pacman.conf. Does nothing on Kiro. |

## NVIDIA

`kiro-hwd` (its own package, on the ISO) picks and installs the right NVIDIA
driver. See [apps.md](./apps.md) and [troubleshooting.md](./troubleshooting.md).
