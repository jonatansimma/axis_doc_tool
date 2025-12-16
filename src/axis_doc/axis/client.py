from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class AxisDeviceClient:
    """
    Stub client. No network calls in this phase.

    Later this will wrap VAPIX/HTTP calls and return parsed structures.
    """
    ip: str
    username: str | None = None
    password: str | None = None
    https: bool = True
    timeout_s: float = 5.0

    def ping(self) -> bool:
        """
        Placeholder for reachability checks later.
        Must remain side-effect-free and network-free in this phase.
        """
        return True

    def fetch_system_info(self) -> dict[str, Any]:
        """
        Placeholder for VAPIX system info later.
        """
        return {}
