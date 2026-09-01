#!/usr/bin/env python3
"""Generate the static source-level declaration index used by Lean badges."""

from __future__ import annotations

import json
from pathlib import Path


INSTANCE = Path(__file__).resolve().parents[1]
DECLMAP = INSTANCE / "crosswalk" / "lean-decl-map.json"
MANIFEST = INSTANCE.parent / "DFP_counterexample" / "sentence-locks.json"
OUTPUT = INSTANCE / "web-assets" / "site" / "formalizations" / "DFPWolfe" / "declarations.json"
REPOSITORY = "https://github.com/imathwy/DFP_wolfe_local"


def main() -> None:
    declmap = json.loads(DECLMAP.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    declarations: dict[str, dict[str, object]] = {}
    for paper_label, records in declmap.items():
        for record in records:
            name = record["decl"]
            entry = declarations.setdefault(
                name,
                {
                    "file": record["file"],
                    "line": record["line"],
                    "cited": record.get("cited", ""),
                    "paper_labels": [],
                },
            )
            labels = entry["paper_labels"]
            if paper_label not in labels:
                labels.append(paper_label)
    payload = {
        "schema_version": 1,
        "repository": REPOSITORY,
        "snapshot": manifest["source"]["snapshot_commit"],
        "declarations": declarations,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {OUTPUT} ({len(declarations)} declarations)")


if __name__ == "__main__":
    main()
