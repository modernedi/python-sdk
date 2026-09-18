# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.scenario_run_timeline_operation import ScenarioRunTimelineOperation
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioRunTimelineResponse(BaseModel):
    """
    ScenarioRunTimelineResponse
    """ # noqa: E501
    success: StrictBool
    run_id: Annotated[str, Field(strict=True)] = Field(alias="runId")
    operations: Annotated[List[ScenarioRunTimelineOperation], Field(max_length=100)]
    next_cursor: Optional[Annotated[str, Field(strict=True, max_length=1024)]] = Field(description="Opaque tenant-and-run-bound keyset cursor for the next page, or null when the timeline is exhausted.", alias="nextCursor")
    __properties: ClassVar[List[str]] = ["success", "runId", "operations", "nextCursor"]

    @field_validator('run_id', mode="before")
    def run_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^run-[0-9a-f-]+$", value):
            raise ValueError(r"must validate the regular expression /^run-[0-9a-f-]+$/")
        return value

    @field_validator('next_cursor', mode="before")
    def next_cursor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[A-Za-z0-9_-]+$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9_-]+$/")
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
        """Create an instance of ScenarioRunTimelineResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in operations (list)
        _items = []
        if self.operations:
            for _item_operations in self.operations:
                if _item_operations:
                    _items.append(_item_operations.to_dict())
            _dict['operations'] = _items
        # set to None if next_cursor (nullable) is None
        # and model_fields_set contains the field
        if self.next_cursor is None and "next_cursor" in self.model_fields_set:
            _dict['nextCursor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioRunTimelineResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "runId": obj.get("runId"),
            "operations": [ScenarioRunTimelineOperation.from_dict(_item) for _item in obj["operations"]] if obj.get("operations") is not None else None,
            "nextCursor": obj.get("nextCursor")
        }.items() if key in obj})
        return _obj
