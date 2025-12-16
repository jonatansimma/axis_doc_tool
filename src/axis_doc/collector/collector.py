from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from axis_doc.models import CameraDocumentation, CameraIdentity


@dataclass(frozen=True)
class CollectorConfig:
    """
    Placeholder for future collector options.
    Keep minimal until v1.2+.
    """
    pass


class DocumentationCollector:
    """
    Builds CameraDocumentation objects.

    Current phase:
    - No API calls
    - Identity only (IP)
    """

    def __init__(self, config: CollectorConfig | None = None) -> None:
        self._config = config or CollectorConfig()

    def collect_for_ips(self, ips: Iterable[str]) -> list[CameraDocumentation]:
        docs: list[CameraDocumentation] = []
        for ip in ips:
            ident = CameraIdentity(ip=ip)
            docs.append(CameraDocumentation(identity=ident))
        return docs
