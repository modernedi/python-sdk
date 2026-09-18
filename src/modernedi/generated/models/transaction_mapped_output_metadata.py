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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.mapping_purpose import MappingPurpose
from modernedi.generated.models.transaction_business_key import TransactionBusinessKey
from modernedi.generated.models.transaction_mapped_output_mapping import TransactionMappedOutputMapping
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionMappedOutputMetadata(BaseModel):
    """
    Metadata and map provenance for an application-facing document produced by an incoming map.
    """ # noqa: E501
    id: StrictStr = Field(description="Artifact identifier within the transaction response, such as `mapped-output-1`. This is not the managed-queue id and cannot be used with `/v1/mapped-outputs/{id}/ack`. Stored transaction details expose the queue correlation id separately as `delivery.outputId`. ", json_schema_extra={"examples": ["mapped-output-1"]})
    sequence_number: StrictInt = Field(description="One-based display order of this output within the transaction response.", alias="sequenceNumber", json_schema_extra={"examples": [1]})
    purpose: MappingPurpose
    content_type: Optional[StrictStr] = Field(default=None, description="Media type of the corresponding mapped-output document body, or `null` for historical artifacts without recorded content type.", alias="contentType", json_schema_extra={"examples": ["application/json"]})
    created_at: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="createdAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    business_key: Optional[TransactionBusinessKey] = Field(default=None, description="Map-derived reconciliation identifier, or `null` when the map did not produce one.", alias="businessKey")
    mapping: Optional[TransactionMappedOutputMapping] = None
    extra_fields: Optional[Dict[str, StrictStr]] = Field(default=None, description="Runtime routing metadata captured with the output; this is not the map's selectable delivered context.", alias="extraFields")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "sequenceNumber", "purpose", "contentType", "createdAt", "businessKey", "mapping", "extraFields"]

    @field_validator('created_at', mode="before")
    def created_at_validate_regular_expression(cls, value):
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
        """Create an instance of TransactionMappedOutputMetadata from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of business_key
        if self.business_key:
            _dict['businessKey'] = self.business_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mapping
        if self.mapping:
            _dict['mapping'] = self.mapping.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if content_type (nullable) is None
        # and model_fields_set contains the field
        if self.content_type is None and "content_type" in self.model_fields_set:
            _dict['contentType'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['createdAt'] = None

        # set to None if business_key (nullable) is None
        # and model_fields_set contains the field
        if self.business_key is None and "business_key" in self.model_fields_set:
            _dict['businessKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionMappedOutputMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "sequenceNumber": obj.get("sequenceNumber"),
            "purpose": obj.get("purpose"),
            "contentType": obj.get("contentType"),
            "createdAt": obj.get("createdAt"),
            "businessKey": TransactionBusinessKey.from_dict(obj["businessKey"]) if obj.get("businessKey") is not None else None,
            "mapping": TransactionMappedOutputMapping.from_dict(obj["mapping"]) if obj.get("mapping") is not None else None,
            "extraFields": obj.get("extraFields")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
