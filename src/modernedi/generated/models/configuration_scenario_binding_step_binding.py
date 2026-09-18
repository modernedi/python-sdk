# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

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
from modernedi.generated.models.configuration_scenario_binding_fact_source_binding import ConfigurationScenarioBindingFactSourceBinding
from modernedi.generated.models.configuration_scenario_binding_syntax_tree_reference import ConfigurationScenarioBindingSyntaxTreeReference
from modernedi.generated.models.configuration_scenario_binding_target import ConfigurationScenarioBindingTarget
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioBindingStepBinding(BaseModel):
    """
    Connects one definition step to an executable or observation target and binds every declared semantic fact to an implementation-guide source. syntaxTree is optional while authoring; Apply resolves an exact authoritative syntax-tree artifact before runtime execution.
    """ # noqa: E501
    step_id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="stepId")
    syntax_tree: Optional[ConfigurationScenarioBindingSyntaxTreeReference] = Field(default=None, alias="syntaxTree")
    target: ConfigurationScenarioBindingTarget
    fact_sources: Optional[Annotated[List[ConfigurationScenarioBindingFactSourceBinding], Field(max_length=200)]] = Field(default=None, description="One source for every fact declared by this ScenarioDefinition step. Omission is a deliberate authoring shorthand only when the step declares no facts; canonical Apply materializes an empty array. Server validation otherwise requires exact fact-name coverage. Collection shape, element type, cardinality, normalization, and sensitivity come only from the declaration and are intentionally not duplicated here.", alias="factSources")
    __properties: ClassVar[List[str]] = ["stepId", "syntaxTree", "target", "factSources"]

    @field_validator('step_id', mode="before")
    def step_id_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationScenarioBindingStepBinding from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of syntax_tree
        if self.syntax_tree:
            _dict['syntaxTree'] = self.syntax_tree.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fact_sources (list)
        _items = []
        if self.fact_sources:
            for _item_fact_sources in self.fact_sources:
                if _item_fact_sources:
                    _items.append(_item_fact_sources.to_dict())
            _dict['factSources'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioBindingStepBinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "stepId": obj.get("stepId"),
            "syntaxTree": ConfigurationScenarioBindingSyntaxTreeReference.from_dict(obj["syntaxTree"]) if obj.get("syntaxTree") is not None else None,
            "target": ConfigurationScenarioBindingTarget.from_dict(obj["target"]) if obj.get("target") is not None else None,
            "factSources": [ConfigurationScenarioBindingFactSourceBinding.from_dict(_item) for _item in obj["factSources"]] if obj.get("factSources") is not None else None
        }.items() if key in obj})
        return _obj
