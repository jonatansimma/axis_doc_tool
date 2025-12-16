from axis_doc.axis.capabilities import resolve_capabilities
from axis_doc.models import CameraKind


def test_resolve_unknown_when_no_model():
    assert resolve_capabilities(None).kind == CameraKind.UNKNOWN


def test_resolve_multisensor_for_q18():
    assert resolve_capabilities("AXIS Q1806-LE").kind == CameraKind.MULTISENSOR


def test_resolve_multisensor_for_p37():
    assert resolve_capabilities("AXIS P3748-PLVE").kind == CameraKind.MULTISENSOR


def test_resolve_ptz_when_ptz_hint_present():
    assert resolve_capabilities("AXIS Q6358-LE PTZ").kind == CameraKind.PTZ


def test_resolve_fixed_for_other_series():
    assert resolve_capabilities("AXIS M4228-LVE").kind == CameraKind.FIXED
