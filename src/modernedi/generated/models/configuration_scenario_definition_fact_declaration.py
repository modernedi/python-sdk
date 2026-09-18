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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_scenario_definition_scalar_type import ConfigurationScenarioDefinitionScalarType
from modernedi.generated.models.configuration_scenario_definition_value_type import ConfigurationScenarioDefinitionValueType
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionFactDeclaration(BaseModel):
    """
    Stable semantic ABI for one fact exposed by a step occurrence. The binding/runtime capability separately defines extraction provenance.
    """ # noqa: E501
    name: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    type: ConfigurationScenarioDefinitionValueType
    element_type: Optional[ConfigurationScenarioDefinitionScalarType] = Field(default=None, alias="elementType")
    cardinality: StrictStr = Field(description="Presence of the typed value on each occurrence. Collection multiplicity is expressed by type list/set, never by a separate many cardinality.")
    normalization: Annotated[List[StrictStr], Field(max_length=5)] = Field(description="Ordered, deterministic normalization applied before typed evaluation.")
    sensitivity: StrictStr = Field(description="Data-handling classification carried with evidence and diagnostics.")
    __properties: ClassVar[List[str]] = ["name", "type", "elementType", "cardinality", "normalization", "sensitivity"]

    @field_validator('name', mode="before")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('cardinality')
    def cardinality_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['one', 'optional']):
            raise ValueError("must be one of enum values ('one', 'optional')")
        return value

    @field_validator('normalization')
    def normalization_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['trim', 'collapse_whitespace', 'uppercase', 'lowercase', 'decimal_canonical']):
                raise ValueError("each list item must be one of ('trim', 'collapse_whitespace', 'uppercase', 'lowercase', 'decimal_canonical')")
        return value

    @field_validator('sensitivity')
    def sensitivity_validate_enum(cls, value):
        """Validates the enum"""
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
        """Create an instance of ConfigurationScenarioDefinitionFactDeclaration from a JSON string"""
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
        """Create an instance of ConfigurationScenarioDefinitionFactDeclaration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "name": obj.get("name"),
            "type": obj.get("type"),
            "elementType": obj.get("elementType"),
            "cardinality": obj.get("cardinality"),
            "normalization": obj.get("normalization"),
            "sensitivity": obj.get("sensitivity")
        }.items() if key in obj})
        return _obj
