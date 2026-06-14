#!/usr/bin/env python
"""Maintainer tool: refresh knowledge/videos.md from the YouTube channel.

Incremental and additive — it fetches the channel's uploads newest-first and
stops as soon as it reaches videos already captured, so each run only ADDS
newly published videos and leaves existing entries alone. Run it before the
weekly push.

Data lives in build/videos-data.json (committed, public data only). videos.md
is regenerated from that cache on every run.

Requirements (maintainer machine only):
  - YouTube Data API OAuth creds in ~/.config/kiro-youtube/ (token.json), the
    same creds the kiro-youtube tool uses.
  - Optional: set KIRO_WEBSITE_DIR to the Kiro website checkout to refresh the
    "featured on the website" set. If unset, the cached website set is kept.

Usage:
  python build/sync-videos.py
  KIRO_WEBSITE_DIR=/path/to/kiro-website python build/sync-videos.py
"""
import json
import os
import re
import sys
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
TOKEN_FILE = os.path.expanduser("~/.config/kiro-youtube/token.json")

REPO = Path(__file__).resolve().parents[1]
CACHE = REPO / "build" / "videos-data.json"
OUT = REPO / "knowledge" / "videos.md"
CHANNEL = "https://www.youtube.com/@ErikDubois"

VID_RE = re.compile(r"youtu(?:be\.com/(?:watch\?v=|embed/)|\.be/)([A-Za-z0-9_-]{11})")


def service():
    creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds.valid and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    return build("youtube", "v3", credentials=creds)


def load_cache():
    if CACHE.exists():
        return json.loads(CACHE.read_text())
    return {"last_published": "", "videos": {}}


def save_cache(cache):
    CACHE.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n")


def classify(title):
    if "KIRO" in title:
        return "caps"
    if re.search(r"kiro", title, re.IGNORECASE):
        return "low"
    return None


# Erik's descriptions often LEAD with a "Membership is live" line and/or a bare
# URL before the real body, and END with the standing upload footer. So we skip
# that leading noise, then stop at the first trailing-footer marker.
_MEMBERSHIP_RE = re.compile(r"^\s*membership is live", re.IGNORECASE)
_BARE_URL_RE = re.compile(r"^\s*https?://\S+\s*$", re.IGNORECASE)
_FOOTER_RE = re.compile(
    r"^\s*("
    r"kiro\s*[—-]\s*arch linux"      # footer header "Kiro — Arch Linux, built right"
    r"|about kiro"
    r"|support\b"
    r"|github sponsors"
    r"|ko-?fi"
    r"|paypal"
    r"|youtube member"
    r"|patreon"
    r"|website\s*[:=]"
    r"|={3,}$|-{3,}$"                # separator lines
    r"|#\w+"
    r")",
    re.IGNORECASE,
)

SUMMARY_MAX = 280


def summarize(description):
    """Reduce a raw YouTube description to a short, footer-free summary."""
    body = []
    for raw in (description or "").splitlines():
        s = raw.strip()
        if not body and (_MEMBERSHIP_RE.match(s) or _BARE_URL_RE.match(s)):
            continue
        if _FOOTER_RE.match(s) or (body and _MEMBERSHIP_RE.match(s)):
            break
        if s:
            body.append(s)
    text = " ".join(" ".join(body).split())
    if len(text) > SUMMARY_MAX:
        text = text[:SUMMARY_MAX].rsplit(" ", 1)[0] + "…"
    return text


