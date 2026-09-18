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
from uuid import UUID
from modernedi.generated.models.configuration_resource_kind import ConfigurationResourceKind
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationSnapshotResource(BaseModel):
    """
    ConfigurationSnapshotResource
    """ # noqa: E501
    kind: ConfigurationResourceKind
    key: UUID = Field(description="Stable portable identity from the corresponding resource document.")
    resource_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="Current workspace-scoped database id used by the existing per-resource Integration API endpoints.", alias="resourceId")
    content_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="contentSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    api_etag: Annotated[str, Field(strict=True)] = Field(description="Current quoted ETag from the corresponding partner, AS2 connection, or mapping API representation.", alias="apiEtag")
    __properties: ClassVar[List[str]] = ["kind", "key", "resourceId", "contentSha256", "apiEtag"]

    @field_validator('content_sha256', mode="before")
    def content_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('api_etag', mode="before")
    def api_etag_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\"[0-9a-f]{64}\"$", value):
            raise ValueError(r"must validate the regular expression /^\"[0-9a-f]{64}\"$/")
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
        """Create an instance of ConfigurationSnapshotResource from a JSON string"""
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
        """Create an instance of ConfigurationSnapshotResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "kind": obj.get("kind"),
            "key": obj.get("key"),
            "resourceId": obj.get("resourceId"),
            "contentSha256": obj.get("contentSha256"),
            "apiEtag": obj.get("apiEtag")
        }.items() if key in obj})
        return _obj
