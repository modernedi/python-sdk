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
from modernedi.generated.models.transaction_functional_acknowledgment_event import TransactionFunctionalAcknowledgmentEvent
from modernedi.generated.models.transaction_functional_acknowledgment_mdn_event import TransactionFunctionalAcknowledgmentMdnEvent
from modernedi.generated.models.transaction_implementation_acknowledgment_event import TransactionImplementationAcknowledgmentEvent
from modernedi.generated.models.transaction_implementation_acknowledgment_mdn_event import TransactionImplementationAcknowledgmentMdnEvent
from modernedi.generated.models.transaction_lifecycle_event import TransactionLifecycleEvent
from modernedi.generated.models.transaction_mapped_output_event import TransactionMappedOutputEvent
from modernedi.generated.models.transaction_mapping_event import TransactionMappingEvent
from modernedi.generated.models.transaction_mdn_event import TransactionMdnEvent
from modernedi.generated.models.transaction_technical_acknowledgment_event import TransactionTechnicalAcknowledgmentEvent
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

TRANSACTIONEVENT_ONE_OF_SCHEMAS = ["TransactionFunctionalAcknowledgmentEvent", "TransactionFunctionalAcknowledgmentMdnEvent", "TransactionImplementationAcknowledgmentEvent", "TransactionImplementationAcknowledgmentMdnEvent", "TransactionLifecycleEvent", "TransactionMappedOutputEvent", "TransactionMappingEvent", "TransactionMdnEvent", "TransactionTechnicalAcknowledgmentEvent"]

