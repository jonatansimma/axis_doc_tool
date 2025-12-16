from __future__ import annotations

import re

from axis_doc.models import CameraCapabilities, CameraKind


_PTZ_RE = re.compile(r"\b(Q\d{3,4})\b", re.IGNORECASE)          # Axis Q series often PTZ, but not always
_MULTI_RE = re.compile(r"\b(P37|Q18)\b", re.IGNORECASE)         # P37, Q18 commonly multisensor
_PTZ_HINT_RE = re.compile(r"\bPTZ\b", re.IGNORECASE)


def resolve_capabilities(model: str | None) -> CameraCapabilities:
    if not model:
        return CameraCapabilities(kind=CameraKind.UNKNOWN)

    m = model.strip()

    if _PTZ_HINT_RE.search(m):
        return CameraCapabilities(kind=CameraKind.PTZ)

    if _MULTI_RE.search(m):
        return CameraCapabilities(kind=CameraKind.MULTISENSOR)

    # Conservative: if it looks like Q-series, keep UNKNOWN unless explicitly PTZ
    if _PTZ_RE.search(m):
        return CameraCapabilities(kind=CameraKind.UNKNOWN)

    return CameraCapabilities(kind=CameraKind.FIXED)
