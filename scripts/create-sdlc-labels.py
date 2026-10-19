#!/usr/bin/env python3
"""Create or update SDLC labels from .github/sdlc-labels.json.

Uses the GitHub CLI (`gh`) and the caller's existing auth. Does not read or
write tokens itself. `--dry-run` validates the file and prints the labels
without calling GitHub.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

REQUIRED = [
    "sdlc",
    *[f"sdlc:stage/{n}" for n in range(8)],
    "sdlc:tier/T0",
    "sdlc:tier/T1",
    "sdlc:tier/T2",
    "sdlc:blocked",
    "sdlc:awaiting-joseph",
    "sdlc:owner/chief-of-staff",
    "sdlc:owner/product",
    "sdlc:owner/architect",
    "sdlc:owner/developer",
    "sdlc:owner/reviewer",
    "sdlc:owner/ops",
    "sdlc:owner/scribe",
]

REPO_ROOT = Path(__file__).resolve().parents[1]
LABELS_PATH = REPO_ROOT / ".github" / "sdlc-labels.json"


def load_labels() -> list[dict[str, str]]:
    raw = json.loads(LABELS_PATH.read_text())
    if not isinstance(raw, list):
        raise SystemExit(f"{LABELS_PATH} must be a JSON array")
    names: list[str] = []
    for index, entry in enumerate(raw):
        if not isinstance(entry, dict):
            raise SystemExit(f"label {index} is not an object")
        for key in ("name", "color", "description"):
            value = entry.get(key)
            if not isinstance(value, str) or not value.strip():
                raise SystemExit(f"label {index} needs a non-empty string {key}")
        name = entry["name"]
        color = entry["color"]
        description = entry["description"]
        if len(name) > 50:
            raise SystemExit(f"{name!r} is longer than GitHub's 50-character limit")
        if len(description) > 100:
            raise SystemExit(f"{name!r} description is longer than 100 characters")
        if len(color) != 6 or any(ch not in "0123456789abcdefABCDEF" for ch in color):
            raise SystemExit(f"{name!r} color must be 6 hex digits, no leading #")
        names.append(name)
    missing = [name for name in REQUIRED if name not in names]
    if missing:
        raise SystemExit("missing required labels: " + ", ".join(missing))
    if len(names) != len(set(names)):
        raise SystemExit("duplicate label names in the definition file")
    return raw


def create_label(entry: dict[str, str]) -> None:
    command = [
        "gh",
        "label",
        "create",
        entry["name"],
        "--color",
        entry["color"],
        "--description",
        entry["description"],
        "--force",
    ]
    completed = subprocess.run(command, check=False, text=True, capture_output=True)
    if completed.returncode != 0:
        sys.stderr.write(completed.stderr)
        raise SystemExit(f"gh label create failed for {entry['name']}")
    print(entry["name"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="validate and print labels; do not call GitHub",
    )
    args = parser.parse_args()
    labels = load_labels()
    if args.dry_run:
        for entry in labels:
            print(f"{entry['name']}\t{entry['color']}\t{entry['description']}")
        return
    if shutil.which("gh") is None:
        raise SystemExit("gh is not on PATH. Install the GitHub CLI and authenticate, or pass --dry-run.")
    for entry in labels:
        create_label(entry)


if __name__ == "__main__":
    main()
