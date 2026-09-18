# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class X12ElementPreview(BaseModel):
    """
    One populated X12 data element from a parsed segment.
    """ # noqa: E501
    element_position: Annotated[int, Field(strict=True, ge=1)] = Field(description="One-based element position within the segment.", alias="elementPosition")
    definition: StrictStr = Field(description="X12 data-element definition number from the reference catalog.")
    description: StrictStr = Field(description="Human-readable data-element name from the reference catalog.")
    data_type: Optional[StrictStr] = Field(default=None, description="Normalized data type from the X12 reference catalog for this populated element.", alias="dataType")
    implied_decimal_digits: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Number of trailing digits interpreted as fractional for a NUMERIC (Nn) element; omitted for every other data type.", alias="impliedDecimalDigits")
    value: StrictStr = Field(description="Exact parsed source value; treat it as potentially sensitive business data.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["elementPosition", "definition", "description", "dataType", "impliedDecimalDigits", "value"]

    @field_validator('data_type')
    def data_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ALPHANUMERIC', 'BINARY', 'DATE', 'ID', 'NUMERIC', 'DECIMAL', 'TIME', 'COMPOSITE', 'NONE']):
            raise ValueError("must be one of enum values ('ALPHANUMERIC', 'BINARY', 'DATE', 'ID', 'NUMERIC', 'DECIMAL', 'TIME', 'COMPOSITE', 'NONE')")
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
        """Create an instance of X12ElementPreview from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of X12ElementPreview from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "elementPosition": obj.get("elementPosition"),
            "definition": obj.get("definition"),
            "description": obj.get("description"),
            "dataType": obj.get("dataType"),
            "impliedDecimalDigits": obj.get("impliedDecimalDigits"),
            "value": obj.get("value")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
