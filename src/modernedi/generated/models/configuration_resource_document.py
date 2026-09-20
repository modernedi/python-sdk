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
from modernedi.generated.models.configuration_as2_connection_resource_document import ConfigurationAs2ConnectionResourceDocument
from modernedi.generated.models.configuration_mapping_resource_document import ConfigurationMappingResourceDocument
from modernedi.generated.models.configuration_partner_resource_document import ConfigurationPartnerResourceDocument
from modernedi.generated.models.configuration_scenario_binding_resource_document import ConfigurationScenarioBindingResourceDocument
from modernedi.generated.models.configuration_scenario_definition_resource_document import ConfigurationScenarioDefinitionResourceDocument
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CONFIGURATIONRESOURCEDOCUMENT_ONE_OF_SCHEMAS = ["ConfigurationAs2ConnectionResourceDocument", "ConfigurationMappingResourceDocument", "ConfigurationPartnerResourceDocument", "ConfigurationScenarioBindingResourceDocument", "ConfigurationScenarioDefinitionResourceDocument"]

class ConfigurationResourceDocument(BaseModel):
    """
    Portable connection, partner, mapping, or optional scenario desired-state document. References use stable UUID keys rather than workspace database ids. Scenario resources contain the complete authored document under spec.source; runtime snapshots and evidence are not source configuration.
    """
    # data type: ConfigurationAs2ConnectionResourceDocument
    oneof_schema_1_validator: Optional[ConfigurationAs2ConnectionResourceDocument] = None
    # data type: ConfigurationPartnerResourceDocument
    oneof_schema_2_validator: Optional[ConfigurationPartnerResourceDocument] = None
    # data type: ConfigurationMappingResourceDocument
    oneof_schema_3_validator: Optional[ConfigurationMappingResourceDocument] = None
    # data type: ConfigurationScenarioDefinitionResourceDocument
    oneof_schema_4_validator: Optional[ConfigurationScenarioDefinitionResourceDocument] = None
    # data type: ConfigurationScenarioBindingResourceDocument
    oneof_schema_5_validator: Optional[ConfigurationScenarioBindingResourceDocument] = None
    actual_instance: Optional[Union[ConfigurationAs2ConnectionResourceDocument, ConfigurationMappingResourceDocument, ConfigurationPartnerResourceDocument, ConfigurationScenarioBindingResourceDocument, ConfigurationScenarioDefinitionResourceDocument]] = None
    one_of_schemas: Set[str] = { "ConfigurationAs2ConnectionResourceDocument", "ConfigurationMappingResourceDocument", "ConfigurationPartnerResourceDocument", "ConfigurationScenarioBindingResourceDocument", "ConfigurationScenarioDefinitionResourceDocument" }

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
        instance = ConfigurationResourceDocument.model_construct()
        error_messages = []
        match = 0
        # validate data type: ConfigurationAs2ConnectionResourceDocument
        if not isinstance(v, ConfigurationAs2ConnectionResourceDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationAs2ConnectionResourceDocument`")
        else:
            match += 1
        # validate data type: ConfigurationPartnerResourceDocument
        if not isinstance(v, ConfigurationPartnerResourceDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationPartnerResourceDocument`")
        else:
            match += 1
        # validate data type: ConfigurationMappingResourceDocument
        if not isinstance(v, ConfigurationMappingResourceDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationMappingResourceDocument`")
        else:
            match += 1
        # validate data type: ConfigurationScenarioDefinitionResourceDocument
        if not isinstance(v, ConfigurationScenarioDefinitionResourceDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationScenarioDefinitionResourceDocument`")
        else:
            match += 1
        # validate data type: ConfigurationScenarioBindingResourceDocument
        if not isinstance(v, ConfigurationScenarioBindingResourceDocument):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConfigurationScenarioBindingResourceDocument`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ConfigurationResourceDocument with oneOf schemas: ConfigurationAs2ConnectionResourceDocument, ConfigurationMappingResourceDocument, ConfigurationPartnerResourceDocument, ConfigurationScenarioBindingResourceDocument, ConfigurationScenarioDefinitionResourceDocument. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ConfigurationResourceDocument with oneOf schemas: ConfigurationAs2ConnectionResourceDocument, ConfigurationMappingResourceDocument, ConfigurationPartnerResourceDocument, ConfigurationScenarioBindingResourceDocument, ConfigurationScenarioDefinitionResourceDocument. Details: " + ", ".join(error_messages))
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

        # deserialize data into ConfigurationAs2ConnectionResourceDocument
        try:
            instance.actual_instance = ConfigurationAs2ConnectionResourceDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigurationPartnerResourceDocument
        try:
            instance.actual_instance = ConfigurationPartnerResourceDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigurationMappingResourceDocument
        try:
            instance.actual_instance = ConfigurationMappingResourceDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigurationScenarioDefinitionResourceDocument
        try:
            instance.actual_instance = ConfigurationScenarioDefinitionResourceDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConfigurationScenarioBindingResourceDocument
        try:
            instance.actual_instance = ConfigurationScenarioBindingResourceDocument.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ConfigurationResourceDocument with oneOf schemas: ConfigurationAs2ConnectionResourceDocument, ConfigurationMappingResourceDocument, ConfigurationPartnerResourceDocument, ConfigurationScenarioBindingResourceDocument, ConfigurationScenarioDefinitionResourceDocument. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ConfigurationResourceDocument with oneOf schemas: ConfigurationAs2ConnectionResourceDocument, ConfigurationMappingResourceDocument, ConfigurationPartnerResourceDocument, ConfigurationScenarioBindingResourceDocument, ConfigurationScenarioDefinitionResourceDocument. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], ConfigurationAs2ConnectionResourceDocument, ConfigurationMappingResourceDocument, ConfigurationPartnerResourceDocument, ConfigurationScenarioBindingResourceDocument, ConfigurationScenarioDefinitionResourceDocument]]:
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
