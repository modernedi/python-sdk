# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class TechnicalAcknowledgmentStatus(str, Enum):
    """
    Stable requested-TA1 lifecycle and normalized TA104 outcome.
    """

    """
    allowed enum values
    """
    NOT_REQUESTED = 'not_requested'
    PENDING = 'pending'
    RECEIVED = 'received'
    RECEIVED_WITH_ERRORS = 'received_with_errors'
    REJECTED = 'rejected'
    UNKNOWN = 'unknown'
    OVERDUE = 'overdue'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TechnicalAcknowledgmentStatus from a JSON string"""
        return cls(json.loads(json_str))
