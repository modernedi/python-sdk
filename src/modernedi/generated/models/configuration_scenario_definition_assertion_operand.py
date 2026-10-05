# coding: utf-8

"""Generated from the ModernEDI Integration API 1.36.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import json
from modernedi._wire import to_wire_value
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from modernedi.generated.models.configuration_scenario_definition_fact_operand import ConfigurationScenarioDefinitionFactOperand
from modernedi.generated.models.configuration_scenario_definition_keyed_fact_operand import ConfigurationScenarioDefinitionKeyedFactOperand
from modernedi.generated.models.configuration_scenario_definition_literal_operand import ConfigurationScenarioDefinitionLiteralOperand
from modernedi.generated.models.configuration_scenario_definition_parameter_operand import ConfigurationScenarioDefinitionParameterOperand
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGURATIONSCENARIODEFINITIONASSERTIONOPERAND_ONE_OF_SCHEMAS = ["ConfigurationScenarioDefinitionFactOperand", "ConfigurationScenarioDefinitionKeyedFactOperand", "ConfigurationScenarioDefinitionLiteralOperand", "ConfigurationScenarioDefinitionParameterOperand"]

class ConfigurationScenarioDefinitionAssertionOperand(BaseModel):
    """
    ConfigurationScenarioDefinitionAssertionOperand
    """
    # data type: ConfigurationScenarioDefinitionFactOperand
    oneof_schema_1_validator: Optional[ConfigurationScenarioDefinitionFactOperand] = None
    # data type: ConfigurationScenarioDefinitionParameterOperand
    oneof_schema_2_validator: Optional[ConfigurationScenarioDefinitionParameterOperand] = None
    # data type: ConfigurationScenarioDefinitionLiteralOperand
    oneof_schema_3_validator: Optional[ConfigurationScenarioDefinitionLiteralOperand] = None
    # data type: ConfigurationScenarioDefinitionKeyedFactOperand
    oneof_schema_4_validator: Optional[ConfigurationScenarioDefinitionKeyedFactOperand] = None
    actual_instance: Optional[Union[ConfigurationScenarioDefinitionFactOperand, ConfigurationScenarioDefinitionKeyedFactOperand, ConfigurationScenarioDefinitionLiteralOperand, ConfigurationScenarioDefinitionParameterOperand]] = None
    one_of_schemas: Set[str] = { "ConfigurationScenarioDefinitionFactOperand", "ConfigurationScenarioDefinitionKeyedFactOperand", "ConfigurationScenarioDefinitionLiteralOperand", "ConfigurationScenarioDefinitionParameterOperand" }

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
        instance = ConfigurationScenarioDefinitionAssertionOperand.model_construct()
        error_messages = []
        match = 0
        # validate data type: ConfigurationScenarioDefinitionFactOperand
        if not isinstance(v, ConfigurationScenarioDefinitionFactOperand):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationScenarioDefinitionFactOperand`")
        else:
            match += 1
        # validate data type: ConfigurationScenarioDefinitionParameterOperand
        if not isinstance(v, ConfigurationScenarioDefinitionParameterOperand):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationScenarioDefinitionParameterOperand`")
        else:
            match += 1
        # validate data type: ConfigurationScenarioDefinitionLiteralOperand
        if not isinstance(v, ConfigurationScenarioDefinitionLiteralOperand):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationScenarioDefinitionLiteralOperand`")
        else:
            match += 1
        # validate data type: ConfigurationScenarioDefinitionKeyedFactOperand
        if not isinstance(v, ConfigurationScenarioDefinitionKeyedFactOperand):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationScenarioDefinitionKeyedFactOperand`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigurationScenarioDefinitionAssertionOperand with oneOf schemas: ConfigurationScenarioDefinitionFactOperand, ConfigurationScenarioDefinitionKeyedFactOperand, ConfigurationScenarioDefinitionLiteralOperand, ConfigurationScenarioDefinitionParameterOperand. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigurationScenarioDefinitionAssertionOperand with oneOf schemas: ConfigurationScenarioDefinitionFactOperand, ConfigurationScenarioDefinitionKeyedFactOperand, ConfigurationScenarioDefinitionLiteralOperand, ConfigurationScenarioDefinitionParameterOperand. Details: " + ", ".join(error_messages))
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

        # deserialize data into ConfigurationScenarioDefinitionFactOperand
        try:
            instance.actual_instance = ConfigurationScenarioDefinitionFactOperand.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigurationScenarioDefinitionParameterOperand
        try:
            instance.actual_instance = ConfigurationScenarioDefinitionParameterOperand.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigurationScenarioDefinitionLiteralOperand
        try:
            instance.actual_instance = ConfigurationScenarioDefinitionLiteralOperand.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigurationScenarioDefinitionKeyedFactOperand
        try:
            instance.actual_instance = ConfigurationScenarioDefinitionKeyedFactOperand.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigurationScenarioDefinitionAssertionOperand with oneOf schemas: ConfigurationScenarioDefinitionFactOperand, ConfigurationScenarioDefinitionKeyedFactOperand, ConfigurationScenarioDefinitionLiteralOperand, ConfigurationScenarioDefinitionParameterOperand. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigurationScenarioDefinitionAssertionOperand with oneOf schemas: ConfigurationScenarioDefinitionFactOperand, ConfigurationScenarioDefinitionKeyedFactOperand, ConfigurationScenarioDefinitionLiteralOperand, ConfigurationScenarioDefinitionParameterOperand. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ConfigurationScenarioDefinitionFactOperand, ConfigurationScenarioDefinitionKeyedFactOperand, ConfigurationScenarioDefinitionLiteralOperand, ConfigurationScenarioDefinitionParameterOperand]]:
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
