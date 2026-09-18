# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_scenario_definition_assurance import ConfigurationScenarioDefinitionAssurance
from modernedi.generated.models.configuration_scenario_definition_fact_declaration import ConfigurationScenarioDefinitionFactDeclaration
from modernedi.generated.models.configuration_scenario_definition_occurrence import ConfigurationScenarioDefinitionOccurrence
from modernedi.generated.models.configuration_scenario_definition_pipeline_stage import ConfigurationScenarioDefinitionPipelineStage
from modernedi.generated.models.configuration_scenario_definition_transaction import ConfigurationScenarioDefinitionTransaction
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionStep(BaseModel):
    """
    One directed X12 business-document exchange. Functional acknowledgments (997/999) are evidence requirements, not business steps.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    from_actor: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="fromActor")
    to_actor: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="toActor")
    transaction: ConfigurationScenarioDefinitionTransaction
    occurrence: ConfigurationScenarioDefinitionOccurrence
    assurance: Optional[ConfigurationScenarioDefinitionAssurance] = None
    facts: Annotated[List[ConfigurationScenarioDefinitionFactDeclaration], Field(max_length=100)] = Field(description="Typed semantic facts exposed by this step. Use an empty array when the step exposes none. Declarations name the stable ABI only; extraction provenance belongs to runtime capability and binding layers.")
    pipeline: Annotated[List[ConfigurationScenarioDefinitionPipelineStage], Field(min_length=1, max_length=20)] = Field(description="Ordered abstract processing stages for each step occurrence. Stages describe behavior without naming mapper or transport artifacts.")
    __properties: ClassVar[List[str]] = ["id", "fromActor", "toActor", "transaction", "occurrence", "assurance", "facts", "pipeline"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('from_actor', mode="before")
    def from_actor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('to_actor', mode="before")
    def to_actor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
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
        """Create an instance of ConfigurationScenarioDefinitionStep from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of occurrence
        if self.occurrence:
            _dict['occurrence'] = self.occurrence.to_dict()
        # override the default output from pydantic by calling `to_dict()` of assurance
        if self.assurance:
            _dict['assurance'] = self.assurance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in facts (list)
        _items = []
        if self.facts:
            for _item_facts in self.facts:
                if _item_facts:
                    _items.append(_item_facts.to_dict())
            _dict['facts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pipeline (list)
        _items = []
        if self.pipeline:
            for _item_pipeline in self.pipeline:
                if _item_pipeline:
                    _items.append(_item_pipeline.to_dict())
            _dict['pipeline'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "fromActor": obj.get("fromActor"),
            "toActor": obj.get("toActor"),
            "transaction": ConfigurationScenarioDefinitionTransaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "occurrence": ConfigurationScenarioDefinitionOccurrence.from_dict(obj["occurrence"]) if obj.get("occurrence") is not None else None,
            "assurance": ConfigurationScenarioDefinitionAssurance.from_dict(obj["assurance"]) if obj.get("assurance") is not None else None,
            "facts": [ConfigurationScenarioDefinitionFactDeclaration.from_dict(_item) for _item in obj["facts"]] if obj.get("facts") is not None else None,
            "pipeline": [ConfigurationScenarioDefinitionPipelineStage.from_dict(_item) for _item in obj["pipeline"]] if obj.get("pipeline") is not None else None
        }.items() if key in obj})
        return _obj
