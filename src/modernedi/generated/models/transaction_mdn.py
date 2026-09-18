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
from typing_extensions import Annotated
from modernedi.generated.models.transaction_mdn_status import TransactionMdnStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionMdn(BaseModel):
    """
    AS2 message disposition notification (MDN) metadata without its report body. For an outbound document ModernEDI normally requests an asynchronous signed receipt. While that receipt is outstanding this object has `status: pending`; it becomes `overdue` after the platform response deadline, which defaults to one hour after send. A received receipt is accepted as `processed` only after its Original-Message-ID, requested MIC algorithm, returned MIC, and disposition are validated. Review `as2_mdn_attention` before resending; ModernEDI does not resend automatically because an invalid or missing receipt does not prove the partner failed to process the document.
    """ # noqa: E501
    message_id: Optional[StrictStr] = Field(description="Message-ID of the MDN itself. Null while an asynchronous receipt is still pending or overdue.", alias="messageId", json_schema_extra={"examples": ["mdn-850-api"]})
    disposition: Optional[StrictStr] = Field(description="Raw AS2 Disposition field returned by the partner. Use normalized `status` for automation and retain this value for partner troubleshooting.", json_schema_extra={"examples": ["processed"]})
    sent: Optional[StrictBool] = Field(description="True when ModernEDI sent this MDN for an inbound document; false when it received or is awaiting the partner's MDN for an outbound document.")
    timestamp: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    status: TransactionMdnStatus
    asynchronous: Optional[StrictBool] = Field(description="True when the receipt was requested or delivered through the asynchronous Receipt-Delivery-Option callback rather than the original HTTP response.")
    mic_matched: Optional[StrictBool] = Field(description="Whether the partner's Received-content-MIC digest and algorithm matched the canonical content ModernEDI sent. Null while pending or when comparison was not possible.", alias="micMatched")
    received_content_mic: Optional[StrictStr] = Field(description="Partner-supplied Received-content-MIC value, including its algorithm token when present.", alias="receivedContentMic")
    expected_content_mic: Optional[StrictStr] = Field(description="Base64 digest ModernEDI calculated over the exact canonical MIME content sent to the partner.", alias="expectedContentMic")
    expected_mic_algorithm: Optional[StrictStr] = Field(description="Receipt MIC algorithm ModernEDI requested from the partner; currently `sha1` for compatibility with legacy partner connections.", alias="expectedMicAlgorithm")
    expected_by: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="expectedBy", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    validation_error: Optional[StrictStr] = Field(description="Specific validation or partner-disposition problem that caused `warning`, `rejected`, `invalid`, or `mic_mismatch`.", alias="validationError")
    partner_configuration_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(description="Lowercase SHA-256 of the exact partner runtime configuration recorded for this transaction, receipt, or acknowledgment. It is `null` for legacy rows written before configuration stamping. Scenario verification accepts persisted evidence only when this value exactly matches the partner configuration frozen into the applied binding. ", alias="partnerConfigurationSha256", json_schema_extra={"examples": ["0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"]})
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["messageId", "disposition", "sent", "timestamp", "status", "asynchronous", "micMatched", "receivedContentMic", "expectedContentMic", "expectedMicAlgorithm", "expectedBy", "validationError", "partnerConfigurationSha256"]

    @field_validator('timestamp', mode="before")
    def timestamp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('expected_by', mode="before")
    def expected_by_validate_regular_expression(cls, value):
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
        """Create an instance of TransactionMdn from a JSON string"""
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

        # set to None if message_id (nullable) is None
        # and model_fields_set contains the field
        if self.message_id is None and "message_id" in self.model_fields_set:
            _dict['messageId'] = None

        # set to None if disposition (nullable) is None
        # and model_fields_set contains the field
        if self.disposition is None and "disposition" in self.model_fields_set:
            _dict['disposition'] = None

        # set to None if sent (nullable) is None
        # and model_fields_set contains the field
        if self.sent is None and "sent" in self.model_fields_set:
            _dict['sent'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if asynchronous (nullable) is None
        # and model_fields_set contains the field
        if self.asynchronous is None and "asynchronous" in self.model_fields_set:
            _dict['asynchronous'] = None

        # set to None if mic_matched (nullable) is None
        # and model_fields_set contains the field
        if self.mic_matched is None and "mic_matched" in self.model_fields_set:
            _dict['micMatched'] = None

        # set to None if received_content_mic (nullable) is None
        # and model_fields_set contains the field
        if self.received_content_mic is None and "received_content_mic" in self.model_fields_set:
            _dict['receivedContentMic'] = None

        # set to None if expected_content_mic (nullable) is None
        # and model_fields_set contains the field
        if self.expected_content_mic is None and "expected_content_mic" in self.model_fields_set:
            _dict['expectedContentMic'] = None

        # set to None if expected_mic_algorithm (nullable) is None
        # and model_fields_set contains the field
        if self.expected_mic_algorithm is None and "expected_mic_algorithm" in self.model_fields_set:
            _dict['expectedMicAlgorithm'] = None

        # set to None if expected_by (nullable) is None
        # and model_fields_set contains the field
        if self.expected_by is None and "expected_by" in self.model_fields_set:
            _dict['expectedBy'] = None

        # set to None if validation_error (nullable) is None
        # and model_fields_set contains the field
        if self.validation_error is None and "validation_error" in self.model_fields_set:
            _dict['validationError'] = None

        # set to None if partner_configuration_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.partner_configuration_sha256 is None and "partner_configuration_sha256" in self.model_fields_set:
            _dict['partnerConfigurationSha256'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionMdn from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "messageId": obj.get("messageId"),
            "disposition": obj.get("disposition"),
            "sent": obj.get("sent"),
            "timestamp": obj.get("timestamp"),
            "status": obj.get("status"),
            "asynchronous": obj.get("asynchronous"),
            "micMatched": obj.get("micMatched"),
            "receivedContentMic": obj.get("receivedContentMic"),
            "expectedContentMic": obj.get("expectedContentMic"),
            "expectedMicAlgorithm": obj.get("expectedMicAlgorithm"),
            "expectedBy": obj.get("expectedBy"),
            "validationError": obj.get("validationError"),
            "partnerConfigurationSha256": obj.get("partnerConfigurationSha256")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