class TransactionEvent(BaseModel):
    """
    One derived operator-timeline entry. `type` is a discriminator for the stable `details` payload; clients do not need to infer fields from `label` or reverse-engineer examples.
    """
    # data type: TransactionLifecycleEvent
    oneof_schema_1_validator: Optional[TransactionLifecycleEvent] = None
    # data type: TransactionMappedOutputEvent
    oneof_schema_2_validator: Optional[TransactionMappedOutputEvent] = None
    # data type: TransactionMappingEvent
    oneof_schema_3_validator: Optional[TransactionMappingEvent] = None
    # data type: TransactionMdnEvent
    oneof_schema_4_validator: Optional[TransactionMdnEvent] = None
    # data type: TransactionFunctionalAcknowledgmentEvent
    oneof_schema_5_validator: Optional[TransactionFunctionalAcknowledgmentEvent] = None
    # data type: TransactionFunctionalAcknowledgmentMdnEvent
    oneof_schema_6_validator: Optional[TransactionFunctionalAcknowledgmentMdnEvent] = None
    # data type: TransactionImplementationAcknowledgmentEvent
    oneof_schema_7_validator: Optional[TransactionImplementationAcknowledgmentEvent] = None
    # data type: TransactionImplementationAcknowledgmentMdnEvent
    oneof_schema_8_validator: Optional[TransactionImplementationAcknowledgmentMdnEvent] = None
    # data type: TransactionTechnicalAcknowledgmentEvent
    oneof_schema_9_validator: Optional[TransactionTechnicalAcknowledgmentEvent] = None
    actual_instance: Optional[Union[TransactionFunctionalAcknowledgmentEvent, TransactionFunctionalAcknowledgmentMdnEvent, TransactionImplementationAcknowledgmentEvent, TransactionImplementationAcknowledgmentMdnEvent, TransactionLifecycleEvent, TransactionMappedOutputEvent, TransactionMappingEvent, TransactionMdnEvent, TransactionTechnicalAcknowledgmentEvent]] = None
    one_of_schemas: Set[str] = { "TransactionFunctionalAcknowledgmentEvent", "TransactionFunctionalAcknowledgmentMdnEvent", "TransactionImplementationAcknowledgmentEvent", "TransactionImplementationAcknowledgmentMdnEvent", "TransactionLifecycleEvent", "TransactionMappedOutputEvent", "TransactionMappingEvent", "TransactionMdnEvent", "TransactionTechnicalAcknowledgmentEvent" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )

    discriminator_value_class_map: Dict[str, str] = {
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
    def actual_instance_must_validate_oneof(cls, v):
        instance = TransactionEvent.model_construct()
        error_messages = []
        match = 0
        # validate data type: TransactionLifecycleEvent
        if not isinstance(v, TransactionLifecycleEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionLifecycleEvent`")
        else:
            match += 1
        # validate data type: TransactionMappedOutputEvent
        if not isinstance(v, TransactionMappedOutputEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionMappedOutputEvent`")
        else:
            match += 1
        # validate data type: TransactionMappingEvent
        if not isinstance(v, TransactionMappingEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionMappingEvent`")
        else:
            match += 1
        # validate data type: TransactionMdnEvent
        if not isinstance(v, TransactionMdnEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionMdnEvent`")
        else:
            match += 1
        # validate data type: TransactionFunctionalAcknowledgmentEvent
        if not isinstance(v, TransactionFunctionalAcknowledgmentEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionFunctionalAcknowledgmentEvent`")
        else:
            match += 1
        # validate data type: TransactionFunctionalAcknowledgmentMdnEvent
        if not isinstance(v, TransactionFunctionalAcknowledgmentMdnEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionFunctionalAcknowledgmentMdnEvent`")
        else:
            match += 1
        # validate data type: TransactionImplementationAcknowledgmentEvent
        if not isinstance(v, TransactionImplementationAcknowledgmentEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionImplementationAcknowledgmentEvent`")
        else:
            match += 1
        # validate data type: TransactionImplementationAcknowledgmentMdnEvent
        if not isinstance(v, TransactionImplementationAcknowledgmentMdnEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionImplementationAcknowledgmentMdnEvent`")
        else:
            match += 1
        # validate data type: TransactionTechnicalAcknowledgmentEvent
        if not isinstance(v, TransactionTechnicalAcknowledgmentEvent):
            error_messages.append(f"Error! Input type `{type(v)}` is not `TransactionTechnicalAcknowledgmentEvent`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in TransactionEvent with oneOf schemas: TransactionFunctionalAcknowledgmentEvent, TransactionFunctionalAcknowledgmentMdnEvent, TransactionImplementationAcknowledgmentEvent, TransactionImplementationAcknowledgmentMdnEvent, TransactionLifecycleEvent, TransactionMappedOutputEvent, TransactionMappingEvent, TransactionMdnEvent, TransactionTechnicalAcknowledgmentEvent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in TransactionEvent with oneOf schemas: TransactionFunctionalAcknowledgmentEvent, TransactionFunctionalAcknowledgmentMdnEvent, TransactionImplementationAcknowledgmentEvent, TransactionImplementationAcknowledgmentMdnEvent, TransactionLifecycleEvent, TransactionMappedOutputEvent, TransactionMappingEvent, TransactionMdnEvent, TransactionTechnicalAcknowledgmentEvent. Details: " + ", ".join(error_messages))
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

        # deserialize data into TransactionLifecycleEvent
        try:
            instance.actual_instance = TransactionLifecycleEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionMappedOutputEvent
        try:
            instance.actual_instance = TransactionMappedOutputEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionMappingEvent
        try:
            instance.actual_instance = TransactionMappingEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionMdnEvent
        try:
            instance.actual_instance = TransactionMdnEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionFunctionalAcknowledgmentEvent
        try:
            instance.actual_instance = TransactionFunctionalAcknowledgmentEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionFunctionalAcknowledgmentMdnEvent
        try:
            instance.actual_instance = TransactionFunctionalAcknowledgmentMdnEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionImplementationAcknowledgmentEvent
        try:
            instance.actual_instance = TransactionImplementationAcknowledgmentEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionImplementationAcknowledgmentMdnEvent
        try:
            instance.actual_instance = TransactionImplementationAcknowledgmentMdnEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into TransactionTechnicalAcknowledgmentEvent
        try:
            instance.actual_instance = TransactionTechnicalAcknowledgmentEvent.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into TransactionEvent with oneOf schemas: TransactionFunctionalAcknowledgmentEvent, TransactionFunctionalAcknowledgmentMdnEvent, TransactionImplementationAcknowledgmentEvent, TransactionImplementationAcknowledgmentMdnEvent, TransactionLifecycleEvent, TransactionMappedOutputEvent, TransactionMappingEvent, TransactionMdnEvent, TransactionTechnicalAcknowledgmentEvent. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into TransactionEvent with oneOf schemas: TransactionFunctionalAcknowledgmentEvent, TransactionFunctionalAcknowledgmentMdnEvent, TransactionImplementationAcknowledgmentEvent, TransactionImplementationAcknowledgmentMdnEvent, TransactionLifecycleEvent, TransactionMappedOutputEvent, TransactionMappingEvent, TransactionMdnEvent, TransactionTechnicalAcknowledgmentEvent. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], TransactionFunctionalAcknowledgmentEvent, TransactionFunctionalAcknowledgmentMdnEvent, TransactionImplementationAcknowledgmentEvent, TransactionImplementationAcknowledgmentMdnEvent, TransactionLifecycleEvent, TransactionMappedOutputEvent, TransactionMappingEvent, TransactionMdnEvent, TransactionTechnicalAcknowledgmentEvent]]:
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
