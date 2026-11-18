#!/usr/bin/env bash
# Install every native skill from this complete checkout. No Python or npm.
set -euo pipefail

repository_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd -P)
destination_dir="${CODEX_HOME:-${HOME}/.codex}/skills"
list_only=false
agent_kind=codex
custom_destination=false
dry_run=false
project_install=false
selected_names=()

wants_skill() {
    ((${#selected_names[@]} == 0)) && return 0
    for requested_name in "${selected_names[@]}"; do
        [[ "$requested_name" == "$1" ]] && return 0
    done
    return 1
}

usage() {
    cat <<'HELP'
Usage: bash install.sh [--codex|--claude|--opencode] [--dest DIRECTORY] [--list]

Installs ALL skills, including references, scripts, assets and source notices.
Codex uses its native complete-skills bundle. Other agents receive native
skill directories linked to the complete checkout.

  --codex       Install the complete native Codex bundle (default)
  --claude      Install in ~/.claude/skills
  --opencode    Install in ~/.config/opencode/skills
  --dest DIR    Use another agent's native skills directory
  --list        Print every skill name and its collection without installing

Existing unrelated skills are preserved. A conflicting destination stops the
installation before any skill is changed. Re-running the same install is safe.
HELP
}

while (($#)); do
    case "$1" in
        --codex) agent_kind=codex; destination_dir="${CODEX_HOME:-${HOME}/.codex}/skills" ;;
        codex) agent_kind=codex; destination_dir="${CODEX_HOME:-${HOME}/.codex}/skills" ;;
        --claude) agent_kind=claude; destination_dir="${HOME}/.claude/skills" ;;
        claude|claude-code) agent_kind=claude; destination_dir="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}/skills" ;;
        --opencode) agent_kind=opencode; destination_dir="${XDG_CONFIG_HOME:-${HOME}/.config}/opencode/skills" ;;
        opencode) agent_kind=opencode; destination_dir="${XDG_CONFIG_HOME:-${HOME}/.config}/opencode/skills" ;;
        auto)
            if command -v codex >/dev/null; then agent_kind=codex
            elif command -v claude >/dev/null; then agent_kind=claude; destination_dir="${CLAUDE_CONFIG_DIR:-${HOME}/.claude}/skills"
            elif command -v opencode >/dev/null; then agent_kind=opencode; destination_dir="${XDG_CONFIG_HOME:-${HOME}/.config}/opencode/skills"
            else printf 'Choose codex, claude-code or opencode.\n' >&2; exit 1; fi
            ;;
        all) agent_kind=all ;;
        --dest)
            (($# >= 2)) || { printf 'Missing directory after --dest\n' >&2; exit 2; }
            destination_dir=$2
            custom_destination=true
            shift
            ;;
        --list) list_only=true ;;
        --all) selected_names=() ;;
        --project) project_install=true ;;
        --dry-run) dry_run=true ;;
        --skill)
            (($# >= 2)) || { printf 'Missing name after --skill\n' >&2; exit 2; }
            selected_names+=("$2"); shift
            ;;
        -h|--help) usage; exit 0 ;;
        *) printf 'Unknown option: %s\n' "$1" >&2; usage >&2; exit 2 ;;
    esac
    shift
done

if [[ "$agent_kind" == all ]]; then
    extra_options=()
    "$dry_run" && extra_options+=(--dry-run)
    "$project_install" && extra_options+=(--project)
    "$custom_destination" && extra_options+=(--dest "$destination_dir")
    "$list_only" && extra_options+=(--list)
    for skill_name in "${selected_names[@]}"; do extra_options+=(--skill "$skill_name"); done
    detected=0
    for agent in codex claude opencode; do
        if command -v "$agent" >/dev/null; then
            bash "${BASH_SOURCE[0]}" "--$agent" "${extra_options[@]}"
            detected=$((detected + 1))
        fi
    done
    ((detected > 0)) || { printf 'No supported agent was detected.\n' >&2; exit 1; }
    exit 0
fi

if "$project_install"; then
    custom_destination=true
    case "$agent_kind" in
        codex) destination_dir="$PWD/.agents/skills" ;;
        claude) destination_dir="$PWD/.claude/skills" ;;
        opencode) destination_dir="$PWD/.opencode/skills" ;;
    esac
fi

manifest_path="$repository_dir/native-skills.tsv"
[[ -f "$manifest_path" ]] || { printf 'Missing native-skills.tsv; use a complete Git clone.\n' >&2; exit 1; }

