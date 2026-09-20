# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
from inspect import getfullargspec
import json
from modernedi._wire import to_wire_value
import pprint
import re  # noqa: F401
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Optional
from modernedi.generated.models.partner_draft_x12_identities import PartnerDraftX12Identities
from modernedi.generated.models.partner_x12_identities import PartnerX12Identities
from typing import Union, Any, List, Set, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal, Self
from pydantic import Field

INTEGRATIONPARTNERX12_ANY_OF_SCHEMAS = ["PartnerDraftX12Identities", "PartnerX12Identities"]

class IntegrationPartnerX12(BaseModel):
    """
    Connected partners satisfy `PartnerX12Identities`; detached drafts may contain incomplete authoring values until an AS2 connection is attached.
    """

    # data type: PartnerX12Identities
    anyof_schema_1_validator: Optional[PartnerX12Identities] = None
    # data type: PartnerDraftX12Identities
    anyof_schema_2_validator: Optional[PartnerDraftX12Identities] = None
    if TYPE_CHECKING:
        actual_instance: Optional[Union[PartnerDraftX12Identities, PartnerX12Identities]] = None
    else:
        actual_instance: Any = None
    any_of_schemas: Set[str] = { "PartnerDraftX12Identities", "PartnerX12Identities" }

    model_config = {
        "validate_assignment": True,
        "protected_namespaces": (),
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = IntegrationPartnerX12.model_construct()
        error_messages = []
        # validate data type: PartnerX12Identities
        if not isinstance(v, PartnerX12Identities):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PartnerX12Identities`")
        else:
            return v

        # validate data type: PartnerDraftX12Identities
        if not isinstance(v, PartnerDraftX12Identities):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PartnerDraftX12Identities`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in IntegrationPartnerX12 with anyOf schemas: PartnerDraftX12Identities, PartnerX12Identities. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Self:
        return cls.from_json(json.dumps(to_wire_value(obj), ensure_ascii=False, allow_nan=False))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        # anyof_schema_1_validator: Optional[PartnerX12Identities] = None
        try:
            instance.actual_instance = PartnerX12Identities.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[PartnerDraftX12Identities] = None
        try:
            instance.actual_instance = PartnerDraftX12Identities.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into IntegrationPartnerX12 with anyOf schemas: PartnerDraftX12Identities, PartnerX12Identities. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(to_wire_value(self.actual_instance), ensure_ascii=False, allow_nan=False)

    def to_dict(self) -> Optional[Union[Dict[str, Any], PartnerDraftX12Identities, PartnerX12Identities]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            return to_wire_value(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
