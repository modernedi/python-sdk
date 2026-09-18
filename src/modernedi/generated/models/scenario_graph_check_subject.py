# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioGraphCheckSubject(BaseModel):
    """
    ScenarioGraphCheckSubject
    """ # noqa: E501
    step_id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="stepId")
    occurrence: Annotated[int, Field(strict=True, ge=1)]
    redacted: StrictBool
    fact: Optional[Annotated[str, Field(strict=True)]] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    sensitivity: Optional[StrictStr]
    evidence_references: List[Annotated[str, Field(min_length=1, strict=True)]] = Field(alias="evidenceReferences")
    __properties: ClassVar[List[str]] = ["stepId", "occurrence", "redacted", "fact", "sensitivity", "evidenceReferences"]

    @field_validator('step_id', mode="before")
    def step_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('fact', mode="before")
    def fact_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('sensitivity')
    def sensitivity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['business', 'personal', 'financial', 'health', 'restricted']):
            raise ValueError("must be one of enum values ('business', 'personal', 'financial', 'health', 'restricted')")
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
        """Create an instance of ScenarioGraphCheckSubject from a JSON string"""
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
        # set to None if fact (nullable) is None
        # and model_fields_set contains the field
        if self.fact is None and "fact" in self.model_fields_set:
            _dict['fact'] = None

        # set to None if sensitivity (nullable) is None
        # and model_fields_set contains the field
        if self.sensitivity is None and "sensitivity" in self.model_fields_set:
            _dict['sensitivity'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioGraphCheckSubject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "stepId": obj.get("stepId"),
            "occurrence": obj.get("occurrence"),
            "redacted": obj.get("redacted"),
            "fact": obj.get("fact"),
            "sensitivity": obj.get("sensitivity"),
            "evidenceReferences": obj.get("evidenceReferences")
        }.items() if key in obj})
        return _obj
