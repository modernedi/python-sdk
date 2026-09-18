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
from modernedi.generated.models.configuration_snapshot_state import ConfigurationSnapshotState
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationPlanAdvisoryStateFile(BaseModel):
    """
    Optional untrusted snapshot copied from configuration export. It is accepted only with the canonical path, role, and JSON representation. ModernEDI compares its digest with current state to report `BASE_SNAPSHOT_STALE`, but never trusts its database ids, ETags, revision, or resource inventory as mutation authority.
    """ # noqa: E501
    path: StrictStr
    role: StrictStr
    format: StrictStr
    media_type: StrictStr = Field(alias="mediaType")
    content_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="contentSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    content: ConfigurationSnapshotState
    __properties: ClassVar[List[str]] = ["path", "role", "format", "mediaType", "contentSha256", "content"]

    @field_validator('path')
    def path_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['_state/snapshot.json']):
            raise ValueError("must be one of enum values ('_state/snapshot.json')")
        return value

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['STATE']):
            raise ValueError("must be one of enum values ('STATE')")
        return value

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['JSON']):
            raise ValueError("must be one of enum values ('JSON')")
        return value

    @field_validator('media_type')
    def media_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['application/json']):
            raise ValueError("must be one of enum values ('application/json')")
        return value

    @field_validator('content_sha256', mode="before")
    def content_sha256_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationPlanAdvisoryStateFile from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict['content'] = self.content.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationPlanAdvisoryStateFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "path": obj.get("path"),
            "role": obj.get("role"),
            "format": obj.get("format"),
            "mediaType": obj.get("mediaType"),
            "contentSha256": obj.get("contentSha256"),
            "content": ConfigurationSnapshotState.from_dict(obj["content"]) if obj.get("content") is not None else None
        }.items() if key in obj})
        return _obj
