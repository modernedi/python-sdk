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
from modernedi.generated.models.correlation_matching import CorrelationMatching
from modernedi.generated.models.positional_matching import PositionalMatching
from modernedi.generated.models.previous_occurrence_matching import PreviousOccurrenceMatching
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGURATIONSCENARIODEFINITIONOCCURRENCEMATCHING_ONE_OF_SCHEMAS = ["CorrelationMatching", "PositionalMatching", "PreviousOccurrenceMatching"]

class ConfigurationScenarioDefinitionOccurrenceMatching(BaseModel):
    """
    How actual repeated documents are paired across a transition, plus what happens to documents with no match. correlate pairs documents whose declared fact or reply-link conditions pass; position pairs by observation order; previous pairs each revision with the immediately preceding occurrence of the same step, such as the second 860 order change with the first.
    """
    # data type: CorrelationMatching
    oneof_schema_1_validator: Optional[CorrelationMatching] = None
    # data type: PositionalMatching
    oneof_schema_2_validator: Optional[PositionalMatching] = None
    # data type: PreviousOccurrenceMatching
    oneof_schema_3_validator: Optional[PreviousOccurrenceMatching] = None
    actual_instance: Optional[Union[CorrelationMatching, PositionalMatching, PreviousOccurrenceMatching]] = None
    one_of_schemas: Set[str] = { "CorrelationMatching", "PositionalMatching", "PreviousOccurrenceMatching" }

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
        instance = ConfigurationScenarioDefinitionOccurrenceMatching.model_construct()
        error_messages = []
        match = 0
        # validate data type: CorrelationMatching
        if not isinstance(v, CorrelationMatching):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CorrelationMatching`")
        else:
            match += 1
        # validate data type: PositionalMatching
        if not isinstance(v, PositionalMatching):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PositionalMatching`")
        else:
            match += 1
        # validate data type: PreviousOccurrenceMatching
        if not isinstance(v, PreviousOccurrenceMatching):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PreviousOccurrenceMatching`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigurationScenarioDefinitionOccurrenceMatching with oneOf schemas: CorrelationMatching, PositionalMatching, PreviousOccurrenceMatching. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigurationScenarioDefinitionOccurrenceMatching with oneOf schemas: CorrelationMatching, PositionalMatching, PreviousOccurrenceMatching. Details: " + ", ".join(error_messages))
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

        # deserialize data into CorrelationMatching
        try:
            instance.actual_instance = CorrelationMatching.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PositionalMatching
        try:
            instance.actual_instance = PositionalMatching.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PreviousOccurrenceMatching
        try:
            instance.actual_instance = PreviousOccurrenceMatching.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigurationScenarioDefinitionOccurrenceMatching with oneOf schemas: CorrelationMatching, PositionalMatching, PreviousOccurrenceMatching. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigurationScenarioDefinitionOccurrenceMatching with oneOf schemas: CorrelationMatching, PositionalMatching, PreviousOccurrenceMatching. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], CorrelationMatching, PositionalMatching, PreviousOccurrenceMatching]]:
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
