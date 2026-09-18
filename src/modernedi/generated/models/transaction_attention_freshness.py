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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionAttentionFreshness(BaseModel):
    """
    Reconciliation state for the selected environment. Until the first complete sweep, attention-filtered or exact-status-filtered rows and counts can be partial or empty; `complete: false` means an empty result is not proof of zero. An incomplete or failed sweep does not clear previously observed active attention items.
    """ # noqa: E501
    status: StrictStr = Field(description="Reconciliation lifecycle: pending, actively reconciling, current, or stale.")
    complete: StrictBool = Field(description="Whether the currently reported projection is complete and current. This is false while the first sweep is pending, while a refresh is reconciling, or when reconciliation is stale; previously observed active items remain visible during those states. ")
    last_completed_at: Optional[str] = Field(description="UTC instant of the latest completed full attention sweep, or `null` before the first completion.", alias="lastCompletedAt")
    reconciliation_started_at: Optional[str] = Field(description="UTC instant when the current reconciliation began, or `null` when no sweep is running.", alias="reconciliationStartedAt")
    message: Optional[StrictStr] = Field(description="Safe operator-facing freshness or retry guidance; internal errors are not exposed.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["status", "complete", "lastCompletedAt", "reconciliationStartedAt", "message"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pending', 'reconciling', 'current', 'stale']):
            raise ValueError("must be one of enum values ('pending', 'reconciling', 'current', 'stale')")
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
        """Create an instance of TransactionAttentionFreshness from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if last_completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_completed_at is None and "last_completed_at" in self.model_fields_set:
            _dict['lastCompletedAt'] = None

        # set to None if reconciliation_started_at (nullable) is None
        # and model_fields_set contains the field
        if self.reconciliation_started_at is None and "reconciliation_started_at" in self.model_fields_set:
            _dict['reconciliationStartedAt'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionAttentionFreshness from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "status": obj.get("status"),
            "complete": obj.get("complete"),
            "lastCompletedAt": obj.get("lastCompletedAt"),
            "reconciliationStartedAt": obj.get("reconciliationStartedAt"),
            "message": obj.get("message")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
