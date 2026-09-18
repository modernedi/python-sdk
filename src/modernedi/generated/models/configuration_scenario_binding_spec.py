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
from modernedi.generated.models.configuration_scenario_binding_actor_binding import ConfigurationScenarioBindingActorBinding
from modernedi.generated.models.configuration_scenario_binding_definition_reference import ConfigurationScenarioBindingDefinitionReference
from modernedi.generated.models.configuration_scenario_binding_step_binding import ConfigurationScenarioBindingStepBinding
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioBindingSpec(BaseModel):
    """
    References one exact published definition and binds all of its actors and steps. Apply resolves and freezes authoritative artifacts for runtime use.
    """ # noqa: E501
    definition: ConfigurationScenarioBindingDefinitionReference
    environment: StrictStr = Field(description="Required workspace traffic selector, frozen into the applied binding. Production and test traffic use the same deployed mappings; this does not deploy unpublished mappings or create another workspace. Runs use the selected AS2/X12 profile and keep transaction lookup, acknowledgments, and evidence in that environment, without falling back to the other profile.")
    actors: Annotated[List[ConfigurationScenarioBindingActorBinding], Field(min_length=1, max_length=100)] = Field(description="Exactly one binding for every definition actor. IDs must be unique; exactly one endpoint must be this workspace and at least one must be a current external partner.")
    steps: Annotated[List[ConfigurationScenarioBindingStepBinding], Field(min_length=1, max_length=500)] = Field(description="Exactly one binding for every definition step. IDs must be unique.")
    __properties: ClassVar[List[str]] = ["definition", "environment", "actors", "steps"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['production', 'test']):
            raise ValueError("must be one of enum values ('production', 'test')")
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
        """Create an instance of ConfigurationScenarioBindingSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in actors (list)
        _items = []
        if self.actors:
            for _item_actors in self.actors:
                if _item_actors:
                    _items.append(_item_actors.to_dict())
            _dict['actors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioBindingSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "definition": ConfigurationScenarioBindingDefinitionReference.from_dict(obj["definition"]) if obj.get("definition") is not None else None,
            "environment": obj.get("environment"),
            "actors": [ConfigurationScenarioBindingActorBinding.from_dict(_item) for _item in obj["actors"]] if obj.get("actors") is not None else None,
            "steps": [ConfigurationScenarioBindingStepBinding.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None
        }.items() if key in obj})
        return _obj
