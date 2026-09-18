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
from modernedi.generated.models.assure_stage import AssureStage
from modernedi.generated.models.checkpoint_stage import CheckpointStage
from modernedi.generated.models.exchange_stage import ExchangeStage
from modernedi.generated.models.extract_stage import ExtractStage
from modernedi.generated.models.map_stage import MapStage
from modernedi.generated.models.prepare_stage import PrepareStage
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGURATIONSCENARIODEFINITIONPIPELINESTAGE_ONE_OF_SCHEMAS = ["AssureStage", "CheckpointStage", "ExchangeStage", "ExtractStage", "MapStage", "PrepareStage"]

class ConfigurationScenarioDefinitionPipelineStage(BaseModel):
    """
    One named action in the ordered processing of an observed document. A definition says prepare, map, exchange, extract facts, check evidence, or emit a checkpoint; the binding later selects the concrete map, partner, or adapter. Keeping those artifact IDs out of the definition lets the same conversation recipe be reused by another tenant.
    """
    # data type: PrepareStage
    oneof_schema_1_validator: Optional[PrepareStage] = None
    # data type: MapStage
    oneof_schema_2_validator: Optional[MapStage] = None
    # data type: ExchangeStage
    oneof_schema_3_validator: Optional[ExchangeStage] = None
    # data type: ExtractStage
    oneof_schema_4_validator: Optional[ExtractStage] = None
    # data type: AssureStage
    oneof_schema_5_validator: Optional[AssureStage] = None
    # data type: CheckpointStage
    oneof_schema_6_validator: Optional[CheckpointStage] = None
    actual_instance: Optional[Union[AssureStage, CheckpointStage, ExchangeStage, ExtractStage, MapStage, PrepareStage]] = None
    one_of_schemas: Set[str] = { "AssureStage", "CheckpointStage", "ExchangeStage", "ExtractStage", "MapStage", "PrepareStage" }

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
        instance = ConfigurationScenarioDefinitionPipelineStage.model_construct()
        error_messages = []
        match = 0
        # validate data type: PrepareStage
        if not isinstance(v, PrepareStage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PrepareStage`")
        else:
            match += 1
        # validate data type: MapStage
        if not isinstance(v, MapStage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MapStage`")
        else:
            match += 1
        # validate data type: ExchangeStage
        if not isinstance(v, ExchangeStage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExchangeStage`")
        else:
            match += 1
        # validate data type: ExtractStage
        if not isinstance(v, ExtractStage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ExtractStage`")
        else:
            match += 1
        # validate data type: AssureStage
        if not isinstance(v, AssureStage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AssureStage`")
        else:
            match += 1
        # validate data type: CheckpointStage
        if not isinstance(v, CheckpointStage):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CheckpointStage`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigurationScenarioDefinitionPipelineStage with oneOf schemas: AssureStage, CheckpointStage, ExchangeStage, ExtractStage, MapStage, PrepareStage. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigurationScenarioDefinitionPipelineStage with oneOf schemas: AssureStage, CheckpointStage, ExchangeStage, ExtractStage, MapStage, PrepareStage. Details: " + ", ".join(error_messages))
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

        # deserialize data into PrepareStage
        try:
            instance.actual_instance = PrepareStage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MapStage
        try:
            instance.actual_instance = MapStage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExchangeStage
        try:
            instance.actual_instance = ExchangeStage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ExtractStage
        try:
            instance.actual_instance = ExtractStage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AssureStage
        try:
            instance.actual_instance = AssureStage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CheckpointStage
        try:
            instance.actual_instance = CheckpointStage.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigurationScenarioDefinitionPipelineStage with oneOf schemas: AssureStage, CheckpointStage, ExchangeStage, ExtractStage, MapStage, PrepareStage. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigurationScenarioDefinitionPipelineStage with oneOf schemas: AssureStage, CheckpointStage, ExchangeStage, ExtractStage, MapStage, PrepareStage. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], AssureStage, CheckpointStage, ExchangeStage, ExtractStage, MapStage, PrepareStage]]:
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
