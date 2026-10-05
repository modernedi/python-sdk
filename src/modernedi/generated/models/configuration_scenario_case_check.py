# coding: utf-8

"""Generated from the ModernEDI Integration API 1.36.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioCaseCheck(BaseModel):
    """
    ConfigurationScenarioCaseCheck
    """ # noqa: E501
    id: Annotated[str, Field(strict=True, max_length=1024)] = Field(description="Stable interpreter check ID, such as assertion:invoiceCurrencyMatches.")
    outcome: StrictStr = Field(description="Actual outcome of the interpreter check, not the saved test's status.")
    code: StrictStr = Field(description="Interpreter result code, without fact values or document contents.")
    __properties: ClassVar[List[str]] = ["id", "outcome", "code"]

    @field_validator('outcome')
    def outcome_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PASSED', 'FAILED', 'PENDING', 'INCONCLUSIVE']):
            raise ValueError("must be one of enum values ('PASSED', 'FAILED', 'PENDING', 'INCONCLUSIVE')")
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
        """Create an instance of ConfigurationScenarioCaseCheck from a JSON string"""
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
        """Create an instance of ConfigurationScenarioCaseCheck from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "outcome": obj.get("outcome"),
            "code": obj.get("code")
        }.items() if key in obj})
        return _obj
