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
from modernedi.generated.models.configuration_scenario_definition_value_operand import ConfigurationScenarioDefinitionValueOperand
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionAssertion(BaseModel):
    """
    A fact rule that must hold for the run to pass. For example, exists can require every 810 invoice to expose invoiceTotal, sum_equal can compare shipped and invoiced totals, and monotonic can require successive 315 status timestamps to move forward. Binary operators require right; unary operators reject it.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    operator: StrictStr
    left: ConfigurationScenarioDefinitionValueOperand
    right: Optional[ConfigurationScenarioDefinitionValueOperand] = None
    __properties: ClassVar[List[str]] = ["id", "operator", "left", "right"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('operator')
    def operator_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['equal', 'not_equal', 'exists', 'unique', 'same_set', 'subset', 'sum_equal', 'less_than_or_equal', 'greater_than_or_equal', 'monotonic']):
            raise ValueError("must be one of enum values ('equal', 'not_equal', 'exists', 'unique', 'same_set', 'subset', 'sum_equal', 'less_than_or_equal', 'greater_than_or_equal', 'monotonic')")
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
        """Create an instance of ConfigurationScenarioDefinitionAssertion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of left
        if self.left:
            _dict['left'] = self.left.to_dict()
        # override the default output from pydantic by calling `to_dict()` of right
        if self.right:
            _dict['right'] = self.right.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionAssertion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "operator": obj.get("operator"),
            "left": ConfigurationScenarioDefinitionValueOperand.from_dict(obj["left"]) if obj.get("left") is not None else None,
            "right": ConfigurationScenarioDefinitionValueOperand.from_dict(obj["right"]) if obj.get("right") is not None else None
        }.items() if key in obj})
        return _obj
