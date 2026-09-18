# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_scenario_definition_actor import ConfigurationScenarioDefinitionActor
from modernedi.generated.models.configuration_scenario_definition_assertion import ConfigurationScenarioDefinitionAssertion
from modernedi.generated.models.configuration_scenario_definition_branch import ConfigurationScenarioDefinitionBranch
from modernedi.generated.models.configuration_scenario_definition_checkpoint import ConfigurationScenarioDefinitionCheckpoint
from modernedi.generated.models.configuration_scenario_definition_parameter import ConfigurationScenarioDefinitionParameter
from modernedi.generated.models.configuration_scenario_definition_step import ConfigurationScenarioDefinitionStep
from modernedi.generated.models.configuration_scenario_definition_transition import ConfigurationScenarioDefinitionTransition
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionSpec(BaseModel):
    """
    The business-conversation recipe. Actors name the business roles, steps name their X12 document exchanges, and transitions state how those exchanges relate. ModernEDI also verifies unique IDs, references, a connected conversation, and the absence of ordinary transition cycles during Validate and Publish. Omitted transitions, assertions, parameters, checkpoints, or branches mean empty arrays; published JSON materializes every collection.
    """ # noqa: E501
    actors: Annotated[List[ConfigurationScenarioDefinitionActor], Field(min_length=1, max_length=100)] = Field(description="Business roles participating in the conversation. Every actor ID must be unique.")
    steps: Annotated[List[ConfigurationScenarioDefinitionStep], Field(min_length=1, max_length=500)] = Field(description="Business-document exchanges. Every step ID must be unique and must reference two different declared actors.")
    transitions: Optional[Annotated[List[ConfigurationScenarioDefinitionTransition], Field(max_length=2000)]] = Field(default=None, description="Rules connecting document steps. For example, an 810 invoice can follow its matching 850 purchase order, a later 860 can supersede an earlier order change, and an ocean 303 can cancel a matching 301 booking confirmation. Transition IDs must be unique. Except for a same-step supersedes revision chain, ordinary next-document paths cannot loop and every step must belong to one connected conversation.")
    assertions: Optional[Annotated[List[ConfigurationScenarioDefinitionAssertion], Field(max_length=1000)]] = Field(default=None, description="Run-level facts that must hold across one or more observed step occurrences. Assertion IDs must be unique.")
    parameters: Optional[Annotated[List[ConfigurationScenarioDefinitionParameter], Field(max_length=100)]] = Field(default=None, description="Prepared values supplied when a run starts. Parameters declare only their semantic type, required flag, and optional default; bindings and runtime APIs supply values.")
    checkpoints: Optional[Annotated[List[ConfigurationScenarioDefinitionCheckpoint], Field(max_length=100)]] = Field(default=None, description="Named completion events emitted after a step finishes a declared processing stage. A checkpoint can trigger a choice between allowed next steps. For example, a bookingDisposition checkpoint emitted after an X12 301 booking confirmation can choose between an X12 303 cancellation and X12 304 shipping instructions.")
    branches: Optional[Annotated[List[ConfigurationScenarioDefinitionBranch], Field(max_length=100)]] = Field(default=None, description="Explicit choices between allowed next-document transitions, evaluated only after a named checkpoint is emitted. For example, after an X12 301 booking confirmation emits bookingDisposition, cancelRequested=true can select the X12 303 cancellation path and otherwise can select X12 304 shipping instructions. Choices are evaluated in deterministic rounds from the steps already available at the start of that round; a destination document cannot provide the fact that selects its own path.")
    __properties: ClassVar[List[str]] = ["actors", "steps", "transitions", "assertions", "parameters", "checkpoints", "branches"]

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
        """Create an instance of ConfigurationScenarioDefinitionSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in actors (list)
        _items = []
        if self.actors:
            for _item_actors in self.actors:
                if _item_actors:
                    _items.append(_item_actors.to_dict())
            _dict['actors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transitions (list)
        _items = []
        if self.transitions:
            for _item_transitions in self.transitions:
                if _item_transitions:
                    _items.append(_item_transitions.to_dict())
            _dict['transitions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in assertions (list)
        _items = []
        if self.assertions:
            for _item_assertions in self.assertions:
                if _item_assertions:
                    _items.append(_item_assertions.to_dict())
            _dict['assertions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item_parameters in self.parameters:
                if _item_parameters:
                    _items.append(_item_parameters.to_dict())
            _dict['parameters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in checkpoints (list)
        _items = []
        if self.checkpoints:
            for _item_checkpoints in self.checkpoints:
                if _item_checkpoints:
                    _items.append(_item_checkpoints.to_dict())
            _dict['checkpoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in branches (list)
        _items = []
        if self.branches:
            for _item_branches in self.branches:
                if _item_branches:
                    _items.append(_item_branches.to_dict())
            _dict['branches'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "actors": [ConfigurationScenarioDefinitionActor.from_dict(_item) for _item in obj["actors"]] if obj.get("actors") is not None else None,
            "steps": [ConfigurationScenarioDefinitionStep.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "transitions": [ConfigurationScenarioDefinitionTransition.from_dict(_item) for _item in obj["transitions"]] if obj.get("transitions") is not None else None,
            "assertions": [ConfigurationScenarioDefinitionAssertion.from_dict(_item) for _item in obj["assertions"]] if obj.get("assertions") is not None else None,
            "parameters": [ConfigurationScenarioDefinitionParameter.from_dict(_item) for _item in obj["parameters"]] if obj.get("parameters") is not None else None,
            "checkpoints": [ConfigurationScenarioDefinitionCheckpoint.from_dict(_item) for _item in obj["checkpoints"]] if obj.get("checkpoints") is not None else None,
            "branches": [ConfigurationScenarioDefinitionBranch.from_dict(_item) for _item in obj["branches"]] if obj.get("branches") is not None else None
        }.items() if key in obj})
        return _obj
