#!/usr/bin/env python3
"""Copy the 24 November news image to the output directory.

Reads entry.png from the directory this file lives in and writes it to
$MAKEFUN_OUTPUT_DIR (or /output when unset) as entry.png. The copy is
byte for byte the same on every run. Exits 1 if the copy's size does not
match the source.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        print("error: size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
