from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class CameraIdentity:
    ip: str
    host: str | None = None
    serial: str | None = None
    mac: str | None = None
    model: str | None = None
    firmware: str | None = None


@dataclass(frozen=True)
class TechnicianNotes:
    """
    Minimal technician input (kept small by design).
    Extend only when the frozen plan explicitly requires it.
    """
    site_name: str | None = None
    location_label: str | None = None
    mount_height_m: float | None = None
    notes: str | None = None


@dataclass(frozen=True)
class CameraDocumentation:
    """
    Read-only documentation payload.

    This is a container for:
    - identity & system facts (from Axis APIs later)
    - minimal technician notes
    - raw excerpts/attachments references (later)
    """
    identity: CameraIdentity
    technician: TechnicianNotes = field(default_factory=TechnicianNotes)
    collected_at: datetime = field(default_factory=lambda: datetime.now().astimezone())

    # Future-proof containers (no schema enforcement yet)
    facts: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
