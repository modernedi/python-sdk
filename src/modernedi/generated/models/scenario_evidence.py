# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from modernedi.generated.models.scenario_evidence_check import ScenarioEvidenceCheck
from modernedi.generated.models.scenario_evidence_counts import ScenarioEvidenceCounts
from modernedi.generated.models.scenario_evidence_reference import ScenarioEvidenceReference
from modernedi.generated.models.scenario_evidence_step import ScenarioEvidenceStep
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidence(BaseModel):
    """
    ScenarioEvidence
    """ # noqa: E501
    kind: StrictStr
    counts: ScenarioEvidenceCounts
    steps: List[ScenarioEvidenceStep]
    checks: List[ScenarioEvidenceCheck]
    references: List[ScenarioEvidenceReference]
    __properties: ClassVar[List[str]] = ["kind", "counts", "steps", "checks", "references"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['graph']):
            raise ValueError("must be one of enum values ('graph')")
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
        """Create an instance of ScenarioEvidence from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of counts
        if self.counts:
            _dict['counts'] = self.counts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in checks (list)
        _items = []
        if self.checks:
            for _item_checks in self.checks:
                if _item_checks:
                    _items.append(_item_checks.to_dict())
            _dict['checks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in references (list)
        _items = []
        if self.references:
            for _item_references in self.references:
                if _item_references:
                    _items.append(_item_references.to_dict())
            _dict['references'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidence from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "kind": obj.get("kind"),
            "counts": ScenarioEvidenceCounts.from_dict(obj["counts"]) if obj.get("counts") is not None else None,
            "steps": [ScenarioEvidenceStep.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "checks": [ScenarioEvidenceCheck.from_dict(_item) for _item in obj["checks"]] if obj.get("checks") is not None else None,
            "references": [ScenarioEvidenceReference.from_dict(_item) for _item in obj["references"]] if obj.get("references") is not None else None
        }.items() if key in obj})
        return _obj