def fetch_new(yt, since):
    """Return (new_videos, newest_published). Stops at the first video that is
    not newer than `since` (uploads come back newest-first)."""
    ch = yt.channels().list(part="contentDetails", mine=True).execute()
    uploads = ch["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    new, newest, token, stop = [], since, None, False
    while not stop:
        resp = yt.playlistItems().list(
            part="snippet", playlistId=uploads, maxResults=50, pageToken=token
        ).execute()
        for it in resp["items"]:
            sn = it["snippet"]
            pub = sn.get("publishedAt", "")
            if since and pub <= since:
                stop = True
                break
            newest = max(newest, pub)
            new.append({
                "id": sn.get("resourceId", {}).get("videoId", ""),
                "title": sn.get("title", ""),
                "published": pub,
            })
        token = resp.get("nextPageToken")
        if not token:
            break
        sys.stderr.write(f"\rfetched {len(new)} new…")
        sys.stderr.flush()
    sys.stderr.write("\n")
    return new, newest


def website_ids(dirpath):
    ids = set()
    base = Path(dirpath)
    for path in base.rglob("*"):
        if not path.is_file() or "/.git/" in str(path):
            continue
        if path.suffix not in (".html", ".js", ".json", ".md"):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        # A video featured only in the repo CHANGELOG is an incidental mention,
        # not a curated website video — skip those.
        if path.name == "CHANGELOG.md":
            continue
        ids.update(VID_RE.findall(text))
    return ids


def kiro_num(title):
    m = re.match(r"^KIRO\s*0*(\d+)", title)
    return int(m.group(1)) if m else 9999


def render(cache):
    vids = cache["videos"]
    site = [v for v in vids.values() if v.get("website")]
    site.sort(key=lambda v: (kiro_num(v["title"]), v["published"]))

    caps = [v for v in vids.values() if v.get("cls") == "caps"]
    series = [v for v in caps if re.match(r"^KIRO\s*\d+", v["title"])]
    caps_other = [v for v in caps if not re.match(r"^KIRO\s*\d+", v["title"])]
    series.sort(key=lambda v: (kiro_num(v["title"]), v["published"]))

    older = caps_other + [v for v in vids.values() if v.get("cls") == "low"]
    older.sort(key=lambda v: v["published"], reverse=True)

    def link(v):
        line = f"- [{v['title']}](https://youtu.be/{v['id']})"
        summary = v.get("summary")
        if summary:
            line += f" — {summary}"
        return line

    out = []
    a = out.append
    a("# Kiro Video Tutorials")
    a("")
    a("Erik Dubois publishes Kiro tutorials on YouTube. Use this file to point")
    a("users at the right video. Suggested order when helping someone:")
    a("")
    a("1. **Start with the website videos** below — the curated starting point")
    a("   hand-picked for kiroproject.be, the beginning of the Linux/Kiro")
    a("   journey.")
    a("2. Then the **KIRO** series — the current, numbered Kiro tutorial series.")
    a("3. Then the older **Kiro** videos for release history and earlier how-tos.")
    a("")
    a(f"Channel: {CHANNEL}")
    a("")
    a("> When you can't find an exact match here, **send the user to search the")
    a("> channel** — see *Search the channel* at the bottom. That is the single")
    a("> most useful thing you can do; the catalog is far larger than this list.")
    a("")
    a("## 1. Start here — videos featured on the website")
    a("")
    a("These are the videos Erik put on kiroproject.be on purpose: the intended")
    a("first stop for a new user.")
    a("")
    out.extend(link(v) for v in site)
    a("")
    a("## 2. The KIRO series (current Kiro tutorials)")
    a("")
    a(f"The numbered KIRO series — {len(series)} videos, the up-to-date tutorials")
    a("for Kiro as it ships today. Listed in series order (start low, or jump to")
    a("a topic by keyword in the title).")
    a("")
    out.extend(link(v) for v in series)
    a("")
    a("## 3. Older Kiro videos (release history and earlier how-tos)")
    a("")
    a(f"Earlier Kiro videos — {len(older)} of them, newest first. These cover")
    a("past ISO releases, build walkthroughs, and earlier workflows. Some")
    a("reference older tooling, so treat them as background rather than current")
    a("instructions.")
    a("")
    out.extend(link(v) for v in older)
    a("")
    a("## Older videos still apply more often than you'd think")
    a("")
    a("The channel has thousands of older videos (including the ArcoLinux era)")
    a("that are not listed here. Don't dismiss them: Kiro runs the same apps,")
    a("with the same or only slightly different configuration, so a great deal")
    a("still applies directly. Many are also **workflow** videos and")
    a("**common-sense, analytical** videos — the thinking carries over to Kiro")
    a("unchanged. If a topic isn't covered above, an older video may answer it.")
    a("")
    a("## Search the channel")
    a("")
    a("This list is a small slice of the catalog. When in doubt, point the user")
    a("to **search Erik's YouTube channel** directly:")
    a("")
    a(f"- Browse: {CHANNEL}/videos")
    a(f"- Search a topic: {CHANNEL}/search?query=YOUR+TERM")
    a("")
    a("Suggest a concrete search term based on what they asked (e.g. `nvidia`,")
    a("`calamares`, `qtile`, `theming`). Searching our channel is the best way")
    a("to find the one video that fits.")
    OUT.write_text("\n".join(out) + "\n")


def main():
    cache = load_cache()
    vids = cache["videos"]
    yt = service()

    new, newest = fetch_new(yt, cache["last_published"])
    added = 0
    for v in new:
        cls = classify(v["title"])
        if cls and v["id"] not in vids:
            vids[v["id"]] = {
                "id": v["id"], "title": v["title"],
                "published": v["published"], "cls": cls,
            }
            added += 1
    cache["last_published"] = newest

    site_dir = os.environ.get("KIRO_WEBSITE_DIR")
    if site_dir and os.path.isdir(site_dir):
        wanted = website_ids(site_dir)
        # Pull titles for any website videos we don't already know about.
        missing = [i for i in wanted if i not in vids]
        for batch_start in range(0, len(missing), 50):
            chunk = missing[batch_start:batch_start + 50]
            resp = yt.videos().list(part="snippet", id=",".join(chunk)).execute()
            for it in resp["items"]:
                vids[it["id"]] = {
                    "id": it["id"], "title": it["snippet"]["title"],
                    "published": it["snippet"]["publishedAt"],
                    "cls": classify(it["snippet"]["title"]),
                }
        for vid in vids.values():
            vid["website"] = vid["id"] in wanted
        print(f"website set refreshed: {len(wanted)} videos")
    else:
        print("KIRO_WEBSITE_DIR not set — keeping cached website set")

    # Backfill a short, footer-free summary for any video missing one. The
    # description rides along in the videos.list snippet, so this is cheap
    # (~1 quota unit per 50 videos) and idempotent — an empty body stores "",
    # and every requested id gets a key so deleted/private videos aren't
    # refetched on every run.
    need = [vid for vid, v in vids.items() if not v.get("summary")]
    for batch_start in range(0, len(need), 50):
        chunk = need[batch_start:batch_start + 50]
        resp = yt.videos().list(part="snippet", id=",".join(chunk)).execute()
        got = {it["id"]: it["snippet"].get("description", "") for it in resp["items"]}
        for vid in chunk:
            vids[vid]["summary"] = summarize(got.get(vid, ""))
    if need:
        print(f"summaries backfilled: {len(need)} video(s)")

    save_cache(cache)
    render(cache)
    print(f"added {added} new video(s); {len(vids)} total in index")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
