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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappedOutputWebhookTestResponse(BaseModel):
    """
    Result of one synthetic webhook connectivity attempt. This response never represents or changes a real mapped output.
    """ # noqa: E501
    success: StrictBool = Field(description="The ModernEDI test operation completed. This does not mean the destination accepted the event; inspect `delivered`.")
    synthetic: StrictBool = Field(description="Always true so this result cannot be mistaken for production mapped-output delivery.")
    event: StrictStr = Field(description="Synthetic event name sent in both the signed body and `X-ModernEDI-Event` header.")
    delivery_id: StrictStr = Field(description="Synthetic `test_`-prefixed delivery correlation id. It is not a mapped-output queue id or receipt handle.", alias="deliveryId")
    request_id: StrictStr = Field(description="Request correlation id returned in `X-Request-Id` and included in the signed synthetic event.", alias="requestId")
    attempted_at: str = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`.", alias="attemptedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    attempted: StrictBool = Field(description="Always true because ModernEDI invoked the validated delivery path. A null `statusCode` means the path failed before an HTTP response was received.")
    delivered: StrictBool = Field(description="True only when the destination returned HTTP 2xx. A `200` from this ModernEDI API operation can still contain `delivered: false`. ")
    status_code: Optional[StrictInt] = Field(description="Destination HTTP status, or null when public-address validation, DNS, connection, TLS, or timeout failure prevented an HTTP response. ", alias="statusCode")
    error: Optional[StrictStr] = Field(description="Safe delivery failure summary, or null when `delivered` is true.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "synthetic", "event", "deliveryId", "requestId", "attemptedAt", "attempted", "delivered", "statusCode", "error"]

    @field_validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['mapped_output.test']):
            raise ValueError("must be one of enum values ('mapped_output.test')")
        return value

    @field_validator('attempted_at', mode="before")
    def attempted_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of MappedOutputWebhookTestResponse from a JSON string"""
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

        # set to None if status_code (nullable) is None
        # and model_fields_set contains the field
        if self.status_code is None and "status_code" in self.model_fields_set:
            _dict['statusCode'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappedOutputWebhookTestResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "synthetic": obj.get("synthetic"),
            "event": obj.get("event"),
            "deliveryId": obj.get("deliveryId"),
            "requestId": obj.get("requestId"),
            "attemptedAt": obj.get("attemptedAt"),
            "attempted": obj.get("attempted"),
            "delivered": obj.get("delivered"),
            "statusCode": obj.get("statusCode"),
            "error": obj.get("error")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
