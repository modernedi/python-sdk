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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.mapped_output_acknowledgment import MappedOutputAcknowledgment
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappedOutputBulkAckResponse(BaseModel):
    """
    Atomic confirmation that every requested mapped-output lease was acknowledged.
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true`; if any lease is invalid the entire request fails and no output is acknowledged.")
    environment: TransactionEnvironmentValue = Field(description="Selects the isolated transaction history containing the original transaction. Defaults to `production` when omitted.")
    acknowledged_count: Annotated[int, Field(le=100, strict=True, ge=1)] = Field(description="Number of outputs acknowledged by this atomic batch.", alias="acknowledgedCount")
    acknowledgments: List[MappedOutputAcknowledgment] = Field(description="Canonical acknowledgment records in the same successful batch.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "environment", "acknowledgedCount", "acknowledgments"]

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
        """Create an instance of MappedOutputBulkAckResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in acknowledgments (list)
        _items = []
        if self.acknowledgments:
            for _item_acknowledgments in self.acknowledgments:
                if _item_acknowledgments:
                    _items.append(_item_acknowledgments.to_dict())
            _dict['acknowledgments'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappedOutputBulkAckResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "environment": obj.get("environment"),
            "acknowledgedCount": obj.get("acknowledgedCount"),
            "acknowledgments": [MappedOutputAcknowledgment.from_dict(_item) for _item in obj["acknowledgments"]] if obj.get("acknowledgments") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
