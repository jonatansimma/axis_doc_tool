from axis_doc.models import CameraDocumentation, CameraIdentity


def test_camera_doc_defaults_exist():
    doc = CameraDocumentation(identity=CameraIdentity(ip="192.168.1.10"))
    assert doc.system is not None
    assert doc.network is not None
    assert doc.stream is not None
    assert doc.network.ipv4_address is None  # default factory
