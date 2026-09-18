# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict
from modernedi.generated.models.configuration_context_response_api_key import ConfigurationContextResponseApiKey
from modernedi.generated.models.configuration_context_response_workspace import ConfigurationContextResponseWorkspace
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationContextResponse(BaseModel):
    """
    ConfigurationContextResponse
    """ # noqa: E501
    success: StrictBool
    workspace: ConfigurationContextResponseWorkspace
    api_key: ConfigurationContextResponseApiKey = Field(alias="apiKey")
    __properties: ClassVar[List[str]] = ["success", "workspace", "apiKey"]

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
        """Create an instance of ConfigurationContextResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of workspace
        if self.workspace:
            _dict['workspace'] = self.workspace.to_dict()
        # override the default output from pydantic by calling `to_dict()` of api_key
        if self.api_key:
            _dict['apiKey'] = self.api_key.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationContextResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "workspace": ConfigurationContextResponseWorkspace.from_dict(obj["workspace"]) if obj.get("workspace") is not None else None,
            "apiKey": ConfigurationContextResponseApiKey.from_dict(obj["apiKey"]) if obj.get("apiKey") is not None else None
        }.items() if key in obj})
        return _obj
