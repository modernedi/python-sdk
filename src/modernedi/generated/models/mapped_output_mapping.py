# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappedOutputMapping(BaseModel):
    """
    Identity and immutable execution provenance of the published incoming map that generated a queued output.
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Workspace-scoped mapping id, or `null` for historical outputs that predate persisted map identity.", json_schema_extra={"examples": [44]})
    type: Optional[StrictStr] = Field(default=None, description="Runtime mapping implementation name, or `null` when it was not recorded with an older output.", json_schema_extra={"examples": ["ManagedQueueMapping"]})
    file: Optional[StrictStr] = Field(default=None, description="Customer-visible source filename, or `null` when unavailable on an older output.", json_schema_extra={"examples": ["customer-one-850.jslt"]})
    file_sha256_hash: Optional[StrictStr] = Field(default=None, description="Base64-encoded SHA-256 hash of the published map contents. Omitted when `deliveredMetadata.mappingSourceHash` is `false`. ", alias="fileSha256Hash", json_schema_extra={"examples": ["5vG51TfOLEo9YN0WSMf0bj+xzluq2UptTm4flVSo8EE="]})
    syntax_tree_catalog_revision: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Immutable grammar-catalog revision declared by the mapping execution; omitted for legacy outputs.", alias="syntaxTreeCatalogRevision")
    syntax_tree_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="SHA-256 of the exact transaction-set grammar bytes used by the mapping execution; omitted for legacy outputs.", alias="syntaxTreeSha256")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "type", "file", "fileSha256Hash", "syntaxTreeCatalogRevision", "syntaxTreeSha256"]

    @field_validator('syntax_tree_catalog_revision', mode="before")
    def syntax_tree_catalog_revision_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('syntax_tree_sha256', mode="before")
    def syntax_tree_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of MappedOutputMapping from a JSON string"""
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

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if file (nullable) is None
        # and model_fields_set contains the field
        if self.file is None and "file" in self.model_fields_set:
            _dict['file'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappedOutputMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "type": obj.get("type"),
            "file": obj.get("file"),
            "fileSha256Hash": obj.get("fileSha256Hash"),
            "syntaxTreeCatalogRevision": obj.get("syntaxTreeCatalogRevision"),
            "syntaxTreeSha256": obj.get("syntaxTreeSha256")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
