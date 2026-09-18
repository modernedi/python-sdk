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
from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_apply_operation_status import ConfigurationApplyOperationStatus
from modernedi.generated.models.configuration_changed_by import ConfigurationChangedBy
from modernedi.generated.models.configuration_plan_summary import ConfigurationPlanSummary
from modernedi.generated.models.runtime_publication import RuntimePublication
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationApplyOperationHistoryEntry(BaseModel):
    """
    Compact workspace change-history entry; use the operation endpoint for its full change list.
    """ # noqa: E501
    operation_id: Annotated[str, Field(strict=True)] = Field(description="Immutable public id formed as `apply-` followed by a canonical lowercase UUID.", alias="operationId", json_schema_extra={"examples": ["apply-3ee360bd-7e41-4c55-80f8-3f1e5839804d"]})
    changed_by: ConfigurationChangedBy = Field(alias="changedBy")
    status: ConfigurationApplyOperationStatus
    desired_bundle_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="desiredBundleSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    plan_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="planSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    base_snapshot_etag: Annotated[str, Field(strict=True)] = Field(description="Exact successful-plan snapshot ETag supplied in `If-Match`.", alias="baseSnapshotEtag")
    applied_snapshot_etag: Annotated[str, Field(strict=True)] = Field(description="Strong quoted SHA-256 identity of the committed post-apply configuration snapshot. It is available in both PENDING and SUCCEEDED operations because PENDING publication occurs only after database commit.", alias="appliedSnapshotEtag")
    runtime_configuration_revision: Annotated[int, Field(strict=True, ge=0)] = Field(description="Tenant-wide runtime configuration revision committed by the aggregate database transaction.", alias="runtimeConfigurationRevision")
    summary: ConfigurationPlanSummary
    runtime_publication: RuntimePublication = Field(alias="runtimePublication")
    requested_at: str = Field(description="UTC instant when ModernEDI first accepted this idempotency key and semantic apply request.", alias="requestedAt")
    committed_at: str = Field(description="UTC instant when the aggregate database transaction committed.", alias="committedAt")
    completed_at: Optional[str] = Field(description="UTC instant when runtime publication reached its terminal state, or null while `status` is `PENDING`.", alias="completedAt")
    __properties: ClassVar[List[str]] = ["operationId", "changedBy", "status", "desiredBundleSha256", "planSha256", "baseSnapshotEtag", "appliedSnapshotEtag", "runtimeConfigurationRevision", "summary", "runtimePublication", "requestedAt", "committedAt", "completedAt"]

    @field_validator('operation_id', mode="before")
    def operation_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^apply-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(r"must validate the regular expression /^apply-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/")
        return value

    @field_validator('desired_bundle_sha256', mode="before")
    def desired_bundle_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('plan_sha256', mode="before")
    def plan_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('base_snapshot_etag', mode="before")
    def base_snapshot_etag_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\"[0-9a-f]{64}\"$", value):
            raise ValueError(r"must validate the regular expression /^\"[0-9a-f]{64}\"$/")
        return value

    @field_validator('applied_snapshot_etag', mode="before")
    def applied_snapshot_etag_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\"[0-9a-f]{64}\"$", value):
            raise ValueError(r"must validate the regular expression /^\"[0-9a-f]{64}\"$/")
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
        """Create an instance of ConfigurationApplyOperationHistoryEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of changed_by
        if self.changed_by:
            _dict['changedBy'] = self.changed_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of runtime_publication
        if self.runtime_publication:
            _dict['runtimePublication'] = self.runtime_publication.to_dict()
        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationApplyOperationHistoryEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "operationId": obj.get("operationId"),
            "changedBy": ConfigurationChangedBy.from_dict(obj["changedBy"]) if obj.get("changedBy") is not None else None,
            "status": obj.get("status"),
            "desiredBundleSha256": obj.get("desiredBundleSha256"),
            "planSha256": obj.get("planSha256"),
            "baseSnapshotEtag": obj.get("baseSnapshotEtag"),
            "appliedSnapshotEtag": obj.get("appliedSnapshotEtag"),
            "runtimeConfigurationRevision": obj.get("runtimeConfigurationRevision"),
            "summary": ConfigurationPlanSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "runtimePublication": RuntimePublication.from_dict(obj["runtimePublication"]) if obj.get("runtimePublication") is not None else None,
            "requestedAt": obj.get("requestedAt"),
            "committedAt": obj.get("committedAt"),
            "completedAt": obj.get("completedAt")
        }.items() if key in obj})
        return _obj
