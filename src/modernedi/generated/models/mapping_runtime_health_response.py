# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List
from modernedi.generated.models.mapping_runtime_health_totals import MappingRuntimeHealthTotals
from modernedi.generated.models.mapping_runtime_mapping_health import MappingRuntimeMappingHealth
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappingRuntimeHealthResponse(BaseModel):
    """
    Environment-wide summary of retained mapping failures and recoveries.
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true`; authorization, billing, or runtime-read failures use an error response.")
    environment: TransactionEnvironmentValue
    generated_at: str = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`.", alias="generatedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    truncated: StrictBool = Field(description="True when the bounded health scan could not summarize every retained attempt.")
    totals: MappingRuntimeHealthTotals
    mappings: List[MappingRuntimeMappingHealth] = Field(description="Mapping- or unmatched-request-level groups with failure or recovery activity.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "environment", "generatedAt", "truncated", "totals", "mappings"]

    @field_validator('generated_at', mode="before")
    def generated_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
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
        """Create an instance of MappingRuntimeHealthResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_unset=True,
        )
        # override the default output from pydantic by calling `to_dict()` of totals
        if self.totals:
            _dict['totals'] = self.totals.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in mappings (list)
        _items = []
        if self.mappings:
            for _item_mappings in self.mappings:
                if _item_mappings:
                    _items.append(_item_mappings.to_dict())
            _dict['mappings'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappingRuntimeHealthResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "environment": obj.get("environment"),
            "generatedAt": obj.get("generatedAt"),
            "truncated": obj.get("truncated"),
            "totals": MappingRuntimeHealthTotals.from_dict(obj["totals"]) if obj.get("totals") is not None else None,
            "mappings": [MappingRuntimeMappingHealth.from_dict(_item) for _item in obj["mappings"]] if obj.get("mappings") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
