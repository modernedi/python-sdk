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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.scenario_evidence_mapping_authority import ScenarioEvidenceMappingAuthority
from modernedi.generated.models.scenario_evidence_partner_authority import ScenarioEvidencePartnerAuthority
from modernedi.generated.models.scenario_evidence_syntax_tree_authority import ScenarioEvidenceSyntaxTreeAuthority
from modernedi.generated.models.scenario_evidence_target_authority import ScenarioEvidenceTargetAuthority
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceAuthority(BaseModel):
    """
    ScenarioEvidenceAuthority
    """ # noqa: E501
    partners: Annotated[List[ScenarioEvidencePartnerAuthority], Field(max_length=100)]
    mappings: Annotated[List[ScenarioEvidenceMappingAuthority], Field(max_length=100)]
    syntax_trees: Annotated[List[ScenarioEvidenceSyntaxTreeAuthority], Field(max_length=100)] = Field(alias="syntaxTrees")
    targets: Annotated[List[ScenarioEvidenceTargetAuthority], Field(max_length=100)]
    __properties: ClassVar[List[str]] = ["partners", "mappings", "syntaxTrees", "targets"]

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
        """Create an instance of ScenarioEvidenceAuthority from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in partners (list)
        _items = []
        if self.partners:
            for _item_partners in self.partners:
                if _item_partners:
                    _items.append(_item_partners.to_dict())
            _dict['partners'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mappings (list)
        _items = []
        if self.mappings:
            for _item_mappings in self.mappings:
                if _item_mappings:
                    _items.append(_item_mappings.to_dict())
            _dict['mappings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in syntax_trees (list)
        _items = []
        if self.syntax_trees:
            for _item_syntax_trees in self.syntax_trees:
                if _item_syntax_trees:
                    _items.append(_item_syntax_trees.to_dict())
            _dict['syntaxTrees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item_targets in self.targets:
                if _item_targets:
                    _items.append(_item_targets.to_dict())
            _dict['targets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceAuthority from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "partners": [ScenarioEvidencePartnerAuthority.from_dict(_item) for _item in obj["partners"]] if obj.get("partners") is not None else None,
            "mappings": [ScenarioEvidenceMappingAuthority.from_dict(_item) for _item in obj["mappings"]] if obj.get("mappings") is not None else None,
            "syntaxTrees": [ScenarioEvidenceSyntaxTreeAuthority.from_dict(_item) for _item in obj["syntaxTrees"]] if obj.get("syntaxTrees") is not None else None,
            "targets": [ScenarioEvidenceTargetAuthority.from_dict(_item) for _item in obj["targets"]] if obj.get("targets") is not None else None
        }.items() if key in obj})
        return _obj
