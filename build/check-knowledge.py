#!/usr/bin/env python3
"""Report drift between the knowledge pack and the Kiro source repos.

Maintainer-only, read-only: run before each monthly release. Source paths come
from environment variables so no personal path is baked into this public repo:
KIRO_ISO_DIR, KIRO_ATT_DIR, KIRO_SYSTEM_FILES_DIR, KIRO_WEBSITE_DIR. A check
whose variable is unset is skipped. Exit code 1 when anything drifted.
"""

import ast
import html
import os
import re
import sys
from pathlib import Path

KNOW = Path(__file__).resolve().parent.parent / "knowledge"
drift = []


def _env(name):
    value = os.environ.get(name)
    if not value:
        print(f"skip: {name} not set")
        return None
    return Path(value)


def _read(name):
    return (KNOW / name).read_text(encoding="utf-8")


def _literal(path, var):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == var for t in node.targets):
            return node.value
    raise SystemExit(f"{var} not found in {path}")


def _expect(ok, message):
    print(("ok    " if ok else "DRIFT ") + message)
    if not ok:
        drift.append(message)


def check_iso():
    """Kernel pair and boot-entry wording."""
    iso = _env("KIRO_ISO_DIR")
    if not iso:
        return
    conf = (iso / "build-scripts/build.conf").read_text(encoding="utf-8")
    pair = re.search(r'^kernel="([^"]+)"', conf, re.M).group(1).split()
    kernels = _read("kernels.md")
    _expect(all(f"`{k}`" in kernels for k in pair), f"kernels.md names this release's pair {pair}")
    install = _read("install.md")
    for entry in sorted((iso / "archiso/efiboot/loader/entries").glob("*.conf")):
        title = re.search(r"^title\s+.*?UEFI, (.*)\)$", entry.read_text(encoding="utf-8"), re.M)
        if title and "fallback kernel" not in title.group(1):
            _expect(title.group(1) in install, f"install.md has boot entry '{title.group(1)}'")


def check_att():
    """Desktop, Wayland and kernel counts in ATT."""
    att = _env("KIRO_ATT_DIR")
    if not att:
        return
    src = att / "usr/share/archlinux-tweak-tool"
    desktops = len(_literal(src / "desktopr.py", "desktops").elts)
    wayland = _literal(src / "wayland.py", "WAYLAND_WMS").elts
    ready = sum(1 for d in wayland if any(
        getattr(k, "value", None) == "ready" and getattr(v, "value", None) is True for k, v in zip(d.keys, d.values)))
    kernels = len(_literal(src / "kernel.py", "KERNELS").elts)
    _expect(f"**ATT → Desktop** ({desktops}" in _read("desktops.md"), f"desktops.md says {desktops} Desktop entries")
    _expect(f"{ready} Kiro Wayland configs" in _read("wayland.md"), f"wayland.md says {ready} Wayland entries")
    _expect(f"{desktops + ready}**" in _read("desktops.md"), f"desktops.md total is {desktops + ready}")
    _expect(f"{kernels} kernels" in _read("att.md"), f"att.md says {kernels} kernels")


def check_tools():
    """Every kiro-* command is in tools.md."""
    sysf = _env("KIRO_SYSTEM_FILES_DIR")
    if not sysf:
        return
    tools = _read("tools.md")
    hidden = {"kiro-xlibre-swap", "kiro-common.sh"}
    for tool in sorted(p.name for p in (sysf / "usr/local/bin").glob("kiro-*")):
        if tool not in hidden:
            _expect(f"`{tool}`" in tools or f"/ `{tool}`" in tools, f"tools.md lists {tool}")


def check_website():
    """KiroTux editions and FAQ questions."""
    site = _env("KIRO_WEBSITE_DIR")
    if not site:
        return
    kirotux = _read("kirotux.md")
    for page in sorted(site.glob("kirotux-*.html")):
        _expect(page.name in kirotux, f"kirotux.md links {page.name}")
    index = (site / "index.html").read_text(encoding="utf-8")
    start = index.find('id="faq"')
    section = index[start:index.find("</section>", start)]
    live = re.findall(r"<summary[^>]*>(.*?)</summary>", section, re.S)
    faq = re.sub(r"\s+", " ", _read("faq.md"))
    for question in live:
        text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", question))).strip()
        if text and text[:40] not in faq:
            _expect(False, f"faq.md has '{text[:60]}' (run build/sync-faq.py)")


def main():
    """Run every check and report."""
    for check in (check_iso, check_att, check_tools, check_website):
        check()
    print(f"\n{len(drift)} drift item(s)")
    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main())
