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

class MappedOutputWebhookStatus(BaseModel):
    """
    Per-partner HTTPS push configuration and last observed delivery attempt.
    """ # noqa: E501
    partner_id: StrictInt = Field(description="Stable workspace-scoped partner id whose mapped outputs use this webhook.", alias="partnerId")
    enabled: StrictBool = Field(description="Whether ModernEDI currently attempts HTTPS push delivery for this partner.")
    endpoint_url: Optional[StrictStr] = Field(default=None, description="Configured public HTTPS destination, or `null` when no endpoint has been stored.", alias="endpointUrl")
    signing_secret_configured: StrictBool = Field(description="Whether ModernEDI has a secret for signing webhook requests; the full secret is never returned here.", alias="signingSecretConfigured")
    signing_secret_last_four: Optional[StrictStr] = Field(default=None, description="Last four characters only; the signing secret is never returned.", alias="signingSecretLastFour")
    activated_at: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="activatedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    last_delivery_attempt_at: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="lastDeliveryAttemptAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    last_delivery_success_at: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="lastDeliverySuccessAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    last_delivery_status_code: Optional[StrictInt] = Field(default=None, description="Most recent webhook HTTP response status, or `null` before a response has been recorded.", alias="lastDeliveryStatusCode")
    last_delivery_error: Optional[StrictStr] = Field(default=None, description="Safe most-recent delivery error, or `null` when the latest attempt succeeded or none has occurred.", alias="lastDeliveryError")
    created_at: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="createdAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    last_updated_at: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="lastUpdatedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    etag: StrictStr = Field(description="Quoted SHA-256 configuration ETag, also returned in the HTTP `ETag` header.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["partnerId", "enabled", "endpointUrl", "signingSecretConfigured", "signingSecretLastFour", "activatedAt", "lastDeliveryAttemptAt", "lastDeliverySuccessAt", "lastDeliveryStatusCode", "lastDeliveryError", "createdAt", "lastUpdatedAt", "etag"]

    @field_validator('activated_at', mode="before")
    def activated_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('last_delivery_attempt_at', mode="before")
    def last_delivery_attempt_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('last_delivery_success_at', mode="before")
    def last_delivery_success_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('created_at', mode="before")
    def created_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('last_updated_at', mode="before")
    def last_updated_at_validate_regular_expression(cls, value):
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
        """Create an instance of MappedOutputWebhookStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "etag",
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

        # set to None if endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_url is None and "endpoint_url" in self.model_fields_set:
            _dict['endpointUrl'] = None

        # set to None if signing_secret_last_four (nullable) is None
        # and model_fields_set contains the field
        if self.signing_secret_last_four is None and "signing_secret_last_four" in self.model_fields_set:
            _dict['signingSecretLastFour'] = None

        # set to None if activated_at (nullable) is None
        # and model_fields_set contains the field
        if self.activated_at is None and "activated_at" in self.model_fields_set:
            _dict['activatedAt'] = None

        # set to None if last_delivery_attempt_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_delivery_attempt_at is None and "last_delivery_attempt_at" in self.model_fields_set:
            _dict['lastDeliveryAttemptAt'] = None

        # set to None if last_delivery_success_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_delivery_success_at is None and "last_delivery_success_at" in self.model_fields_set:
            _dict['lastDeliverySuccessAt'] = None

        # set to None if last_delivery_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.last_delivery_status_code is None and "last_delivery_status_code" in self.model_fields_set:
            _dict['lastDeliveryStatusCode'] = None

        # set to None if last_delivery_error (nullable) is None
        # and model_fields_set contains the field
        if self.last_delivery_error is None and "last_delivery_error" in self.model_fields_set:
            _dict['lastDeliveryError'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['createdAt'] = None

        # set to None if last_updated_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_at is None and "last_updated_at" in self.model_fields_set:
            _dict['lastUpdatedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappedOutputWebhookStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "partnerId": obj.get("partnerId"),
            "enabled": obj.get("enabled"),
            "endpointUrl": obj.get("endpointUrl"),
            "signingSecretConfigured": obj.get("signingSecretConfigured"),
            "signingSecretLastFour": obj.get("signingSecretLastFour"),
            "activatedAt": obj.get("activatedAt"),
            "lastDeliveryAttemptAt": obj.get("lastDeliveryAttemptAt"),
            "lastDeliverySuccessAt": obj.get("lastDeliverySuccessAt"),
            "lastDeliveryStatusCode": obj.get("lastDeliveryStatusCode"),
            "lastDeliveryError": obj.get("lastDeliveryError"),
            "createdAt": obj.get("createdAt"),
            "lastUpdatedAt": obj.get("lastUpdatedAt"),
            "etag": obj.get("etag")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
