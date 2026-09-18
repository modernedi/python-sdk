# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict
from modernedi.generated.models.scenario_evidence import ScenarioEvidence
from modernedi.generated.models.scenario_evidence_binding import ScenarioEvidenceBinding
from modernedi.generated.models.scenario_evidence_claim import ScenarioEvidenceClaim
from modernedi.generated.models.scenario_evidence_operations import ScenarioEvidenceOperations
from modernedi.generated.models.scenario_evidence_run import ScenarioEvidenceRun
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceReport(BaseModel):
    """
    ScenarioEvidenceReport
    """ # noqa: E501
    api_version: StrictStr = Field(alias="apiVersion")
    created_at: str = Field(alias="createdAt")
    claim: ScenarioEvidenceClaim
    run: ScenarioEvidenceRun
    binding: ScenarioEvidenceBinding
    operations: ScenarioEvidenceOperations
    evidence: ScenarioEvidence
    __properties: ClassVar[List[str]] = ["apiVersion", "createdAt", "claim", "run", "binding", "operations", "evidence"]

    @field_validator('api_version')
    def api_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['modernedi.com/scenario-evidence-report/v1']):
            raise ValueError("must be one of enum values ('modernedi.com/scenario-evidence-report/v1')")
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
        """Create an instance of ScenarioEvidenceReport from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of claim
        if self.claim:
            _dict['claim'] = self.claim.to_dict()
        # override the default output from pydantic by calling `to_dict()` of run
        if self.run:
            _dict['run'] = self.run.to_dict()
        # override the default output from pydantic by calling `to_dict()` of binding
        if self.binding:
            _dict['binding'] = self.binding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operations
        if self.operations:
            _dict['operations'] = self.operations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of evidence
        if self.evidence:
            _dict['evidence'] = self.evidence.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "apiVersion": obj.get("apiVersion"),
            "createdAt": obj.get("createdAt"),
            "claim": ScenarioEvidenceClaim.from_dict(obj["claim"]) if obj.get("claim") is not None else None,
            "run": ScenarioEvidenceRun.from_dict(obj["run"]) if obj.get("run") is not None else None,
            "binding": ScenarioEvidenceBinding.from_dict(obj["binding"]) if obj.get("binding") is not None else None,
            "operations": ScenarioEvidenceOperations.from_dict(obj["operations"]) if obj.get("operations") is not None else None,
            "evidence": ScenarioEvidence.from_dict(obj["evidence"]) if obj.get("evidence") is not None else None
        }.items() if key in obj})
        return _obj
