# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from modernedi.generated.models.transaction_mapping_attempt import TransactionMappingAttempt
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappingRuntimeFailuresResponse(BaseModel):
    """
    MappingRuntimeFailuresResponse
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true`; invalid filters, cursors, or runtime-read failures use an error response.")
    environment: TransactionEnvironmentValue
    failures: List[TransactionMappingAttempt] = Field(description="Reverse-chronological safe diagnostics matching the supplied environment and filters.")
    next_cursor: Optional[StrictStr] = Field(description="Opaque cursor for the next page, or `null` when this page is complete.", alias="nextCursor")
    has_more: StrictBool = Field(description="True when `nextCursor` should be sent back for another page.", alias="hasMore")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "environment", "failures", "nextCursor", "hasMore"]

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
        """Create an instance of MappingRuntimeFailuresResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in failures (list)
        _items = []
        if self.failures:
            for _item_failures in self.failures:
                if _item_failures:
                    _items.append(_item_failures.to_dict())
            _dict['failures'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if next_cursor (nullable) is None
        # and model_fields_set contains the field
        if self.next_cursor is None and "next_cursor" in self.model_fields_set:
            _dict['nextCursor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappingRuntimeFailuresResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "environment": obj.get("environment"),
            "failures": [TransactionMappingAttempt.from_dict(_item) for _item in obj["failures"]] if obj.get("failures") is not None else None,
            "nextCursor": obj.get("nextCursor"),
            "hasMore": obj.get("hasMore")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
