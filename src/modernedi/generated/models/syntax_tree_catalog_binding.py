# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class SyntaxTreeCatalogBinding(BaseModel):
    """
    Content-addressed identifiers for the exact X12 grammar used to validate and execute a mapping. These values support reproducibility and diagnostics and do not expose internal storage locations.
    """ # noqa: E501
    schema_version: StrictInt = Field(description="Version of this catalog-binding metadata contract, used by clients to interpret the immutable grammar identifiers safely.", alias="schemaVersion")
    catalog_revision: Annotated[str, Field(strict=True)] = Field(description="SHA-256 identity of the complete immutable syntax-tree catalog at approval time. This approval revision can differ from a later active platform catalog when syntaxTreeSha256 proves that the exact grammar for this mapping's X12 version and transaction set is unchanged. ", alias="catalogRevision")
    manifest_sha256: Annotated[str, Field(strict=True)] = Field(description="SHA-256 of the canonical catalog manifest.", alias="manifestSha256")
    syntax_tree_sha256: Annotated[str, Field(strict=True)] = Field(description="SHA-256 of the exact normalized grammar bytes for this X12 version and transaction set.", alias="syntaxTreeSha256")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["schemaVersion", "catalogRevision", "manifestSha256", "syntaxTreeSha256"]

    @field_validator('schema_version')
    def schema_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set([1]):
            raise ValueError("must be one of enum values (1)")
        return value

    @field_validator('catalog_revision', mode="before")
    def catalog_revision_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('manifest_sha256', mode="before")
    def manifest_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('syntax_tree_sha256', mode="before")
    def syntax_tree_sha256_validate_regular_expression(cls, value):
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
        """Create an instance of SyntaxTreeCatalogBinding from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SyntaxTreeCatalogBinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "schemaVersion": obj.get("schemaVersion"),
            "catalogRevision": obj.get("catalogRevision"),
            "manifestSha256": obj.get("manifestSha256"),
            "syntaxTreeSha256": obj.get("syntaxTreeSha256")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
