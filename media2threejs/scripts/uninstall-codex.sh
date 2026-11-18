#!/usr/bin/env bash
set -euo pipefail
target="${HOME}/.agents/skills/media2threejs"
if [[ ! -L "$target" ]]; then echo "No media2threejs symlink at $target"; exit 0; fi
unlink "$target"; echo "Removed $target"
