from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class AppResult:
    ok: bool
    message: str = ""


class App:
    """
    Shared application entry point.

    Strict baseline:
    - No API calls
    - No business logic
    - No Rich layouts
    - No side effects
    """

    def run(self, mode: str, argv: Sequence[str] | None = None) -> AppResult:
        # argv is accepted for future expansion; unused in baseline.
        if mode == "cli":
            print("axis_doc_tool: placeholder (CLI). Baseline wiring OK.")
            return AppResult(ok=True)

        if mode == "tui":
            print("axis_doc_tool: placeholder (TUI). Baseline wiring OK.")
            return AppResult(ok=True)

        print(f"axis_doc_tool: unknown mode={mode!r}")
        return AppResult(ok=False, message=f"Unknown mode: {mode!r}")


def run(mode: str, argv: Sequence[str] | None = None) -> int:
    """Convenience wrapper for console entry points."""
    result = App().run(mode=mode, argv=argv)
    return 0 if result.ok else 1
