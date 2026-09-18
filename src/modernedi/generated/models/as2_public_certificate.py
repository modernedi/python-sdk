# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2PublicCertificate(BaseModel):
    """
    Public half of a ModernEDI AS2 signing/encryption certificate; private keys are never exposed.
    """ # noqa: E501
    slot: StrictStr = Field(description="Certificate lifecycle slot: `active` is in service and `next` is staged for partner-by-partner rollover.")
    subject_dn: Optional[StrictStr] = Field(default=None, description="X.509 subject distinguished name, or `null` when certificate parsing did not provide it.", alias="subjectDn")
    issuer_dn: Optional[StrictStr] = Field(default=None, description="X.509 issuer distinguished name, or `null` when certificate parsing did not provide it.", alias="issuerDn")
    serial_number: Optional[StrictStr] = Field(default=None, description="Certificate serial number rendered for partner correlation, or `null` when unavailable.", alias="serialNumber")
    fingerprint_sha256: Optional[StrictStr] = Field(default=None, description="SHA-256 certificate fingerprint for out-of-band verification, or `null` when unavailable.", alias="fingerprintSha256")
    not_before: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="notBefore", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    not_after: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="notAfter", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    public_cert_pem: StrictStr = Field(description="PEM-encoded public certificate safe to share with trading partners.", alias="publicCertPem")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["slot", "subjectDn", "issuerDn", "serialNumber", "fingerprintSha256", "notBefore", "notAfter", "publicCertPem"]

    @field_validator('slot')
    def slot_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['active', 'next']):
            raise ValueError("must be one of enum values ('active', 'next')")
        return value

    @field_validator('not_before', mode="before")
    def not_before_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('not_after', mode="before")
    def not_after_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
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
        """Create an instance of As2PublicCertificate from a JSON string"""
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

        # set to None if subject_dn (nullable) is None
        # and model_fields_set contains the field
        if self.subject_dn is None and "subject_dn" in self.model_fields_set:
            _dict['subjectDn'] = None

        # set to None if issuer_dn (nullable) is None
        # and model_fields_set contains the field
        if self.issuer_dn is None and "issuer_dn" in self.model_fields_set:
            _dict['issuerDn'] = None

        # set to None if serial_number (nullable) is None
        # and model_fields_set contains the field
        if self.serial_number is None and "serial_number" in self.model_fields_set:
            _dict['serialNumber'] = None

        # set to None if fingerprint_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.fingerprint_sha256 is None and "fingerprint_sha256" in self.model_fields_set:
            _dict['fingerprintSha256'] = None

        # set to None if not_before (nullable) is None
        # and model_fields_set contains the field
        if self.not_before is None and "not_before" in self.model_fields_set:
            _dict['notBefore'] = None

        # set to None if not_after (nullable) is None
        # and model_fields_set contains the field
        if self.not_after is None and "not_after" in self.model_fields_set:
            _dict['notAfter'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of As2PublicCertificate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "slot": obj.get("slot"),
            "subjectDn": obj.get("subjectDn"),
            "issuerDn": obj.get("issuerDn"),
            "serialNumber": obj.get("serialNumber"),
            "fingerprintSha256": obj.get("fingerprintSha256"),
            "notBefore": obj.get("notBefore"),
            "notAfter": obj.get("notAfter"),
            "publicCertPem": obj.get("publicCertPem")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
