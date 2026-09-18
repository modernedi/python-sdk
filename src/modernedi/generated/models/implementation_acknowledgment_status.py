# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class ImplementationAcknowledgmentStatus(str, Enum):
    """
    Stable normalized 999 acknowledgment status used for aggregate, group, and transaction-set results. Raw IK501 `A` is not clean when its AK2 loop contains IK3/IK4 error detail; that contradictory result is `unknown`.
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
        """Create an instance of ImplementationAcknowledgmentStatus from a JSON string"""
        return cls(json.loads(json_str))
