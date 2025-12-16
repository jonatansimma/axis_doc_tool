from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class CameraKind(str, Enum):
    UNKNOWN = "unknown"
    FIXED = "fixed"
    PTZ = "ptz"
    MULTISENSOR = "multisensor"


@dataclass(frozen=True)
class CameraCapabilities:
    """
    Resolved capabilities for the camera.

    In this phase:
    - populated only from local hints (e.g., user-supplied model string)
    - no device calls
    """
    kind: CameraKind = CameraKind.UNKNOWN

    # Future flags (leave as None/False until populated from API later)
    has_ir: bool | None = None
    has_audio: bool | None = None
    supports_object_analytics: bool | None = None
    supports_mqtt: bool | None = None
