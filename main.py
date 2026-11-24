"""news-image-20261124 entry: copy the rendered front page to the output dir.

The image (entry.png, 1024x1024) sums up the world news of Tuesday
24 November 2026 in one front page: masthead, stat strip, world map,
6 lead stories and 30 more in the grid — 36 stories across 9 regions.
Standard library only; no network, no environment execution.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    # Empty-file guard: never leave a zero-byte (or truncated) image behind.
    got = os.path.getsize(dest)
    want = os.path.getsize(SOURCE)
    if got == 0 or got != want:
        raise SystemExit(
            "entry.png copy failed: wrote %d bytes, expected %d" % (got, want)
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
