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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2PartnerEnvironmentResolved(BaseModel):
    """
    Persisted AS2 partner environment with all secure inbound-protection defaults resolved.
    """ # noqa: E501
    as2_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Partner's environment-specific AS2 identifier. ModernEDI matches it as inbound `AS2-From` and sends it as outbound `AS2-To`.", alias="as2Identifier", json_schema_extra={"examples": ["RETAILER_PROD"]})
    endpoint_url: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(default=None, description="Optional outbound destination. Omit it or use `null` for an inbound-only profile. When present, it must be an absolute HTTP or HTTPS partner destination URL without user information or a fragment. Endpoint workspaces must use HTTPS; plain HTTP requires Endpoint Plus, Static Outbound, Static Network, or Enterprise. The host must be publicly routable; local, private, link-local, multicast, carrier-grade NAT, documentation, benchmark, and other reserved address targets are rejected.", alias="endpointUrl", json_schema_extra={"examples": ["https://as2.retailer.example/receive"]})
    public_certificate_pem: StrictStr = Field(description="Exactly one PEM-encoded partner X.509 public certificate. ModernEDI canonicalizes it before storage.", alias="publicCertificatePem", json_schema_extra={"examples": ["-----BEGIN CERTIFICATE-----\nMIIB...partner-public-certificate...\n-----END CERTIFICATE-----"]})
    require_signature: StrictBool = Field(description="When `true` (the secure default), ModernEDI rejects non-MDN inbound messages for this environment unless the sender signature is present and successfully verified with the configured certificate. This policy belongs to the AS2 connection/environment and therefore applies to every attached partner on a shared or VAN connection. Set `false` only for a documented connection-wide exception. Omission on create resolves to `true`; resolved connection responses always include the field.", alias="requireSignature")
    require_encryption: StrictBool = Field(description="When `true` (the secure default), ModernEDI rejects non-MDN inbound messages for this environment unless their encrypted content was successfully decrypted. This policy belongs to the AS2 connection/environment and therefore applies to every attached partner on a shared or VAN connection. Set `false` only for a documented connection-wide exception. Omission on create resolves to `true`; resolved connection responses always include the field.", alias="requireEncryption")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["as2Identifier", "endpointUrl", "publicCertificatePem", "requireSignature", "requireEncryption"]

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
        """Create an instance of As2PartnerEnvironmentResolved from a JSON string"""
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

        # set to None if endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_url is None and "endpoint_url" in self.model_fields_set:
            _dict['endpointUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of As2PartnerEnvironmentResolved from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "as2Identifier": obj.get("as2Identifier"),
            "endpointUrl": obj.get("endpointUrl"),
            "publicCertificatePem": obj.get("publicCertificatePem"),
            "requireSignature": obj.get("requireSignature") if obj.get("requireSignature") is not None else True,
            "requireEncryption": obj.get("requireEncryption") if obj.get("requireEncryption") is not None else True
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
