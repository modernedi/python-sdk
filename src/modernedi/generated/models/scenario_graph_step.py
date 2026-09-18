# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.scenario_graph_occurrence import ScenarioGraphOccurrence
from modernedi.generated.models.scenario_graph_step_occurrence import ScenarioGraphStepOccurrence
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioGraphStep(BaseModel):
    """
    ScenarioGraphStep
    """ # noqa: E501
    step_id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="stepId")
    from_actor: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="fromActor")
    to_actor: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="toActor")
    transaction_set: Annotated[str, Field(strict=True)] = Field(alias="transactionSet")
    direction: StrictStr
    target_kind: StrictStr = Field(alias="targetKind")
    attachable: StrictBool = Field(description="True only for runtime_mapping and observation_only targets. Adapter steps are advanced through /advance.")
    occurrence: ScenarioGraphStepOccurrence
    observed_occurrences: List[Annotated[int, Field(strict=True, ge=1)]] = Field(alias="observedOccurrences")
    occurrences: List[ScenarioGraphOccurrence]
    __properties: ClassVar[List[str]] = ["stepId", "fromActor", "toActor", "transactionSet", "direction", "targetKind", "attachable", "occurrence", "observedOccurrences", "occurrences"]

    @field_validator('step_id', mode="before")
    def step_id_validate_regular_expression(cls, value):
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

    @field_validator('transaction_set', mode="before")
    def transaction_set_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9]{3}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{3}$/")
        return value

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['incoming', 'outgoing']):
            raise ValueError("must be one of enum values ('incoming', 'outgoing')")
        return value

    @field_validator('target_kind')
    def target_kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['adapter', 'runtime_mapping', 'observation_only']):
            raise ValueError("must be one of enum values ('adapter', 'runtime_mapping', 'observation_only')")
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
        """Create an instance of ScenarioGraphStep from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of occurrence
        if self.occurrence:
            _dict['occurrence'] = self.occurrence.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in occurrences (list)
        _items = []
        if self.occurrences:
            for _item_occurrences in self.occurrences:
                if _item_occurrences:
                    _items.append(_item_occurrences.to_dict())
            _dict['occurrences'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioGraphStep from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "stepId": obj.get("stepId"),
            "fromActor": obj.get("fromActor"),
            "toActor": obj.get("toActor"),
            "transactionSet": obj.get("transactionSet"),
            "direction": obj.get("direction"),
            "targetKind": obj.get("targetKind"),
            "attachable": obj.get("attachable"),
            "occurrence": ScenarioGraphStepOccurrence.from_dict(obj["occurrence"]) if obj.get("occurrence") is not None else None,
            "observedOccurrences": obj.get("observedOccurrences"),
            "occurrences": [ScenarioGraphOccurrence.from_dict(_item) for _item in obj["occurrences"]] if obj.get("occurrences") is not None else None
        }.items() if key in obj})
        return _obj
