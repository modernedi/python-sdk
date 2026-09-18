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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class X12FunctionalGroupValidationError(BaseModel):
    """
    Validation finding associated with one GS/GE functional group.
    """ # noqa: E501
    functional_group_index: Annotated[int, Field(strict=True, ge=0)] = Field(description="Zero-based functional-group index within the parsed interchange.", alias="functionalGroupIndex")
    functional_identifier_code: StrictStr = Field(description="GS01 functional identifier code for the affected group.", alias="functionalIdentifierCode")
    functional_identifier_description: Optional[StrictStr] = Field(description="Human-readable GS01 code meaning, or `null` when the code is not in ModernEDI's reference catalog.", alias="functionalIdentifierDescription")
    control_number: StrictStr = Field(description="GS06 functional-group control number used to correlate the finding with source X12.", alias="controlNumber")
    code: StrictStr = Field(description="X12 validator code for the functional-group finding.")
    description: StrictStr = Field(description="Human-readable explanation of the functional-group finding.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["functionalGroupIndex", "functionalIdentifierCode", "functionalIdentifierDescription", "controlNumber", "code", "description"]

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
        """Create an instance of X12FunctionalGroupValidationError from a JSON string"""
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

        # set to None if functional_identifier_description (nullable) is None
        # and model_fields_set contains the field
        if self.functional_identifier_description is None and "functional_identifier_description" in self.model_fields_set:
            _dict['functionalIdentifierDescription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of X12FunctionalGroupValidationError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "functionalGroupIndex": obj.get("functionalGroupIndex"),
            "functionalIdentifierCode": obj.get("functionalIdentifierCode"),
            "functionalIdentifierDescription": obj.get("functionalIdentifierDescription"),
            "controlNumber": obj.get("controlNumber"),
            "code": obj.get("code"),
            "description": obj.get("description")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
