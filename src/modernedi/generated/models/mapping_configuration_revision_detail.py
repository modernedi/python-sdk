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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.mapping_configuration_revision_transform_detail import MappingConfigurationRevisionTransformDetail
from modernedi.generated.models.syntax_tree_catalog_binding import SyntaxTreeCatalogBinding
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappingConfigurationRevisionDetail(BaseModel):
    """
    MappingConfigurationRevisionDetail
    """ # noqa: E501
    revision_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="Immutable id for this stored mapping-configuration revision.", alias="revisionId")
    created_at: str = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`.", alias="createdAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    source_hash: StrictStr = Field(description="Base64-encoded SHA-256 hash of the transform source text. This identifies source content; it is not a concurrency-control ETag.", alias="sourceHash", json_schema_extra={"examples": ["5vG51TfOLEo9YN0WSMf0bj+xzluq2UptTm4flVSo8EE="]})
    configuration_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(description="Lowercase hexadecimal SHA-256 identity of the complete immutable mapping configuration, or `null` for a legacy revision written before exact configuration identities were recorded.", alias="configurationSha256", json_schema_extra={"examples": ["d52e4b71d52e4b71d52e4b71d52e4b71d52e4b71d52e4b71d52e4b71d52e4b71"]})
    current: StrictBool = Field(description="Whether this exact mapping configuration is currently published. Source text alone is insufficient to make a revision current.")
    syntax_tree_catalog: Optional[SyntaxTreeCatalogBinding] = Field(default=None, alias="syntaxTreeCatalog")
    transform: MappingConfigurationRevisionTransformDetail
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["revisionId", "createdAt", "sourceHash", "configurationSha256", "current", "syntaxTreeCatalog", "transform"]

    @field_validator('created_at', mode="before")
    def created_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('configuration_sha256', mode="before")
    def configuration_sha256_validate_regular_expression(cls, value):
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
        """Create an instance of MappingConfigurationRevisionDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of syntax_tree_catalog
        if self.syntax_tree_catalog:
            _dict['syntaxTreeCatalog'] = self.syntax_tree_catalog.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transform
        if self.transform:
            _dict['transform'] = self.transform.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if configuration_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.configuration_sha256 is None and "configuration_sha256" in self.model_fields_set:
            _dict['configurationSha256'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappingConfigurationRevisionDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "revisionId": obj.get("revisionId"),
            "createdAt": obj.get("createdAt"),
            "sourceHash": obj.get("sourceHash"),
            "configurationSha256": obj.get("configurationSha256"),
            "current": obj.get("current"),
            "syntaxTreeCatalog": SyntaxTreeCatalogBinding.from_dict(obj["syntaxTreeCatalog"]) if obj.get("syntaxTreeCatalog") is not None else None,
            "transform": MappingConfigurationRevisionTransformDetail.from_dict(obj["transform"]) if obj.get("transform") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
