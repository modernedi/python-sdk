# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionEdiMetadata(BaseModel):
    """
    X12 envelope and delimiter context captured for a transaction.
    """ # noqa: E501
    x12_version: Optional[StrictStr] = Field(default=None, description="Numeric X12 implementation version, or `null` when it was not recorded.", alias="x12Version", json_schema_extra={"examples": ["4010"]})
    functional_identifier_code: Optional[StrictStr] = Field(default=None, description="GS01 functional identifier code, or `null` when it was not recorded.", alias="functionalIdentifierCode", json_schema_extra={"examples": ["PO"]})
    transaction_group_type: Optional[StrictStr] = Field(default=None, description="ST01 transaction set identifier code recorded by the runtime.", alias="transactionGroupType", json_schema_extra={"examples": ["850"]})
    segment_terminator: Optional[StrictStr] = Field(default=None, description="Single-character segment terminator detected from the interchange, or `null` when unavailable.", alias="segmentTerminator", json_schema_extra={"examples": ["~"]})
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["x12Version", "functionalIdentifierCode", "transactionGroupType", "segmentTerminator"]

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
        """Create an instance of TransactionEdiMetadata from a JSON string"""
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

        # set to None if x12_version (nullable) is None
        # and model_fields_set contains the field
        if self.x12_version is None and "x12_version" in self.model_fields_set:
            _dict['x12Version'] = None

        # set to None if functional_identifier_code (nullable) is None
        # and model_fields_set contains the field
        if self.functional_identifier_code is None and "functional_identifier_code" in self.model_fields_set:
            _dict['functionalIdentifierCode'] = None

        # set to None if transaction_group_type (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_group_type is None and "transaction_group_type" in self.model_fields_set:
            _dict['transactionGroupType'] = None

        # set to None if segment_terminator (nullable) is None
        # and model_fields_set contains the field
        if self.segment_terminator is None and "segment_terminator" in self.model_fields_set:
            _dict['segmentTerminator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionEdiMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "x12Version": obj.get("x12Version"),
            "functionalIdentifierCode": obj.get("functionalIdentifierCode"),
            "transactionGroupType": obj.get("transactionGroupType"),
            "segmentTerminator": obj.get("segmentTerminator")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
