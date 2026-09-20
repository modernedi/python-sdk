# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from modernedi._wire import to_wire_value
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from modernedi.generated.models.business_effective_timestamp import BusinessEffectiveTimestamp
from modernedi.generated.models.time_modern_edi_observed_the_revision import TimeModernEDIObservedTheRevision
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGURATIONSCENARIODEFINITIONEFFECTIVEAT_ONE_OF_SCHEMAS = ["BusinessEffectiveTimestamp", "TimeModernEDIObservedTheRevision"]

class ConfigurationScenarioDefinitionEffectiveAt(BaseModel):
    """
    When a replacement or cancellation begins to govern the conversation. observed_at uses the time ModernEDI observed the later document. value uses an explicit timestamp, such as effectiveTimestamp extracted from an X12 860 order change. The value must be a timestamp, not only a date or clock time. A fact value belongs to the matched revision pair and must come from its source or later document; for a previous-matched same-step revision, it is read from the later revision occurrence.
    """
    # data type: TimeModernEDIObservedTheRevision
    oneof_schema_1_validator: Optional[TimeModernEDIObservedTheRevision] = None
    # data type: BusinessEffectiveTimestamp
    oneof_schema_2_validator: Optional[BusinessEffectiveTimestamp] = None
    actual_instance: Optional[Union[BusinessEffectiveTimestamp, TimeModernEDIObservedTheRevision]] = None
    one_of_schemas: Set[str] = { "BusinessEffectiveTimestamp", "TimeModernEDIObservedTheRevision" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )

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
    def actual_instance_must_validate_oneof(cls, v):
        instance = ConfigurationScenarioDefinitionEffectiveAt.model_construct()
        error_messages = []
        match = 0
        # validate data type: TimeModernEDIObservedTheRevision
        if not isinstance(v, TimeModernEDIObservedTheRevision):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TimeModernEDIObservedTheRevision`")
        else:
            match += 1
        # validate data type: BusinessEffectiveTimestamp
        if not isinstance(v, BusinessEffectiveTimestamp):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BusinessEffectiveTimestamp`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigurationScenarioDefinitionEffectiveAt with oneOf schemas: BusinessEffectiveTimestamp, TimeModernEDIObservedTheRevision. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigurationScenarioDefinitionEffectiveAt with oneOf schemas: BusinessEffectiveTimestamp, TimeModernEDIObservedTheRevision. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(to_wire_value(obj), ensure_ascii=False, allow_nan=False))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into TimeModernEDIObservedTheRevision
        try:
            instance.actual_instance = TimeModernEDIObservedTheRevision.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BusinessEffectiveTimestamp
        try:
            instance.actual_instance = BusinessEffectiveTimestamp.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigurationScenarioDefinitionEffectiveAt with oneOf schemas: BusinessEffectiveTimestamp, TimeModernEDIObservedTheRevision. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigurationScenarioDefinitionEffectiveAt with oneOf schemas: BusinessEffectiveTimestamp, TimeModernEDIObservedTheRevision. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], BusinessEffectiveTimestamp, TimeModernEDIObservedTheRevision]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return to_wire_value(self.actual_instance)

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())
