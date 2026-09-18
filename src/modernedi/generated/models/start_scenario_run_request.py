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
from modernedi.generated.models.scenario_definition_identity import ScenarioDefinitionIdentity
from modernedi.generated.models.scenario_run_parameter_value import ScenarioRunParameterValue
from modernedi.generated.models.start_scenario_run_request_binding import StartScenarioRunRequestBinding
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class StartScenarioRunRequest(BaseModel):
    """
    StartScenarioRunRequest
    """ # noqa: E501
    definition: ScenarioDefinitionIdentity
    environment: StrictStr
    binding: StartScenarioRunRequestBinding
    parameters: Optional[Dict[str, ScenarioRunParameterValue]] = Field(default=None, description="Values keyed by declared definition parameter ID. The server rejects unknown, missing-required, or type-invalid values and materializes declared defaults before hashing the run input. Raw parameter values are never returned by the run API.", json_schema_extra={"examples": [{"shipmentCount": 2, "cutoffTotal": "1250.00", "priority": True, "allowedWarehouses": ["PHX", "LAX"]}]})
    __properties: ClassVar[List[str]] = ["definition", "environment", "binding", "parameters"]

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
        """Create an instance of StartScenarioRunRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of binding
        if self.binding:
            _dict['binding'] = self.binding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in parameters (dict)
        _field_dict = {}
        if self.parameters:
            for _key_parameters in self.parameters:
                if self.parameters[_key_parameters]:
                    _field_dict[_key_parameters] = self.parameters[_key_parameters].to_dict()
            _dict['parameters'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StartScenarioRunRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "definition": ScenarioDefinitionIdentity.from_dict(obj["definition"]) if obj.get("definition") is not None else None,
            "environment": obj.get("environment"),
            "binding": StartScenarioRunRequestBinding.from_dict(obj["binding"]) if obj.get("binding") is not None else None,
            "parameters": dict(
                (_k, ScenarioRunParameterValue.from_dict(_v))
                for _k, _v in obj["parameters"].items()
            )
            if obj.get("parameters") is not None
            else None
        }.items() if key in obj})
        return _obj
