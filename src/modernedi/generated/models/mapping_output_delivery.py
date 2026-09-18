# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class MappingOutputDelivery(str, Enum):
    """
    Safe delivery category without infrastructure identifiers:  - `MAPPED_OUTPUTS`: managed polling and per-partner webhook delivery - `TRANSACTION_RECORD`: incoming result retained on the transaction record - `OUTBOUND_AS2`: outbound source-to-X12 transform used by AS2 send APIs
    """

    """
    allowed enum values
    """
    MAPPED_OUTPUTS = 'MAPPED_OUTPUTS'
    TRANSACTION_RECORD = 'TRANSACTION_RECORD'
    OUTBOUND_AS2 = 'OUTBOUND_AS2'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MappingOutputDelivery from a JSON string"""
        return cls(json.loads(json_str))
