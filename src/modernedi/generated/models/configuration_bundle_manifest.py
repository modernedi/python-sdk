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
from typing import Any, ClassVar, Dict, List
from modernedi.generated.models.configuration_document_api_version import ConfigurationDocumentApiVersion
from modernedi.generated.models.configuration_manifest_file import ConfigurationManifestFile
from modernedi.generated.models.configuration_manifest_resource import ConfigurationManifestResource
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationBundleManifest(BaseModel):
    """
    Portable desired-state manifest stored at `modernedi.json`. It inventories resources and all desired files but intentionally excludes the manifest itself and `_state/snapshot.json`.
    """ # noqa: E501
    api_version: ConfigurationDocumentApiVersion = Field(alias="apiVersion")
    kind: StrictStr
    resources: List[ConfigurationManifestResource] = Field(description="Exported resources sorted lexicographically by their resource-document path.")
    files: List[ConfigurationManifestFile] = Field(description="Resource and mapping-source files sorted lexicographically by path. Manifest and state files are excluded.")
    __properties: ClassVar[List[str]] = ["apiVersion", "kind", "resources", "files"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['IntegrationConfiguration']):
            raise ValueError("must be one of enum values ('IntegrationConfiguration')")
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
        """Create an instance of ConfigurationBundleManifest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in resources (list)
        _items = []
        if self.resources:
            for _item_resources in self.resources:
                if _item_resources:
                    _items.append(_item_resources.to_dict())
            _dict['resources'] = _items
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
        """Create an instance of ConfigurationBundleManifest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "apiVersion": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "resources": [ConfigurationManifestResource.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None,
            "files": [ConfigurationManifestFile.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None
        }.items() if key in obj})
        return _obj
