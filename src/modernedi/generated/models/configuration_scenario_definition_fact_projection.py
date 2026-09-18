# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class ConfigurationScenarioDefinitionFactProjection(str, Enum):
    """
    Select one declared per-occurrence fact value, aggregate values across occurrences as a list or set, or select the first/latest observed occurrence. Correlations require value.
    """

    """
    allowed enum values
    """
    VALUE = 'value'
    LIST = 'list'
    SET = 'set'
    FIRST = 'first'
    LATEST = 'latest'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfigurationScenarioDefinitionFactProjection from a JSON string"""
        return cls(json.loads(json_str))
