#!/bin/bash
set -euo pipefail

#####################################################################
# Author : Erik Dubois
# Website : https://kiroproject.be
#
# DO NOT JUST RUN THIS. EXAMINE AND JUDGE. RUN AT YOUR OWN RISK.
#
# Purpose:
#   Sync the ArcoLinux Archive (preserved arcolinux.com / arcolinuxd.com
#   content) into ../knowledge/archive/ as a searchable HISTORICAL tier
#   the assistant can grep when current knowledge has no answer.
#
# Why:
#   The archive is a big body of still-useful Erik-authored how-tos. It
#   is preserved in its own repo (arcolinux-archive); this copies the
#   generated Markdown in so it ships with the assistant. Maintainer-only:
#   the source path is read from $ARCOLINUX_ARCHIVE_DIR so NO personal
#   path is ever baked into this PUBLIC repo. Inert when the var is unset
#   (the committed copy is kept untouched).
#####################################################################

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

# ── Colors ──────────────────────────────────────────────────────────
if [ -t 1 ]; then
  RED="$(tput setaf 1)"; GREEN="$(tput setaf 2)"; YELLOW="$(tput setaf 3)"
  BLUE="$(tput setaf 4)"; CYAN="$(tput setaf 6)"; RESET="$(tput sgr0)"
else
  RED=""; GREEN=""; YELLOW=""; BLUE=""; CYAN=""; RESET=""
fi

# ── Logging ─────────────────────────────────────────────────────────
log_section() { echo "${GREEN}############ $* ############${RESET}"; }
log_info()    { echo "${BLUE}############ $* ############${RESET}"; }
log_warn()    { echo "${YELLOW}############ $* ############${RESET}"; }
log_error()   { echo "${RED}############ $* ############${RESET}"; }
log_success() { echo "${GREEN}############ $* ############${RESET}"; }

# ── Error handling ──────────────────────────────────────────────────
on_error() {
  echo "${RED}ERROR on line $1: $2${RESET}"
  sleep 10
}
trap 'on_error "$LINENO" "$BASH_COMMAND"' ERR

# ── Functions ───────────────────────────────────────────────────────
DEST="$(cd -- "$SCRIPT_DIR/.." && pwd)/knowledge/archive"

sync_archive() {
  local src="${ARCOLINUX_ARCHIVE_DIR:-}"
  if [ -z "$src" ] || [ ! -d "$src/archive" ]; then
    log_warn "ARCOLINUX_ARCHIVE_DIR unset or has no archive/ — keeping committed copy"
    return 0
  fi
  mkdir -p "$DEST"
  # Keep the hand-written tier README (it is not part of the source archive).
  rsync -a --delete --exclude='.git' --exclude='README.md' "$src/archive/" "$DEST/"
  log_info "Synced $(find "$DEST" -name '*.md' | wc -l) Markdown files into $DEST"
}

# ── Main ────────────────────────────────────────────────────────────
main() {
  log_section "Kiro Assistant — archive sync"
  sync_archive
  log_success "$(basename "$0") done"
}

main "$@"
