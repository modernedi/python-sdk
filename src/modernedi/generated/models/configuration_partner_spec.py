# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from uuid import UUID
from modernedi.generated.models.configuration_partner_separator_set import ConfigurationPartnerSeparatorSet
from modernedi.generated.models.configuration_partner_spec_x12 import ConfigurationPartnerSpecX12
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationPartnerSpec(BaseModel):
    """
    Complete persisted partner configuration. It replaces `as2ConnectionId` with a portable `as2ConnectionKey` and includes advanced runtime compatibility settings that participate in workspace configuration.
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Unique partner display name in this workspace.")
    as2_connection_key: Optional[UUID] = Field(description="Portable key of the referenced AS2 connection, or `null` for a detached map-authoring draft.", alias="as2ConnectionKey")
    x12: ConfigurationPartnerSpecX12
    edi_support_email: StrictStr = Field(description="Partner EDI support address, or an empty string when unavailable.", alias="ediSupportEmail")
    carbon_copy_only: StrictBool = Field(alias="carbonCopyOnly")
    implementation_acknowledgment_enabled: StrictBool = Field(description="Whether eligible inbound documents receive a 999 instead of a 997.", alias="implementationAcknowledgmentEnabled")
    unmapped_inbound_policy: StrictStr = Field(alias="unmappedInboundPolicy")
    signing_certificate_slot: StrictStr = Field(alias="signingCertificateSlot")
    supports_newline_after_segment_terminator: StrictBool = Field(alias="supportsNewlineAfterSegmentTerminator")
    override_user_agent_string: Optional[StrictStr] = Field(description="Optional AS2 HTTP User-Agent compatibility override.", alias="overrideUserAgentString")
    override_separator_set: Optional[ConfigurationPartnerSeparatorSet] = Field(description="Optional X12 separator override, or `null` to use runtime defaults.", alias="overrideSeparatorSet")
    message_type_gs_version_overrides: Dict[str, StrictStr] = Field(description="Closed runtime compatibility map from supported X12 message-type names to GS08 version overrides. An empty object means no overrides.", alias="messageTypeGsVersionOverrides")
    __properties: ClassVar[List[str]] = ["name", "as2ConnectionKey", "x12", "ediSupportEmail", "carbonCopyOnly", "implementationAcknowledgmentEnabled", "unmappedInboundPolicy", "signingCertificateSlot", "supportsNewlineAfterSegmentTerminator", "overrideUserAgentString", "overrideSeparatorSet", "messageTypeGsVersionOverrides"]

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
        """Create an instance of ConfigurationPartnerSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_unset=True,
        )
        # override the default output from pydantic by calling `to_dict()` of x12
        if self.x12:
            _dict['x12'] = self.x12.to_dict()
        # override the default output from pydantic by calling `to_dict()` of override_separator_set
        if self.override_separator_set:
            _dict['overrideSeparatorSet'] = self.override_separator_set.to_dict()
        # set to None if as2_connection_key (nullable) is None
        # and model_fields_set contains the field
        if self.as2_connection_key is None and "as2_connection_key" in self.model_fields_set:
            _dict['as2ConnectionKey'] = None

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
        """Create an instance of ConfigurationPartnerSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "name": obj.get("name"),
            "as2ConnectionKey": obj.get("as2ConnectionKey"),
            "x12": ConfigurationPartnerSpecX12.from_dict(obj["x12"]) if obj.get("x12") is not None else None,
            "ediSupportEmail": obj.get("ediSupportEmail"),
            "carbonCopyOnly": obj.get("carbonCopyOnly"),
            "implementationAcknowledgmentEnabled": obj.get("implementationAcknowledgmentEnabled"),
            "unmappedInboundPolicy": obj.get("unmappedInboundPolicy"),
            "signingCertificateSlot": obj.get("signingCertificateSlot"),
            "supportsNewlineAfterSegmentTerminator": obj.get("supportsNewlineAfterSegmentTerminator"),
            "overrideUserAgentString": obj.get("overrideUserAgentString"),
            "overrideSeparatorSet": ConfigurationPartnerSeparatorSet.from_dict(obj["overrideSeparatorSet"]) if obj.get("overrideSeparatorSet") is not None else None,
            "messageTypeGsVersionOverrides": obj.get("messageTypeGsVersionOverrides")
        }.items() if key in obj})
        return _obj
