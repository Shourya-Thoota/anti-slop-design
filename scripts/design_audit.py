#!/usr/bin/env python3
"""Source review candidates only. Not an AI detector or browser conformance test."""
import argparse
import bisect
import json
import os
import re
from pathlib import Path

EXTENSIONS = {".html", ".htm", ".css", ".scss", ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte"}
EXCLUDED = {".git", "node_modules", ".next", ".nuxt", ".svelte-kit", "dist", "build",
            "coverage", ".cache", "__pycache__", "vendor"}
MAX_BYTES = 1024 * 1024
MAX_FILES = 10000
RULES = [
    ("placeholder-link", "functional_review", r"""href\s*=\s*["'](?:#|javascript:void\(0\))["']""",
     "Check destination/action; a placeholder must not appear to be working navigation."),
    ("transition-all", "motion_review", r"\btransition(?:-property)?\s*:\s*all\b|\btransition-all\b",
     "Use explicit motion properties and the selected system's motion tokens."),
    ("gradient-default", "style_review", r"\b(?:linear|radial|conic)-gradient\s*\(",
     "Verify product/brand purpose; a gradient is not proof of machine authorship."),
    ("backdrop-blur", "style_review", r"\bbackdrop-filter\s*:|\bbackdrop-blur[-\w]*",
     "Check whether translucency clarifies layers and remains legible/performance-safe."),
    ("oversized-z-index", "engineering_review", r"\bz-index\s*:\s*(?:[1-9]\d{3,})\b|\bz-\[(?:[1-9]\d{3,})\]",
     "Replace arbitrary stacking escalation with the project's named layering model."),
    ("infinite-animation", "motion_review", r"\banimation[^;{}\n]*\binfinite\b|\brepeat\s*:\s*-1\b",
     "Check distraction, controls, purpose, and reduced-motion behavior."),
    ("focus-removal", "accessibility_review", r"\boutline\s*:\s*(?:none|0(?:px)?)\b|\boutline-none\b",
     "Verify an equally visible keyboard-focus alternative on rendered controls."),
    ("global-overflow-mask", "responsive_review",
     r"(?:html|body|\*)\s*\{[^}]{0,500}overflow(?:-x)?\s*:\s*(?:hidden|clip)",
     "Check for concealed content; scope intentional artwork clipping instead."),
    ("hover-scale", "style_review", r"hover:scale[-\[]|:hover\s*\{[^}]{0,400}\bscale\s*\(",
     "Verify selective semantic feedback rather than universal scale/lift effects."),
    ("tracking-eyebrow", "style_review", r"\btracking-(?:wide|wider|widest)\b|\bletter-spacing\s*:\s*0\.[2-9]\d*em",
     "Inspect repeated over-tracked labels; preserve genuinely useful typography."),
    ("disabled-zoom", "accessibility_review", r"user-scalable\s*=\s*(?:no|0)|maximum-scale\s*=\s*1(?:[,\s\"']|$)",
     "Check viewport settings; do not prevent required zoom."),
    ("hidden-proof-placeholder", "content_review",
     r"trusted by\s+(?:10[,.]?000|50[,.]?000|1[,.]?000)|(?:99\.9%|10x faster|100% secure)",
     "Verify the claim and context; sample numbers and absolutes are not evidence."),
    ("hype-copy", "content_review", r"\b(?:revolutionize|unlock your potential|seamless experience|game-changing)\b",
     "Check whether specific product information can replace unsupported generic claims."),
    ("fake-urgency-candidate", "trust_review", r"\b(?:only \d+ left|offer ends in|limited time offer)\b",
     "Verify real availability/deadline; this text alone cannot establish deception."),
]


def contrast_ratio(foreground, background):
    def luminance(value):
        if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
            raise ValueError("Contrast inputs must be opaque six-digit hex colors, e.g. #112233.")
        channels = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        linear = [v / 12.92 if v <= .04045 else ((v + .055) / 1.055) ** 2.4 for v in channels]
        return sum(a * b for a, b in zip(linear, (.2126, .7152, .0722)))
    values = sorted((luminance(foreground), luminance(background)))
    return (values[1] + .05) / (values[0] + .05)


def inspect_source(text, name):
    findings = []
    newlines = [m.start() for m in re.finditer("\n", text)]
    for rule_id, category, pattern, message in RULES:
        for match in re.finditer(pattern, text, re.I | re.S):
            findings.append({
                "rule_id": rule_id, "category": category, "status": "needs_review",
                "path": name, "line": bisect.bisect_right(newlines, match.start()) + 1,
                "evidence": match.group(0).replace("\n", " ")[:160], "message": message,
            })
    # This deliberately does not infer JSX expressions, computed labels, or CSS rendering.
    if Path(name).suffix.lower() in {".html", ".htm", ".jsx", ".tsx", ".vue", ".svelte"}:
        for match in re.finditer(r"<img\b[^>]*>", text, re.I):
            if not re.search(r"\balt\s*=", match.group(0), re.I):
                findings.append({
                    "rule_id": "image-alt-source-review", "category": "accessibility_review",
                    "status": "needs_review", "path": name,
                    "line": bisect.bisect_right(newlines, match.start()) + 1,
                    "evidence": match.group(0)[:160],
                    "message": "Check appropriate alternatives; dynamic props and decorative semantics need runtime review.",
                })
    return findings


def audit(root):
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError("Project root must be an existing directory.")
    findings, skipped, scanned = [], [], 0
    def on_error(error):
        skipped.append({"path": str(error.filename), "reason": type(error).__name__})

    stopped = False
    for directory, directories, filenames in os.walk(root, followlinks=False, onerror=on_error):
        directories[:] = sorted(d for d in directories
                                if d not in EXCLUDED and not d.startswith(".")
                                and not (Path(directory) / d).is_symlink())
        for filename in sorted(filenames):
            path = Path(directory) / filename
            relative = path.relative_to(root)
            if path.suffix.lower() not in EXTENSIONS or filename.startswith("."):
                continue
            if scanned >= MAX_FILES:
                skipped.append({"path": str(relative), "reason": "scan_limit"})
                stopped = True
                break
            if path.is_symlink() or not path.resolve().is_relative_to(root):
                skipped.append({"path": str(relative), "reason": "symlink_or_outside_root"})
                continue
            try:
                if path.stat().st_size > MAX_BYTES:
                    skipped.append({"path": str(relative), "reason": "over_1_MiB"})
                    continue
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                skipped.append({"path": str(relative), "reason": type(exc).__name__})
                continue
            scanned += 1
            findings.extend(inspect_source(text, str(relative)))
        if stopped:
            break
    return {
        "kind": "static_design_review", "root": str(root), "files_scanned": scanned,
        "findings_count": len(findings), "findings": findings, "skipped": skipped,
        "limitations": [
            "No AI-authorship probability is calculated.",
            "Source matches require contextual review and can be false positives.",
            "Rendered contrast, layout, keyboard, screen-reader, behavior, backend, and field performance were not tested.",
            "No findings does not mean the quality gate passed.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_root", nargs="?")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--contrast", nargs=2, metavar=("FOREGROUND", "BACKGROUND"))
    args = parser.parse_args()
    try:
        if args.contrast:
            ratio = contrast_ratio(*args.contrast)
            result = {"ratio": round(ratio, 3), "normal_text_4_5": ratio >= 4.5,
                      "large_text_3": ratio >= 3,
                      "scope": "Opaque color pair only; not rendered accessibility conformance."}
        elif args.project_root:
            result = audit(args.project_root)
        else:
            parser.error("Provide a project root or --contrast colors.")
    except ValueError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(result, indent=2))
    elif "ratio" in result:
        print(json.dumps(result, indent=2))
    else:
        print(f"Source files: {result['files_scanned']}; review candidates: {result['findings_count']}")
        for finding in result["findings"]:
            print(f"{finding['path']}:{finding['line']} [{finding['rule_id']}] {finding['message']}")
        print("\n".join(result["limitations"]))


if __name__ == "__main__":
    main()
