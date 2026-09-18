# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class ConfigurationScenarioDefinitionScalarType(str, Enum):
    """
    Closed scalar type used directly or as the element type of list and set values.
    """

    """
    allowed enum values
    """
    STRING = 'string'
    DECIMAL = 'decimal'
    DATE = 'date'
    TIME = 'time'
    TIMESTAMP = 'timestamp'
    BOOLEAN = 'boolean'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfigurationScenarioDefinitionScalarType from a JSON string"""
        return cls(json.loads(json_str))
