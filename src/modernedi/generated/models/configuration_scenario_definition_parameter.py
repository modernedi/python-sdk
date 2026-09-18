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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_scenario_definition_scalar_type import ConfigurationScenarioDefinitionScalarType
from modernedi.generated.models.configuration_scenario_definition_value_type import ConfigurationScenarioDefinitionValueType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionParameter(BaseModel):
    """
    A typed value supplied when a run starts through the Workspace UI or API, or resolved from its declared default when optional.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    type: ConfigurationScenarioDefinitionValueType
    element_type: Optional[ConfigurationScenarioDefinitionScalarType] = Field(default=None, alias="elementType")
    required: StrictBool = Field(description="Whether the run must explicitly provide this value. A required parameter cannot also have a default.")
    default: Optional[Any] = Field(default=None, description="Optional JSON value used when the run omits a non-required parameter.")
    __properties: ClassVar[List[str]] = ["id", "type", "elementType", "required", "default"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of ConfigurationScenarioDefinitionParameter from a JSON string"""
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
        # set to None if default (nullable) is None
        # and model_fields_set contains the field
        if self.default is None and "default" in self.model_fields_set:
            _dict['default'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionParameter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "type": obj.get("type"),
            "elementType": obj.get("elementType"),
            "required": obj.get("required"),
            "default": obj.get("default")
        }.items() if key in obj})
        return _obj
