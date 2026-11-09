# ArchLinux Tweak Tool (ATT)

**ArchLinux Tweak Tool** (one word; abbreviated ATT) is Kiro's modular GTK4
system tool. It puts common Arch tasks — desktops, kernels, themes, services,
pacman, locale and more — behind one window. Works on X11 and Wayland.

## Launching

- **Menu:** "Arch Linux Tweak Tool".
- **Terminal:** `archlinux-tweak-tool`, or the short `att`.
- Run it as the normal user; it **refuses to start as root** and asks for the
  password itself when a change needs it. A second launch brings the open
  window to the front.
- The sidebar has a **search box** to find a page.
- Header bar: a **language dropdown** (ATT speaks 14 languages; a change
  applies after **Restart ATT**), **Support** and **Quit ATT**.

Step-by-step recipes with the button labels in every language:
[howto.md](./howto.md).

## Pages (sidebar order)

| Page | What it does |
|---|---|
| **Accessibility** | Accessibility tools |
| **AI Tools** | Install/remove local LLM runners (Ollama, Open WebUI, Jan), CLI coding assistants (Claude Code, Aider, Codex CLI, OpenCode, GitHub Copilot CLI, …) and web-app shortcuts |
| **Arc themes** | Arc GTK themes |
| **Autostart** | Apps that start at login |
| **Backup** | Personal-file backup (Pika, Vorta) |
| **Btrfs** | Snapshots with snapper + snap-pac + Btrfs Assistant, one click ("Enable snapshots"). Greyed out unless the root file system is btrfs |
| **Celestial themes** | Celestial GTK themes |
| **Desktop** | Install X11 desktops and window managers (15) — see [desktops.md](./desktops.md) |
| **Desktop - Wayland** | Install Kiro Wayland configs (14) — see [wayland.md](./wayland.md) |
| **Fastfetch** | fastfetch config |
| **Hybrid graphics** | Two-GPU laptops: installs nvidia-prime + switcheroo-control, per-app "Always use discrete GPU". Greyed out with fewer than two GPUs |
| **Icons Horst** / **Icons Neo Candy** / **Icons Surfn** | Icon theme families |
| **ISO** | Kiro ISO Builder showcase (build your own Kiro ISO) |
| **Kernels** | Kernel manager: 33 kernels in groups (Standard Arch, CachyOS, Xanmod, Liquorix, Mainline, LTS versions, x86-64 levels, AMD Zen, specialty), plus a CachyOS list from the repo; "Set as Default", "Regenerate All Initramfs". Chaotic-AUR kernels show once that repo is on |
| **Locale** | Language, keyboard (X11/Wayland and console), timezone, language packs |
| **Logging** | Log investigator |
| **Maintenance** | Update, cache clean, pacman lock, mirrors (reflector, rate-mirrors), keys & GPG ("Fix keys"), pacman.conf reset, cursors, initramfs |
| **Network** | Network tools, Samba, and the **Firewall** tab (firewalld on/off, mDNS, Samba sharing, firewall-config) |
| **Office** | Office suites and productivity apps |
| **Packages** | Export and import package lists |
| **Pacman** | pacman.conf editor: Arch repo switches (incl. multilib, testing), **Enable Nemesis / Chaotic-Aur / CachyOS repo**, custom repo, AUR helper (yay, paru) |
| **Plymouth** | Boot splash themes |
| **Privacy** | Privacy/security settings, incl. hBlock ad-blocking |
| **Performance** | Performance tuning |
| **Sddm** | Login screen config and themes, "Fix SDDM config". Hidden when SDDM isn't the login manager |
| **Services** | Audio (PipeWire/PulseAudio), Bluetooth, Printing (CUPS), user services |
| **Shells** | bash / zsh / fish: default shell ("Apply fish" etc.), configs, plugins |
| **Software** | Curated installers for common apps |
| **Streamline** | Remove optional apps by category (Kiro and KiroTux only) |
| **System** | System inspector |
| **Themer** | Apply a coordinated theme set |
| **User** | User management |
| **Wallpaper** | Set the wallpaper |

`att --dev` adds a developer **Dev** page.

## Common tasks (short)

- **Add a desktop** → Desktop (X11) or Desktop - Wayland.
- **Kernel** → Kernels; keep two installed.
- **Firewall** → Network → Firewall (not Services).
- **Default shell** → Shells.
- **Repos** → Pacman.
- **Broken keys or slow mirrors** → Maintenance.
- **Snapshots** → Btrfs (btrfs installs); Timeshift otherwise.
- **System language** → Locale (recipe in [howto.md](./howto.md)).
