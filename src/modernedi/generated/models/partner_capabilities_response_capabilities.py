# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from modernedi.generated.models.partner_mapping_capability import PartnerMappingCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class PartnerCapabilitiesResponseCapabilities(BaseModel):
    """
    Published maps grouped by the direction in which data crosses the partner boundary.
    """ # noqa: E501
    incoming: List[PartnerMappingCapability] = Field(description="Maps that transform inbound partner X12 into application-facing mapped outputs.")
    outgoing: List[PartnerMappingCapability] = Field(description="Maps that transform application payloads into outbound partner X12.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["incoming", "outgoing"]

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
        """Create an instance of PartnerCapabilitiesResponseCapabilities from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in incoming (list)
        _items = []
        if self.incoming:
            for _item_incoming in self.incoming:
                if _item_incoming:
                    _items.append(_item_incoming.to_dict())
            _dict['incoming'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in outgoing (list)
        _items = []
        if self.outgoing:
            for _item_outgoing in self.outgoing:
                if _item_outgoing:
                    _items.append(_item_outgoing.to_dict())
            _dict['outgoing'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PartnerCapabilitiesResponseCapabilities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "incoming": [PartnerMappingCapability.from_dict(_item) for _item in obj["incoming"]] if obj.get("incoming") is not None else None,
            "outgoing": [PartnerMappingCapability.from_dict(_item) for _item in obj["outgoing"]] if obj.get("outgoing") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
