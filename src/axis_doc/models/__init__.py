"""
axis_doc.models

Central exports for model types used across the application.

Keep imports here lightweight and stable. During early development, some models
may not exist yet (e.g., snapshot/capabilities). Those are imported optionally
to avoid breaking the package while we build incrementally.
"""

from __future__ import annotations

# Core (must exist)
from .camera_doc import (
    CameraDocumentation,
    CameraIdentity,
    TechnicianNotes,
    SystemFacts,
    NetworkFacts,
    StreamFacts,
)

__all__ = [
    "CameraDocumentation",
    "CameraIdentity",
    "TechnicianNotes",
    "SystemFacts",
    "NetworkFacts",
    "StreamFacts",
]

# Optional models (may be added later)
try:
    from .snapshot import SnapshotMetadata  # type: ignore

    __all__.append("SnapshotMetadata")
except Exception:
    pass

try:
    from .capabilities import CameraCapabilities  # type: ignore

    __all__.append("CameraCapabilities")
except Exception:
    pass
