# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class MappingPurpose(str, Enum):
    """
    Purpose of the runtime map that produced this output. `PROCESSING` means the output is for the normal application workflow. `ACKNOWLEDGMENT` means the output is an automatically generated response document.
    """

    """
    allowed enum values
    """
    PROCESSING = 'PROCESSING'
    ACKNOWLEDGMENT = 'ACKNOWLEDGMENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MappingPurpose from a JSON string"""
        return cls(json.loads(json_str))
