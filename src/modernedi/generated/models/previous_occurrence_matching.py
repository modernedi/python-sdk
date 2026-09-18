# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.previous_occurrence_matching_quantifiers_inner import PreviousOccurrenceMatchingQuantifiersInner
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PreviousOccurrenceMatching(BaseModel):
    """
    For a same-step supersedes transition whose step occurrence max is at least 2, pair occurrence n with n-1. The first occurrence is recorded as the initial revision, so both matching.unmatched and effect.unmatched must be record. A separate cross-step transition can link an initial 850 to the first 860. cancels uses a distinct cancellation-document step and cannot use previous matching.
    """ # noqa: E501
    strategy: StrictStr
    quantifiers: Annotated[List[PreviousOccurrenceMatchingQuantifiersInner], Field(min_length=1, max_length=1)]
    unmatched: StrictStr = Field(description="Record the first occurrence because it has no predecessor; later occurrences must match their immediate predecessor.")
    __properties: ClassVar[List[str]] = ["strategy", "quantifiers", "unmatched"]

    @field_validator('strategy')
    def strategy_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['previous']):
            raise ValueError("must be one of enum values ('previous')")
        return value

    @field_validator('unmatched')
    def unmatched_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['record']):
            raise ValueError("must be one of enum values ('record')")
        return value

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PreviousOccurrenceMatching from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_unset=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in quantifiers (list)
        _items = []
        if self.quantifiers:
            for _item_quantifiers in self.quantifiers:
                if _item_quantifiers:
                    _items.append(_item_quantifiers.to_dict())
            _dict['quantifiers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PreviousOccurrenceMatching from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "strategy": obj.get("strategy"),
            "quantifiers": [PreviousOccurrenceMatchingQuantifiersInner.from_dict(_item) for _item in obj["quantifiers"]] if obj.get("quantifiers") is not None else None,
            "unmatched": obj.get("unmatched")
        }.items() if key in obj})
        return _obj
