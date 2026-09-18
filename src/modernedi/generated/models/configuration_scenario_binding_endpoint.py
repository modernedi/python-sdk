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
from modernedi.generated.models.partner_endpoint import PartnerEndpoint
from modernedi.generated.models.workspace_endpoint import WorkspaceEndpoint
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGURATIONSCENARIOBINDINGENDPOINT_ONE_OF_SCHEMAS = ["PartnerEndpoint", "WorkspaceEndpoint"]

class ConfigurationScenarioBindingEndpoint(BaseModel):
    """
    OneOf discriminator: workspace accepts only kind; partner also requires a positive tenant partner ID.
    """
    # data type: WorkspaceEndpoint
    oneof_schema_1_validator: Optional[WorkspaceEndpoint] = None
    # data type: PartnerEndpoint
    oneof_schema_2_validator: Optional[PartnerEndpoint] = None
    actual_instance: Optional[Union[PartnerEndpoint, WorkspaceEndpoint]] = None
    one_of_schemas: Set[str] = { "PartnerEndpoint", "WorkspaceEndpoint" }

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
        instance = ConfigurationScenarioBindingEndpoint.model_construct()
        error_messages = []
        match = 0
        # validate data type: WorkspaceEndpoint
        if not isinstance(v, WorkspaceEndpoint):
            error_messages.append(f"Error! Input type `{type(v)}` is not `WorkspaceEndpoint`")
        else:
            match += 1
        # validate data type: PartnerEndpoint
        if not isinstance(v, PartnerEndpoint):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PartnerEndpoint`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigurationScenarioBindingEndpoint with oneOf schemas: PartnerEndpoint, WorkspaceEndpoint. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigurationScenarioBindingEndpoint with oneOf schemas: PartnerEndpoint, WorkspaceEndpoint. Details: " + ", ".join(error_messages))
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

        # deserialize data into WorkspaceEndpoint
        try:
            instance.actual_instance = WorkspaceEndpoint.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PartnerEndpoint
        try:
            instance.actual_instance = PartnerEndpoint.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigurationScenarioBindingEndpoint with oneOf schemas: PartnerEndpoint, WorkspaceEndpoint. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigurationScenarioBindingEndpoint with oneOf schemas: PartnerEndpoint, WorkspaceEndpoint. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], PartnerEndpoint, WorkspaceEndpoint]]:
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
