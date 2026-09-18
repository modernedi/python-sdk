# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TechnicalAcknowledgmentOutcome(BaseModel):
    """
    Parsed TA1 interchange-level result. Only `received` is a clean outcome; every other received status requires operator review.
    """ # noqa: E501
    status: StrictStr = Field(description="Normalized TA104 result. `A` becomes `received`, `E` becomes `received_with_errors`, and `R` becomes `rejected`.")
    acknowledgment_code: Optional[StrictStr] = Field(description="Raw TA104 interchange acknowledgment code (`A`, `E`, or `R`) when available.", alias="acknowledgmentCode", json_schema_extra={"examples": ["A"]})
    error_code: Optional[StrictStr] = Field(description="Raw TA105 interchange note/error code. Interpret it with the partner's X12 implementation guidance; `000` normally accompanies a clean acceptance.", alias="errorCode", json_schema_extra={"examples": ["000"]})
    acknowledged_interchange_control_number: Optional[StrictStr] = Field(description="TA101 control number identifying the original ISA13 interchange acknowledged by this TA1.", alias="acknowledgedInterchangeControlNumber", json_schema_extra={"examples": ["000000017"]})
    summary: StrictStr = Field(description="Customer-readable interpretation of the TA104 outcome.")
    parsed: StrictBool = Field(description="True when ModernEDI found a structurally usable TA1 segment and recognized TA104.")
    unknown_reason: Optional[StrictStr] = Field(description="Stable reason `status` is `unknown`, or `null` for a recognized outcome.", alias="unknownReason")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["status", "acknowledgmentCode", "errorCode", "acknowledgedInterchangeControlNumber", "summary", "parsed", "unknownReason"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['received', 'received_with_errors', 'rejected', 'unknown']):
            raise ValueError("must be one of enum values ('received', 'received_with_errors', 'rejected', 'unknown')")
        return value

    @field_validator('unknown_reason')
    def unknown_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['missing_x12', 'invalid_structure', 'missing_ta1', 'unsupported_acknowledgment_code']):
            raise ValueError("must be one of enum values ('missing_x12', 'invalid_structure', 'missing_ta1', 'unsupported_acknowledgment_code')")
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
        """Create an instance of TechnicalAcknowledgmentOutcome from a JSON string"""
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

        # set to None if acknowledgment_code (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledgment_code is None and "acknowledgment_code" in self.model_fields_set:
            _dict['acknowledgmentCode'] = None

        # set to None if error_code (nullable) is None
        # and model_fields_set contains the field
        if self.error_code is None and "error_code" in self.model_fields_set:
            _dict['errorCode'] = None

        # set to None if acknowledged_interchange_control_number (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledged_interchange_control_number is None and "acknowledged_interchange_control_number" in self.model_fields_set:
            _dict['acknowledgedInterchangeControlNumber'] = None

        # set to None if unknown_reason (nullable) is None
        # and model_fields_set contains the field
        if self.unknown_reason is None and "unknown_reason" in self.model_fields_set:
            _dict['unknownReason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TechnicalAcknowledgmentOutcome from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "status": obj.get("status"),
            "acknowledgmentCode": obj.get("acknowledgmentCode"),
            "errorCode": obj.get("errorCode"),
            "acknowledgedInterchangeControlNumber": obj.get("acknowledgedInterchangeControlNumber"),
            "summary": obj.get("summary"),
            "parsed": obj.get("parsed"),
            "unknownReason": obj.get("unknownReason")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
