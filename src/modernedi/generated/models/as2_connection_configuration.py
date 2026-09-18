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
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from modernedi.generated.models.as2_connection_resolved_environments import As2ConnectionResolvedEnvironments
from modernedi.generated.models.as2_resolved_functional_acknowledgment_settings import As2ResolvedFunctionalAcknowledgmentSettings
from modernedi.generated.models.as2_resolved_mdn_settings import As2ResolvedMdnSettings
from modernedi.generated.models.as2_resolved_outbound_settings import As2ResolvedOutboundSettings
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2ConnectionConfiguration(BaseModel):
    """
    Complete persisted AS2 connection returned by configuration operations.
    """ # noqa: E501
    connection_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="Stable workspace-scoped identifier used when attaching partners or updating this connection.", alias="connectionId")
    environments: As2ConnectionResolvedEnvironments
    outbound: As2ResolvedOutboundSettings
    functional_acknowledgment: As2ResolvedFunctionalAcknowledgmentSettings = Field(alias="functionalAcknowledgment")
    mdn: As2ResolvedMdnSettings
    cms_algorithm_protection: StrictBool = Field(description="Effective RFC 6211 `cmsAlgorithmProtect` compatibility setting for signed outbound messages and MDNs.", alias="cmsAlgorithmProtection")
    digest_canonicalization_policy: StrictStr = Field(description="Effective inbound signature-verification treatment of MIME line endings.", alias="digestCanonicalizationPolicy")
    etag: StrictStr = Field(description="Quoted SHA-256 identity of the observed AS2 connection configuration. Changes use the aggregate export–plan–apply workflow.")
    __properties: ClassVar[List[str]] = ["connectionId", "environments", "outbound", "functionalAcknowledgment", "mdn", "cmsAlgorithmProtection", "digestCanonicalizationPolicy", "etag"]

    @field_validator('digest_canonicalization_policy')
    def digest_canonicalization_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['AUTO', 'CANONICALIZE', 'PRESERVE']):
            raise ValueError("must be one of enum values ('AUTO', 'CANONICALIZE', 'PRESERVE')")
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
        """Create an instance of As2ConnectionConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of environments
        if self.environments:
            _dict['environments'] = self.environments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of outbound
        if self.outbound:
            _dict['outbound'] = self.outbound.to_dict()
        # override the default output from pydantic by calling `to_dict()` of functional_acknowledgment
        if self.functional_acknowledgment:
            _dict['functionalAcknowledgment'] = self.functional_acknowledgment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mdn
        if self.mdn:
            _dict['mdn'] = self.mdn.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of As2ConnectionConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "connectionId": obj.get("connectionId"),
            "environments": As2ConnectionResolvedEnvironments.from_dict(obj["environments"]) if obj.get("environments") is not None else None,
            "outbound": As2ResolvedOutboundSettings.from_dict(obj["outbound"]) if obj.get("outbound") is not None else None,
            "functionalAcknowledgment": As2ResolvedFunctionalAcknowledgmentSettings.from_dict(obj["functionalAcknowledgment"]) if obj.get("functionalAcknowledgment") is not None else None,
            "mdn": As2ResolvedMdnSettings.from_dict(obj["mdn"]) if obj.get("mdn") is not None else None,
            "cmsAlgorithmProtection": obj.get("cmsAlgorithmProtection"),
            "digestCanonicalizationPolicy": obj.get("digestCanonicalizationPolicy"),
            "etag": obj.get("etag")
        }.items() if key in obj})
        return _obj
