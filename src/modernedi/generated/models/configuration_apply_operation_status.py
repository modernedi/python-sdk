# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class ConfigurationApplyOperationStatus(str, Enum):
    """
    `PENDING` means the aggregate database change committed and runtime publication is retrying. `SUCCEEDED` means the stored apply operation is terminal.
    """

    """
    allowed enum values
    """
    PENDING = 'PENDING'
    SUCCEEDED = 'SUCCEEDED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfigurationApplyOperationStatus from a JSON string"""
        return cls(json.loads(json_str))
