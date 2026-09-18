# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from enum import Enum
from typing_extensions import Self

class ConfigurationDocumentApiVersion(str, Enum):
    """
    Version of the portable configuration document contract used by export, planning, and apply.
    """

    """
    allowed enum values
    """
    MODERNEDI_DOT_COM_SLASH_V1 = 'modernedi.com/v1'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ConfigurationDocumentApiVersion from a JSON string"""
        return cls(json.loads(json_str))
