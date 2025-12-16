from __future__ import annotations

import argparse
from typing import Sequence

from .app import run as app_run


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="axis-doc",
        description="axis_doc_tool (read-only) — documentation underlay generator for Axis cameras.",
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Print version placeholder and exit.",
    )

    parser.add_argument(
        "--targets",
        type=str,
        default=None,
        help=(
            "Manual IP targets (single IP, ranges, CIDR, or mixed list). "
            "Examples: '192.168.1.10', '192.168.1.10-25', "
            "'192.168.1.10-192.168.1.20', '192.168.1.0/28', "
            "'192.168.1.10,192.168.1.20 192.168.1.30-35'."
        ),
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print("axis_doc_tool version placeholder (0.1.0)")
        return 0

    return app_run(mode="cli", argv=argv, targets_text=args.targets)
