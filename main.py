#!/usr/bin/env python3
"""Hand in the front page for 'The World Today', 22 November 2026.

The picture itself (entry.png) was drawn when this entry was built and
ships in this repository. This program only carries it to the output
directory, checking on the way that it is a whole PNG of the right size:
at most 1 MiB and at most 1024 by 1024 pixels. Standard library only,
so it runs in the grader's sandbox with no network and nothing installed.
"""

import hashlib
import os
import struct
import sys

MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    sys.stderr.write("entry: " + message + "\n")
    raise SystemExit(1)


def read_picture(path):
    try:
        with open(path, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (path, exc))
    if len(data) > MAX_BYTES:
        fail("entry.png is %d bytes, over the 1 MiB cap" % len(data))
    if data[:8] != PNG_MAGIC:
        fail("entry.png does not start with the PNG signature")
    if len(data) < 33:
        fail("entry.png is too short to hold an IHDR chunk")
    chunk_len = struct.unpack(">I", data[8:12])[0]
    chunk_type = data[12:16]
    if chunk_type != b"IHDR" or chunk_len != 13:
        fail("entry.png has no 13-byte IHDR chunk first")
    width, height = struct.unpack(">II", data[16:24])
    if width > MAX_SIDE or height > MAX_SIDE:
        fail("entry.png is %dx%d, over the 1024x1024 cap" % (width, height))
    if width == 0 or height == 0:
        fail("entry.png has a zero side")
    if data[-12:] != struct.pack(">I", 0) + b"IEND" + b"\xaeB`\x82":
        fail("entry.png does not end with the IEND chunk")
    return data, width, height


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(out_dir, "entry.png")

    data, width, height = read_picture(source)
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(target, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        fail("cannot write %s: %s" % (target, exc))

    with open(target, "rb") as handle:
        written = handle.read()
    if hashlib.sha256(written).hexdigest() != hashlib.sha256(data).hexdigest():
        fail("the copy in %s differs from entry.png" % out_dir)
    print("entry.png: %dx%d, %d bytes -> %s" % (width, height, len(data), target))


if __name__ == "__main__":
    main()
