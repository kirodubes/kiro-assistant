# Changelog

## 2026.06.15

### What Changed

- The assistant now always renders the YouTube channel as a clickable markdown
  link in its answers (browse, topic-search, and community/off-topic pointers),
  never a bare URL — same for individual video links.
- Added **topic playlists** to the knowledge pack. The assistant can now hand a
  user a whole topic playlist (Btrfs, Nvidia, kernels, a window manager, ATT,
  pure-Arch install, …) for a deep dive, on top of the individual videos. It
  follows a tiered serve order: KIRO videos → kiro videos → tier-3 topic
  playlists, falling back to a channel search only when all three miss.

### Technical Details

- Added a "Always make the YouTube channel a clickable link" rule to the
  "How to answer" section of `CLAUDE.md`, with the canonical channel and
  topic-search link forms.
- New generator `build/sync-playlists.py` renders `knowledge/playlists.md` from
  a **curated** `build/playlists.json` (81 playlists), refreshing each
  playlist's live title/video-count from the YouTube Data API (same
  `~/.config/kiro-youtube` OAuth as `sync-videos.py`). Unlike videos, playlists
  are curated, not auto-discovered — the channel has 700+, so only a
  topic-relevant slice ships. Curated down from 707: excluded other-distro,
  icon-theme, and distro-spin playlists (kept pure-Arch install, archinstall and
  Archiso under an Installation category); relabeled the survivors by topic
  (dropping the "ArcoLinux" brand); grouped into 10 tier-3 categories plus a
  Kiro series section. ATT-specific playlists are kept regardless of which
  Arch-based distro they were filmed on.
- Rewrote the "Point to video tutorials" rule in `CLAUDE.md` as an explicit
  three-tier order pointing at both `videos.md` and `playlists.md`, added a
  "tool videos cross distros" rule, and extended the "never claim a video is
  missing" grep to cover `playlists.md` too.
- `up.sh` gained an optional `build/sync-playlists.py` hook beside the existing
  `sync-videos.py` one (inert in other repos). README updated to document both
  generators and the curated `playlists.json`.

### Files Modified

- `CLAUDE.md`
- `build/sync-playlists.py` (new)
- `build/playlists.json` (new)
- `knowledge/playlists.md` (new, generated)
- `up.sh`
- `README.md`

## 2026.06.14

### What Changed

- Initial scaffold of the Kiro Assistant: a bring-your-own-key AI helper for
  Kiro users, grounded in a curated knowledge base.

### Technical Details

- Root `CLAUDE.md` holds the assistant's instructions and auto-loads in Claude
  Code; it doubles as the repo's project instructions (no second CLAUDE.md).
- `knowledge/` — all files filled in with grounded content (no fabrication;
  every fact verified against the public source repos): `architecture.md`,
  `install.md`, `packages.md`, `att.md`, `troubleshooting.md`, `kernels.md`,
  plus `desktops.md`. Sources include the production `kiro-iso` profile
  (packages, pacman.conf, bootloader entries), `kiro-calamares-config`,
  `nemesis_repo`, `kiro-system-files`, and ATT's `gui.py` page registrations.
- `knowledge/desktops.md` filled in for real from the production `kiro-iso`
  package list and the editions build config: editions model, default
  `xfce ohmychadwm` ISO, the six full-desktop editions, the seven tiling WMs,
  config locations, and the per-environment keybindings cheatsheets.
- Added packaging: `usr/bin/kiro-assistant` launcher (reads the shipped pack in
  place from `/usr/share/kiro-assistant` and runs `claude` there),
  `usr/share/applications/kiro-assistant.desktop`, and GPL3 `LICENSE`.
- Local test PKGBUILD recipe created at
  `~/KIRO-PKG-BUILD-APPS/kiro-assistant/` (builds from the working tree; depends
  on `claude-code`). First test package built: `kiro-assistant-26.06-01-any`.
- Added `knowledge/videos.md` — a video-tutorial index generated from a scan of
  the @ErikDubois YouTube channel (5,825 uploads). Sections: website "start
  here" videos (27), the numbered KIRO series (102), older Kiro videos (60), a
  note that older/ArcoLinux-era videos still apply (same apps), and a
  search-the-channel redirect. ArcoLinux videos (4,253) intentionally excluded
  from the lists. CLAUDE.md updated with a rule to point users at these videos.
- Added `build/sync-videos.py` — the maintainer tool that regenerates
  `videos.md` for the weekly push. Incremental and additive: it fetches the
  channel newest-first and stops at the first already-captured video, so it
  only adds newly published videos and leaves existing entries alone. State is
  kept in the committed `build/videos-data.json` (public data only); the
  website set refreshes when `KIRO_WEBSITE_DIR` is set. No personal paths
  (repo-relative output, `~/.config/kiro-youtube` creds, env-var website dir).
