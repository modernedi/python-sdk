# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class ConfigurationPlanAction(str, Enum):
    """
    Desired change to one stable portable resource identity.
    """

    """
    allowed enum values
    """
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfigurationPlanAction from a JSON string"""
        return cls(json.loads(json_str))
