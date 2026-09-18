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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.configuration_export_file import ConfigurationExportFile
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationExportResponse(BaseModel):
    """
    Deterministic logical file bundle representing the workspace's current exportable configuration and its observed API state.
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true`; failures use the documented error response instead.")
    bundle_sha256: Annotated[str, Field(strict=True)] = Field(description="SHA-256 of the canonical `modernedi.json` manifest content. This identifies the portable desired-state bundle and excludes `_state/snapshot.json`.", alias="bundleSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    snapshot_sha256: Annotated[str, Field(strict=True)] = Field(description="SHA-256 of the canonical `_state/snapshot.json` content, including current database ids and public API ETags.", alias="snapshotSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    snapshot_etag: Annotated[str, Field(strict=True)] = Field(description="Quoted `snapshotSha256`, also returned in the HTTP `ETag` header and accepted by `If-None-Match`.", alias="snapshotEtag")
    files: List[ConfigurationExportFile] = Field(description="Complete export sorted lexicographically by `path`. It contains the desired resource and source files plus `modernedi.json` and `_state/snapshot.json`.")
    __properties: ClassVar[List[str]] = ["success", "bundleSha256", "snapshotSha256", "snapshotEtag", "files"]

    @field_validator('bundle_sha256', mode="before")
    def bundle_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('snapshot_sha256', mode="before")
    def snapshot_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('snapshot_etag', mode="before")
    def snapshot_etag_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationExportResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item_files in self.files:
                if _item_files:
                    _items.append(_item_files.to_dict())
            _dict['files'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationExportResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "bundleSha256": obj.get("bundleSha256"),
            "snapshotSha256": obj.get("snapshotSha256"),
            "snapshotEtag": obj.get("snapshotEtag"),
            "files": [ConfigurationExportFile.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None
        }.items() if key in obj})
        return _obj
