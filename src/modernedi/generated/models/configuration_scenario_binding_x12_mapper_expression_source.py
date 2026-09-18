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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioBindingX12MapperExpressionSource(BaseModel):
    """
    Evaluates one ordinary X12 Mapper expression against the step transaction. Validate and Apply use the same parser, semantic validator, function registry, budget mechanism, and syntax-tree-aware engine as runtime mappings and primaryKeyExtractor, with scenario-specific bounded limits. Validate and Apply reject an expression that is statically incapable of reading an X12 segment or element, and runtime fails closed when the executed path produces no concrete X12 read. Scenario evidence uses that engine's element-read tracing facility; this does not imply that existing primary-key persistence emits the same trace. The ScenarioDefinition remains authoritative for value type, cardinality, normalization, and sensitivity.
    """ # noqa: E501
    kind: StrictStr = Field(description="Uses ModernEDI's existing X12 Mapper expression language and engine, shared with primaryKeyExtractor.")
    expression: Annotated[str, Field(min_length=1, strict=True, max_length=16384)] = Field(description="One value-returning X12 Mapper expression that reads at least one X12 segment or element. A constant-only expression cannot provide authoritative document evidence. Scalars, lists, and sets are interpreted according to the matching fact declaration; secrets and credentials must never appear here.", json_schema_extra={"examples": ["ST->BEG(03)"]})
    __properties: ClassVar[List[str]] = ["kind", "expression"]

    @field_validator('kind')
    def kind_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['x12-mapper-expression']):
            raise ValueError("must be one of enum values ('x12-mapper-expression')")
        return value

    @field_validator('expression', mode="before")
    def expression_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"\S", value):
            raise ValueError(r"must validate the regular expression /\S/")
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
        """Create an instance of ConfigurationScenarioBindingX12MapperExpressionSource from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioBindingX12MapperExpressionSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "kind": obj.get("kind"),
            "expression": obj.get("expression")
        }.items() if key in obj})
        return _obj
