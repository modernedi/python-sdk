# coding: utf-8

"""Generated from the ModernEDI Integration API 1.36.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class AdvanceScenarioRunRequest(BaseModel):
    """
    AdvanceScenarioRunRequest
    """ # noqa: E501
    close_steps: Optional[Annotated[List[Annotated[str, Field(strict=True)]], Field(min_length=1, max_length=100)]] = Field(default=None, description="Optional explicit no-more-documents decision. Only reachable open steps declared with closure.kind=explicit are eligible. Their exact attached counts and server time are recorded atomically with the result and actor-attributed operation. All business and evidence checks still apply; incomplete fulfillment can fail. New documents cannot be attached after closure, but existing observations can refresh pending evidence while the run remains active. This action never dispatches EDI and needs no messages:write scope or supplemental x-api-key. It cannot bypass an expired deadline. For an ambiguous response retry the same list, If-Match and Idempotency-Key.", alias="closeSteps")
    __properties: ClassVar[List[str]] = ["closeSteps"]

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
        """Create an instance of AdvanceScenarioRunRequest from a JSON string"""
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
        """Create an instance of AdvanceScenarioRunRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "closeSteps": obj.get("closeSteps")
        }.items() if key in obj})
        return _obj
