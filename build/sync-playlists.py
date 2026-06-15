#!/usr/bin/env python
"""Maintainer tool: regenerate knowledge/playlists.md from build/playlists.json.

Unlike sync-videos.py, the playlist set is CURATED, not auto-discovered: the
channel has 700+ playlists and only a hand-picked, topic-relevant slice belongs
in the knowledge pack. The curation lives in build/playlists.json — add or
remove an entry there to change what ships. Each entry carries the editorial
fields (topic label, category, tier, blurb); this script only refreshes the
live title/video-count from the API and re-renders the markdown.

Tiers map to the assistant's serve order:
  1 = KIRO series, 2 = kiro videos (both also covered by videos.md),
  3 = ArcoLinux-legacy topic playlists — still apply, used as the fallback.

Requirements (maintainer machine only):
  - YouTube Data API OAuth creds in ~/.config/kiro-youtube/ (token.json), the
    same creds sync-videos.py and the kiro-youtube tool use.

Usage:
  python build/sync-playlists.py
"""
import json
import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
TOKEN_FILE = os.path.expanduser("~/.config/kiro-youtube/token.json")

REPO = Path(__file__).resolve().parents[1]
DATA = REPO / "build" / "playlists.json"
OUT = REPO / "knowledge" / "playlists.md"
CHANNEL = "https://www.youtube.com/@ErikDubois"

# Tier-3 category order in the rendered file.
CATEGORY_ORDER = [
    "Installation & Arch base",
    "Hardware / system",
    "Troubleshooting",
    "Apps / tooling",
    "Shell",
    "Login / autostart / skel",
    "Tiling WMs",
    "Desktop environments",
    "Theming / ricing",
    "Workflow / philosophy",
]


def service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds.valid and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)


def refresh_counts(yt, playlists):
    """Refresh live title + video count for every curated playlist id."""
    by_id = {p["id"]: p for p in playlists}
    ids = list(by_id)
    for start in range(0, len(ids), 50):
        chunk = ids[start:start + 50]
        resp = yt.playlists().list(
            part="snippet,contentDetails", id=",".join(chunk), maxResults=50
        ).execute()
        for it in resp["items"]:
            p = by_id[it["id"]]
            p["title"] = it["snippet"]["title"]
            p["count"] = it["contentDetails"]["itemCount"]


def plink(p):
    url = f"https://www.youtube.com/playlist?list={p['id']}"
    return f"- [{p['topic']}]({url}) — {p['count']} videos — {p['blurb']}"


def render(playlists):
    out = []
    a = out.append
    a("# Kiro Playlists (topic-organized video collections)")
    a("")
    a("Erik Dubois groups his videos into topic playlists. Use this file to hand")
    a("a user a whole playlist when they want to go deep on one subject.")
    a("")
    a("**Serve order — always try videos before playlists:**")
    a("")
    a("1. **Tier 1** — the KIRO series in [videos.md](./videos.md).")
    a("2. **Tier 2** — the older kiro videos in [videos.md](./videos.md).")
    a("3. **Tier 3** — the topic playlists below. These are largely")
    a("   ArcoLinux-era recordings, but Kiro is Arch-based and runs the same")
    a("   apps, so they still apply directly. Reach for them when tiers 1–2 have")
    a("   no close match, or when the user wants a deep dive on one topic.")
    a("")
    a("Tool videos (ATT especially) are often filmed on other Arch-based distros")
    a("— EndeavourOS, Garuda and friends. The tool is the same, so do not dismiss")
    a("a video because of the distro in its title.")
    a("")
    a(f"Channel: {CHANNEL}")
    a("")

    kiro = [p for p in playlists if p["tier"] in (1, 2)]
    kiro.sort(key=lambda p: (p["tier"], -p["count"]))
    a("## Kiro series playlists")
    a("")
    a("Browse-the-whole-series links for Kiro itself. Prefer the individual")
    a("videos in [videos.md](./videos.md) first; these are for when the user")
    a("wants everything in one place.")
    a("")
    out.extend(plink(p) for p in kiro)
    a("")

    a("## Tier 3 — topic playlists (ArcoLinux-legacy, still apply)")
    a("")
    tier3 = [p for p in playlists if p["tier"] == 3]
    for cat in CATEGORY_ORDER:
        group = [p for p in tier3 if p["category"] == cat]
        if not group:
            continue
        group.sort(key=lambda p: -p["count"])
        a(f"### {cat}")
        a("")
        out.extend(plink(p) for p in group)
        a("")

    a("## When nothing here fits")
    a("")
    a("Send the user to **search the channel** — far larger than this list:")
    a("")
    a(f"- Browse playlists: {CHANNEL}/playlists")
    a(f"- Search a topic: {CHANNEL}/search?query=YOUR+TERM")
    OUT.write_text("\n".join(out) + "\n")


def main():
    data = json.loads(DATA.read_text())
    playlists = data["playlists"]

    try:
        yt = service()
        refresh_counts(yt, playlists)
        DATA.write_text(json.dumps(data, indent=2) + "\n")
        print(f"refreshed {len(playlists)} playlist(s) from the API")
    except Exception as exc:  # noqa: BLE001 — render from cache on any API failure
        print(f"API refresh skipped ({exc}); rendering from cached playlists.json")

    render(playlists)
    print(f"wrote {OUT} ({len(playlists)} playlists)")


if __name__ == "__main__":
    main()
