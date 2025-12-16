from axis_doc.ipparse import parse_targets


def test_parse_single_ip():
    r = parse_targets("192.168.1.10")
    assert r.targets == ["192.168.1.10"]
    assert r.rejected == []


def test_parse_full_range():
    r = parse_targets("192.168.1.10-192.168.1.12")
    assert r.targets == ["192.168.1.10", "192.168.1.11", "192.168.1.12"]


def test_parse_short_range():
    r = parse_targets("192.168.1.10-12")
    assert r.targets == ["192.168.1.10", "192.168.1.11", "192.168.1.12"]


def test_parse_cidr_hosts():
    r = parse_targets("192.168.1.0/30")
    # /30 => 4 addresses; hosts() yields 2 usable hosts (.1, .2)
    assert r.targets == ["192.168.1.1", "192.168.1.2"]


def test_dedup_and_rejects():
    r = parse_targets("192.168.1.10 192.168.1.10 junk")
    assert r.targets == ["192.168.1.10"]
    assert r.rejected == ["junk"]