- Prepared nemesis_repo delivery: PKGBUILD switched from the local-test variant
  to the production **git-source** variant (`git+https://github.com/kirodubes/kiro-assistant`,
  `makedepends=git`); added canonical `up.sh` + `setup.sh` to the source repo;
  registered `flow-kiro-assistant` in the flow generator manifest and
  regenerated it. Remaining gated step: create/push the public GitHub repo
  before the flow can build in chroot.
- Wired `build/sync-videos.py` into the push: the canonical `up.sh` template
  gained an optional `build/sync-videos.py` hook (runs before commit if the
  script is present), so `up.sh` — and therefore `flow-kiro-assistant` — now
  refreshes `videos.md` with newly published videos on every run. The repo's
  `up.sh` is identical to canonical again (no divergence). Runs without
  `KIRO_WEBSITE_DIR` by default (public script — no baked path), keeping the
  cached website set.
- Validated the incremental video sync live: after two new uploads (KIRO 101 —
  signed packages, KIRO 102 — MintStick USB writer), `sync-videos.py` fetched
  exactly those two (stopped at the cursor, no full rescan), classified them
  into the KIRO series, regenerated `videos.md`, and advanced the cursor. Index
  now at 164 videos.
- Added per-video **summaries** to the video index so the assistant can match a
  user's question against real content, not just the (terse, numbered) title.
  `sync-videos.py` now backfills a short, footer-free summary for any video
  one — the description rides along in the `videos.list` snippet (~1 quota unit
  per 50 videos), so it's cheap. `summarize()` first skips the leading boilerplate
  Erik's descriptions open with (a "Membership is live" line and/or a bare URL),
  then collects the body and stops at the standing upload footer ("Kiro — Arch
  Linux, built right" header, Support block, About/links, separator/hashtag
  lines), capped at 280 chars. The backfill retries any video whose summary is
  empty, so a description edited later self-heals on the next run. Result:
  164/168 videos summarized; the 4 empties are genuinely body-less (footer-only)
  descriptions. Summaries render inline after each link in `videos.md`.
- `build/sync-knowledge.sh` stubbed following the canonical bash template.
- Surfaced Kiro Assistant in the XFCE **Kiro** applications-menu folder: tagged
  `kiro-assistant.desktop` with `Categories=...;X-Kiro;` so garcon includes it
  in the Kiro folder (kept `Utility;System;` so it still shows in its normal
  categories). The matching `<Layout>` entry lives in `kiro-dot-files`'
  `kiro.menu`.
- README "For maintainers" gained a standing reminder: on every knowledge-base
  update, re-check the website FAQ (canonical public Q&A, mirrored in
  `Kiro-HQ/FAQ.md`) for newly added questions and fold them in, watching for
  contradictions between the two sources (e.g. the USB-writer guidance — the
  website FAQ still lists Ventoy, which this pack deliberately does not
  recommend in favour of MintStick).
- Reworked the launcher's writable-state model. The original wrapper copied the
  whole pack into `~/.local/share/kiro-assistant` on every launch, which would
  silently overwrite any knowledge the assistant wrote into a shipped file on
  the next run. Verified empirically that Claude Code runs cleanly with cwd set
  to the read-only, root-owned `/usr/share/kiro-assistant` (loads the pack's
  `CLAUDE.md`, writes nothing to cwd — session state goes to `~/.claude`), so
  the copy was removed entirely. The launcher now reads the pack in place and
  only creates `~/.claude/kiro-assistant/` — a dedicated, persistent user
  knowledge layer that never collides with the pack and survives updates. The
  shipped `CLAUDE.md` gained a "Your memory" section telling the assistant to
  eager-load that folder at session start, write remembered notes there (never
  into the pack), prefer additive notes over overriding shipped facts so updates
  keep reaching the user, and treat it as the one folder to back up / carry to a
  new install.

### Files Modified

- `CLAUDE.md` (new)
- `README.md` (new)
- `CHANGELOG.md` (new)
- `knowledge/architecture.md` (new)
- `knowledge/install.md` (new)
- `knowledge/packages.md` (new)
- `knowledge/desktops.md` (new)
- `knowledge/kernels.md` (new)
- `knowledge/att.md` (new)
- `knowledge/troubleshooting.md` (new)
- `build/sync-knowledge.sh` (new)
- `usr/share/applications/kiro-assistant.desktop`
