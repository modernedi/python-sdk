# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.technical_acknowledgment_outcome import TechnicalAcknowledgmentOutcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionTechnicalAcknowledgmentDocumentMetadata(BaseModel):
    """
    Send or receive direction and retained HTTP status for a technical acknowledgment.
    """ # noqa: E501
    sent: Optional[StrictBool] = Field(description="True when ModernEDI sent the technical acknowledgment; false when it received one.")
    response_status_code: Optional[StrictInt] = Field(description="Retained downstream HTTP status, or `null`.", alias="responseStatusCode")
    outcome: Optional[TechnicalAcknowledgmentOutcome] = Field(description="Parsed TA1 result, or `null` when this artifact is only a retained HTTP response without TA1 X12.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["sent", "responseStatusCode", "outcome"]

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
        """Create an instance of TransactionTechnicalAcknowledgmentDocumentMetadata from a JSON string"""
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

        # set to None if response_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.response_status_code is None and "response_status_code" in self.model_fields_set:
            _dict['responseStatusCode'] = None

        # set to None if outcome (nullable) is None
        # and model_fields_set contains the field
        if self.outcome is None and "outcome" in self.model_fields_set:
            _dict['outcome'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionTechnicalAcknowledgmentDocumentMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "sent": obj.get("sent"),
            "responseStatusCode": obj.get("responseStatusCode"),
            "outcome": TechnicalAcknowledgmentOutcome.from_dict(obj["outcome"]) if obj.get("outcome") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
