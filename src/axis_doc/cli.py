from __future__ import annotations

import argparse
from typing import Sequence

from .app import run as app_run


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="axis-doc",
        description="axis_doc_tool (read-only) — documentation underlay generator for Axis cameras.",
    )
    # Baseline only: accept no functional args yet, but keep a slot for later.
    parser.add_argument(
        "--version",
        action="store_true",
        help="Print version placeholder and exit.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        # Keep this simple in baseline; version wiring can be added later.
        print("axis_doc_tool version placeholder (0.1.0)")
        return 0

    # Placeholder run routed through shared app
    return app_run(mode="cli", argv=argv)
