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
from uuid import UUID
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from modernedi.generated.models.transaction_replay_error import TransactionReplayError
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionReplay(BaseModel):
    """
    Persisted audit and lifecycle state for one transaction replay.
    """ # noqa: E501
    id: UUID = Field(description="Globally unique replay identifier used to correlate regenerated mapping attempts.")
    status: StrictStr = Field(description="Current replay lifecycle; a synchronous success normally returns `succeeded`.")
    environment: TransactionEnvironmentValue
    message_id: StrictStr = Field(description="Source inbound AS2 Message-Id replayed by this operation.", alias="messageId")
    transaction_key: StrictStr = Field(description="Source transaction key within the message replayed by this operation.", alias="transactionKey")
    mode: StrictStr = Field(description="Mapping revision policy; public replays always use the maps currently published.")
    delivery: StrictStr = Field(description="Delivery boundary; public replay outputs are returned in the response and never queued or pushed.")
    reason: Optional[StrictStr] = Field(description="Caller-supplied operator context, or `null` when no reason was provided.")
    requested_by_api_key_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="Internal id of the scoped Integration API key that requested the replay.", alias="requestedByApiKeyId")
    attempts: Annotated[int, Field(strict=True, ge=1)] = Field(description="Number of replay execution attempts recorded for this request.")
    requested_at: str = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`.", alias="requestedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    started_at: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="startedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    completed_at: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="completedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    error: Optional[TransactionReplayError]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "status", "environment", "messageId", "transactionKey", "mode", "delivery", "reason", "requestedByApiKeyId", "attempts", "requestedAt", "startedAt", "completedAt", "error"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['succeeded', 'processing', 'failed']):
            raise ValueError("must be one of enum values ('succeeded', 'processing', 'failed')")
        return value

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['current_maps']):
            raise ValueError("must be one of enum values ('current_maps')")
        return value

    @field_validator('delivery')
    def delivery_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['response_only']):
            raise ValueError("must be one of enum values ('response_only')")
        return value

    @field_validator('requested_at', mode="before")
    def requested_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('started_at', mode="before")
    def started_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('completed_at', mode="before")
    def completed_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
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
        """Create an instance of TransactionReplay from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_unset=True,
        )
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        # set to None if started_at (nullable) is None
        # and model_fields_set contains the field
        if self.started_at is None and "started_at" in self.model_fields_set:
            _dict['startedAt'] = None

        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completedAt'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionReplay from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "status": obj.get("status"),
            "environment": obj.get("environment"),
            "messageId": obj.get("messageId"),
            "transactionKey": obj.get("transactionKey"),
            "mode": obj.get("mode"),
            "delivery": obj.get("delivery"),
            "reason": obj.get("reason"),
            "requestedByApiKeyId": obj.get("requestedByApiKeyId"),
            "attempts": obj.get("attempts"),
            "requestedAt": obj.get("requestedAt"),
            "startedAt": obj.get("startedAt"),
            "completedAt": obj.get("completedAt"),
            "error": TransactionReplayError.from_dict(obj["error"]) if obj.get("error") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
