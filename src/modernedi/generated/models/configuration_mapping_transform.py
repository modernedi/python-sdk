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
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationMappingTransform(BaseModel):
    """
    ConfigurationMappingTransform
    """ # noqa: E501
    type: StrictStr = Field(description="Executable mapping language.")
    file_name: Annotated[str, Field(min_length=1, strict=True, max_length=255)] = Field(description="Source-controlled transform filename shown in workspace and transaction provenance.", alias="fileName")
    source_path: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Relative path of the corresponding `SOURCE` file in this bundle.", alias="sourcePath")
    source_sha256: Annotated[str, Field(strict=True)] = Field(description="SHA-256 of the exact UTF-8 mapping source bytes at `sourcePath`.", alias="sourceSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    __properties: ClassVar[List[str]] = ["type", "fileName", "sourcePath", "sourceSha256"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['X12_MAPPER', 'XSLT', 'JSLT']):
            raise ValueError("must be one of enum values ('X12_MAPPER', 'XSLT', 'JSLT')")
        return value

    @field_validator('source_path', mode="before")
    def source_path_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z0-9._\/-]+$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9._\/-]+$/")
        return value

    @field_validator('source_sha256', mode="before")
    def source_sha256_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationMappingTransform from a JSON string"""
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
        """Create an instance of ConfigurationMappingTransform from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "type": obj.get("type"),
            "fileName": obj.get("fileName"),
            "sourcePath": obj.get("sourcePath"),
            "sourceSha256": obj.get("sourceSha256")
        }.items() if key in obj})
        return _obj
