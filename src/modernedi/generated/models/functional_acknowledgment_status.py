# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class FunctionalAcknowledgmentStatus(str, Enum):
    """
    Stable normalized acknowledgment status used for group and transaction-set results. This is not a direct alias for AK901 or AK501; in particular, an AK501 `A` with AK3/AK4 or AK502 and later error detail is `accepted_with_errors`, while the raw `acknowledgmentCode` remains `A`.
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
        """Create an instance of FunctionalAcknowledgmentStatus from a JSON string"""
        return cls(json.loads(json_str))
