# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class FilterableTransactionMdnStatus(str, Enum):
    """
    Closed set of normalized AS2 receipt-assurance statuses accepted by exact transaction-list filtering. Response models use a separate forward-compatible enum so a newer response status does not prevent an older SDK from reading the row.
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
        """Create an instance of FilterableTransactionMdnStatus from a JSON string"""
        return cls(json.loads(json_str))
