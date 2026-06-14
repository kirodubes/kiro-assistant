# Changelog

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
- Added packaging: `usr/bin/kiro-assistant` launcher (seeds a per-user writable
  copy under `~/.local/share/kiro-assistant`, then runs `claude` there),
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
- Validated the incremental video sync live: after two new uploads (KIRO 101 —
  signed packages, KIRO 102 — MintStick USB writer), `sync-videos.py` fetched
  exactly those two (stopped at the cursor, no full rescan), classified them
  into the KIRO series, regenerated `videos.md`, and advanced the cursor. Index
  now at 164 videos.
- `build/sync-knowledge.sh` stubbed following the canonical bash template.

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
