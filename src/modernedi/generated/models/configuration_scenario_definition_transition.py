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
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.configuration_scenario_definition_correlation import ConfigurationScenarioDefinitionCorrelation
from modernedi.generated.models.configuration_scenario_definition_occurrence_matching import ConfigurationScenarioDefinitionOccurrenceMatching
from modernedi.generated.models.configuration_scenario_definition_revision_effect import ConfigurationScenarioDefinitionRevisionEffect
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionTransition(BaseModel):
    """
    A rule from one document step to another. Correlations identify which actual documents belong together. follows models ordinary order, such as a matching 810 invoice after an 850 order. supersedes records a replacement, such as a later 860 order change replacing the prior 850 or 860. cancels records a removal, such as an ocean 303 cancellation for a 301 booking confirmation. Supersedes and cancels inspect every stored observation before any replacement or cancellation is applied; they do not make an otherwise unavailable next-document path available and cannot themselves be branch alternatives.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    from_step: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="fromStep")
    to_step: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="toStep")
    relationship: StrictStr = Field(description="Choose follows when a matched later document must occur at or after the earlier one, such as an 810 invoice after its 850 order. Choose supersedes when the later document replaces the matched earlier occurrence, such as an 860 order change replacing an 850 or prior 860. Choose cancels when the later document cancels the matched earlier occurrence, such as an ocean 303 cancelling a 301 booking confirmation. supersedes and cancels require effect to say when the change begins and whether later checks keep using the original document or reevaluate with the replacement/removal. Business labels such as acknowledges, reports status, or settles belong in the transition ID and prose unless an assertion or evidence requirement actually verifies them.")
    within: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="A positive ISO 8601 duration accepted by java.time.Duration, no longer than P365D. Examples: PT30M, PT4H, P2D. The server enforces the upper bound.")
    correlations: Optional[Annotated[List[ConfigurationScenarioDefinitionCorrelation], Field(min_length=0, max_length=100)]] = Field(default=None, description="Conditions the scenario evaluator uses to pair actual source and target documents. For example, compare the purchase-order number extracted from an 850 with the purchase-order number extracted from an 810. Correlation IDs must be unique within this transition.")
    matching: ConfigurationScenarioDefinitionOccurrenceMatching
    effect: Optional[ConfigurationScenarioDefinitionRevisionEffect] = None
    __properties: ClassVar[List[str]] = ["id", "fromStep", "toStep", "relationship", "within", "correlations", "matching", "effect"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('from_step', mode="before")
    def from_step_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('to_step', mode="before")
    def to_step_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('relationship')
    def relationship_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['follows', 'supersedes', 'cancels']):
            raise ValueError("must be one of enum values ('follows', 'supersedes', 'cancels')")
        return value

    @field_validator('within', mode="before")
    def within_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^P(?=.+)(?!0+(?:D|T(?:0+H)?(?:0+M)?(?:0+(?:\.0+)?S)?$))(?:[0-9]+D)?(?:T(?=[0-9])(?:[0-9]+H)?(?:[0-9]+M)?(?:[0-9]+(?:\.[0-9]+)?S)?)?$", value):
            raise ValueError(r"must validate the regular expression /^P(?=.+)(?!0+(?:D|T(?:0+H)?(?:0+M)?(?:0+(?:\.0+)?S)?$))(?:[0-9]+D)?(?:T(?=[0-9])(?:[0-9]+H)?(?:[0-9]+M)?(?:[0-9]+(?:\.[0-9]+)?S)?)?$/")
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
        """Create an instance of ConfigurationScenarioDefinitionTransition from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in correlations (list)
        _items = []
        if self.correlations:
            for _item_correlations in self.correlations:
                if _item_correlations:
                    _items.append(_item_correlations.to_dict())
            _dict['correlations'] = _items
        # override the default output from pydantic by calling `to_dict()` of matching
        if self.matching:
            _dict['matching'] = self.matching.to_dict()
        # override the default output from pydantic by calling `to_dict()` of effect
        if self.effect:
            _dict['effect'] = self.effect.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionTransition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "fromStep": obj.get("fromStep"),
            "toStep": obj.get("toStep"),
            "relationship": obj.get("relationship"),
            "within": obj.get("within"),
            "correlations": [ConfigurationScenarioDefinitionCorrelation.from_dict(_item) for _item in obj["correlations"]] if obj.get("correlations") is not None else None,
            "matching": ConfigurationScenarioDefinitionOccurrenceMatching.from_dict(obj["matching"]) if obj.get("matching") is not None else None,
            "effect": ConfigurationScenarioDefinitionRevisionEffect.from_dict(obj["effect"]) if obj.get("effect") is not None else None
        }.items() if key in obj})
        return _obj
