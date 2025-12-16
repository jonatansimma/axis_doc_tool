from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .ipparse import parse_targets

from axis_doc.collector import DocumentationCollector
from axis_doc.render import render_multi_camera_md



@dataclass(frozen=True)
class AppResult:
    ok: bool
    message: str = ""
    exit_code: int = 0


class App:
    """
    Shared application entry point.

    Current phase:
    - No API calls
    - No Rich layouts
    - Minimal plumbing only
    """

        def run(
        self,
        mode: str,
        argv: Sequence[str] | None = None,
        *,
        targets_text: str | None = None,
    ) -> AppResult:
        if mode == "cli":
            if targets_text:
                return self._run_cli_parse(targets_text)
            print("axis_doc_tool: placeholder (CLI). Baseline wiring OK.")
            return AppResult(ok=True, exit_code=0)

        if mode == "cli-doc":
            if not targets_text:
                print("No targets provided.")
                return AppResult(ok=False, exit_code=2)

            parsed = parse_targets(targets_text)
            if not parsed.targets:
                print("No valid targets parsed.")
                return AppResult(ok=False, exit_code=2)

            collector = DocumentationCollector()
            docs = collector.collect_for_ips(parsed.targets)
            print(render_multi_camera_md(docs))
            return AppResult(ok=True, exit_code=0)

        if mode == "tui":
            print("axis_doc_tool: placeholder (TUI). Baseline wiring OK.")
            return AppResult(ok=True, exit_code=0)

        print(f"axis_doc_tool: unknown mode={mode!r}")
        return AppResult(ok=False, message=f"Unknown mode: {mode!r}", exit_code=2)

    def _run_cli_parse(self, targets_text: str) -> AppResult:
        parsed = parse_targets(targets_text)

        print(f"Parsed targets: {len(parsed.targets)}")
        if parsed.rejected:
            print(f"Rejected tokens ({len(parsed.rejected)}):")
            for t in parsed.rejected:
                print(f"  - {t}")

        if parsed.targets:
            preview = parsed.targets[:10]
            print("Targets preview:")
            for ip in preview:
                print(f"  - {ip}")
            if len(parsed.targets) > len(preview):
                print(f"  ... (+{len(parsed.targets) - len(preview)} more)")
            return AppResult(ok=True, exit_code=0)

        print("No valid targets parsed.")
        return AppResult(ok=False, message="No valid targets parsed.", exit_code=2)


def run(mode: str, argv: Sequence[str] | None = None, *, targets_text: str | None = None) -> int:
    result = App().run(mode=mode, argv=argv, targets_text=targets_text)
    return result.exit_code
