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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.configuration_scenario_definition_predicate import ConfigurationScenarioDefinitionPredicate
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionBranchAlternative(BaseModel):
    """
    One ordinary follows transition that a branch may select, either when its conditions pass or as the explicit otherwise fallback. For example, cancelRequested=true selects the 301-to-303 follows transition; otherwise selects 301-to-304. supersedes and cancels transitions are revision records, not branch alternatives.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    kind: StrictStr
    transition_id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="transitionId")
    conditions: Annotated[List[ConfigurationScenarioDefinitionPredicate], Field(max_length=20)] = Field(description="Conditions may use parameters, literals, or facts from the alternatives' shared fromStep. They cannot read a destination step to select that destination.")
    __properties: ClassVar[List[str]] = ["id", "kind", "transitionId", "conditions"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['when', 'otherwise']):
            raise ValueError("must be one of enum values ('when', 'otherwise')")
        return value

    @field_validator('transition_id', mode="before")
    def transition_id_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationScenarioDefinitionBranchAlternative from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionBranchAlternative from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "kind": obj.get("kind"),
            "transitionId": obj.get("transitionId"),
            "conditions": [ConfigurationScenarioDefinitionPredicate.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None
        }.items() if key in obj})
        return _obj
