from __future__ import annotations

from axis_doc.models import CameraDocumentation


def render_camera_doc_md(doc: CameraDocumentation) -> str:
    lines: list[str] = []

    lines.append("# Camera Documentation (placeholder)")
    lines.append("")

    # Identity
    lines.append("## Identity")
    lines.append(f"- **IP:** {doc.identity.ip}")
    if doc.identity.host:
        lines.append(f"- **Host:** {doc.identity.host}")
    if doc.identity.model:
        lines.append(f"- **Model:** {doc.identity.model}")
    if doc.identity.firmware:
        lines.append(f"- **Firmware:** {doc.identity.firmware}")
    lines.append("")
    lines.append("## Capabilities (placeholder)")
    lines.append(f"- **Kind:** {doc.capabilities.kind.value}")
    lines.append("")


    # System
    lines.append("## System (placeholder)")
    lines.append(f"- **AXIS OS:** {doc.system.axis_os_version or '—'}")
    lines.append(f"- **Timezone:** {doc.system.timezone or '—'}")
    lines.append(
        f"- **NTP:** {', '.join(doc.system.ntp_servers) if doc.system.ntp_servers else '—'}"
    )
    lines.append("")

    # Network
    lines.append("## Network (placeholder)")
    lines.append(f"- **IPv4:** {doc.network.ipv4_address or doc.identity.ip}")
    lines.append(f"- **Netmask:** {doc.network.ipv4_netmask or '—'}")
    lines.append(f"- **Gateway:** {doc.network.ipv4_gateway or '—'}")
    lines.append(
        f"- **DNS:** {', '.join(doc.network.dns_servers) if doc.network.dns_servers else '—'}"
    )
    lines.append(
        f"- **DHCP:** {doc.network.dhcp_enabled if doc.network.dhcp_enabled is not None else '—'}"
    )
    lines.append("")

    # Notes
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
        if i > 1:
            parts.append("---")
            parts.append("")
        parts.append(f"## Camera {i}")
        parts.append("")
        parts.append(f"- **IP:** {d.identity.ip}")
        parts.append("")
        parts.append(f"- **Kind:** {d.capabilities.kind.value}")


    return "\n".join(parts)
