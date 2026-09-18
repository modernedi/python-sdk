# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappedOutputAcknowledgment(BaseModel):
    """
    Durable receipt record proving when your integration acknowledged one mapped output version.
    """ # noqa: E501
    id: StrictStr = Field(description="Stable generated-output version id that was acknowledged.")
    message_id: StrictStr = Field(description="Original inbound AS2 message id associated with the acknowledged output.", alias="messageId")
    mapped_output_key: StrictStr = Field(description="Unique mapped-output key within the source transaction.", alias="mappedOutputKey")
    acked_at: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="ackedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "messageId", "mappedOutputKey", "ackedAt"]

    @field_validator('acked_at', mode="before")
    def acked_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
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
        """Create an instance of MappedOutputAcknowledgment from a JSON string"""
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

        # set to None if acked_at (nullable) is None
        # and model_fields_set contains the field
        if self.acked_at is None and "acked_at" in self.model_fields_set:
            _dict['ackedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappedOutputAcknowledgment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "messageId": obj.get("messageId"),
            "mappedOutputKey": obj.get("mappedOutputKey"),
            "ackedAt": obj.get("ackedAt")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
