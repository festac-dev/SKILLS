#!/bin/sh
# Install from a checkout, or download one when this script is piped to sh.
set -eu

if [ "${1:-}" = "--help" ] || [ "${1:-}" = "-h" ]; then
    cat <<'EOF'
Usage: install.sh [auto|codex|claude-code|opencode|all] [options]

Installs the main toolkit for detected agents by default.
  --skill NAME   Install a named skill (repeat to select several)
  --all          Install every registered skill
  --project      Install in the current project instead of your user profile
  --dest PATH    Use a custom skill directory
  --dry-run      Show the links without changing files

Requires Python 3.10+. Downloading a checkout also requires Git.
EOF
    exit 0
fi

command -v python3 >/dev/null 2>&1 || {
    echo 'Python 3.10+ is required. Install Python and run this command again.' >&2
    exit 1
}
python3 -c 'import sys; raise SystemExit(sys.version_info < (3, 10))' || {
    echo 'Python 3.10+ is required. Update Python and run this command again.' >&2
    exit 1
}

skills_source=${SKILLS_SOURCE:-}
if [ -z "$skills_source" ] && [ -f "$0" ]; then
    skills_script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
    if [ -f "$skills_script_dir/scripts/install.py" ]; then
        skills_source=$skills_script_dir
    fi
fi
if [ -z "$skills_source" ] && [ -f ./scripts/install.py ] && [ -f ./SKILL.md ]; then
    skills_source=$(pwd)
fi
if [ -z "$skills_source" ]; then
    skills_source=${XDG_DATA_HOME:-"$HOME/.local/share"}/SKILLS
    if [ ! -e "$skills_source" ]; then
        command -v git >/dev/null 2>&1 || {
            echo 'Git is required to download SKILLS.' >&2
            exit 1
        }
        mkdir -p -- "$(dirname -- "$skills_source")"
        skills_staging=$(mktemp -d "${skills_source}.download.XXXXXX")
        trap 'rm -rf -- "$skills_staging"' EXIT HUP INT TERM
        git clone --depth 1 --single-branch --branch "${SKILLS_REF:-main}" \
            "${SKILLS_REPO:-https://github.com/festac-dev/SKILLS.git}" "$skills_staging"
        mv -- "$skills_staging" "$skills_source"
        trap - EXIT HUP INT TERM
    fi
fi

if [ ! -f "$skills_source/scripts/install.py" ] || [ ! -f "$skills_source/SKILL.md" ]; then
    echo "Not a SKILLS checkout: $skills_source" >&2
    exit 1
fi

exec python3 "$skills_source/scripts/install.py" "$@"
