# Website FAQ

The public questions and answers from the Kiro website FAQ
(https://kiroproject.be/#faq), copied here so your answers match what the
website says. Generated from the website source — regenerate, don't hand-edit.
The topic files (kernels.md, install.md, troubleshooting.md, …) rank above
this file: where they disagree, the topic file wins. Known stale answers below:

- NVIDIA answers mention `chwd` (`chwd --list`, `sudo chwd -a`): chwd no longer
  ships. Use `kiro-hwd detect` and `sudo kiro-hwd install` instead. kiro-hwd
  has no 470xx branch: Kepler and older stay on nouveau.
- Boot entries: the first one is now titled "open drivers: AMD / Intel - NVIDIA
  driver removed" (see install.md for all five).
- The USB answer lists Ventoy: recommend MintStick, never Ventoy.
- Kernel answers name a pair ("stock linux … with linux-lts", or cachyos + zen
  in the Liquorix answer): the pair rotates per release (see kernels.md).
- Header names like `linux-cachyos-headers`: use the headers of the kernels
  actually installed.

### Why Kiro instead of vanilla Arch?

Same Arch underneath, less assembly. Calamares replaces the wiki transcription, the repos save you from rebuilding common packages, and the defaults are opinionated so you can boot into a usable desktop in under an hour.

### Who's behind Kiro, and who is it for?

Kiro is built by Erik Dubois — the creator of ArcoLinux, who has spent years building teaching-first, community-focused Arch distributions and documenting every step on YouTube — working with Claude AI (Anthropic) as his dev partner. It's a one-developer-plus-AI project. For the past year Kiro has been his personal build: the exact system he runs every day, shared openly. From June 1, 2026 the focus shifts — the same opinionated foundation, now shaped for the people who use it (driven by what users actually need, not what the creator happens to like). Code lives on GitHub and the walkthroughs on YouTube — the everyday tutorials stay free forever, while the more advanced, deep-dive courses live in the members-only realm. See [Community](https://kiroproject.be/#community).

### How is Kiro different from CachyOS, Garuda, EndeavourOS, or other Arch-based systems?

They're all Arch-based, just with different priorities. CachyOS is performance-first — a custom scheduler and its own optimized repos. Garuda leans gaming, with heavy GUI theming. EndeavourOS stays deliberately close to upstream Arch with a light touch. Kiro ships the stock linux kernel by default with linux-lts alongside (CachyOS or Zen kernels are one pick away in the Kiro ISO Builder) and sane defaults, while keeping the userland close to upstream Arch. It adds chaotic-aur for pre-built AUR binaries, its own nemesis_repo, the ArchLinux Tweak Tool, and AI-assisted development. Less gaming and ricing, more a curated, learnable Arch you can daily-drive.

### Why two kernels — and why does the pair change from month to month?

Every Kiro ISO ships two kernels: one boots by default, the other is installed alongside as a fallback. If a kernel update ever leaves your machine unable to boot, you pick the other entry from the boot menu instead of reaching for a rescue USB.

The pair is chosen per release and deliberately changes from month to month, so the stock, LTS, Zen, CachyOS and hardened kernels all get real use on real installs. Each release card on the [release notes page](https://kiroproject.be/releases.html) lists the kernels that ISO shipped. This month:

- linux — the default. The stock Arch kernel from [core], kept close to mainline, with security fixes landing quickly.

- linux-lts — the fallback. The long-term-support kernel, also from [core]: an older, slower-moving branch that is a known-safe boot option if the newest kernel ever misbehaves after an update.

Prefer a different pair? Pick any combination yourself in the [Kiro ISO Builder](https://kiroproject.be/byoi.html), or install another kernel later via ATT.

And the rest of Kiro is kernel-agnostic by design — every sysctl, udev rule, systemd drop-in and tmpfile is written without any hardcoded kernel name or kernel-specific path. Swap to linux-cachyos, linux-hardened, or roll your own custom kernel: the tuning, security baseline, and audit checks all keep working. The shipped pair is the default, not a lock-in.

### Wasn't Kiro shipping the Liquorix kernel? What happened?

It did, for a stretch — and the choice was made openly. Kiro tested several Arch-based distros side by side; PrismLinux ran linux-lqx (Liquorix) and on real hardware it simply felt faster than stock linux. Liquorix's desktop-latency scheduler, 1000 Hz tick, and full preemption explained the feel. It was a sensible first pick and got documented as such.

What changed was the depth of the analysis. Kiro members got an in-depth kernel study — published on YouTube and Patreon for the members tier — that put every realistic Arch kernel option side by side. The data pointed at linux-cachyos and linux-zen as the stronger pair, security in particular, with responsiveness and stability close behind. (The full reasoning lives in the members content; the question above gives the short public version of what the new pair brings.)

That's why the default actually changed. Kiro is a community distro, not a personal one — so when the numbers say a different pair serves the people installing Kiro better, on security especially, the default has to follow the numbers. Even when personal preference would have stayed with Liquorix. The default is what arrives on every fresh install; it gets decided by what's best for the people running it, not by taste.

None of this is a knock on Liquorix — it's a great kernel. You can install, switch to, and boot it any time via the ArchLinux Tweak Tool (ATT) that ships in every Kiro install — same goes for any other Arch kernel you'd rather run. The Kiro principle is simple: when the evidence shifts, the default shifts with it — in the open, and in the community's favour.

### Kiro won't boot from the USB stick — what should I check?

The most common cause is Secure Boot. Like most Arch-based ISOs, the Kiro image isn't signed for Secure Boot, so you need to turn it off in your firmware before the USB will boot.

- Enter firmware setup at power-on — usually Del, F2, or F12.

- Find Secure Boot (usually under Boot or Security) and set it to Disabled, then save and exit.

- Make sure the USB was written in image / DD mode — use Ventoy, Rufus in DD mode, or dd. A plain file copy onto the stick won't boot.

Then boot from the USB again.

### I have an NVIDIA card — which boot entry do I pick, and how do I add the driver later?

Kiro's boot menu offers three driver choices, and the one you pick decides what your installed system gets:

- open source: AMD / Intel (driver=free) — the open mesa stack. The right pick for AMD and Intel GPUs; it does not install a proprietary NVIDIA driver.

- NVIDIA proprietary, modern (driver=nonfree) — keeps NVIDIA's open kernel modules (nvidia-open-dkms), recommended for Turing / RTX 20-series and newer. No detection step — the fastest path if you know you have a modern card.

- NVIDIA proprietary, auto-detect (driver=nonfreechwd) — runs chwd, which detects your exact GPU and installs the right driver, including the legacy branch for older cards.

Installed on the open entry and want NVIDIA now? No reinstall needed — run chwd on the running system:

- chwd --list — show the profile your GPU wants

- sudo chwd -a — install it automatically

The proprietary profiles chwd can install: nvidia-open-dkms (modern, Turing / RTX 20-series+), nvidia-dkms-580xx (current branch), nvidia-dkms-470xx (legacy, for older cards the current branch dropped), and the .prime variant of each for hybrid-graphics laptops. For cards too old even for 470xx, chwd falls back to the open driver. The same tool sets up AMD, Intel, and VM guests too.

### Is the proprietary NVIDIA driver verified on modern cards (RTX 20-series and newer)?

Yes for the modern path, not yet for the auto-detect path — and we'll be straight about the difference:

- The “NVIDIA proprietary, modern” entry (driver=nonfree) keeps the baked nvidia-open-dkms with no detection step. This path is verified on real modern NVIDIA hardware — the recommended pick for RTX 20-series and newer.

- The “NVIDIA proprietary, auto-detect” entry (driver=nonfreechwd) lets chwd pick and install the driver. We've verified its install logic, but not yet end-to-end on real NVIDIA hardware — a VM routes to the VirtualBox profile, so chwd's proprietary install is a known limitation pending a real-hardware pass.

If you pick a NVIDIA entry and something's off (a black screen), from a working session: confirm kernel headers (linux-headers or linux-lts-headers), re-run sudo chwd -a, and check dkms status reads nvidia … installed (not added) with nvidia-smi seeing the card. We'll mark the auto-detect path verified once confirmed on real hardware — reports from your card welcome.

### What are the hardware requirements?

Any 64-bit (x86_64) PC. For a comfortable desktop, aim for around 4 GB of RAM and ~20 GB of disk — the tiling window managers plus zram-compressed memory keep things responsive on older or lighter machines too. Both UEFI and legacy BIOS boot are supported.

### Is there a 32-bit version?

No. Kiro is 64-bit (x86_64) only, and there will never be a 32-bit build. Upstream Arch Linux dropped 32-bit (i686) support back in 2017, so a 32-bit Kiro simply isn't possible — if a machine can't run a 64-bit OS, Kiro isn't the distro for it.

### Why isn't there a torrent download?

Torrents only beat a direct download when lots of people leave their client running and seed the file. A small, fast-moving distro rarely has that, so a swarm tends to sit at one or two seeders — slower and less reliable than a plain HTTPS link, not faster. They also add real upkeep: a fresh .torrent for every build, a tracker or webseed, and an always-on seed box — for little gain at Kiro's scale, and Kiro ships new ISOs often.

The direct download already covers what people use torrents for. The ISO is served over HTTPS with published checksums and signature/verify commands, so you can confirm integrity without BitTorrent — and it works on the locked-down or corporate networks that block torrent traffic but allow HTTPS.

It's not off the table forever. If Kiro grows to where a swarm would actually stay healthy, adding a torrent or magnet alongside the direct link is easy to revisit.

### How many Kiro ISOs are there, and what's in each?

Just two.

- The default ISO — what the [Download](https://kiroproject.be/#download) button gives you (SourceForge's /files/latest/). It ships Xfce + Ohmychadwm, the Calamares installer, the nemesis_repo, and the full Kiro app suite (ATT and friends). From there the ArchLinux Tweak Tool installs any of the other desktops on demand.

- The Plasma ISO — the fully-themed KDE Plasma edition, in the [Plasma folder on SourceForge](https://sourceforge.net/projects/kiro/files/Plasma/).

The shipped kernels can change from build to build, so for the exact contents of any release check the package list (the .pkglist.txt file) next to the ISO on SourceForge.

### Older Kiro ISOs are gone from SourceForge — why, and can I still get them?

Kiro's downloads are hosted on SourceForge, and we're genuinely grateful for the free hosting and bandwidth they give open-source projects. Using a free service well isn't the same as abusing it — so we keep our footprint small and tidy up after ourselves, removing older ISOs once a newer release is out. That keeps our storage modest and means we never trip SourceForge's automated “please clean up” maintenance reminders.

Kiro is a rolling release, so an older ISO dates quickly — the newest one is almost always what you want for a fresh install, and your installed system keeps updating no matter which ISO it started from.

Want to keep a specific build? Download it and keep your own copy safe. We don't promise past ISOs stay online — only the current release is guaranteed to be there, always reachable from the [Download](https://kiroproject.be/#download) link.

### What desktops are available?

Kiro ships ATT, which installs any of 29 desktops on demand:

- 9 X11 tilers

Awesome · Bspwm · Chadwm · Dusk · Hlwm · I3 · Leftwm · Ohmychadwm · Qtile

- 14 Wayland sessions

Hyprland · Niri · Sway · Wayfire · River · Labwc · Mango · Scroll · Dwl · and shell variants

- 6 full DEs

Budgie · Cinnamon · Gnome · Mate · Plasma · Xfce

Pick what fits, or install several and switch from your login screen.

### I picked "Xfce Session (Wayland)" at login and got a black screen — is Kiro broken?

Nothing's broken — and it's not a Kiro setting. That "Xfce Session (Wayland)" entry is XFCE 4.20's own experimental Wayland mode (startxfce4 --wayland), shipped inside Arch's xfce4-session package, not anything Kiro adds. It's still in development upstream and needs a separate Wayland compositor to run — which an X11-based setup like Kiro doesn't include — so it bails out immediately and leaves you on a black screen.

The fix takes one click: at the Kiro (SDDM) login screen, pick the plain Xfce Session — not the one marked (Wayland). SDDM remembers your choice, so it sticks after the first pick.

Why we don't just remove it: the entry lives inside XFCE's own packaging, so deleting the session file would only get put back on the next package update — any distro shipping XFCE 4.20 from the Arch packages carries the exact same entry. As XFCE matures its Wayland session this disappears on its own; until then the plain X11 Xfce session is the one to use.

Full walkthrough: [XFCE Wayland session black screen — don't click it](https://youtu.be/sf_uHpio5YI).

### I installed KDE Plasma through ATT and it looks black — how do I get Plasma's own theme back?

That's expected — and it's not a Plasma bug. Kiro ships XFCE as the default desktop, and the default has to look right the moment you boot. Part of that polish is a small set of theming variables in /etc/environment that unify how Qt and GTK applications look so nothing clashes out of the box — the same approach the [ArchWiki](https://wiki.archlinux.org/title/Uniform_look_for_Qt_and_GTK_applications) documents.

The catch: those variables work system-wide. When you install Plasma on top, Plasma has its own theming engine — but the XFCE-tuned variables override it. That's where the unexpected black comes from.

The fix takes about a minute. Open /etc/environment, comment out the three theming lines with a #, then log out or reboot:

```
# /etc/environment — comment these three out for Plasma
#QT_QPA_PLATFORMTHEME=qt5ct
#QT_STYLE_OVERRIDE=kvantum
#GTK_THEME=Arc-Dawn-Dark
```

There's deliberately no one-click button — editing this by hand is what protects your XFCE look and lets you see exactly what each line does. ATT also warns you before installing a big desktop like Plasma or GNOME, because removing one again is a one-way, messy operation.

Full walkthrough: [Why KDE Plasma looks black on Kiro — and how to get the default theme back](https://youtu.be/lZbjJ6rK_3Q).

### Kiro is all dark — how do I switch to a light theme?

Dark by default is a deliberate design choice — we like everything dark, so the whole desktop is set system-wide to the Arc-Dawn-Dark theme. File manager, menus, and applications all match out of the box. A viewer asked online about the black look, and that's the honest answer: nothing's wrong, it's intentional.

Prefer a light desktop? Nothing is broken. The bright sibling in the same family is the plain Arc theme. People sometimes switch to it, notice it behaves a little differently, and assume something's off — it isn't, it's just a different look set in the same place.

That place is the system-wide theme variable in /etc/environment (the same GTK_THEME line behind the Plasma question above). Press Super + Shift + Enter to open the file manager, and change the theme to whatever you like:

```
# /etc/environment — dark default …
GTK_THEME=Arc-Dawn-Dark
# … swap to the light sibling
GTK_THEME=Arc
```

Then log out and log back in so the new look applies everywhere. That last step is the one people miss — without it you can sit there waiting, wondering why nothing changed.

One thing to watch: once you switch, your icons may not match anymore. On a light desktop a dark-leaning icon set can read as too bright — pick an icon set that suits your new theme and you're back in full control of all the colours.

This is one of those settings tucked away on purpose — a hidden gem, not for everybody. Most people are happy with the dark default and never touch it. But if you want the desktop to be truly yours, this is the knob you were looking for.

### Is Kiro available in my language?

Yes. The Kiro apps come in 14 languages: English, Dutch, German, French, Spanish, Italian, Brazilian Portuguese, Polish, Romanian, Hungarian, Turkish, Russian, Japanese and simplified Chinese. That covers the Arch Linux Tweak Tool, Kiro ISO Builder, Kiro News, KiroTux Drive and the ohmychadwm system menu, and on KiroTux the premium settings app too.

They follow the system language you pick in the installer. To use another one, pick it in the language menu at the top right of the app and restart the app when it asks; Kiro News switches with the globe button on its page, and the ohmychadwm menu always follows the system language. The desktops, Firefox and the other apps follow their own upstream translations, and this website is available in English and seven other languages through the globe button at the top.

### Is it stable enough for daily use?

Kiro is rolling-release, like Arch. Newer packages occasionally break. If you want zero-maintenance, this isn't the distro for you. If you want fresh software and don't mind reading a forum thread when something snaps, you'll be at home.

### How do updates work?

Like Arch — it's rolling. Update everything with sudo pacman -Syu (or through the pamac-aur GUI). Always do a full system upgrade rather than installing single packages, to avoid partial-upgrade breakage. Updates from the nemesis_repo arrive through the same command.

### What if an update breaks something?

Kiro ships Timeshift, so you can roll back to a snapshot you've taken — set it up once and snapshot before big changes, or put it on a schedule. Arch also lets you downgrade an individual package from the local cache. And when you need a hand, the YouTube channel and GitHub issues are there — see [Community](https://kiroproject.be/#community).

### Can I use GRUB instead of systemd-boot? What about Limine or rEFInd?

Yes to GRUB — choose it before you install. On UEFI, Kiro installs systemd-boot by default; in the live session, open Calamares Tweak Tool, pick GRUB, and launch the installer from there (it also pairs the right LUKS version if you encrypt). Legacy BIOS machines get GRUB automatically.

Most people want GRUB for snapshots — and here ATT makes life easy. Pick btrfs in the partitioning step, then open the Btrfs tab in ATT: one click installs and configures snapper + snap-pac (a snapshot pair on every pacman action, old pairs pruned automatically) and Btrfs Assistant to browse and restore. Want to pick a snapshot from the boot menu? Add grub-btrfs on a GRUB install.

Limine and rEFInd are not installer choices and are not on the roadmap for now. Neither is a tool to switch bootloaders on an already installed machine — one mistake there leaves the machine unbootable, so make the choice at install time.

Watch it step by step: [KIRO 170 · Install Kiro with Btrfs, grub-btrfs snapshots, the Calamares Tweak Tool and ATT](https://youtu.be/YuQtGL5rHEs) and [KIRO 057 · Btrfs snapshots on Kiro: roll back any broken update in seconds](https://youtu.be/XVAou9TtYlg).

### I see "Unable to resume from device…" at boot — is something broken?

No. Calamares wires up resume=UUID=… when you pick swap with hibernation; on every boot the system checks that swap for a saved hibernation image, and prints the warning when it doesn't find one. Boot continues normally — nothing's broken. If you don't plan to hibernate, remove resume= from the kernel command line to silence it; otherwise leave it.

### Is there any telemetry or tracking?

None. Kiro doesn't phone home — no usage stats, no crash reporting, no opt-ins hidden in the defaults. What you install and run stays on your machine.

### Is there a firewall?

Yes — Kiro ships firewalld on by default, with its firewall-config GUI for managing zones and rules. The defaults are sensible and need no tweaking out of the box; you'd only adjust them for specific cases, such as allowing .local/mDNS discovery on your network.

### Can I switch power profiles?

Yes — Kiro runs the tuned daemon enabled by default, providing power profiles through the standard power-profiles interface. Switch between balanced, performance, and power-saving from your desktop's power menu — no extra setup, and it works with the battery/power applet out of the box.

### Can I remove the AI / Claude parts?

Yes. The AI tooling is opt-in convenience, not a dependency. Remove the package with sudo pacman -R claude-code and delete the "Open Claude Here" entry from Thunar's right-click menu — the rest of the system is unaffected.

### Are the repos signed?

Yes — packages are PGP-signed with the Kiro Signing Key (149A BD0C 3A05 63EE), trusted via kiro-keyring. The repo inherits the system default SigLevel = Required DatabaseOptional, so pacman verifies every package signature.

### Can I use the nemesis_repo on a non-Kiro Arch system?

Yes — Erik's pre-built packages work on any Arch install. Append this block to /etc/pacman.conf:

```
# /etc/pacman.conf — append at the bottom
[nemesis_repo]
Server = https://erikdubois.github.io/$repo/$arch
```

No per-repo SigLevel line is needed — the repo inherits your global signing policy. Then trust the Kiro Signing Key and install the keyring + mirrorlist:

```
sudo pacman -Sy
sudo pacman-key --recv-keys 149ABD0C3A0563EE --keyserver keyserver.ubuntu.com
sudo pacman-key --lsign-key 149ABD0C3A0563EE
sudo pacman -Sy --needed kiro-keyring kiro-mirrorlist
```

Packages are then verified against the signed key. Optionally swap the Server line for Include = /etc/pacman.d/kiro-mirrorlist — the same line the default Kiro config ships. On a fresh Kiro install the repo is already configured; this is only needed if you want Erik's packages on stock Arch or another Arch-based distro.

Curious what's inside? Browse the live package index at [erikdubois.github.io/nemesis_repo](https://erikdubois.github.io/nemesis_repo/).

### Is it free? Why the donation links?

Yes — Kiro is free and open, with no paid tiers to use it. Donations are entirely optional and help cover development time and the AI tooling that speeds it up. See [Support](https://kiroproject.be/#support) for the ways to chip in.

### Can I help or contribute?

Yes — everything happens in public on GitHub. Pull requests, issues, and stars are all welcome. See the [Community](https://kiroproject.be/#community) section for the relevant accounts.

### Where do I get support?

Bug reports and feature requests live on GitHub. For walkthroughs, tutorials, and release updates, the YouTube channel is the main channel — see [Community](https://kiroproject.be/#community) for links.
