from __future__ import annotations

import ipaddress
import re
from dataclasses import dataclass
from typing import Iterable


_RANGE_FULL_RE = re.compile(r"^\s*(\d+\.\d+\.\d+\.\d+)\s*-\s*(\d+\.\d+\.\d+\.\d+)\s*$")
_RANGE_SHORT_RE = re.compile(r"^\s*(\d+\.\d+\.\d+)\.(\d+)\s*-\s*(\d+)\s*$")


@dataclass(frozen=True)
class ParsedTargets:
    targets: list[str]
    rejected: list[str]


def _split_tokens(text: str) -> list[str]:
    # Split on common separators and remove empties
    raw = re.split(r"[\s,;]+", text.strip())
    return [t for t in (r.strip() for r in raw) if t]


def _expand_cidr(token: str) -> Iterable[ipaddress.IPv4Address]:
    net = ipaddress.ip_network(token, strict=False)
    if not isinstance(net, ipaddress.IPv4Network):
        return []
    # Exclude network/broadcast where applicable by iterating hosts()
    return net.hosts()


def _expand_range_full(a: str, b: str) -> Iterable[ipaddress.IPv4Address]:
    start = ipaddress.IPv4Address(a)
    end = ipaddress.IPv4Address(b)
    if int(end) < int(start):
        start, end = end, start
    for i in range(int(start), int(end) + 1):
        yield ipaddress.IPv4Address(i)


def _expand_range_short(prefix: str, start_oct: str, end_oct: str) -> Iterable[ipaddress.IPv4Address]:
    s = int(start_oct)
    e = int(end_oct)
    if e < s:
        s, e = e, s
    for last in range(s, e + 1):
        yield ipaddress.IPv4Address(f"{prefix}.{last}")


def parse_targets(text: str) -> ParsedTargets:
    """
    Parse manual IP input into an ordered, de-duplicated list of IPv4 strings.
    No network activity. No file I/O.

    Returns ParsedTargets(targets=[...], rejected=[...]).
    """
    if not text or not text.strip():
        return ParsedTargets(targets=[], rejected=[])

    tokens = _split_tokens(text)
    out: list[str] = []
    seen: set[str] = set()
    rejected: list[str] = []

    for token in tokens:
        try:
            # CIDR
            if "/" in token:
                for ip in _expand_cidr(token):
                    s = str(ip)
                    if s not in seen:
                        seen.add(s)
                        out.append(s)
                continue

            # full range A-B
            m = _RANGE_FULL_RE.match(token)
            if m:
                a, b = m.group(1), m.group(2)
                for ip in _expand_range_full(a, b):
                    s = str(ip)
                    if s not in seen:
                        seen.add(s)
                        out.append(s)
                continue

            # short range 192.168.0.10-25
            m2 = _RANGE_SHORT_RE.match(token)
            if m2:
                prefix, a, b = m2.group(1), m2.group(2), m2.group(3)
                for ip in _expand_range_short(prefix, a, b):
                    s = str(ip)
                    if s not in seen:
                        seen.add(s)
                        out.append(s)
                continue

            # single IP
            ip = ipaddress.IPv4Address(token)
            s = str(ip)
            if s not in seen:
                seen.add(s)
                out.append(s)

        except Exception:
            rejected.append(token)

    return ParsedTargets(targets=out, rejected=rejected)
