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
from modernedi.generated.models.as2_network_capability import As2NetworkCapability
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2NetworkProfile(BaseModel):
    """
    Current tenant-runtime network and certificate provisioning state.
    """ # noqa: E501
    provisioning_status: Optional[StrictStr] = Field(description="Latest tenant-runtime provisioning state, or `null` before a status has been recorded.", alias="provisioningStatus")
    tls_certificate_status: Optional[StrictStr] = Field(description="Latest TLS certificate deployment state for the AS2 hostname, or `null` when unavailable.", alias="tlsCertificateStatus")
    static_inbound: As2NetworkCapability = Field(alias="staticInbound")
    static_outbound: As2NetworkCapability = Field(alias="staticOutbound")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["provisioningStatus", "tlsCertificateStatus", "staticInbound", "staticOutbound"]

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
        """Create an instance of As2NetworkProfile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of static_inbound
        if self.static_inbound:
            _dict['staticInbound'] = self.static_inbound.to_dict()
        # override the default output from pydantic by calling `to_dict()` of static_outbound
        if self.static_outbound:
            _dict['staticOutbound'] = self.static_outbound.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if provisioning_status (nullable) is None
        # and model_fields_set contains the field
        if self.provisioning_status is None and "provisioning_status" in self.model_fields_set:
            _dict['provisioningStatus'] = None

        # set to None if tls_certificate_status (nullable) is None
        # and model_fields_set contains the field
        if self.tls_certificate_status is None and "tls_certificate_status" in self.model_fields_set:
            _dict['tlsCertificateStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of As2NetworkProfile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "provisioningStatus": obj.get("provisioningStatus"),
            "tlsCertificateStatus": obj.get("tlsCertificateStatus"),
            "staticInbound": As2NetworkCapability.from_dict(obj["staticInbound"]) if obj.get("staticInbound") is not None else None,
            "staticOutbound": As2NetworkCapability.from_dict(obj["staticOutbound"]) if obj.get("staticOutbound") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