if "$list_only"; then
    while IFS=$'\t' read -r skill_name skill_path collection; do
        [[ -z "$skill_name" || "$skill_name" == \#* ]] && continue
        printf '%s\t%s\n' "$skill_name" "$collection"
    done < "$manifest_path"
    exit 0
fi

if [[ "$agent_kind" == codex && "$custom_destination" == false && ${#selected_names[@]} == 0 ]]; then
    if "$dry_run"; then
        printf 'Would install the complete native Codex bundle from %s\n' "$repository_dir"
        exit 0
    fi
    command -v codex >/dev/null || { printf 'Install Codex CLI first, then rerun this command.\n' >&2; exit 1; }
    [[ -f "$repository_dir/.codex-plugin/plugin.json" && -f "$repository_dir/.agents/plugins/marketplace.json" ]] || {
        printf 'Missing native bundle metadata; use a complete Git clone.\n' >&2; exit 1;
    }
    codex plugin marketplace add "$repository_dir" --json
    bundle_version=$(sed -nE 's/^[[:space:]]*"version": "([^"]+)"[,]?$/\1/p' "$repository_dir/.codex-plugin/plugin.json")
    installed_bundle="${CODEX_HOME:-${HOME}/.codex}/plugins/cache/festac-skills/complete-skills/$bundle_version"
    if [[ "$repository_dir" != "$installed_bundle" ]]; then
        codex plugin add complete-skills@festac-skills --json
    fi
    printf 'Installed the complete native Codex bundle, with all skills and supporting files.\n'
    printf 'Open a fresh Codex session. Skill names use the complete-skills: prefix.\n'
    exit 0
fi

[[ "$destination_dir" == /* ]] || destination_dir="$PWD/$destination_dir"
[[ "$destination_dir" != "$repository_dir" && "$destination_dir" != "$repository_dir/"* ]] || {
    printf 'Destination must not be inside the skill source.\n' >&2; exit 1;
}

# Preflight the complete manifest, including collisions, before creating links.
count=0
while IFS=$'\t' read -r skill_name skill_path collection; do
    [[ -z "$skill_name" || "$skill_name" == \#* ]] && continue
    wants_skill "$skill_name" || continue
    [[ "$skill_name" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ && ${#skill_name} -le 64 ]] || {
        printf 'Invalid skill name: %s\n' "$skill_name" >&2; exit 1;
    }
    [[ "$skill_path" != /* && "/$skill_path/" != */../* ]] || {
        printf 'Invalid skill path: %s\n' "$skill_path" >&2; exit 1;
    }
    source_file="$repository_dir/$skill_path"
    [[ -f "$source_file" ]] || { printf 'Incomplete checkout: %s\n' "$skill_path" >&2; exit 1; }
    grep -m 1 -Eq "^name: [\"']?${skill_name}[\"']?$" "$source_file" || {
        printf 'Skill header does not match the manifest: %s\n' "$skill_path" >&2; exit 1;
    }
    target_path="$destination_dir/$skill_name"
    if [[ "$skill_path" == SKILL.md ]]; then
        if [[ -e "$target_path" || -L "$target_path" ]]; then
            [[ -d "$target_path" && -f "$target_path/.skills-repository" ]] || {
                printf 'Existing unrelated skill preserved: %s\n' "$target_path" >&2; exit 1;
            }
            [[ "$(cat "$target_path/.skills-repository")" == "$repository_dir" ]] || {
                printf 'Skill is managed by another checkout: %s\n' "$target_path" >&2; exit 1;
            }
        fi
    else
        source_dir=$(cd -- "$(dirname -- "$source_file")" && pwd -P)
        if [[ -e "$target_path" || -L "$target_path" ]]; then
            [[ -L "$target_path" && "$(readlink -- "$target_path")" == "$source_dir" ]] || {
                printf 'Existing unrelated skill preserved: %s\n' "$target_path" >&2; exit 1;
            }
        fi
    fi
    count=$((count + 1))
done < "$manifest_path"
((count > 0)) || { printf 'The native manifest is empty.\n' >&2; exit 1; }
for requested_name in "${selected_names[@]}"; do
    grep -qF "${requested_name}"$'\t' "$manifest_path" || {
        printf 'Unknown skill: %s\n' "$requested_name" >&2; exit 1;
    }
done
if "$dry_run"; then
    printf 'Would install %s native skills in %s\n' "$count" "$destination_dir"
    exit 0
fi
mkdir -p -- "$destination_dir"
destination_dir=$(cd -- "$destination_dir" && pwd -P)

# The core skill exposes its complete resources without recursively exposing
# every imported collection a second time through the root skill directory.
installed=0
if wants_skill professional-product-creation; then
core_dir="$destination_dir/professional-product-creation"
mkdir -p -- "$core_dir"
printf '%s\n' "$repository_dir" > "$core_dir/.skills-repository"
for resource in SKILL.md README.md LICENSE NOTICE.md CATALOG.md COLLECTION_RULES.md \
    orchestrator specialists references templates quality-gates playbooks \
    scripts tests reports evals examples motion-studio; do
    [[ -e "$repository_dir/$resource" ]] || continue
    target="$core_dir/$resource"
    if [[ -L "$target" && "$(readlink -- "$target")" == "$repository_dir/$resource" ]]; then
        continue
    fi
    [[ ! -e "$target" && ! -L "$target" ]] || {
        printf 'Existing core resource preserved: %s\n' "$target" >&2; exit 1;
    }
    ln -s -- "$repository_dir/$resource" "$target"
done
installed=1
fi

while IFS=$'\t' read -r skill_name skill_path collection; do
    [[ -z "$skill_name" || "$skill_name" == \#* || "$skill_path" == SKILL.md ]] && continue
    wants_skill "$skill_name" || continue
    source_dir=$(cd -- "$(dirname -- "$repository_dir/$skill_path")" && pwd -P)
    target_path="$destination_dir/$skill_name"
    [[ -L "$target_path" ]] || ln -s -- "$source_dir" "$target_path"
    installed=$((installed + 1))
    if ((installed % 1000 == 0)); then
        printf 'Installed %s/%s skills\n' "$installed" "$count"
    fi
done < "$manifest_path"
printf 'Installed all %s native skills in %s\n' "$installed" "$destination_dir"
printf 'References, scripts, assets and notices remain available in %s\n' "$repository_dir"
printf 'Open a fresh agent session to load the updated skills.\n'
