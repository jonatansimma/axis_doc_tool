from __future__ import annotations

from typing import Sequence

from .app import run as app_run


def main(argv: Sequence[str] | None = None) -> int:
    # Placeholder run routed through shared app
    return app_run(mode="tui", argv=argv)
