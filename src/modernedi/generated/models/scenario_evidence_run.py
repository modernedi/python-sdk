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
from typing_extensions import Annotated
from modernedi.generated.models.scenario_definition_identity import ScenarioDefinitionIdentity
from modernedi.generated.models.scenario_evidence_run_binding import ScenarioEvidenceRunBinding
from modernedi.generated.models.scenario_run_actor import ScenarioRunActor
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceRun(BaseModel):
    """
    ScenarioEvidenceRun
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)]
    status: StrictStr
    outcome: StrictStr
    phase: Annotated[str, Field(strict=True)]
    revision: Annotated[int, Field(strict=True, ge=0)]
    environment: StrictStr
    adapter_id: StrictStr = Field(alias="adapterId")
    definition: ScenarioDefinitionIdentity
    binding: ScenarioEvidenceRunBinding
    started_by: ScenarioRunActor = Field(alias="startedBy")
    started_at: str = Field(alias="startedAt")
    completed_at: str = Field(alias="completedAt")
    last_updated_at: str = Field(alias="lastUpdatedAt")
    __properties: ClassVar[List[str]] = ["id", "status", "outcome", "phase", "revision", "environment", "adapterId", "definition", "binding", "startedBy", "startedAt", "completedAt", "lastUpdatedAt"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^run-[0-9a-f-]+$", value):
            raise ValueError(r"must validate the regular expression /^run-[0-9a-f-]+$/")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['completed', 'cancelled']):
            raise ValueError("must be one of enum values ('completed', 'cancelled')")
        return value

    @field_validator('outcome')
    def outcome_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['passed', 'failed', 'inconclusive']):
            raise ValueError("must be one of enum values ('passed', 'failed', 'inconclusive')")
        return value

    @field_validator('phase', mode="before")
    def phase_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[a-z][a-z0-9_]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_]*$/")
        return value

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['production', 'test']):
            raise ValueError("must be one of enum values ('production', 'test')")
        return value

    @field_validator('adapter_id')
    def adapter_id_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['scenario-graph-interpreter-v1']):
            raise ValueError("must be one of enum values ('scenario-graph-interpreter-v1')")
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
        """Create an instance of ScenarioEvidenceRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of started_by
        if self.started_by:
            _dict['startedBy'] = self.started_by.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "status": obj.get("status"),
            "outcome": obj.get("outcome"),
            "phase": obj.get("phase"),
            "revision": obj.get("revision"),
            "environment": obj.get("environment"),
            "adapterId": obj.get("adapterId"),
            "definition": ScenarioDefinitionIdentity.from_dict(obj["definition"]) if obj.get("definition") is not None else None,
            "binding": ScenarioEvidenceRunBinding.from_dict(obj["binding"]) if obj.get("binding") is not None else None,
            "startedBy": ScenarioRunActor.from_dict(obj["startedBy"]) if obj.get("startedBy") is not None else None,
            "startedAt": obj.get("startedAt"),
            "completedAt": obj.get("completedAt"),
            "lastUpdatedAt": obj.get("lastUpdatedAt")
        }.items() if key in obj})
        return _obj
