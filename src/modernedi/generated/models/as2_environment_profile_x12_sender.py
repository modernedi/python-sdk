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

class As2EnvironmentProfileX12Sender(BaseModel):
    """
    ModernEDI X12 envelope identity for documents sent from this environment.
    """ # noqa: E501
    isa_qualifier: Optional[StrictStr] = Field(description="ISA05/ISA07 qualifier for ModernEDI's environment identity, or `null` while unprovisioned.", alias="isaQualifier")
    isa_id: Optional[StrictStr] = Field(description="ISA06/ISA08 identifier for ModernEDI's environment identity, or `null` while unprovisioned.", alias="isaId")
    gs_id: Optional[StrictStr] = Field(description="GS02/GS03 identifier for ModernEDI's environment identity, or `null` while unprovisioned.", alias="gsId")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["isaQualifier", "isaId", "gsId"]

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
        """Create an instance of As2EnvironmentProfileX12Sender from a JSON string"""
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

        # set to None if isa_qualifier (nullable) is None
        # and model_fields_set contains the field
        if self.isa_qualifier is None and "isa_qualifier" in self.model_fields_set:
            _dict['isaQualifier'] = None

        # set to None if isa_id (nullable) is None
        # and model_fields_set contains the field
        if self.isa_id is None and "isa_id" in self.model_fields_set:
            _dict['isaId'] = None

        # set to None if gs_id (nullable) is None
        # and model_fields_set contains the field
        if self.gs_id is None and "gs_id" in self.model_fields_set:
            _dict['gsId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of As2EnvironmentProfileX12Sender from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "isaQualifier": obj.get("isaQualifier"),
            "isaId": obj.get("isaId"),
            "gsId": obj.get("gsId")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
