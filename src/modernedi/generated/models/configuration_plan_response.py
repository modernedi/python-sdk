# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_plan_affected_run import ConfigurationPlanAffectedRun
from modernedi.generated.models.configuration_plan_affected_scenario import ConfigurationPlanAffectedScenario
from modernedi.generated.models.configuration_plan_diagnostic import ConfigurationPlanDiagnostic
from modernedi.generated.models.configuration_plan_operation import ConfigurationPlanOperation
from modernedi.generated.models.configuration_plan_summary import ConfigurationPlanSummary
from modernedi.generated.models.configuration_plan_validation_context import ConfigurationPlanValidationContext
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationPlanResponse(BaseModel):
    """
    Deterministic read-only comparison between one validated desired bundle and the workspace's current portable AS2, partner, and mapping configuration.
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true` when planning completed, including a plan with semantic errors.")
    applicable: StrictBool = Field(description="Whether the desired configuration passed semantic validation and complete scenario-impact analysis and can therefore receive a `planSha256`.")
    desired_bundle_sha256: Annotated[str, Field(strict=True)] = Field(description="SHA-256 of the submitted canonical `modernedi.json` manifest.", alias="desiredBundleSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    current_snapshot_etag: Annotated[str, Field(strict=True)] = Field(description="Strong quoted SHA-256 identity of the current configuration snapshot used for this comparison.", alias="currentSnapshotEtag")
    runtime_configuration_revision: Annotated[int, Field(strict=True, ge=0)] = Field(description="Tenant-wide runtime configuration revision observed by the same repeatable-read planning transaction.", alias="runtimeConfigurationRevision")
    validation_context: ConfigurationPlanValidationContext = Field(alias="validationContext")
    plan_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(description="Deterministic identity binding desired state, current snapshot, validation context, operations, and scenario impact. Null when `applicable` is false.", alias="planSha256")
    summary: ConfigurationPlanSummary
    operations: List[ConfigurationPlanOperation] = Field(description="Changed resources only, in deterministic dependency-aware display order. Unchanged resources are counted in `summary.unchanged`.")
    diagnostics: List[ConfigurationPlanDiagnostic] = Field(description="Deterministically ordered semantic errors and warnings. Any ERROR makes `applicable` false.")
    scenario_impact_complete: StrictBool = Field(description="Whether ModernEDI safely evaluated every applied scenario binding that could depend on a changed resource. False makes `applicable` false.", alias="scenarioImpactComplete")
    affected_scenarios: List[ConfigurationPlanAffectedScenario] = Field(description="Applied scenario bindings that would require reapplication if these operations were later applied.", alias="affectedScenarios")
    affected_runs: List[ConfigurationPlanAffectedRun] = Field(description="ACTIVE scenario runs pinned to affected binding revisions. Any entry makes the plan inapplicable until the run is cancelled or completed and configuration is planned again.", alias="affectedRuns")
    __properties: ClassVar[List[str]] = ["success", "applicable", "desiredBundleSha256", "currentSnapshotEtag", "runtimeConfigurationRevision", "validationContext", "planSha256", "summary", "operations", "diagnostics", "scenarioImpactComplete", "affectedScenarios", "affectedRuns"]

    @field_validator('desired_bundle_sha256', mode="before")
    def desired_bundle_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('current_snapshot_etag', mode="before")
    def current_snapshot_etag_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\"[0-9a-f]{64}\"$", value):
            raise ValueError(r"must validate the regular expression /^\"[0-9a-f]{64}\"$/")
        return value

    @field_validator('plan_sha256', mode="before")
    def plan_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
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
        """Create an instance of ConfigurationPlanResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of validation_context
        if self.validation_context:
            _dict['validationContext'] = self.validation_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in operations (list)
        _items = []
        if self.operations:
            for _item_operations in self.operations:
                if _item_operations:
                    _items.append(_item_operations.to_dict())
            _dict['operations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in diagnostics (list)
        _items = []
        if self.diagnostics:
            for _item_diagnostics in self.diagnostics:
                if _item_diagnostics:
                    _items.append(_item_diagnostics.to_dict())
            _dict['diagnostics'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in affected_scenarios (list)
        _items = []
        if self.affected_scenarios:
            for _item_affected_scenarios in self.affected_scenarios:
                if _item_affected_scenarios:
                    _items.append(_item_affected_scenarios.to_dict())
            _dict['affectedScenarios'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in affected_runs (list)
        _items = []
        if self.affected_runs:
            for _item_affected_runs in self.affected_runs:
                if _item_affected_runs:
                    _items.append(_item_affected_runs.to_dict())
            _dict['affectedRuns'] = _items
        # set to None if plan_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.plan_sha256 is None and "plan_sha256" in self.model_fields_set:
            _dict['planSha256'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationPlanResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "applicable": obj.get("applicable"),
            "desiredBundleSha256": obj.get("desiredBundleSha256"),
            "currentSnapshotEtag": obj.get("currentSnapshotEtag"),
            "runtimeConfigurationRevision": obj.get("runtimeConfigurationRevision"),
            "validationContext": ConfigurationPlanValidationContext.from_dict(obj["validationContext"]) if obj.get("validationContext") is not None else None,
            "planSha256": obj.get("planSha256"),
            "summary": ConfigurationPlanSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "operations": [ConfigurationPlanOperation.from_dict(_item) for _item in obj["operations"]] if obj.get("operations") is not None else None,
            "diagnostics": [ConfigurationPlanDiagnostic.from_dict(_item) for _item in obj["diagnostics"]] if obj.get("diagnostics") is not None else None,
            "scenarioImpactComplete": obj.get("scenarioImpactComplete"),
            "affectedScenarios": [ConfigurationPlanAffectedScenario.from_dict(_item) for _item in obj["affectedScenarios"]] if obj.get("affectedScenarios") is not None else None,
            "affectedRuns": [ConfigurationPlanAffectedRun.from_dict(_item) for _item in obj["affectedRuns"]] if obj.get("affectedRuns") is not None else None
        }.items() if key in obj})
        return _obj
