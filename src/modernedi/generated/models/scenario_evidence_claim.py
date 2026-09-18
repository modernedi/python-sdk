# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceClaim(BaseModel):
    """
    ScenarioEvidenceClaim
    """ # noqa: E501
    type: StrictStr
    statement: StrictStr
    scope: StrictStr
    __properties: ClassVar[List[str]] = ["type", "statement", "scope"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['implementation_verification']):
            raise ValueError("must be one of enum values ('implementation_verification')")
        return value

    @field_validator('statement')
    def statement_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ModernEDI observed and evaluated this scenario run against the exact applied binding recorded in this report.']):
            raise ValueError("must be one of enum values ('ModernEDI observed and evaluated this scenario run against the exact applied binding recorded in this report.')")
        return value

    @field_validator('scope')
    def scope_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['This report proves only the recorded run; it does not certify the tenant\'s broader EDI implementation.']):
            raise ValueError("must be one of enum values ('This report proves only the recorded run; it does not certify the tenant\'s broader EDI implementation.')")
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
        """Create an instance of ScenarioEvidenceClaim from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceClaim from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "type": obj.get("type"),
            "statement": obj.get("statement"),
            "scope": obj.get("scope")
        }.items() if key in obj})
        return _obj
