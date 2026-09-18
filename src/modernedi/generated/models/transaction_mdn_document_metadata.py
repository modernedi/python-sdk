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

class TransactionMdnDocumentMetadata(BaseModel):
    """
    Full receipt-assurance metadata for the original transaction's MDN report.
    """ # noqa: E501
    message_id: Optional[StrictStr] = Field(description="Message-ID of the MDN itself, or `null` while an asynchronous receipt is pending.", alias="messageId")
    disposition: Optional[StrictStr] = Field(description="Raw AS2 Disposition value returned by the partner.")
    status: StrictStr = Field(description="Normalized receipt-assurance outcome; only `processed` is a clean final success.")
    asynchronous: Optional[StrictBool] = Field(description="Whether the receipt used the asynchronous Receipt-Delivery-Option callback.")
    mic_matched: Optional[StrictBool] = Field(description="Whether the returned MIC matched the canonical content ModernEDI sent.", alias="micMatched")
    received_content_mic: Optional[StrictStr] = Field(description="Partner-supplied Received-content-MIC value.", alias="receivedContentMic")
    expected_content_mic: Optional[StrictStr] = Field(description="Digest ModernEDI calculated over the sent canonical MIME content.", alias="expectedContentMic")
    expected_mic_algorithm: Optional[StrictStr] = Field(description="MIC algorithm ModernEDI requested.", alias="expectedMicAlgorithm")
    expected_by: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="expectedBy", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    validation_error: Optional[StrictStr] = Field(description="Specific receipt validation or disposition problem, or `null`.", alias="validationError")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["messageId", "disposition", "status", "asynchronous", "micMatched", "receivedContentMic", "expectedContentMic", "expectedMicAlgorithm", "expectedBy", "validationError"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pending', 'processed', 'warning', 'rejected', 'invalid', 'mic_mismatch', 'overdue']):
            raise ValueError("must be one of enum values ('pending', 'processed', 'warning', 'rejected', 'invalid', 'mic_mismatch', 'overdue')")
        return value

    @field_validator('expected_by', mode="before")
    def expected_by_validate_regular_expression(cls, value):
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
        """Create an instance of TransactionMdnDocumentMetadata from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionMdnDocumentMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "messageId": obj.get("messageId"),
            "disposition": obj.get("disposition"),
            "status": obj.get("status"),
            "asynchronous": obj.get("asynchronous"),
            "micMatched": obj.get("micMatched"),
            "receivedContentMic": obj.get("receivedContentMic"),
            "expectedContentMic": obj.get("expectedContentMic"),
            "expectedMicAlgorithm": obj.get("expectedMicAlgorithm"),
            "expectedBy": obj.get("expectedBy"),
            "validationError": obj.get("validationError")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
