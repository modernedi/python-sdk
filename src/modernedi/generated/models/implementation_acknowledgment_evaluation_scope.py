# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class ImplementationAcknowledgmentEvaluationScope(str, Enum):
    """
    Outcome level selected for one transaction from a correlated 999. Group and acknowledgment fallbacks use the documented primary-aware conservative reduction with nested IK5 statuses; raw AK9 and IK5 objects are unchanged.
    """

    """
    allowed enum values
    """
    TRANSACTION_SET = 'transaction_set'
    IMPLEMENTATION_GROUP = 'implementation_group'
    IMPLEMENTATION_ACKNOWLEDGMENT = 'implementation_acknowledgment'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ImplementationAcknowledgmentEvaluationScope from a JSON string"""
        return cls(json.loads(json_str))
