# Kiro Assistant

A personal AI assistant for the **Kiro Linux distro**. It answers questions
about installing, configuring, and troubleshooting Kiro — grounded in a curated
knowledge base built from Kiro's own docs and configs.

## What it ships

- [CLAUDE.md](./CLAUDE.md) — the assistant's instructions (its "brain"). This
  loads automatically when you open the folder in Claude Code.
- [knowledge/](./knowledge/) — the curated Kiro knowledge base the assistant
  answers from (architecture, install, packages, apps, tools, desktops,
  wayland, KiroTux, kernels, ATT, troubleshooting, how-to recipes, and the
  website FAQ), plus generated video references: `videos.md` (the KIRO/kiro
  video catalog) and `playlists.md` (topic playlists for deep dives). The
  `knowledge/archive/` folder is a **Tier 3 historical** layer — preserved
  arcolinux.com / arcolinuxd.com tutorials, always overruled by the current
  knowledge above.
- [build/check-knowledge.py](./build/check-knowledge.py) — maintainer-only
  drift check: compares the pack with the Kiro source repos (kernel pair, boot
  entries, ATT desktop/Wayland/kernel counts, kiro-* tools, KiroTux editions,
  website FAQ) and exits 1 on drift. Source paths come from `KIRO_ISO_DIR`,
  `KIRO_ATT_DIR`, `KIRO_SYSTEM_FILES_DIR` and `KIRO_WEBSITE_DIR`; unset ones
  are skipped.
- [build/sync-faq.py](./build/sync-faq.py) — regenerates `knowledge/faq.md`
  from the website FAQ (`$KIRO_WEBSITE_DIR`; inert when unset).
- [build/sync-videos.py](./build/sync-videos.py) and
  [build/sync-playlists.py](./build/sync-playlists.py) — regenerate `videos.md`
  and `playlists.md` from the YouTube channel (maintainer-only, run by `up.sh`).
- [build/sync-archive.sh](./build/sync-archive.sh) — copies the preserved
  ArcoLinux archive into `knowledge/archive/` from `$ARCOLINUX_ARCHIVE_DIR`
  (maintainer-only; inert when the var is unset, run by `up.sh`).

## How to use it (bring your own key)

You run the assistant with your own Claude access, so it costs you nothing
beyond your own usage:

```bash
git clone https://github.com/kirodubes/kiro-assistant.git
cd kiro-assistant
claude            # opens Claude Code; CLAUDE.md loads automatically
```

Then just ask, e.g. *"How do I write the Kiro ISO to a USB stick?"* or
*"Which kernel does Kiro use by default?"*

## For maintainers

- This repo is **public**. Everything in it ships to users — it must never
  contain personal or system-identifying information (home paths, hostnames,
  IPs, credentials). The build scripts read **only** Kiro's public source
  repos, and take their paths from environment variables.
- The root `CLAUDE.md` doubles as both the product (the assistant's brain) and
  this repo's project instructions — there is intentionally no second
  CLAUDE.md.
- Knowledge files under `knowledge/` are the value. Keep them accurate; an
  out-of-date fact is worse than a missing one. `videos.md` and `playlists.md`
  are **generated** — never hand-edit them. `videos.md` is auto-synced; the
  playlist set is **curated** in [build/playlists.json](./build/playlists.json)
  (add or remove an entry there, then rerun `build/sync-playlists.py`).
- **Before each monthly release, run `build/check-knowledge.py`** and fix every
  DRIFT line. The topic files are hand-maintained; the check tells you which
  one went stale.
- **Harvest recipes on the spot.** When a support answer turns into a
  step-by-step fix (Discussions, YouTube comments, a session), add it to
  `knowledge/howto.md` right away: ATT route first with the button labels
  taken from ATT's `.po` files (never translated by hand), then the terminal
  route.
- **On every knowledge-base update, re-check the website FAQ for new questions.**
  The website FAQ (`kiro-website/index.html` `#faq`, mirrored in
  `Kiro-HQ/FAQ.md`) is the canonical public Q&A and grows a question or two per
  release. Before regenerating, diff the live FAQ headings against what the
  knowledge base already covers and fold in anything new, so the assistant
  answers stay in step with the public answers. Watch for contradictions
  between the two sources and reconcile them (e.g. USB-writer guidance).

<!-- KIRO-FUNDING-FOOTER:START — managed by Kiro-HQ/cascade-readme-footer.sh -->
## Help fund Kiro

Everything I build here stays free and open — always. If Kiro or any of these
tools have ever saved you time or taught you something, a small monthly
contribution helps keep the work going. Donations target break-even, nothing
more — the core always stays free for everyone.

- GitHub Sponsors: https://github.com/sponsors/erikdubois
- Patreon: https://www.patreon.com/c/kiroproject
- YouTube memberships: https://www.youtube.com/@ErikDubois/join
- Ko-fi: https://ko-fi.com/erikdubois
- PayPal: https://www.paypal.me/erikdubois
<!-- KIRO-FUNDING-FOOTER:END -->
