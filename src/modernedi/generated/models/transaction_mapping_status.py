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
from modernedi.generated.models.transaction_mapping_attempt import TransactionMappingAttempt
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionMappingStatus(BaseModel):
    """
    TransactionMappingStatus
    """ # noqa: E501
    status: StrictStr = Field(description="Consolidated mapping outcome. `NOT_RECORDED` means no mapping runtime result was found; it does not claim that a map ran successfully. `UNAVAILABLE` means mapping telemetry could not be read while this response was built. It is fail-soft, has `failureCount: 0`, and does not by itself set `needsAttention`; retry before drawing a conclusion. `RECOVERED` means earlier failures were resolved by a later successful attempt. `COMPLETED_WITH_ERRORS` means at least one attempt succeeded while another failure remains unresolved. ")
    latest_attempt_at: Optional[str] = Field(description="Timestamp of the latest mapping attempt or fallback post-process status.", alias="latestAttemptAt")
    failure_count: Annotated[int, Field(strict=True, ge=0)] = Field(description="Number of unresolved mapping failures for this transaction.", alias="failureCount")
    attempts: List[TransactionMappingAttempt] = Field(description="Mapping attempts in reverse chronological order. This is empty when only fallback post-process status is available.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["status", "latestAttemptAt", "failureCount", "attempts"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['NOT_RECORDED', 'UNAVAILABLE', 'SUCCEEDED', 'FAILED', 'COMPLETED_WITH_ERRORS', 'RECOVERED']):
            raise ValueError("must be one of enum values ('NOT_RECORDED', 'UNAVAILABLE', 'SUCCEEDED', 'FAILED', 'COMPLETED_WITH_ERRORS', 'RECOVERED')")
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
        """Create an instance of TransactionMappingStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in attempts (list)
        _items = []
        if self.attempts:
            for _item_attempts in self.attempts:
                if _item_attempts:
                    _items.append(_item_attempts.to_dict())
            _dict['attempts'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if latest_attempt_at (nullable) is None
        # and model_fields_set contains the field
        if self.latest_attempt_at is None and "latest_attempt_at" in self.model_fields_set:
            _dict['latestAttemptAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionMappingStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "status": obj.get("status"),
            "latestAttemptAt": obj.get("latestAttemptAt"),
            "failureCount": obj.get("failureCount"),
            "attempts": [TransactionMappingAttempt.from_dict(_item) for _item in obj["attempts"]] if obj.get("attempts") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
