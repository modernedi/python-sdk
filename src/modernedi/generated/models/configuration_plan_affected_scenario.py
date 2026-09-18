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
from modernedi.generated.models.configuration_plan_scenario_definition import ConfigurationPlanScenarioDefinition
from modernedi.generated.models.configuration_plan_scenario_resource import ConfigurationPlanScenarioResource
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationPlanAffectedScenario(BaseModel):
    """
    One applied scenario binding whose executable authority depends on a changed resource.
    """ # noqa: E501
    binding_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Stable scenario binding identifier.", alias="bindingId")
    revision: Annotated[int, Field(strict=True, ge=0)] = Field(description="Applied immutable binding revision.")
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Customer-facing binding name.")
    environment: StrictStr
    definition: ConfigurationPlanScenarioDefinition
    effect: StrictStr = Field(description="REAPPLIED_BY_APPLY refreshes the binding's frozen authority in this aggregate apply; RETIRED_BY_APPLY removes it from current configuration while preserving its history; REAPPLY_REQUIRED identifies a binding outside the desired configuration that needs a separate refresh.")
    resources: Annotated[List[ConfigurationPlanScenarioResource], Field(min_length=1)] = Field(description="Planned changes responsible for this scenario effect.")
    __properties: ClassVar[List[str]] = ["bindingId", "revision", "name", "environment", "definition", "effect", "resources"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['production', 'test']):
            raise ValueError("must be one of enum values ('production', 'test')")
        return value

    @field_validator('effect')
    def effect_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['REAPPLY_REQUIRED', 'REAPPLIED_BY_APPLY', 'RETIRED_BY_APPLY']):
            raise ValueError("must be one of enum values ('REAPPLY_REQUIRED', 'REAPPLIED_BY_APPLY', 'RETIRED_BY_APPLY')")
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
        """Create an instance of ConfigurationPlanAffectedScenario from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item_resources in self.resources:
                if _item_resources:
                    _items.append(_item_resources.to_dict())
            _dict['resources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationPlanAffectedScenario from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "bindingId": obj.get("bindingId"),
            "revision": obj.get("revision"),
            "name": obj.get("name"),
            "environment": obj.get("environment"),
            "definition": ConfigurationPlanScenarioDefinition.from_dict(obj["definition"]) if obj.get("definition") is not None else None,
            "effect": obj.get("effect"),
            "resources": [ConfigurationPlanScenarioResource.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None
        }.items() if key in obj})
        return _obj
