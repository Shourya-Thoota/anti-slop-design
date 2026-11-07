#!/usr/bin/env python3
"""Read and materialize the internal design resource database."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

LIBRARY = Path(__file__).resolve().parents[1] / "assets" / "design-library.json"


def safe_path(value):
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError(f"Unsafe resource path: {value!r}")
    return path


def load_library(path=LIBRARY):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if data.get("schema_version") != 1:
        raise ValueError("Unsupported library schema")
    for module, entries in data["modules"].items():
        if len(safe_path(module).parts) != 1:
            raise ValueError("Module name must be one component")
        for name, entry in entries.items():
            safe_path(name)
            digest = hashlib.sha256(entry["text"].encode("utf-8")).hexdigest()
            if digest != entry["sha256"]:
                raise ValueError(f"Checksum mismatch: {module}/{name}")
    return data


def materialize(data, module, output):
    output = Path(output).resolve()
    target = output / module
    if target.is_symlink():
        raise ValueError("Refusing symlink module root")
    entries = data["modules"][module]
    planned = []
    for name, entry in entries.items():
        safe_path(name)
        dest = target / name
        if dest.is_symlink() or any(p.is_symlink() for p in dest.parents if p != output):
            raise ValueError(f"Refusing symlink destination: {dest}")
        if not dest.resolve().is_relative_to(target.resolve()):
            raise ValueError("Destination escapes module")
        raw = entry["text"].encode("utf-8")
        if dest.exists() and (not dest.is_file() or dest.read_bytes() != raw):
            raise ValueError(f"Existing file differs; use a fresh output folder: {dest}")
        planned.append((dest, raw))
    for dest, raw in planned:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            with dest.open("xb") as handle:
                handle.write(raw)
    return target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["list", "read", "materialize", "verify"])
    parser.add_argument("module", nargs="?")
    parser.add_argument("path", nargs="?")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    try:
        data = load_library()
        if args.action == "verify":
            print(json.dumps({m: len(v) for m, v in data["modules"].items()}, indent=2))
            return
        if args.module not in data["modules"]:
            parser.error("Choose module: " + ", ".join(data["modules"]))
        entries = data["modules"][args.module]
        if args.action == "list":
            print("\n".join(entries))
        elif args.action == "read":
            if args.path not in entries:
                parser.error("Unknown resource path; use list first")
            print(entries[args.path]["text"], end="")
        else:
            if args.output_dir is None:
                parser.error("--output-dir is required")
            print(materialize(data, args.module, args.output_dir))
    except (ValueError, OSError, KeyError) as exc:
        sys.exit(str(exc))


if __name__ == "__main__":
    main()
