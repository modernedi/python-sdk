# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioBindingSyntaxTreeReference(BaseModel):
    """
    Optional authoring-time pin to an exact X12 release and transaction set. Both fields are required when this object is present.
    """ # noqa: E501
    x12_version: Annotated[str, Field(strict=True)] = Field(description="X12 release token. Apply canonicalizes accepted forms to a six-digit release such as 004010.", alias="x12Version", json_schema_extra={"examples": ["004010"]})
    transaction_set: Annotated[str, Field(strict=True)] = Field(description="Known three-digit X12 transaction set. The code must match the referenced definition step.", alias="transactionSet")
    __properties: ClassVar[List[str]] = ["x12Version", "transactionSet"]

    @field_validator('x12_version', mode="before")
    def x12_version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[Vv]?(?:00)?[1-9][0-9]{3}$", value):
            raise ValueError(r"must validate the regular expression /^[Vv]?(?:00)?[1-9][0-9]{3}$/")
        return value

    @field_validator('transaction_set', mode="before")
    def transaction_set_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9]{3}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{3}$/")
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
        """Create an instance of ConfigurationScenarioBindingSyntaxTreeReference from a JSON string"""
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
        """Create an instance of ConfigurationScenarioBindingSyntaxTreeReference from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "x12Version": obj.get("x12Version"),
            "transactionSet": obj.get("transactionSet")
        }.items() if key in obj})
        return _obj
