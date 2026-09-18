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
from modernedi.generated.models.scenario_run_summary_guidance_one_of import ScenarioRunSummaryGuidanceOneOf
from modernedi.generated.models.scenario_run_summary_guidance_one_of1 import ScenarioRunSummaryGuidanceOneOf1
from modernedi.generated.models.scenario_run_summary_guidance_one_of2 import ScenarioRunSummaryGuidanceOneOf2
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

SCENARIORUNSUMMARYGUIDANCE_ONE_OF_SCHEMAS = ["ScenarioRunSummaryGuidanceOneOf", "ScenarioRunSummaryGuidanceOneOf1", "ScenarioRunSummaryGuidanceOneOf2"]

class ScenarioRunSummaryGuidance(BaseModel):
    """
    ScenarioRunSummaryGuidance
    """
    # data type: ScenarioRunSummaryGuidanceOneOf
    oneof_schema_1_validator: Optional[ScenarioRunSummaryGuidanceOneOf] = None
    # data type: ScenarioRunSummaryGuidanceOneOf1
    oneof_schema_2_validator: Optional[ScenarioRunSummaryGuidanceOneOf1] = None
    # data type: ScenarioRunSummaryGuidanceOneOf2
    oneof_schema_3_validator: Optional[ScenarioRunSummaryGuidanceOneOf2] = None
    actual_instance: Optional[Union[ScenarioRunSummaryGuidanceOneOf, ScenarioRunSummaryGuidanceOneOf1, ScenarioRunSummaryGuidanceOneOf2]] = None
    one_of_schemas: Set[str] = { "ScenarioRunSummaryGuidanceOneOf", "ScenarioRunSummaryGuidanceOneOf1", "ScenarioRunSummaryGuidanceOneOf2" }

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
        instance = ScenarioRunSummaryGuidance.model_construct()
        error_messages = []
        match = 0
        # validate data type: ScenarioRunSummaryGuidanceOneOf
        if not isinstance(v, ScenarioRunSummaryGuidanceOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ScenarioRunSummaryGuidanceOneOf`")
        else:
            match += 1
        # validate data type: ScenarioRunSummaryGuidanceOneOf1
        if not isinstance(v, ScenarioRunSummaryGuidanceOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ScenarioRunSummaryGuidanceOneOf1`")
        else:
            match += 1
        # validate data type: ScenarioRunSummaryGuidanceOneOf2
        if not isinstance(v, ScenarioRunSummaryGuidanceOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ScenarioRunSummaryGuidanceOneOf2`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ScenarioRunSummaryGuidance with oneOf schemas: ScenarioRunSummaryGuidanceOneOf, ScenarioRunSummaryGuidanceOneOf1, ScenarioRunSummaryGuidanceOneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ScenarioRunSummaryGuidance with oneOf schemas: ScenarioRunSummaryGuidanceOneOf, ScenarioRunSummaryGuidanceOneOf1, ScenarioRunSummaryGuidanceOneOf2. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ScenarioRunSummaryGuidanceOneOf
        try:
            instance.actual_instance = ScenarioRunSummaryGuidanceOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ScenarioRunSummaryGuidanceOneOf1
        try:
            instance.actual_instance = ScenarioRunSummaryGuidanceOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ScenarioRunSummaryGuidanceOneOf2
        try:
            instance.actual_instance = ScenarioRunSummaryGuidanceOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ScenarioRunSummaryGuidance with oneOf schemas: ScenarioRunSummaryGuidanceOneOf, ScenarioRunSummaryGuidanceOneOf1, ScenarioRunSummaryGuidanceOneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ScenarioRunSummaryGuidance with oneOf schemas: ScenarioRunSummaryGuidanceOneOf, ScenarioRunSummaryGuidanceOneOf1, ScenarioRunSummaryGuidanceOneOf2. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ScenarioRunSummaryGuidanceOneOf, ScenarioRunSummaryGuidanceOneOf1, ScenarioRunSummaryGuidanceOneOf2]]:
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
