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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.configuration_scenario_binding_regression_expected import ConfigurationScenarioBindingRegressionExpected
from modernedi.generated.models.configuration_scenario_binding_regression_observation import ConfigurationScenarioBindingRegressionObservation
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioBindingRegressionCase(BaseModel):
    """
    ConfigurationScenarioBindingRegressionCase
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    name: Annotated[str, Field(min_length=1, strict=True, max_length=120)]
    parameters: Dict[str, Any] = Field(description="Ordinary run parameters, resolved and type-checked against this exact definition.")
    observations: Annotated[List[ConfigurationScenarioBindingRegressionObservation], Field(max_length=20)] = Field(description="Listed attachment order. Repeated step IDs are assigned occurrence 1, 2, and so on. No sorting by business event time occurs.")
    evaluated_after_seconds: Annotated[int, Field(le=31536000, strict=True, ge=0)] = Field(description="Whole seconds after the synthetic start (at most 365 days).", alias="evaluatedAfterSeconds")
    close_steps: Annotated[List[Annotated[str, Field(strict=True)]], Field(max_length=100)] = Field(description="Explicit-completion steps to close at the evaluation time. Closing never waives their checks.", alias="closeSteps")
    expected: ConfigurationScenarioBindingRegressionExpected
    __properties: ClassVar[List[str]] = ["id", "name", "parameters", "observations", "evaluatedAfterSeconds", "closeSteps", "expected"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$/")
        return value

    @field_validator('name', mode="before")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"\S", value):
            raise ValueError(r"must validate the regular expression /\S/")
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
        """Create an instance of ConfigurationScenarioBindingRegressionCase from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in observations (list)
        _items = []
        if self.observations:
            for _item_observations in self.observations:
                if _item_observations:
                    _items.append(_item_observations.to_dict())
            _dict['observations'] = _items
        # override the default output from pydantic by calling `to_dict()` of expected
        if self.expected:
            _dict['expected'] = self.expected.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioBindingRegressionCase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "name": obj.get("name"),
            "parameters": obj.get("parameters"),
            "observations": [ConfigurationScenarioBindingRegressionObservation.from_dict(_item) for _item in obj["observations"]] if obj.get("observations") is not None else None,
            "evaluatedAfterSeconds": obj.get("evaluatedAfterSeconds"),
            "closeSteps": obj.get("closeSteps"),
            "expected": ConfigurationScenarioBindingRegressionExpected.from_dict(obj["expected"]) if obj.get("expected") is not None else None
        }.items() if key in obj})
        return _obj
