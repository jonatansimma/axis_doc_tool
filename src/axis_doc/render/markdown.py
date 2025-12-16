from __future__ import annotations

from axis_doc.models import CameraDocumentation


def render_multi_camera_md(docs: list[CameraDocumentation]) -> str:
    parts: list[str] = []
    parts.append("# Site Documentation (placeholder)")
    parts.append("")
    parts.append(f"Camera count: **{len(docs)}**")
    parts.append("")

    for i, d in enumerate(docs, start=1):
        if i > 1:
            parts.append("---")
            parts.append("")

        parts.append(f"## Camera {i}")
        parts.append("")
        parts.append(f"- **IP:** {d.identity.ip}")
        parts.append("")

    return "\n".join(parts)


def render_multi_camera_md(docs: list[CameraDocumentation]) -> str:
    parts: list[str] = []
    parts.append("# Site Documentation (placeholder)")
    parts.append("")
    parts.append(f"Camera count: **{len(docs)}**")
    parts.append("")
    for i, d in enumerate(docs, start=1):
        parts.append(f"---\n\n## Camera {i}\n")
        parts.append(f"- **IP:** {d.identity.ip}")
    parts.append("")
    return "\n".join(parts)
