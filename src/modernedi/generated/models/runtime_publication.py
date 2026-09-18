# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class RuntimePublication(BaseModel):
    """
    Publication state for a committed partner, AS2 connection, mapping, or aggregate configuration mutation. This field is not returned by ordinary reads or webhook configuration changes.
    """ # noqa: E501
    state: StrictStr = Field(description="- `published`: the tenant runtime configuration was published successfully, either inline during rollout or by updating its external configuration pointer. - `pending`: the database mutation committed, but runtime publication failed. ModernEDI's reconciler retries automatically. - `not_provisioned`: the tenant does not have runtime infrastructure yet, so there is no runtime context to publish. ")
    retrying: StrictBool = Field(description="True while the reconciler will continue retrying a pending publication.")
    message: Optional[StrictStr] = Field(default=None, description="Optional safe operational context when publication is pending or not provisioned.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["state", "retrying", "message"]

    @field_validator('state')
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['published', 'pending', 'not_provisioned']):
            raise ValueError("must be one of enum values ('published', 'pending', 'not_provisioned')")
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
        """Create an instance of RuntimePublication from a JSON string"""
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
        """Create an instance of RuntimePublication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "state": obj.get("state"),
            "retrying": obj.get("retrying"),
            "message": obj.get("message")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
