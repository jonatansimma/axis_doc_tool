from __future__ import annotations

import re

from axis_doc.models import CameraCapabilities, CameraKind


# Q18xx series (e.g., Q1806) and P37xx series (e.g., P3748) are multisensor families
_MULTI_RE = re.compile(r"\b(Q18\d{2}|P37\d{2})\b", re.IGNORECASE)

_PTZ_HINT_RE = re.compile(r"\bPTZ\b", re.IGNORECASE)


def resolve_capabilities(model: str | None) -> CameraCapabilities:
    if not model:
        return CameraCapabilities(kind=CameraKind.UNKNOWN)

    m = model.strip()

    # Explicit hint wins
    if _PTZ_HINT_RE.search(m):
        return CameraCapabilities(kind=CameraKind.PTZ)

    # Multisensor families (by model prefix)
    if _MULTI_RE.search(m):
        return CameraCapabilities(kind=CameraKind.MULTISENSOR)

    # Otherwise: default to fixed (conservative enough for now)
    return CameraCapabilities(kind=CameraKind.FIXED)
