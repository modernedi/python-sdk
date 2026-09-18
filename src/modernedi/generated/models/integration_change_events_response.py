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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.integration_change_event import IntegrationChangeEvent
from modernedi.generated.models.transaction_attention_freshness import TransactionAttentionFreshness
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class IntegrationChangeEventsResponse(BaseModel):
    """
    Bootstrap cursor or chronological page of transaction-state invalidations.
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true`; invalid or expired cursors use a structured error response.")
    environment: TransactionEnvironmentValue
    events: List[IntegrationChangeEvent] = Field(description="Events strictly after the supplied cursor, ordered by detection sequence.")
    next_cursor: StrictStr = Field(description="Opaque, integrity-protected cursor bound to this tenant and environment. Return it unchanged on the next poll, including after an empty page. Editing it or using it for another tenant or environment returns HTTP 400. ", alias="nextCursor")
    has_more: StrictBool = Field(description="True when another page is already available after `nextCursor`.", alias="hasMore")
    bootstrap: StrictBool = Field(description="True only when the request omitted `cursor` and established a high-water mark.")
    retention_seconds: Annotated[int, Field(strict=True, ge=1)] = Field(description="Rolling retention of this invalidation feed; independent of transaction-document retention.", alias="retentionSeconds", json_schema_extra={"examples": [2592000]})
    freshness: TransactionAttentionFreshness
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "environment", "events", "nextCursor", "hasMore", "bootstrap", "retentionSeconds", "freshness"]

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
        """Create an instance of IntegrationChangeEventsResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item_events in self.events:
                if _item_events:
                    _items.append(_item_events.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of freshness
        if self.freshness:
            _dict['freshness'] = self.freshness.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IntegrationChangeEventsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "environment": obj.get("environment"),
            "events": [IntegrationChangeEvent.from_dict(_item) for _item in obj["events"]] if obj.get("events") is not None else None,
            "nextCursor": obj.get("nextCursor"),
            "hasMore": obj.get("hasMore"),
            "bootstrap": obj.get("bootstrap"),
            "retentionSeconds": obj.get("retentionSeconds"),
            "freshness": TransactionAttentionFreshness.from_dict(obj["freshness"]) if obj.get("freshness") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
