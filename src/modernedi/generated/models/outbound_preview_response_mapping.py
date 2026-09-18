# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class OutboundPreviewResponseMapping(BaseModel):
    """
    Published outgoing map selected from the partner, content type, X12 version, and request route.
    """ # noqa: E501
    id: StrictInt = Field(description="Stable workspace-scoped identifier of the selected outgoing map.")
    transform_type: StrictStr = Field(description="Transform engine used by the published map, such as `xslt` or `jslt`.", alias="transformType", json_schema_extra={"examples": ["xslt"]})
    file: StrictStr = Field(description="Customer-visible transform filename recorded for the selected map.")
    file_sha256_hash: StrictStr = Field(description="Base64-encoded SHA-256 hash of the published map contents.", alias="fileSha256Hash", json_schema_extra={"examples": ["5vG51TfOLEo9YN0WSMf0bj+xzluq2UptTm4flVSo8EE="]})
    content_type: StrictStr = Field(description="Source media type expected by the selected outgoing map.", alias="contentType")
    x12_version: StrictStr = Field(description="X12 version the selected map generates.", alias="x12Version")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "transformType", "file", "fileSha256Hash", "contentType", "x12Version"]

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
        """Create an instance of OutboundPreviewResponseMapping from a JSON string"""
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
        """Create an instance of OutboundPreviewResponseMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "transformType": obj.get("transformType"),
            "file": obj.get("file"),
            "fileSha256Hash": obj.get("fileSha256Hash"),
            "contentType": obj.get("contentType"),
            "x12Version": obj.get("x12Version")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
