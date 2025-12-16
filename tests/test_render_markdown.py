from axis_doc.models import CameraDocumentation, CameraIdentity
from axis_doc.render.markdown import render_camera_doc_md


def test_render_includes_placeholder_sections():
    doc = CameraDocumentation(identity=CameraIdentity(ip="192.168.1.10"))
    md = render_camera_doc_md(doc)
    assert "## Identity" in md
    assert "## System (placeholder)" in md
    assert "## Network (placeholder)" in md
