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
from modernedi.generated.models.as2_environment_profile_x12_sender import As2EnvironmentProfileX12Sender
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2EnvironmentProfile(BaseModel):
    """
    ModernEDI endpoint and X12 sender identity for one workspace environment.
    """ # noqa: E501
    as2_url: Optional[StrictStr] = Field(description="HTTPS AS2 receive URL to configure at the partner, or `null` while the endpoint is unavailable.", alias="as2Url")
    http_as2_url: Optional[StrictStr] = Field(default=None, description="Plain-HTTP endpoint when included in the tenant's plan and provisioned.", alias="httpAs2Url")
    as2_identifier: Optional[StrictStr] = Field(description="ModernEDI AS2 identifier sent as `AS2-From` and expected as inbound `AS2-To`, or `null` while unprovisioned.", alias="as2Identifier")
    x12_sender: As2EnvironmentProfileX12Sender = Field(alias="x12Sender")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["as2Url", "httpAs2Url", "as2Identifier", "x12Sender"]

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
        """Create an instance of As2EnvironmentProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of x12_sender
        if self.x12_sender:
            _dict['x12Sender'] = self.x12_sender.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if as2_url (nullable) is None
        # and model_fields_set contains the field
        if self.as2_url is None and "as2_url" in self.model_fields_set:
            _dict['as2Url'] = None

        # set to None if as2_identifier (nullable) is None
        # and model_fields_set contains the field
        if self.as2_identifier is None and "as2_identifier" in self.model_fields_set:
            _dict['as2Identifier'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of As2EnvironmentProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "as2Url": obj.get("as2Url"),
            "httpAs2Url": obj.get("httpAs2Url"),
            "as2Identifier": obj.get("as2Identifier"),
            "x12Sender": As2EnvironmentProfileX12Sender.from_dict(obj["x12Sender"]) if obj.get("x12Sender") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
