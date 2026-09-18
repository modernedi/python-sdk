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

class ConfigurationScenarioDefinitionTransaction(BaseModel):
    """
    The business document carried by a step. The server verifies the transaction-set code against ModernEDI's X12 catalog.
    """ # noqa: E501
    standard: StrictStr = Field(description="Transaction standard. v1 supports X12.")
    transaction_set: Annotated[str, Field(strict=True)] = Field(description="Known three-digit X12 business transaction set, such as 850, 855, 856, 810, 875, 880, 940, 945, 204, 214, 300, 301, or 315. Use assurance for 997/999 acknowledgments.", alias="transactionSet")
    business_usage: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="businessUsage")
    __properties: ClassVar[List[str]] = ["standard", "transactionSet", "businessUsage"]

    @field_validator('standard')
    def standard_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['X12']):
            raise ValueError("must be one of enum values ('X12')")
        return value

    @field_validator('transaction_set', mode="before")
    def transaction_set_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^(?!(?:997|999)$)[0-9]{3}$", value):
            raise ValueError(r"must validate the regular expression /^(?!(?:997|999)$)[0-9]{3}$/")
        return value

    @field_validator('business_usage', mode="before")
    def business_usage_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationScenarioDefinitionTransaction from a JSON string"""
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
        """Create an instance of ConfigurationScenarioDefinitionTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "standard": obj.get("standard"),
            "transactionSet": obj.get("transactionSet"),
            "businessUsage": obj.get("businessUsage")
        }.items() if key in obj})
        return _obj
