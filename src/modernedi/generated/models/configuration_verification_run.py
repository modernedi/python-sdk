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
from modernedi.generated.models.configuration_verification_case_result import ConfigurationVerificationCaseResult
from modernedi.generated.models.configuration_verification_identity import ConfigurationVerificationIdentity
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationVerificationRun(BaseModel):
    """
    Durable bounded suite. Results expire after 90 days; only the most recent 200 workspace runs are retained. Freshness is checked on reads.
    """ # noqa: E501
    run_id: Annotated[str, Field(strict=True)] = Field(description="Server-owned verification run identity.", alias="runId")
    status: StrictStr = Field(description="PASSED covers only selected saved cases; it does not establish delivery, partner acceptance or scenario success.")
    created_at: str = Field(description="Server admission time.", alias="createdAt")
    completed_at: Optional[str] = Field(description="Server completion time; null while running.", alias="completedAt")
    applied_operation_id: Optional[StrictStr] = Field(description="Apply operation explicitly linked to this result, or null.", alias="appliedOperationId")
    identity: ConfigurationVerificationIdentity
    cases: Annotated[List[ConfigurationVerificationCaseResult], Field(max_length=100)] = Field(description="Completed case outcomes. Incomplete suites cannot pass.")
    freshness: StrictStr = Field(description="Whether current workspace, evaluator and catalog still match this result.")
    stale_reasons: List[StrictStr] = Field(description="Empty only when current.", alias="staleReasons")
    __properties: ClassVar[List[str]] = ["runId", "status", "createdAt", "completedAt", "appliedOperationId", "identity", "cases", "freshness", "staleReasons"]

    @field_validator('run_id', mode="before")
    def run_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^verify-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(r"must validate the regular expression /^verify-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['RUNNING', 'PASSED', 'FAILED', 'ERROR', 'CANCELLED', 'TIMED_OUT']):
            raise ValueError("must be one of enum values ('RUNNING', 'PASSED', 'FAILED', 'ERROR', 'CANCELLED', 'TIMED_OUT')")
        return value

    @field_validator('freshness')
    def freshness_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CURRENT', 'STALE']):
            raise ValueError("must be one of enum values ('CURRENT', 'STALE')")
        return value

    @field_validator('stale_reasons')
    def stale_reasons_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['EVALUATOR_CHANGED', 'SYNTAX_TREE_CHANGED', 'CONFIGURATION_CHANGED', 'DEPENDENCIES_UNAVAILABLE']):
                raise ValueError("each list item must be one of ('EVALUATOR_CHANGED', 'SYNTAX_TREE_CHANGED', 'CONFIGURATION_CHANGED', 'DEPENDENCIES_UNAVAILABLE')")
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
        """Create an instance of ConfigurationVerificationRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in cases (list)
        _items = []
        if self.cases:
            for _item_cases in self.cases:
                if _item_cases:
                    _items.append(_item_cases.to_dict())
            _dict['cases'] = _items
        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completedAt'] = None

        # set to None if applied_operation_id (nullable) is None
        # and model_fields_set contains the field
        if self.applied_operation_id is None and "applied_operation_id" in self.model_fields_set:
            _dict['appliedOperationId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationVerificationRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "runId": obj.get("runId"),
            "status": obj.get("status"),
            "createdAt": obj.get("createdAt"),
            "completedAt": obj.get("completedAt"),
            "appliedOperationId": obj.get("appliedOperationId"),
            "identity": ConfigurationVerificationIdentity.from_dict(obj["identity"]) if obj.get("identity") is not None else None,
            "cases": [ConfigurationVerificationCaseResult.from_dict(_item) for _item in obj["cases"]] if obj.get("cases") is not None else None,
            "freshness": obj.get("freshness"),
            "staleReasons": obj.get("staleReasons")
        }.items() if key in obj})
        return _obj
