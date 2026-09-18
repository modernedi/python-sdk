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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioGraphGuidance(BaseModel):
    """
    ScenarioGraphGuidance
    """ # noqa: E501
    next_action: Optional[StrictStr] = Field(alias="nextAction")
    step_id: Optional[Annotated[str, Field(strict=True)]] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="stepId")
    occurrence: Optional[Annotated[int, Field(strict=True, ge=1)]]
    __properties: ClassVar[List[str]] = ["nextAction", "stepId", "occurrence"]

    @field_validator('next_action')
    def next_action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['advance_adapter', 'attach_or_refresh']):
            raise ValueError("must be one of enum values ('advance_adapter', 'attach_or_refresh')")
        return value

    @field_validator('step_id', mode="before")
    def step_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
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
        """Create an instance of ScenarioGraphGuidance from a JSON string"""
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
        # set to None if next_action (nullable) is None
        # and model_fields_set contains the field
        if self.next_action is None and "next_action" in self.model_fields_set:
            _dict['nextAction'] = None

        # set to None if step_id (nullable) is None
        # and model_fields_set contains the field
        if self.step_id is None and "step_id" in self.model_fields_set:
            _dict['stepId'] = None

        # set to None if occurrence (nullable) is None
        # and model_fields_set contains the field
        if self.occurrence is None and "occurrence" in self.model_fields_set:
            _dict['occurrence'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioGraphGuidance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "nextAction": obj.get("nextAction"),
            "stepId": obj.get("stepId"),
            "occurrence": obj.get("occurrence")
        }.items() if key in obj})
        return _obj
