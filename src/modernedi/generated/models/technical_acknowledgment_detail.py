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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.technical_acknowledgment_outcome import TechnicalAcknowledgmentOutcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TechnicalAcknowledgmentDetail(BaseModel):
    """
    Metadata for a stored X12 technical acknowledgment or downstream HTTP response. Fetch the indexed document for the body.
    """ # noqa: E501
    sent: Optional[StrictBool] = Field(description="True when ModernEDI sent the technical acknowledgment; false when it received one; `null` when unknown.")
    timestamp: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    response_status_code: Optional[StrictInt] = Field(description="Downstream HTTP response status code, or `null` when no raw transport response was retained.", alias="responseStatusCode", json_schema_extra={"examples": [200]})
    partner_configuration_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(description="Lowercase SHA-256 of the exact partner runtime configuration recorded for this transaction, receipt, or acknowledgment. It is `null` for legacy rows written before configuration stamping. Scenario verification accepts persisted evidence only when this value exactly matches the partner configuration frozen into the applied binding. ", alias="partnerConfigurationSha256", json_schema_extra={"examples": ["0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"]})
    outcome: Optional[TechnicalAcknowledgmentOutcome] = Field(description="Parsed TA1 result, or `null` when the retained technical-acknowledgment record has no TA1 X12 body.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["sent", "timestamp", "responseStatusCode", "partnerConfigurationSha256", "outcome"]

    @field_validator('timestamp', mode="before")
    def timestamp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('partner_configuration_sha256', mode="before")
    def partner_configuration_sha256_validate_regular_expression(cls, value):
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
        """Create an instance of TechnicalAcknowledgmentDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of outcome
        if self.outcome:
            _dict['outcome'] = self.outcome.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if sent (nullable) is None
        # and model_fields_set contains the field
        if self.sent is None and "sent" in self.model_fields_set:
            _dict['sent'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if response_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.response_status_code is None and "response_status_code" in self.model_fields_set:
            _dict['responseStatusCode'] = None

        # set to None if partner_configuration_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.partner_configuration_sha256 is None and "partner_configuration_sha256" in self.model_fields_set:
            _dict['partnerConfigurationSha256'] = None

        # set to None if outcome (nullable) is None
        # and model_fields_set contains the field
        if self.outcome is None and "outcome" in self.model_fields_set:
            _dict['outcome'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TechnicalAcknowledgmentDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "sent": obj.get("sent"),
            "timestamp": obj.get("timestamp"),
            "responseStatusCode": obj.get("responseStatusCode"),
            "partnerConfigurationSha256": obj.get("partnerConfigurationSha256"),
            "outcome": TechnicalAcknowledgmentOutcome.from_dict(obj["outcome"]) if obj.get("outcome") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
