# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, Optional
from uuid import UUID
from modernedi.generated.models.configuration_plan_action import ConfigurationPlanAction
from modernedi.generated.models.configuration_plan_current_value import ConfigurationPlanCurrentValue
from modernedi.generated.models.configuration_plan_desired_value import ConfigurationPlanDesiredValue
from modernedi.generated.models.configuration_resource_kind import ConfigurationResourceKind
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationPlanOperation(BaseModel):
    """
    One changed resource. CREATE has only `desired`, UPDATE has `current` and `desired`, and DELETE has only `current`.
    """ # noqa: E501
    action: ConfigurationPlanAction
    kind: ConfigurationResourceKind
    key: UUID = Field(description="Stable portable resource key.")
    path: StrictStr = Field(description="Desired resource path for CREATE/UPDATE or current exported path for DELETE.")
    current: Optional[ConfigurationPlanCurrentValue] = None
    desired: Optional[ConfigurationPlanDesiredValue] = None
    __properties: ClassVar[List[str]] = ["action", "kind", "key", "path", "current", "desired"]

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
        """Create an instance of ConfigurationPlanOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of current
        if self.current:
            _dict['current'] = self.current.to_dict()
        # override the default output from pydantic by calling `to_dict()` of desired
        if self.desired:
            _dict['desired'] = self.desired.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationPlanOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "action": obj.get("action"),
            "kind": obj.get("kind"),
            "key": obj.get("key"),
            "path": obj.get("path"),
            "current": ConfigurationPlanCurrentValue.from_dict(obj["current"]) if obj.get("current") is not None else None,
            "desired": ConfigurationPlanDesiredValue.from_dict(obj["desired"]) if obj.get("desired") is not None else None
        }.items() if key in obj})
        return _obj
