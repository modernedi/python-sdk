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
from modernedi.generated.models.transaction_mapped_output import TransactionMappedOutput
from modernedi.generated.models.transaction_replay import TransactionReplay
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionReplayResponse(BaseModel):
    """
    Atomic response-only replay result using the mappings currently published for the partner.
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true`; replay validation or execution failures use the replay error response.")
    replay: TransactionReplay
    regenerated_outputs: List[TransactionMappedOutput] = Field(description="Newly generated map results. They are not enqueued and do not trigger mapped-output webhooks.", alias="regeneratedOutputs")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "replay", "regeneratedOutputs"]

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
        """Create an instance of TransactionReplayResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of replay
        if self.replay:
            _dict['replay'] = self.replay.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in regenerated_outputs (list)
        _items = []
        if self.regenerated_outputs:
            for _item_regenerated_outputs in self.regenerated_outputs:
                if _item_regenerated_outputs:
                    _items.append(_item_regenerated_outputs.to_dict())
            _dict['regeneratedOutputs'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionReplayResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "replay": TransactionReplay.from_dict(obj["replay"]) if obj.get("replay") is not None else None,
            "regeneratedOutputs": [TransactionMappedOutput.from_dict(_item) for _item in obj["regeneratedOutputs"]] if obj.get("regeneratedOutputs") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
