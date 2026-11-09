#!/usr/bin/env python3
"""Regenerate knowledge/faq.md from the Kiro website FAQ section.

Maintainer-only. The website source path comes from $KIRO_WEBSITE_DIR so no
personal path is baked into this public repo; inert when the variable is unset.
"""

import html
import os
import re
import sys
from pathlib import Path

SITE = "https://kiroproject.be/"
OUT = Path(__file__).resolve().parent.parent / "knowledge" / "faq.md"
HEADER = """# Website FAQ

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

"""


def _strip(text):
    return re.sub(r"<[^>]+>", "", text)


def _to_md(fragment):
    def link(m):
        href = m.group(1)
        if href.startswith("#"):
            href = SITE + href
        elif not href.startswith("http"):
            href = SITE + href
        return f"[{_strip(m.group(2)).strip()}]({href})"

    x = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', link, fragment, flags=re.S)
    x = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", x, flags=re.S)
    x = re.sub(r"<pre[^>]*>(.*?)</pre>", lambda m: "\n```\n" + _strip(m.group(1)).strip() + "\n```\n", x, flags=re.S)
    x = re.sub(r"<code>(.*?)</code>", r"`\1`", x, flags=re.S)
    x = re.sub(r"<li[^>]*>", "\n- ", x)
    x = re.sub(r"</p>|<br\s*/?>", "\n\n", x)
    x = html.unescape(_strip(x))
    x = re.sub(r"[ \t]+", " ", x)
    x = re.sub(r"\n\s*\n\s*\n+", "\n\n", x)
    lines = [ln if ln.startswith("- ") else ln.strip() for ln in x.strip().split("\n")]
    return "\n".join(lines)


def main():
    """Write knowledge/faq.md from $KIRO_WEBSITE_DIR/index.html."""
    site_dir = os.environ.get("KIRO_WEBSITE_DIR")
    if not site_dir:
        print("KIRO_WEBSITE_DIR not set — faq.md left untouched")
        return 0
    page = Path(site_dir, "index.html").read_text(encoding="utf-8")
    start = page.find('id="faq"')
    if start < 0:
        print("no #faq section found", file=sys.stderr)
        return 1
    section = page[start:page.find("</section>", start)]
    entries = []
    for block in re.findall(r"<details.*?</details>", section, re.S):
        question = re.search(r"<summary[^>]*>(.*?)</summary>", block, re.S).group(1)
        answer = block.split("</summary>", 1)[1]
        entries.append(f"### {_to_md(question)}\n\n{_to_md(answer)}\n")
    OUT.write_text(HEADER + "\n".join(entries).rstrip() + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({len(entries)} questions)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
