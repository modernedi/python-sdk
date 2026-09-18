# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.outbound_business_key import OutboundBusinessKey
from modernedi.generated.models.outbound_preview_response_mapping import OutboundPreviewResponseMapping
from modernedi.generated.models.outbound_preview_response_partner import OutboundPreviewResponsePartner
from modernedi.generated.models.x12_validation_result import X12ValidationResult
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class OutboundPreviewResponse(BaseModel):
    """
    Dry-run result showing map selection, generated X12, validation diagnostics, and partner context without sending AS2.
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true`; map-selection or transform failures use the documented error response instead.")
    generated_x12: StrictStr = Field(description="Complete generated X12 that would be sent by `/v1/as2/send`.", alias="generatedX12")
    validation: X12ValidationResult
    mapping: OutboundPreviewResponseMapping
    partner: OutboundPreviewResponsePartner
    business_key: Optional[OutboundBusinessKey] = Field(description="Business identifier that would be recorded with a real send, or `null` when none was supplied.", alias="businessKey")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "generatedX12", "validation", "mapping", "partner", "businessKey"]

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
        """Create an instance of OutboundPreviewResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of validation
        if self.validation:
            _dict['validation'] = self.validation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mapping
        if self.mapping:
            _dict['mapping'] = self.mapping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of partner
        if self.partner:
            _dict['partner'] = self.partner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_key
        if self.business_key:
            _dict['businessKey'] = self.business_key.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if business_key (nullable) is None
        # and model_fields_set contains the field
        if self.business_key is None and "business_key" in self.model_fields_set:
            _dict['businessKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OutboundPreviewResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "generatedX12": obj.get("generatedX12"),
            "validation": X12ValidationResult.from_dict(obj["validation"]) if obj.get("validation") is not None else None,
            "mapping": OutboundPreviewResponseMapping.from_dict(obj["mapping"]) if obj.get("mapping") is not None else None,
            "partner": OutboundPreviewResponsePartner.from_dict(obj["partner"]) if obj.get("partner") is not None else None,
            "businessKey": OutboundBusinessKey.from_dict(obj["businessKey"]) if obj.get("businessKey") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
