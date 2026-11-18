#!/usr/bin/env bash
# Install one small MCP entrypoint. The dataset and index remain in the checkout.
set -euo pipefail
repository_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
agent_kind=all
destination_dir=
project_install=false
dry_run=false
list_only=false
while (($#)); do
    case "$1" in
        codex|--codex) agent_kind=codex ;;
        claude|claude-code|--claude) agent_kind=claude-code ;;
        opencode|--opencode) agent_kind=opencode ;;
        all|auto|--all) agent_kind=all ;;
        --dest) (($# >= 2)) || exit 2; destination_dir=$2; shift ;;
        --project) project_install=true ;;
        --dry-run) dry_run=true ;;
        --list) list_only=true ;;
        --skill) (($# >= 2)) || exit 2; [[ "$2" == skills-library ]] || { printf 'Use the MCP find/read tools for individual guides. Installable entrypoint: skills-library\n' >&2; exit 2; }; shift ;;
        -h|--help) printf '%s\n' 'Usage: install.sh [all|codex|claude-code|opencode] [--dest DIR] [--project] [--dry-run]' 'Installs one small skills-library entrypoint. Dataset and index stay outside skill folders.' 'Register MCP separately: node scripts/setup-mcp.mjs --all'; exit 0 ;;
        *) printf 'Unknown option: %s\n' "$1" >&2; exit 2 ;;
    esac
    shift
done
if "$list_only"; then printf 'skills-library\tmcp-entrypoint\n'; exit 0; fi
source_dir="$repository_dir/skills-library"
[[ -f "$source_dir/SKILL.md" && -f "$source_dir/scripts/mcp-server.mjs" ]] || { printf 'Missing MCP entrypoint; use a complete checkout.\n' >&2; exit 1; }
destinations=()
if [[ -n "$destination_dir" ]]; then destinations+=("$destination_dir")
else
    prefix=${HOME}
    "$project_install" && prefix=$PWD
    if [[ "$agent_kind" == all || "$agent_kind" == codex ]]; then destinations+=("$prefix/.agents/skills"); fi
    if [[ "$agent_kind" == all || "$agent_kind" == claude-code ]]; then
        if "$project_install"; then destinations+=("$prefix/.claude/skills")
        else destinations+=("${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills"); fi
    fi
    if [[ "$agent_kind" == opencode ]]; then
        if "$project_install"; then destinations+=("$prefix/.opencode/skills")
        else destinations+=("${XDG_CONFIG_HOME:-$HOME/.config}/opencode/skills"); fi
    fi
fi
# Check all conflicts before writing any selected agent's folder.
for destination in "${destinations[@]}"; do
    [[ "$destination" == /* ]] || destination="$PWD/$destination"
    [[ "$destination" != "$repository_dir" && "$destination" != "$repository_dir/"* ]] || { printf 'Destination must not be inside the skill source.\n' >&2; exit 1; }
    target="$destination/skills-library"
    if [[ -e "$target" || -L "$target" ]]; then
        [[ -d "$target" && ! -L "$target" && -f "$target/.library-source" && "$(cat "$target/.library-source")" == "$repository_dir" ]] || { printf 'Existing unrelated skill preserved: %s\n' "$target" >&2; exit 1; }
    fi
done
for destination in "${destinations[@]}"; do
    if "$dry_run"; then printf 'Would install one MCP entrypoint in %s\n' "$destination"; continue; fi
    mkdir -p -- "$destination"
    staging=$(mktemp -d "$destination/.skills-library-install.XXXXXX")
    trap 'rm -rf -- "$staging"' EXIT HUP INT TERM
    cp -R -- "$source_dir/." "$staging/"
    printf '%s\n' "$repository_dir" > "$staging/.library-source"
    target="$destination/skills-library"
    if [[ -d "$target" ]]; then rm -rf -- "$target"; fi
    mv -- "$staging" "$target"
    trap - EXIT HUP INT TERM
    printf 'Installed one MCP entrypoint in %s; dataset remains in %s\n' "$destination" "$repository_dir"
done
