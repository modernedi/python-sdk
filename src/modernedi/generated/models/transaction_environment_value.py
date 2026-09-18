# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class TransactionEnvironmentValue(str, Enum):
    """
    Isolated transaction and queue environment used for this response object.
    """

    """
    allowed enum values
    """
    PRODUCTION = 'production'
    TEST = 'test'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TransactionEnvironmentValue from a JSON string"""
        return cls(json.loads(json_str))
