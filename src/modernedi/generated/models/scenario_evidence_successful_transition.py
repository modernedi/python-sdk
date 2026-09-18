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
from modernedi.generated.models.scenario_run_actor import ScenarioRunActor
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceSuccessfulTransition(BaseModel):
    """
    ScenarioEvidenceSuccessfulTransition
    """ # noqa: E501
    operation_id: Annotated[str, Field(strict=True)] = Field(alias="operationId")
    action: Annotated[str, Field(strict=True)]
    disposition: StrictStr
    from_revision: Annotated[int, Field(strict=True, ge=0)] = Field(alias="fromRevision")
    to_revision: Annotated[int, Field(strict=True, ge=0)] = Field(alias="toRevision")
    actor: ScenarioRunActor
    requested_at: str = Field(alias="requestedAt")
    completed_at: str = Field(alias="completedAt")
    __properties: ClassVar[List[str]] = ["operationId", "action", "disposition", "fromRevision", "toRevision", "actor", "requestedAt", "completedAt"]

    @field_validator('operation_id', mode="before")
    def operation_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,95}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9][A-Za-z0-9._:-]{0,95}$/")
        return value

    @field_validator('action', mode="before")
    def action_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[a-z][a-z0-9_]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z][a-z0-9_]*$/")
        return value

    @field_validator('disposition')
    def disposition_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['started', 'advanced', 'reconciled', 'reconciliation_pending', 'binding_drifted', 'cancelled']):
            raise ValueError("must be one of enum values ('started', 'advanced', 'reconciled', 'reconciliation_pending', 'binding_drifted', 'cancelled')")
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
        """Create an instance of ScenarioEvidenceSuccessfulTransition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceSuccessfulTransition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "operationId": obj.get("operationId"),
            "action": obj.get("action"),
            "disposition": obj.get("disposition"),
            "fromRevision": obj.get("fromRevision"),
            "toRevision": obj.get("toRevision"),
            "actor": ScenarioRunActor.from_dict(obj["actor"]) if obj.get("actor") is not None else None,
            "requestedAt": obj.get("requestedAt"),
            "completedAt": obj.get("completedAt")
        }.items() if key in obj})
        return _obj
