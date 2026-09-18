# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.configuration_partner_separator_set import ConfigurationPartnerSeparatorSet
from modernedi.generated.models.integration_partner_x12 import IntegrationPartnerX12
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class IntegrationPartner(BaseModel):
    """
    IntegrationPartner
    """ # noqa: E501
    partner_id: StrictInt = Field(description="Stable tenant-scoped partner id. Use this value as the `partnerId` query parameter for exact outbound map selection.", alias="partnerId", json_schema_extra={"examples": [1]})
    name: StrictStr = Field(description="Configured partner display name. Use `partnerId` for outbound selection.", json_schema_extra={"examples": ["Customer One"]})
    as2_connection_id: Optional[StrictInt] = Field(description="Tenant-scoped partner AS2 connection id, or `null` while connection details are not yet available.", alias="as2ConnectionId", json_schema_extra={"examples": [12]})
    as2_connection_configured: StrictBool = Field(description="True when this partner is attached to an AS2 connection profile. The profile may be inbound-only and therefore is not necessarily ready for outbound delivery.", alias="as2ConnectionConfigured")
    production_ready: StrictBool = Field(description="True when the partner has a complete production AS2 identifier and certificate, destination URL, and X12 identity, so outbound production delivery can be attempted.", alias="productionReady")
    test_ready: StrictBool = Field(description="True when the partner has a complete test AS2 identifier and certificate, destination URL, and X12 identity, so outbound test delivery can be attempted. False is valid for a production-only or inbound-only partner.", alias="testReady")
    carbon_copy_only: StrictBool = Field(description="True when the partner is intended only as a carbon-copy recipient in the workspace.", alias="carbonCopyOnly")
    implementation_acknowledgment_enabled: StrictBool = Field(description="Whether ModernEDI sends X12 999 implementation acknowledgments for this partner's 005010-and-later documents instead of automatic 997s. Earlier X12 versions continue to receive 997s. Enable this only when the partner requests 999s. A 999 reports X12 syntax and relational validation. It does not indicate semantic or business acceptance, and it is not HIPAA implementation-guide certification. ", alias="implementationAcknowledgmentEnabled")
    edi_support_email: StrictStr = Field(description="Partner EDI support address, or an empty string when one has not been recorded.", alias="ediSupportEmail", json_schema_extra={"examples": ["edi@customer-one.example"]})
    unmapped_inbound_policy: StrictStr = Field(description="Whether inbound transactions without a matching map are rejected from mapped-output delivery or persisted as raw X12.", alias="unmappedInboundPolicy")
    signing_certificate_slot: StrictStr = Field(description="Tenant certificate slot ModernEDI uses to sign AS2 traffic for this partner.", alias="signingCertificateSlot")
    supports_newline_after_segment_terminator: StrictBool = Field(description="Whether ModernEDI may emit a newline after each X12 segment terminator for this partner.", alias="supportsNewlineAfterSegmentTerminator")
    override_user_agent_string: Optional[StrictStr] = Field(description="Optional AS2 HTTP User-Agent compatibility override, or `null` to use the ModernEDI default.", alias="overrideUserAgentString")
    override_separator_set: Optional[ConfigurationPartnerSeparatorSet] = Field(description="Optional X12 separator override, or `null` to use the separators selected by the mapping runtime.", alias="overrideSeparatorSet")
    message_type_gs_version_overrides: Dict[str, StrictStr] = Field(description="Map from functional-group type to the exact GS08 version string required by this partner. An empty object uses each map's normal X12 version.", alias="messageTypeGsVersionOverrides")
    x12: IntegrationPartnerX12
    etag: Optional[StrictStr] = Field(default=None, description="Quoted SHA-256 ETag over mutable partner configuration, present on list and configuration detail responses. Derived `as2ConnectionConfigured`, `productionReady`, and `testReady` values are excluded; changes to the referenced AS2 connection are guarded by that connection's own ETag.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["partnerId", "name", "as2ConnectionId", "as2ConnectionConfigured", "productionReady", "testReady", "carbonCopyOnly", "implementationAcknowledgmentEnabled", "ediSupportEmail", "unmappedInboundPolicy", "signingCertificateSlot", "supportsNewlineAfterSegmentTerminator", "overrideUserAgentString", "overrideSeparatorSet", "messageTypeGsVersionOverrides", "x12", "etag"]

    @field_validator('unmapped_inbound_policy')
    def unmapped_inbound_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MAPPED_ONLY', 'PASSTHROUGH_RAW_X12']):
            raise ValueError("must be one of enum values ('MAPPED_ONLY', 'PASSTHROUGH_RAW_X12')")
        return value

    @field_validator('signing_certificate_slot')
    def signing_certificate_slot_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['active', 'next']):
            raise ValueError("must be one of enum values ('active', 'next')")
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
        """Create an instance of IntegrationPartner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of override_separator_set
        if self.override_separator_set:
            _dict['overrideSeparatorSet'] = self.override_separator_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of x12
        if self.x12:
            _dict['x12'] = self.x12.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if as2_connection_id (nullable) is None
        # and model_fields_set contains the field
        if self.as2_connection_id is None and "as2_connection_id" in self.model_fields_set:
            _dict['as2ConnectionId'] = None

        # set to None if override_user_agent_string (nullable) is None
        # and model_fields_set contains the field
        if self.override_user_agent_string is None and "override_user_agent_string" in self.model_fields_set:
            _dict['overrideUserAgentString'] = None

        # set to None if override_separator_set (nullable) is None
        # and model_fields_set contains the field
        if self.override_separator_set is None and "override_separator_set" in self.model_fields_set:
            _dict['overrideSeparatorSet'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntegrationPartner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "partnerId": obj.get("partnerId"),
            "name": obj.get("name"),
            "as2ConnectionId": obj.get("as2ConnectionId"),
            "as2ConnectionConfigured": obj.get("as2ConnectionConfigured"),
            "productionReady": obj.get("productionReady"),
            "testReady": obj.get("testReady"),
            "carbonCopyOnly": obj.get("carbonCopyOnly"),
            "implementationAcknowledgmentEnabled": obj.get("implementationAcknowledgmentEnabled"),
            "ediSupportEmail": obj.get("ediSupportEmail"),
            "unmappedInboundPolicy": obj.get("unmappedInboundPolicy"),
            "signingCertificateSlot": obj.get("signingCertificateSlot"),
            "supportsNewlineAfterSegmentTerminator": obj.get("supportsNewlineAfterSegmentTerminator"),
            "overrideUserAgentString": obj.get("overrideUserAgentString"),
            "overrideSeparatorSet": ConfigurationPartnerSeparatorSet.from_dict(obj["overrideSeparatorSet"]) if obj.get("overrideSeparatorSet") is not None else None,
            "messageTypeGsVersionOverrides": obj.get("messageTypeGsVersionOverrides"),
            "x12": IntegrationPartnerX12.from_dict(obj["x12"]) if obj.get("x12") is not None else None,
            "etag": obj.get("etag")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
