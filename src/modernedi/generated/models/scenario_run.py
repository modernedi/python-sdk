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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.scenario_definition_identity import ScenarioDefinitionIdentity
from modernedi.generated.models.scenario_graph_check import ScenarioGraphCheck
from modernedi.generated.models.scenario_graph_counts import ScenarioGraphCounts
from modernedi.generated.models.scenario_graph_execution import ScenarioGraphExecution
from modernedi.generated.models.scenario_graph_guidance import ScenarioGraphGuidance
from modernedi.generated.models.scenario_graph_retry import ScenarioGraphRetry
from modernedi.generated.models.scenario_graph_step import ScenarioGraphStep
from modernedi.generated.models.start_scenario_run_request_binding import StartScenarioRunRequestBinding
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioRun(BaseModel):
    """
    ScenarioRun
    """ # noqa: E501
    api_version: StrictStr = Field(alias="apiVersion")
    kind: StrictStr
    id: Annotated[str, Field(strict=True)]
    origin: StrictStr = Field(description="Server-owned run origin. system_managed is reserved for the managed implementation-verification route; tenant_applied identifies an exact tenant-applied binding start.")
    binding: StartScenarioRunRequestBinding
    definition: ScenarioDefinitionIdentity
    environment: StrictStr
    adapter_id: StrictStr = Field(alias="adapterId")
    execution: ScenarioGraphExecution
    status: StrictStr
    outcome: StrictStr
    phase: StrictStr
    revision: Annotated[int, Field(strict=True, ge=0)]
    etag: Annotated[str, Field(strict=True)] = Field(description="Opaque quoted strong ETag for one tenant-scoped run revision. Clients must return the current value unchanged; its fields are not client authority.", json_schema_extra={"examples": ["\"scenario-run:v1:42:cnVuLTUwMDdkYmYzLWYxMTUtNGNhYy04NTMwLTE4OGZiNDMyNmM0NQ:1\""]})
    started_at: Optional[str] = Field(alias="startedAt")
    completed_at: Optional[str] = Field(alias="completedAt")
    last_updated_at: Optional[str] = Field(alias="lastUpdatedAt")
    counts: ScenarioGraphCounts
    retry: ScenarioGraphRetry
    guidance: ScenarioGraphGuidance
    steps: List[ScenarioGraphStep]
    checks: List[ScenarioGraphCheck]
    __properties: ClassVar[List[str]] = ["apiVersion", "kind", "id", "origin", "binding", "definition", "environment", "adapterId", "execution", "status", "outcome", "phase", "revision", "etag", "startedAt", "completedAt", "lastUpdatedAt", "counts", "retry", "guidance", "steps", "checks"]

    @field_validator('api_version')
    def api_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['modernedi.com/scenario-run-response/v1']):
            raise ValueError("must be one of enum values ('modernedi.com/scenario-run-response/v1')")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['graph']):
            raise ValueError("must be one of enum values ('graph')")
        return value

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^run-[0-9a-f-]+$", value):
            raise ValueError(r"must validate the regular expression /^run-[0-9a-f-]+$/")
        return value

    @field_validator('origin')
    def origin_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['system_managed', 'tenant_applied']):
            raise ValueError("must be one of enum values ('system_managed', 'tenant_applied')")
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

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['active', 'completed', 'cancelled']):
            raise ValueError("must be one of enum values ('active', 'completed', 'cancelled')")
        return value

    @field_validator('outcome')
    def outcome_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['waiting', 'passed', 'failed', 'inconclusive']):
            raise ValueError("must be one of enum values ('waiting', 'passed', 'failed', 'inconclusive')")
        return value

    @field_validator('phase')
    def phase_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['observing', 'complete', 'binding_drifted', 'reconciliation_pending']):
            raise ValueError("must be one of enum values ('observing', 'complete', 'binding_drifted', 'reconciliation_pending')")
        return value

    @field_validator('etag', mode="before")
    def etag_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\"scenario-run:v1:[1-9][0-9]*:[A-Za-z0-9_-]+:(?:0|[1-9][0-9]*)\"$", value):
            raise ValueError(r"must validate the regular expression /^\"scenario-run:v1:[1-9][0-9]*:[A-Za-z0-9_-]+:(?:0|[1-9][0-9]*)\"$/")
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
        """Create an instance of ScenarioRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of binding
        if self.binding:
            _dict['binding'] = self.binding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of definition
        if self.definition:
            _dict['definition'] = self.definition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of execution
        if self.execution:
            _dict['execution'] = self.execution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of counts
        if self.counts:
            _dict['counts'] = self.counts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retry
        if self.retry:
            _dict['retry'] = self.retry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of guidance
        if self.guidance:
            _dict['guidance'] = self.guidance.to_dict()
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
        # set to None if started_at (nullable) is None
        # and model_fields_set contains the field
        if self.started_at is None and "started_at" in self.model_fields_set:
            _dict['startedAt'] = None

        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completedAt'] = None

        # set to None if last_updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_at is None and "last_updated_at" in self.model_fields_set:
            _dict['lastUpdatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "apiVersion": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "id": obj.get("id"),
            "origin": obj.get("origin"),
            "binding": StartScenarioRunRequestBinding.from_dict(obj["binding"]) if obj.get("binding") is not None else None,
            "definition": ScenarioDefinitionIdentity.from_dict(obj["definition"]) if obj.get("definition") is not None else None,
            "environment": obj.get("environment"),
            "adapterId": obj.get("adapterId"),
            "execution": ScenarioGraphExecution.from_dict(obj["execution"]) if obj.get("execution") is not None else None,
            "status": obj.get("status"),
            "outcome": obj.get("outcome"),
            "phase": obj.get("phase"),
            "revision": obj.get("revision"),
            "etag": obj.get("etag"),
            "startedAt": obj.get("startedAt"),
            "completedAt": obj.get("completedAt"),
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "counts": ScenarioGraphCounts.from_dict(obj["counts"]) if obj.get("counts") is not None else None,
            "retry": ScenarioGraphRetry.from_dict(obj["retry"]) if obj.get("retry") is not None else None,
            "guidance": ScenarioGraphGuidance.from_dict(obj["guidance"]) if obj.get("guidance") is not None else None,
            "steps": [ScenarioGraphStep.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "checks": [ScenarioGraphCheck.from_dict(_item) for _item in obj["checks"]] if obj.get("checks") is not None else None
        }.items() if key in obj})
        return _obj
