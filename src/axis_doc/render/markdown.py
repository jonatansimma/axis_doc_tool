from __future__ import annotations

from axis_doc.models import CameraDocumentation


def render_camera_doc_md(doc: CameraDocumentation) -> str:
    # Minimal Markdown output (placeholder, but valid and stable)
    lines: list[str] = []
    lines.append(f"# Camera Documentation (placeholder)")
    lines.append("")
    lines.append("## Identity")
    lines.append(f"- **IP:** {doc.identity.ip}")
    if doc.identity.host:
        lines.append(f"- **Host:** {doc.identity.host}")
    if doc.identity.model:
        lines.append(f"- **Model:** {doc.identity.model}")
    if doc.identity.firmware:
        lines.append(f"- **Firmware:** {doc.identity.firmware}")
    lines.append("")
    lines.append("## Notes")
    lines.append("_No data collected yet (API stub phase)._")
    lines.append("")
    return "\n".join(lines)


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
