# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, Optional
from modernedi.generated.models.configuration_scenario_definition_metadata import ConfigurationScenarioDefinitionMetadata
from modernedi.generated.models.configuration_scenario_definition_spec import ConfigurationScenarioDefinitionSpec
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ModernEDIScenarioDefinitionV1(BaseModel):
    """
    Maps define how documents are processed; scenarios define and prove the business conversation those maps implement. A ScenarioDefinition is the portable recipe for that conversation: who exchanges each X12 business document, which documents belong together, what order and repetition are allowed, and what evidence must pass. Tenant partners, syntax trees, mappings, and executable targets belong in a ScenarioBinding.
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, description="Optional portable tooling hint. It does not participate in the definition's canonical content hash.", alias="$schema")
    api_version: StrictStr = Field(description="Wire-contract version for the generally available ScenarioDefinition contract.", alias="apiVersion")
    kind: StrictStr = Field(description="Discriminator for a scenario definition document.")
    metadata: ConfigurationScenarioDefinitionMetadata
    spec: ConfigurationScenarioDefinitionSpec
    __properties: ClassVar[List[str]] = ["$schema", "apiVersion", "kind", "metadata", "spec"]

    @field_validator('var_schema')
    def var_schema_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['https://www.modernedi.com/docs/scenarios/schemas/scenario-definition-v1.schema.json']):
            raise ValueError("must be one of enum values ('https://www.modernedi.com/docs/scenarios/schemas/scenario-definition-v1.schema.json')")
        return value

    @field_validator('api_version')
    def api_version_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['modernedi.com/scenario/v1']):
            raise ValueError("must be one of enum values ('modernedi.com/scenario/v1')")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ScenarioDefinition']):
            raise ValueError("must be one of enum values ('ScenarioDefinition')")
        return value

    model_config = ConfigDict(
        validate_by_name=True,
        validate_by_alias=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(to_jsonable_python(self.to_dict()))

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ModernEDIScenarioDefinitionV1 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_unset=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spec
        if self.spec:
            _dict['spec'] = self.spec.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModernEDIScenarioDefinitionV1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "$schema": obj.get("$schema"),
            "apiVersion": obj.get("apiVersion"),
            "kind": obj.get("kind"),
            "metadata": ConfigurationScenarioDefinitionMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "spec": ConfigurationScenarioDefinitionSpec.from_dict(obj["spec"]) if obj.get("spec") is not None else None
        }.items() if key in obj})
        return _obj
