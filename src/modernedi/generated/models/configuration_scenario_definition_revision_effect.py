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
from typing import Any, ClassVar, Dict
from modernedi.generated.models.configuration_scenario_definition_effective_at import ConfigurationScenarioDefinitionEffectiveAt
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioDefinitionRevisionEffect(BaseModel):
    """
    What a matched replacement or cancellation changes. Raw immutable observation history means every received document remains stored unchanged; the revision rule changes only the run's interpreted business view. A revision transition does not open a next-document path by itself. Each branch-decision round first snapshots the steps already allowed; its conditions see only active reevaluate effects whose original and later-document steps are both in that snapshot, and a chosen path becomes available only in the next round. After branch selection, a revision affects checks only when both endpoint steps remain on the selected conversation path. If several active reevaluate effects target the same original document, the later effectiveAt wins; equal latest times fail with REVISION_EFFECT_CONFLICT instead of choosing arbitrarily.
    """ # noqa: E501
    effective_at: ConfigurationScenarioDefinitionEffectiveAt = Field(alias="effectiveAt")
    downstream: StrictStr = Field(description="retain records the change and effective time but keeps using the original document for branch conditions, ordinary follows transitions, and assertions; for example, record an advisory 860 while later shipment checks still use the original 850. reevaluate recomputes those same consumers with the replacement or removal; for example, use the revised 860 values for later 856/810 checks, or remove a 301 booking confirmation after its 303 cancellation.")
    unmatched: StrictStr = Field(description="Behavior when no prior effective occurrence can be revised or cancelled. previous matching requires record because the first occurrence is the initial revision and necessarily has no prior occurrence.")
    __properties: ClassVar[List[str]] = ["effectiveAt", "downstream", "unmatched"]

    @field_validator('downstream')
    def downstream_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['retain', 'reevaluate']):
            raise ValueError("must be one of enum values ('retain', 'reevaluate')")
        return value

    @field_validator('unmatched')
    def unmatched_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['fail', 'record']):
            raise ValueError("must be one of enum values ('fail', 'record')")
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
        """Create an instance of ConfigurationScenarioDefinitionRevisionEffect from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of effective_at
        if self.effective_at:
            _dict['effectiveAt'] = self.effective_at.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioDefinitionRevisionEffect from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "effectiveAt": ConfigurationScenarioDefinitionEffectiveAt.from_dict(obj["effectiveAt"]) if obj.get("effectiveAt") is not None else None,
            "downstream": obj.get("downstream"),
            "unmatched": obj.get("unmatched")
        }.items() if key in obj})
        return _obj
