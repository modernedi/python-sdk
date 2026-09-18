# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationAs2FileEnvironment(BaseModel):
    """
    ConfigurationAs2FileEnvironment
    """ # noqa: E501
    as2_identifier: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="as2Identifier")
    endpoint_url: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(description="The same publicly routable destination and workspace plan restrictions as the partner form apply.", alias="endpointUrl")
    public_certificate_path: Annotated[str, Field(strict=True)] = Field(description="Relative to connection.json. Production and Test may reference the same file. The file name uses 1-64 lowercase letters, digits, hyphens or underscores and starts with a letter or digit. No absolute paths, URLs, traversal, subdirectories, or other connections. Exports use shared.pem when both environments have the same certificate; otherwise production.pem and test.pem.", alias="publicCertificatePath", json_schema_extra={"examples": ["./certificates/shared.pem"]})
    public_certificate_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="publicCertificateSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    require_signature: StrictBool = Field(alias="requireSignature")
    require_encryption: StrictBool = Field(alias="requireEncryption")
    __properties: ClassVar[List[str]] = ["as2Identifier", "endpointUrl", "publicCertificatePath", "publicCertificateSha256", "requireSignature", "requireEncryption"]

    @field_validator('public_certificate_path', mode="before")
    def public_certificate_path_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\.\/certificates\/[a-z0-9][a-z0-9_-]{0,63}\.pem(?![\s\S])", value):
            raise ValueError(r"must validate the regular expression /^\.\/certificates\/[a-z0-9][a-z0-9_-]{0,63}\.pem(?![\s\S])/")
        return value

    @field_validator('public_certificate_sha256', mode="before")
    def public_certificate_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
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
        """Create an instance of ConfigurationAs2FileEnvironment from a JSON string"""
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
        # set to None if endpoint_url (nullable) is None
        # and model_fields_set contains the field
        if self.endpoint_url is None and "endpoint_url" in self.model_fields_set:
            _dict['endpointUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationAs2FileEnvironment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "as2Identifier": obj.get("as2Identifier"),
            "endpointUrl": obj.get("endpointUrl"),
            "publicCertificatePath": obj.get("publicCertificatePath"),
            "publicCertificateSha256": obj.get("publicCertificateSha256"),
            "requireSignature": obj.get("requireSignature"),
            "requireEncryption": obj.get("requireEncryption")
        }.items() if key in obj})
        return _obj
