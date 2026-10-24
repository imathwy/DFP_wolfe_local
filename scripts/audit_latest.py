#!/usr/bin/env python3
"""Check the paper entry and audit actual declarations, failing closed.

Run from any directory. Logs and the temporary Lean probe stay in .work/.
This is a source/axiom audit, not a verifier of correspondence with prose.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"propext", "Classical.choice", "Quot.sound"}


def code_only(source):
    """Mask nested Lean comments and strings while preserving line positions."""
    out, i, depth, string = [], 0, 0, False
    while i < len(source):
        if depth:
            if source.startswith("/-", i):
                depth += 1
                out.append("  ")
                i += 2
            elif source.startswith("-/", i):
                depth -= 1
                out.append("  ")
                i += 2
            else:
                out.append("\n" if source[i] == "\n" else " ")
                i += 1
        elif string:
            if source[i] == "\\":
                out.append("  ")
                i += 2
            else:
                string = source[i] != '"'
                out.append("\n" if source[i] == "\n" else " ")
                i += 1
        elif source.startswith("/-", i):
            depth = 1
            out.append("  ")
            i += 2
        elif source.startswith("--", i):
            end = source.find("\n", i)
            end = len(source) if end < 0 else end
            out.append(" " * (end - i))
            i = end
        elif source[i] == '"':
            string = True
            out.append(" ")
            i += 1
        else:
            out.append(source[i])
            i += 1
    if depth or string:
        raise ValueError("Unterminated Lean comment or string")
    return "".join(out)


def source_scan():
    files = sorted((ROOT / "ReasLib").rglob("*.lean"))
    files += sorted((ROOT / "DFPWolfe").rglob("*.lean"))
    files += [ROOT / "DFPWolfe.lean", ROOT / "ReasLib.lean"]
    hashes, issues = {}, []
    for path in files:
        data = path.read_bytes()
        relative = path.relative_to(ROOT).as_posix()
        hashes[relative] = hashlib.sha256(data).hexdigest()
        code = code_only(data.decode("utf-8"))
        pattern = r"\b(?:sorry|admit|sorryAx|axiom)\b"
        if relative.startswith("ReasLib/"):
            pattern += r"|#(?:print|check|eval|reduce)\b"
        for match in re.finditer(pattern, code):
            issues.append(f"{relative}:{code.count(chr(10), 0, match.start()) + 1}: "
                          f"{match.group()}")
    if issues:
        raise ValueError("Forbidden source tokens:\n" + "\n".join(issues))
    return hashes


def parse_axioms(log, expected):
    # Lean may wrap long lists across lines. Accept only its two known forms.
    pattern = re.compile(
        r"^'([^'\n]+)' (?:depends on axioms:\s*\[([^\]]*)\]|does not depend on any axioms)",
        re.MULTILINE,
    )
    found = {}
    for match in pattern.finditer(log):
        name = match[1]
        if name in found:
            raise ValueError(f"Duplicate audit result: {name}")
        axioms = [x.strip() for x in (match[2] or "").split(",") if x.strip()]
        if set(axioms) - ALLOWED:
            raise ValueError(f"Unapproved axioms for {name}: {axioms}")
        found[name] = axioms
    if set(found) != set(expected):
        raise ValueError(f"Audit declaration mismatch: missing={set(expected) - set(found)}, "
                         f"unexpected={set(found) - set(expected)}")
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lake", default="lake", help="Lake executable or project wrapper")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "scripts/latest_audit.json").read_text())
    declarations = manifest["declarations"]
    if not declarations or len(declarations) != len(set(declarations)):
        raise ValueError("Empty or duplicated declaration manifest")
    if any(not re.fullmatch(r"[A-Za-z_][A-Za-z_0-9.]*", n) for n in declarations):
        raise ValueError("Invalid declaration name")
    navigation = set()
    for path in (ROOT / "DFPWolfe/Latest").glob("*.lean"):
        navigation.update(re.findall(r"^#check ([A-Za-z_][A-Za-z_0-9.]*)",
                                     code_only(path.read_text()), re.MULTILINE))
    if navigation - set(declarations):
        raise ValueError(f"Navigation declarations missing from audit: {navigation - set(declarations)}")
    hashes = source_scan()
    scratch = ROOT / ".work"
    scratch.mkdir(exist_ok=True)
    run = Path(tempfile.mkdtemp(prefix="latest-audit-", dir=scratch))
    env = os.environ.copy()
    for key in ("TMPDIR", "TMP", "TEMP"):
        env[key] = str(run)
    cache = scratch / "cache"
    cache.mkdir(exist_ok=True)
    env.setdefault("XDG_CACHE_HOME", str(cache))
    probe = run / "Audit.lean"
    result = {"status": "failed", "source_sha256": hashes, "checks": []}
    print(f"Audit logs: {run}", flush=True)
    try:
        probe.write_text("import DFPWolfe.Latest.Paper\n\n" + "\n".join(
            f"#print axioms {name}" for name in declarations) + "\n")
        for target in ["DFPWolfe.lean", str(probe.relative_to(ROOT))]:
            log_path = run / ("axioms.log" if target.endswith("Audit.lean") else "root.log")
            command = [args.lake, "lean", target]
            # The project's remote-only checker accepts a target, not Lake options.
            if env.get("M2F_AGENT_REMOTE_LEAN_ONLY") == "1":
                command = ["m2f-agent-lean-check", target]
            with log_path.open("w") as log:
                completed = subprocess.run(command, cwd=ROOT, env=env, stdout=log,
                                           stderr=subprocess.STDOUT, check=False)
            result["checks"].append({"target": target, "exit_code": completed.returncode})
            if completed.returncode:
                raise RuntimeError(f"Lean failed; see {log_path}")
        result["axioms"] = parse_axioms((run / "axioms.log").read_text(), declarations)
        if source_scan() != hashes:
            raise RuntimeError("Lean sources changed during the audit")
        result["status"] = "passed"
        print(f"Passed: {len(hashes)} source files, {len(declarations)} declarations", flush=True)
    finally:
        probe.unlink(missing_ok=True)
        (run / "result.json").write_text(json.dumps(result, indent=2) + "\n")


if __name__ == "__main__":
    main()
