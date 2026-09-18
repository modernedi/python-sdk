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
from modernedi.generated.models.as2_network_profile import As2NetworkProfile
from modernedi.generated.models.as2_profile_certificates import As2ProfileCertificates
from modernedi.generated.models.as2_profile_environments import As2ProfileEnvironments
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2Profile(BaseModel):
    """
    ModernEDI-hosted AS2 identity and network information for production and test traffic.
    """ # noqa: E501
    domain_name: Optional[StrictStr] = Field(description="Provisioned tenant AS2 hostname, or `null` while the tenant runtime has not published one.", alias="domainName", json_schema_extra={"examples": ["edi.customer.example"]})
    environments: As2ProfileEnvironments
    network: As2NetworkProfile
    certificates: As2ProfileCertificates
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["domainName", "environments", "network", "certificates"]

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
        """Create an instance of As2Profile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of environments
        if self.environments:
            _dict['environments'] = self.environments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of certificates
        if self.certificates:
            _dict['certificates'] = self.certificates.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if domain_name (nullable) is None
        # and model_fields_set contains the field
        if self.domain_name is None and "domain_name" in self.model_fields_set:
            _dict['domainName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of As2Profile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "domainName": obj.get("domainName"),
            "environments": As2ProfileEnvironments.from_dict(obj["environments"]) if obj.get("environments") is not None else None,
            "network": As2NetworkProfile.from_dict(obj["network"]) if obj.get("network") is not None else None,
            "certificates": As2ProfileCertificates.from_dict(obj["certificates"]) if obj.get("certificates") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
