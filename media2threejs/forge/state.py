#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "_shared"))
sys.path.insert(0, str(ROOT))

from workflow_state import (  # noqa: E402
    WorkflowStateError,
    load_state,
    mark_steps,
    new_state,
    save_state,
    status_payload,
)
from shared.project_state import (  # noqa: E402
    ProjectStateError, load_project_state, mark_project_step, new_project_state,
    record_correction, save_project_state, next_payload,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Unified media2threejs project state (with img2threejs compatibility)")
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init")
    init.add_argument("--state", type=Path, default=Path(".img2threejs/state.json"))
    init.add_argument("--reference")
    init.add_argument("--manifest", type=Path)
    init.add_argument("--profile", choices=("generic", "cs2", "character"), default="generic")
    init.add_argument("--spec", default="")
    init.add_argument("--max-per-pass", type=int, default=3)
    init.add_argument("--max-total", type=int, default=None, help="deprecated compatibility option; cumulative corrections are unlimited")

    status = commands.add_parser("status")
    status.add_argument("--state", type=Path, default=Path(".img2threejs/state.json"))
    status.add_argument("--json", action="store_true")

    mark = commands.add_parser("mark")
    mark.add_argument("step", nargs="+")
    mark.add_argument("--state", type=Path, default=Path(".img2threejs/state.json"))
    mark.add_argument("--status", choices=("done", "skipped", "pending"), default="done")
    mark.add_argument("--evidence", action="append", default=[])
    mark.add_argument("--reason", default="")

    correction = commands.add_parser("correct")
    correction.add_argument("--state", type=Path, default=Path(".media2threejs/state.json"))
    correction.add_argument("--stage", required=True)
    correction.add_argument("--action", required=True)

    return parser


def print_status(state: dict, *, as_json: bool = False) -> None:
    payload = status_payload(state)
    if as_json:
        print(json.dumps(payload, ensure_ascii=False))
        return
    loop = payload["loop"]
    total_limit = loop.get("maxTotal") if loop.get("maxTotal") is not None else "unlimited"
    print(
        f"STATE status={payload['status']} step={payload['currentStep']} "
        f"pass={payload['currentPass'] or 'none'} "
        f"loop={loop['passCount']}/{loop['maxPerPass']} total={loop['totalCount']}/{total_limit}"
    )
    if payload["stopReason"]:
        print(f"STOP: {payload['stopReason']}")
    elif payload["nextCommand"]:
        print(f"next command: {payload['nextCommand']}")
    print("pending mandatory steps:")
    for step_id in payload["pending"]:
        print(f"- {step_id}")


def main(argv: list[str]) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "init":
            if args.state.expanduser().exists():
                raise WorkflowStateError(f"refusing to overwrite existing state: {args.state}")
            if args.manifest:
                state = new_project_state(args.manifest, max_per_stage=args.max_per_pass, max_total=args.max_total)
                state["statePath"] = str(args.state)
                save_project_state(args.state, state)
                print(json.dumps(next_payload(state), ensure_ascii=False))
                return 0
            if not args.reference:
                raise ProjectStateError("init requires --manifest or --reference")
            state = new_state(
                args.reference,
                profile=args.profile,
                spec=args.spec,
                max_per_pass=args.max_per_pass,
                max_total=args.max_total,
            )
            save_state(args.state, state)
            print_status(state)
            return 0
        raw = json.loads(args.state.expanduser().read_text(encoding="utf-8"))
        if raw.get("kind") == "media2threejs-project-state":
            state = load_project_state(args.state)
            if args.command == "status":
                print(json.dumps(next_payload(state), ensure_ascii=False) if args.json else f"PROJECT_STATE {next_payload(state)}")
            elif args.command == "mark":
                for step_id in args.step:
                    mark_project_step(state, step_id, args.status, args.evidence, args.reason)
                save_project_state(args.state, state)
                print(json.dumps(next_payload(state), ensure_ascii=False))
            elif args.command == "correct":
                record_correction(state, args.stage, args.action)
                save_project_state(args.state, state)
                print(json.dumps(next_payload(state), ensure_ascii=False))
            return 3 if state.get("status") == "stopped" else 0
        state = load_state(args.state)
        if args.command == "status":
            print_status(state, as_json=args.json)
        elif args.command == "mark":
            mark_steps(state, args.step, status=args.status, evidence=args.evidence, reason=args.reason)
            save_state(args.state, state)
            print_status(state)
        return 3 if state.get("status") == "stopped" else 0
    except (OSError, json.JSONDecodeError, WorkflowStateError, ProjectStateError) as error:
        print(f"state error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
