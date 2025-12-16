from __future__ import annotations

import argparse
from typing import Sequence

from axis_doc.app import run as app_run


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="axis-doc",
        description="axis_doc_tool (read-only) — documentation underlay generator for Axis cameras.",
    )

    sub = parser.add_subparsers(dest="cmd")

    p_doc = sub.add_parser("doc", help="Generate placeholder Markdown docs from targets (no API calls).")
    p_doc.add_argument(
        "--targets",
        required=True,
        type=str,
        help="Manual IP targets (single IP, ranges, CIDR, mixed list).",
    )

    p_parse = sub.add_parser("parse-targets", help="Parse targets and print a preview (no API calls).")
    p_parse.add_argument("--targets", required=True, type=str, help="Manual IP targets string.")

    parser.add_argument("--version", action="store_true", help="Print version placeholder and exit.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print("axis_doc_tool version placeholder (0.1.0)")
        return 0

    if args.cmd == "parse-targets":
        return app_run(mode="cli", argv=argv, targets_text=args.targets)

    if args.cmd == "doc":
        return app_run(mode="cli-doc", argv=argv, targets_text=args.targets)

    # Default: keep baseline behavior
    return app_run(mode="cli", argv=argv)
