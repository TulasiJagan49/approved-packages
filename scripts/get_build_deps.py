#!/usr/bin/env python3
"""
Print the [build-system].requires entries from a source dist tarball.
Usage: python3 get_build_deps.py <path-to-tarball>
"""
import sys
import tarfile
import tomllib

try:
    with tarfile.open(sys.argv[1]) as t:
        for member in t.getmembers():
            if member.name.endswith("/pyproject.toml") or member.name == "pyproject.toml":
                f = t.extractfile(member)
                if f:
                    d = tomllib.load(f)
                    for r in d.get("build-system", {}).get("requires", []):
                        print(r)
                break
except Exception:
    pass
