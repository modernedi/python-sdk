# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class FilterableFunctionalAcknowledgmentStatus(str, Enum):
    """
    Closed set of normalized 997 statuses accepted by exact transaction-list filtering. Response models use a separate forward-compatible enum so a newer response status does not prevent an older SDK from reading the row.
    """

    """
    allowed enum values
    """
    ACCEPTED = 'accepted'
    ACCEPTED_WITH_ERRORS = 'accepted_with_errors'
    PARTIALLY_ACCEPTED = 'partially_accepted'
    REJECTED = 'rejected'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FilterableFunctionalAcknowledgmentStatus from a JSON string"""
        return cls(json.loads(json_str))
