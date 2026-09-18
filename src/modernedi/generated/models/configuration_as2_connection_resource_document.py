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
from modernedi.generated.models.configuration_as2_connection_spec import ConfigurationAs2ConnectionSpec
from modernedi.generated.models.configuration_document_api_version import ConfigurationDocumentApiVersion
from modernedi.generated.models.configuration_resource_metadata import ConfigurationResourceMetadata
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationAs2ConnectionResourceDocument(BaseModel):
    """
    Portable desired state for one AS2 connection.
    """ # noqa: E501
    api_version: ConfigurationDocumentApiVersion = Field(alias="apiVersion")
    kind: StrictStr
    metadata: ConfigurationResourceMetadata
    spec: ConfigurationAs2ConnectionSpec
    __properties: ClassVar[List[str]] = ["apiVersion", "kind", "metadata", "spec"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['As2Connection']):
            raise ValueError("must be one of enum values ('As2Connection')")
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
        """Create an instance of ConfigurationAs2ConnectionResourceDocument from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spec
        if self.spec:
            _dict['spec'] = self.spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationAs2ConnectionResourceDocument from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "apiVersion": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "metadata": ConfigurationResourceMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "spec": ConfigurationAs2ConnectionSpec.from_dict(obj["spec"]) if obj.get("spec") is not None else None
        }.items() if key in obj})
        return _obj
