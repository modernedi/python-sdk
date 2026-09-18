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
from modernedi.generated.models.expected_count_closure import ExpectedCountClosure
from modernedi.generated.models.fixed_closure import FixedClosure
from modernedi.generated.models.maximum_reached_closure import MaximumReachedClosure
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGURATIONSCENARIODEFINITIONOCCURRENCECLOSURE_ONE_OF_SCHEMAS = ["ExpectedCountClosure", "FixedClosure", "MaximumReachedClosure"]

class ConfigurationScenarioDefinitionOccurrenceClosure(BaseModel):
    """
    The objective rule that tells a run no more documents are expected for one repeated step. fixed closes at the required fixed count; max_reached closes only at the authored maximum; expected_count closes at a required or defaulted run parameter, including an explicit zero. Branch selection supplies the no-document outcome for an unselected destination. There is no manual-close operation in v1.
    """
    # data type: FixedClosure
    oneof_schema_1_validator: Optional[FixedClosure] = None
    # data type: MaximumReachedClosure
    oneof_schema_2_validator: Optional[MaximumReachedClosure] = None
    # data type: ExpectedCountClosure
    oneof_schema_3_validator: Optional[ExpectedCountClosure] = None
    actual_instance: Optional[Union[ExpectedCountClosure, FixedClosure, MaximumReachedClosure]] = None
    one_of_schemas: Set[str] = { "ExpectedCountClosure", "FixedClosure", "MaximumReachedClosure" }

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
        instance = ConfigurationScenarioDefinitionOccurrenceClosure.model_construct()
        error_messages = []
        match = 0
        # validate data type: FixedClosure
        if not isinstance(v, FixedClosure):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FixedClosure`")
        else:
            match += 1
        # validate data type: MaximumReachedClosure
        if not isinstance(v, MaximumReachedClosure):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MaximumReachedClosure`")
        else:
            match += 1
        # validate data type: ExpectedCountClosure
        if not isinstance(v, ExpectedCountClosure):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExpectedCountClosure`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigurationScenarioDefinitionOccurrenceClosure with oneOf schemas: ExpectedCountClosure, FixedClosure, MaximumReachedClosure. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigurationScenarioDefinitionOccurrenceClosure with oneOf schemas: ExpectedCountClosure, FixedClosure, MaximumReachedClosure. Details: " + ", ".join(error_messages))
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

        # deserialize data into FixedClosure
        try:
            instance.actual_instance = FixedClosure.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MaximumReachedClosure
        try:
            instance.actual_instance = MaximumReachedClosure.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExpectedCountClosure
        try:
            instance.actual_instance = ExpectedCountClosure.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigurationScenarioDefinitionOccurrenceClosure with oneOf schemas: ExpectedCountClosure, FixedClosure, MaximumReachedClosure. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigurationScenarioDefinitionOccurrenceClosure with oneOf schemas: ExpectedCountClosure, FixedClosure, MaximumReachedClosure. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ExpectedCountClosure, FixedClosure, MaximumReachedClosure]]:
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
