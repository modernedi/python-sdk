# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class ConfigurationResourceKind(str, Enum):
    """
    Exportable ModernEDI configuration resource type.
    """

    """
    allowed enum values
    """
    AS2CONNECTION = 'As2Connection'
    PARTNER = 'Partner'
    MAPPING = 'Mapping'
    SCENARIODEFINITION = 'ScenarioDefinition'
    SCENARIOBINDING = 'ScenarioBinding'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfigurationResourceKind from a JSON string"""
        return cls(json.loads(json_str))
