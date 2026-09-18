# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_scenario_definition_occurrence_closure import ConfigurationScenarioDefinitionOccurrenceClosure
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionOccurrence(BaseModel):
    """
    How many documents this step may contribute to one run and the rule that says when no more are expected. One observed document is one occurrence. For example, an 850 order can be exactly once while 856 shipment notices can repeat. The server also enforces min <= max.
    """ # noqa: E501
    min: Annotated[int, Field(le=1000, strict=True, ge=0)] = Field(description="Minimum accepted count once a reachable step closes. Zero is a no-document outcome only when expected_count resolves to 0 or branch selection makes the step unreachable; zero alone does not close a stream.")
    max: Annotated[int, Field(le=1000, strict=True, ge=1)] = Field(description="Structural per-step ceiling for authored occurrences. Validate and Apply also enforce one conservative run-state capacity budget across all steps, paired documents, checks, and durable evidence.")
    closure: Optional[ConfigurationScenarioDefinitionOccurrenceClosure] = None
    __properties: ClassVar[List[str]] = ["min", "max", "closure"]

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
        """Create an instance of ConfigurationScenarioDefinitionOccurrence from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of closure
        if self.closure:
            _dict['closure'] = self.closure.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionOccurrence from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "min": obj.get("min"),
            "max": obj.get("max"),
            "closure": ConfigurationScenarioDefinitionOccurrenceClosure.from_dict(obj["closure"]) if obj.get("closure") is not None else None
        }.items() if key in obj})
        return _obj
