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
from modernedi.generated.models.as2_partner_environment_resolved import As2PartnerEnvironmentResolved
from modernedi.generated.models.configuration_as2_file_environment import ConfigurationAs2FileEnvironment
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGURATIONAS2ENVIRONMENT_ONE_OF_SCHEMAS = ["As2PartnerEnvironmentResolved", "ConfigurationAs2FileEnvironment"]

class ConfigurationAs2Environment(BaseModel):
    """
    An environment has either one inline public certificate or a file reference, never both. File references are confined to this connection. Production and Test may share one file; replacing it changes both environments' certificates.
    """
    # data type: As2PartnerEnvironmentResolved
    oneof_schema_1_validator: Optional[As2PartnerEnvironmentResolved] = None
    # data type: ConfigurationAs2FileEnvironment
    oneof_schema_2_validator: Optional[ConfigurationAs2FileEnvironment] = None
    actual_instance: Optional[Union[As2PartnerEnvironmentResolved, ConfigurationAs2FileEnvironment]] = None
    one_of_schemas: Set[str] = { "As2PartnerEnvironmentResolved", "ConfigurationAs2FileEnvironment" }

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
        instance = ConfigurationAs2Environment.model_construct()
        error_messages = []
        match = 0
        # validate data type: As2PartnerEnvironmentResolved
        if not isinstance(v, As2PartnerEnvironmentResolved):
            error_messages.append(f"Error! Input type `{type(v)}` is not `As2PartnerEnvironmentResolved`")
        else:
            match += 1
        # validate data type: ConfigurationAs2FileEnvironment
        if not isinstance(v, ConfigurationAs2FileEnvironment):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationAs2FileEnvironment`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigurationAs2Environment with oneOf schemas: As2PartnerEnvironmentResolved, ConfigurationAs2FileEnvironment. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigurationAs2Environment with oneOf schemas: As2PartnerEnvironmentResolved, ConfigurationAs2FileEnvironment. Details: " + ", ".join(error_messages))
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

        # deserialize data into As2PartnerEnvironmentResolved
        try:
            instance.actual_instance = As2PartnerEnvironmentResolved.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigurationAs2FileEnvironment
        try:
            instance.actual_instance = ConfigurationAs2FileEnvironment.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigurationAs2Environment with oneOf schemas: As2PartnerEnvironmentResolved, ConfigurationAs2FileEnvironment. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigurationAs2Environment with oneOf schemas: As2PartnerEnvironmentResolved, ConfigurationAs2FileEnvironment. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], As2PartnerEnvironmentResolved, ConfigurationAs2FileEnvironment]]:
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
