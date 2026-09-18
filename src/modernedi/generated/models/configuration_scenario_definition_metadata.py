# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionMetadata(BaseModel):
    """
    Immutable identity of a published definition. The identity tuple is namespace, key, and version; contentSha256 is computed when the definition is published.
    """ # noqa: E501
    namespace: Annotated[str, Field(strict=True, max_length=253)] = Field(description="A lowercase, DNS-like ownership namespace.")
    key: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    version: Annotated[str, Field(min_length=1, strict=True, max_length=64)] = Field(description="A trim-exact artifact version with no control characters. This versions a published definition; it is separate from apiVersion.")
    __properties: ClassVar[List[str]] = ["namespace", "key", "version"]

    @field_validator('namespace', mode="before")
    def namespace_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[a-z0-9]+(?:[.-][a-z0-9]+)*$", value):
            raise ValueError(r"must validate the regular expression /^[a-z0-9]+(?:[.-][a-z0-9]+)*$/")
        return value

    @field_validator('key', mode="before")
    def key_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('version', mode="before")
    def version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^(?!\s)(?!.*\s$)[^\u0000-\u001F\u007F]+$", value):
            raise ValueError(r"must validate the regular expression /^(?!\s)(?!.*\s$)[^\u0000-\u001F\u007F]+$/")
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
        """Create an instance of ConfigurationScenarioDefinitionMetadata from a JSON string"""
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
        """Create an instance of ConfigurationScenarioDefinitionMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "namespace": obj.get("namespace"),
            "key": obj.get("key"),
            "version": obj.get("version")
        }.items() if key in obj})
        return _obj
