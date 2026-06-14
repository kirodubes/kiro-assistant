# Kiro Assistant

A personal AI assistant for the **Kiro Linux distro**. It answers questions
about installing, configuring, and troubleshooting Kiro — grounded in a curated
knowledge base built from Kiro's own docs and configs.

## What it ships

- [CLAUDE.md](./CLAUDE.md) — the assistant's instructions (its "brain"). This
  loads automatically when you open the folder in Claude Code.
- [knowledge/](./knowledge/) — the curated Kiro knowledge base the assistant
  answers from (architecture, install, packages, desktops, kernels, ATT,
  troubleshooting).
- [build/sync-knowledge.sh](./build/sync-knowledge.sh) — regenerates the
  knowledge base from Kiro's public source repos so it stays current.

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
  IPs, credentials). The `build/sync-knowledge.sh` step pulls **only** from
  Kiro's public source repos.
- The root `CLAUDE.md` doubles as both the product (the assistant's brain) and
  this repo's project instructions — there is intentionally no second
  CLAUDE.md.
- Knowledge files under `knowledge/` are the value. Keep them accurate; an
  out-of-date fact is worse than a missing one.
- **On every knowledge-base update, re-check the website FAQ for new questions.**
  The website FAQ (`kiro-website/index.html` `#faq`, mirrored in
  `Kiro-HQ/FAQ.md`) is the canonical public Q&A and grows a question or two per
  release. Before regenerating, diff the live FAQ headings against what the
  knowledge base already covers and fold in anything new, so the assistant
  answers stay in step with the public answers. Watch for contradictions
  between the two sources and reconcile them (e.g. USB-writer guidance).
