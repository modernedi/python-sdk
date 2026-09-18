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
from modernedi.generated.models.configuration_scenario_definition_branch_alternative import ConfigurationScenarioDefinitionBranchAlternative
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionBranch(BaseModel):
    """
    A choice between mutually exclusive next-document paths after a named checkpoint. The checkpoint must be emitted by the alternatives' shared source step, so the decision precedes every controlled destination. The emitter must also necessarily observe at least one document; expected_count closure with occurrence min 0 cannot emit a branch checkpoint. All alternatives leave the same source step. Example: after a 301 booking confirmation emits bookingDisposition, choose the 303 cancellation path when cancelRequested=true; otherwise choose 304 shipping instructions. exactly_one must choose one path and therefore requires an otherwise fallback. at_most_one may choose no path. A round evaluates only evidence already available when that round began; its selection can make later steps available in the next round.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    mode: StrictStr
    checkpoint: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    alternatives: Annotated[List[ConfigurationScenarioDefinitionBranchAlternative], Field(min_length=1, max_length=20)] = Field(description="at_most_one accepts one or more when alternatives; exactly_one requires at least two alternatives and exactly one otherwise.")
    __properties: ClassVar[List[str]] = ["id", "mode", "checkpoint", "alternatives"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['exactly_one', 'at_most_one']):
            raise ValueError("must be one of enum values ('exactly_one', 'at_most_one')")
        return value

    @field_validator('checkpoint', mode="before")
    def checkpoint_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationScenarioDefinitionBranch from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in alternatives (list)
        _items = []
        if self.alternatives:
            for _item_alternatives in self.alternatives:
                if _item_alternatives:
                    _items.append(_item_alternatives.to_dict())
            _dict['alternatives'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionBranch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "mode": obj.get("mode"),
            "checkpoint": obj.get("checkpoint"),
            "alternatives": [ConfigurationScenarioDefinitionBranchAlternative.from_dict(_item) for _item in obj["alternatives"]] if obj.get("alternatives") is not None else None
        }.items() if key in obj})
        return _obj
