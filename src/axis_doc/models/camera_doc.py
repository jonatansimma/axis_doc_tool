from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from axis_doc.models.capabilities import CameraCapabilities


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


# --- Enriched placeholders (no API calls yet) ---------------------------------

@dataclass(frozen=True)
class SystemFacts:
    axis_os_version: str | None = None
    uptime_s: int | None = None
    timezone: str | None = None
    ntp_servers: tuple[str, ...] = ()


@dataclass(frozen=True)
class NetworkFacts:
    ipv4_address: str | None = None
    ipv4_netmask: str | None = None
    ipv4_gateway: str | None = None
    dns_servers: tuple[str, ...] = ()
    dhcp_enabled: bool | None = None


@dataclass(frozen=True)
class StreamFacts:
    default_codec: str | None = None
    default_resolution: str | None = None
    default_fps: int | None = None
    bitrate_mode: str | None = None


# --- Main documentation model --------------------------------------------------

@dataclass(frozen=True)
class CameraDocumentation:
    """
    Read-only documentation payload.

    Container for:
    - identity & system facts (from Axis APIs later)
    - minimal technician notes
    - structured placeholders that will be filled later
    """
    identity: CameraIdentity
    technician: TechnicianNotes = field(default_factory=TechnicianNotes)
    collected_at: datetime = field(default_factory=lambda: datetime.now().astimezone())

    system: SystemFacts = field(default_factory=SystemFacts)
    network: NetworkFacts = field(default_factory=NetworkFacts)
    stream: StreamFacts = field(default_factory=StreamFacts)
    capabilities: CameraCapabilities = field(default_factory=CameraCapabilities)

    # Future-proof containers (no schema enforcement yet)
    facts: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
