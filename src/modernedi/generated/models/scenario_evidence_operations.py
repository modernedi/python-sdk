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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.scenario_evidence_failure import ScenarioEvidenceFailure
from modernedi.generated.models.scenario_evidence_successful_transition import ScenarioEvidenceSuccessfulTransition
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceOperations(BaseModel):
    """
    ScenarioEvidenceOperations
    """ # noqa: E501
    total: Annotated[int, Field(le=256, strict=True, ge=1)]
    succeeded: Annotated[int, Field(le=256, strict=True, ge=1)]
    failed: Annotated[int, Field(le=256, strict=True, ge=0)]
    successful_transitions: Annotated[List[ScenarioEvidenceSuccessfulTransition], Field(max_length=256)] = Field(alias="successfulTransitions")
    failures: Annotated[List[ScenarioEvidenceFailure], Field(max_length=256)]
    __properties: ClassVar[List[str]] = ["total", "succeeded", "failed", "successfulTransitions", "failures"]

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
        """Create an instance of ScenarioEvidenceOperations from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in successful_transitions (list)
        _items = []
        if self.successful_transitions:
            for _item_successful_transitions in self.successful_transitions:
                if _item_successful_transitions:
                    _items.append(_item_successful_transitions.to_dict())
            _dict['successfulTransitions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in failures (list)
        _items = []
        if self.failures:
            for _item_failures in self.failures:
                if _item_failures:
                    _items.append(_item_failures.to_dict())
            _dict['failures'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceOperations from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "total": obj.get("total"),
            "succeeded": obj.get("succeeded"),
            "failed": obj.get("failed"),
            "successfulTransitions": [ScenarioEvidenceSuccessfulTransition.from_dict(_item) for _item in obj["successfulTransitions"]] if obj.get("successfulTransitions") is not None else None,
            "failures": [ScenarioEvidenceFailure.from_dict(_item) for _item in obj["failures"]] if obj.get("failures") is not None else None
        }.items() if key in obj})
        return _obj
