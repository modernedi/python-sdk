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
from typing_extensions import Annotated
from modernedi.generated.models.configuration_document_api_version import ConfigurationDocumentApiVersion
from modernedi.generated.models.configuration_snapshot_resource import ConfigurationSnapshotResource
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationSnapshotState(BaseModel):
    """
    Observed server state stored at `_state/snapshot.json`. It relates portable resource keys to current workspace ids, API ETags, and exported resource hashes.
    """ # noqa: E501
    api_version: ConfigurationDocumentApiVersion = Field(alias="apiVersion")
    kind: StrictStr
    runtime_configuration_revision: Annotated[int, Field(strict=True, ge=0)] = Field(description="Monotonic workspace runtime-configuration revision observed by this export transaction.", alias="runtimeConfigurationRevision")
    bundle_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="bundleSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    resources: List[ConfigurationSnapshotResource] = Field(description="Observed resource state sorted by kind and portable key.")
    __properties: ClassVar[List[str]] = ["apiVersion", "kind", "runtimeConfigurationRevision", "bundleSha256", "resources"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['IntegrationConfigurationSnapshot']):
            raise ValueError("must be one of enum values ('IntegrationConfigurationSnapshot')")
        return value

    @field_validator('bundle_sha256', mode="before")
    def bundle_sha256_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationSnapshotState from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationSnapshotState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "apiVersion": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "runtimeConfigurationRevision": obj.get("runtimeConfigurationRevision"),
            "bundleSha256": obj.get("bundleSha256"),
            "resources": [ConfigurationSnapshotResource.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None
        }.items() if key in obj})
        return _obj
