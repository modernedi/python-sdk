# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class TransactionMdnStatus(str, Enum):
    """
    Normalized AS2 receipt-assurance status. Only `processed` is a clean completed receipt; `pending` is still within the response window and every other state requires operator review.
    """

    """
    allowed enum values
    """
    PENDING = 'pending'
    PROCESSED = 'processed'
    WARNING = 'warning'
    REJECTED = 'rejected'
    INVALID = 'invalid'
    MIC_MISMATCH = 'mic_mismatch'
    OVERDUE = 'overdue'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionMdnStatus from a JSON string"""
        return cls(json.loads(json_str))
