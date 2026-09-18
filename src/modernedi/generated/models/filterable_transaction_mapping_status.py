# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class FilterableTransactionMappingStatus(str, Enum):
    """
    Durable consolidated mapping states available to exact list filtering. `UNAVAILABLE` is intentionally excluded because it describes a request-local telemetry read failure rather than an indexed transaction state.
    """

    """
    allowed enum values
    """
    NOT_RECORDED = 'NOT_RECORDED'
    SUCCEEDED = 'SUCCEEDED'
    FAILED = 'FAILED'
    COMPLETED_WITH_ERRORS = 'COMPLETED_WITH_ERRORS'
    RECOVERED = 'RECOVERED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FilterableTransactionMappingStatus from a JSON string"""
        return cls(json.loads(json_str))
