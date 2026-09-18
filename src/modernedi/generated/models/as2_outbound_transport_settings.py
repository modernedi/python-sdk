# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2OutboundTransportSettings(BaseModel):
    """
    Optional outbound AS2 algorithms and MIME-compatibility controls. Each omitted field receives its documented default.
    """ # noqa: E501
    signing_algorithm: Optional[StrictStr] = Field(default='SHA256WITHRSA', description="CMS/S/MIME signature algorithm ModernEDI uses for signed outbound payloads, signed automatic X12 acknowledgments, and signed MDNs. Prefer `SHA256WITHRSA`; use `SHA1WITHRSA` only for a legacy partner that cannot verify SHA-2 signatures.", alias="signingAlgorithm", json_schema_extra={"examples": ["SHA256WITHRSA"]})
    encryption_algorithm: Optional[StrictStr] = Field(default='AES256_CBC', description="CMS content-encryption algorithm for outbound AS2 payloads and any encrypted acknowledgments. Prefer `AES256_CBC`; `DES_EDE3_CBC` exists only for legacy partner interoperability.", alias="encryptionAlgorithm", json_schema_extra={"examples": ["AES256_CBC"]})
    compression_algorithm: Optional[StrictStr] = Field(default='ZLIB', description="Compression algorithm used when an outbound AS2 message structure includes compression. `ZLIB` is the only supported customer-selectable value.", alias="compressionAlgorithm", json_schema_extra={"examples": ["ZLIB"]})
    mic_algorithm: Optional[StrictStr] = Field(default='SHA_256', description="Digest algorithm used to calculate and store ModernEDI's local content MIC for outbound X12 payloads and automatic X12 acknowledgments. This does not choose the CMS signature digest (`signingAlgorithm` does), the signed MIME `micalg` token format (`micAlgorithmFormat` does), or the `Received-content-MIC` algorithm used when ModernEDI returns an MDN for an inbound message; that comes from the sender's receipt request.", alias="micAlgorithm")
    mic_algorithm_format: Optional[StrictStr] = Field(default='RFC_3851', description="Advanced partner-compatibility override for the S/MIME `Content-Type` `micalg` parameter on every signed MIME entity ModernEDI generates for this partner, including outbound X12 messages, automatic signed X12 acknowledgments, and the outer wrapper of signed MDNs. `RFC_5751` uses the newer hyphenated token format—for example, `sha-256`—while `RFC_3851` uses the older token `sha256`. Omit this field to use the compatibility-first `RFC_3851` default. This setting changes only the serialized notation of the signature digest selected by `signingAlgorithm` in that MIME parameter; it does not change the digest itself or the algorithm named inside `Received-content-MIC`. Change it only when the partner's AS2 profile or interoperability testing requires a particular token format.", alias="micAlgorithmFormat")
    __properties: ClassVar[List[str]] = ["signingAlgorithm", "encryptionAlgorithm", "compressionAlgorithm", "micAlgorithm", "micAlgorithmFormat"]

    @field_validator('signing_algorithm')
    def signing_algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SHA256WITHRSA', 'SHA384WITHRSA', 'SHA512WITHRSA', 'SHA1WITHRSA']):
            raise ValueError("must be one of enum values ('SHA256WITHRSA', 'SHA384WITHRSA', 'SHA512WITHRSA', 'SHA1WITHRSA')")
        return value

    @field_validator('encryption_algorithm')
    def encryption_algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AES256_CBC', 'AES128_CBC', 'DES_EDE3_CBC']):
            raise ValueError("must be one of enum values ('AES256_CBC', 'AES128_CBC', 'DES_EDE3_CBC')")
        return value

    @field_validator('compression_algorithm')
    def compression_algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ZLIB']):
            raise ValueError("must be one of enum values ('ZLIB')")
        return value

    @field_validator('mic_algorithm')
    def mic_algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SHA_1', 'SHA_256', 'SHA_512']):
            raise ValueError("must be one of enum values ('SHA_1', 'SHA_256', 'SHA_512')")
        return value

    @field_validator('mic_algorithm_format')
    def mic_algorithm_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RFC_5751', 'RFC_3851']):
            raise ValueError("must be one of enum values ('RFC_5751', 'RFC_3851')")
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
        """Create an instance of As2OutboundTransportSettings from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of As2OutboundTransportSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "signingAlgorithm": obj.get("signingAlgorithm") if obj.get("signingAlgorithm") is not None else 'SHA256WITHRSA',
            "encryptionAlgorithm": obj.get("encryptionAlgorithm") if obj.get("encryptionAlgorithm") is not None else 'AES256_CBC',
            "compressionAlgorithm": obj.get("compressionAlgorithm") if obj.get("compressionAlgorithm") is not None else 'ZLIB',
            "micAlgorithm": obj.get("micAlgorithm") if obj.get("micAlgorithm") is not None else 'SHA_256',
            "micAlgorithmFormat": obj.get("micAlgorithmFormat") if obj.get("micAlgorithmFormat") is not None else 'RFC_3851'
        }.items() if key in obj})
        return _obj
