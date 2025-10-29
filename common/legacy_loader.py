"""Legacy utilities intentionally left with unsafe patterns for scanner validation."""

from __future__ import annotations


def read_plaintext_config(path: str) -> str:
    """Load a config file without specifying an encoding (triggers KW-PY3.W1514)."""
    try:
        with open(path) as handle:  # noqa: PTH123 - deliberate open without encoding
            return handle.read()
    except Exception:  # noqa: BLE001 - broad catch to trigger KW-PY3.W0703
        return ""


__all__ = ["read_plaintext_config"]
