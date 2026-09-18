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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionReplayRequest(BaseModel):
    """
    TransactionReplayRequest
    """ # noqa: E501
    environment: Optional[TransactionEnvironmentValue] = None
    mode: Optional[StrictStr] = Field(default='current_maps', description="Uses the mappings currently published for the partner. This is the only public replay mode.")
    delivery: Optional[StrictStr] = Field(default='response_only', description="Regenerated outputs are returned only; no queue item, webhook, or outbound acknowledgment is produced.")
    reason: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, description="Optional operator or automation context recorded on the replay attempt.")
    __properties: ClassVar[List[str]] = ["environment", "mode", "delivery", "reason"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['current_maps']):
            raise ValueError("must be one of enum values ('current_maps')")
        return value

    @field_validator('delivery')
    def delivery_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['response_only']):
            raise ValueError("must be one of enum values ('response_only')")
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
        """Create an instance of TransactionReplayRequest from a JSON string"""
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
        # set to None if reason (nullable) is None
        # and model_fields_set contains the field
        if self.reason is None and "reason" in self.model_fields_set:
            _dict['reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionReplayRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "environment": obj.get("environment"),
            "mode": obj.get("mode") if obj.get("mode") is not None else 'current_maps',
            "delivery": obj.get("delivery") if obj.get("delivery") is not None else 'response_only',
            "reason": obj.get("reason")
        }.items() if key in obj})
        return _obj
