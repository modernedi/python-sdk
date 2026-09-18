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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappingRegressionCase(BaseModel):
    """
    An exact-output test for the existing Mapper engines. Whitespace, line endings, ordering, and delimiters are significant. Incoming X12 Mapper requires application/edi-x12 and null params; its zero-based group and transaction selectors may be null. Outgoing JSLT/XSLT requires JSON/XML input and null selectors; params is an object or null. Outgoing cases may additionally select validateX12 to check the generated document against the mapping's X12 specification using the normal preview/send envelope preparation. No execution results or timestamps belong in this source document.
    """ # noqa: E501
    id: Annotated[str, Field(strict=True, max_length=64)]
    name: Annotated[str, Field(min_length=1, strict=True, max_length=120)]
    comparison: StrictStr
    validate_x12: Optional[StrictBool] = Field(default=None, description="Optional outgoing-only document validation in addition to exact-text comparison. Defaults to false when omitted. Complete document bodies are wrapped for validation; partial fragments need not opt in. Does not send EDI or prove business correctness or partner acceptance.", alias="validateX12")
    input: Annotated[str, Field(strict=True, max_length=65536)]
    content_type: StrictStr = Field(alias="contentType")
    params: Optional[Dict[str, Any]]
    functional_group_index: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(alias="functionalGroupIndex")
    transaction_index: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=0)]] = Field(alias="transactionIndex")
    expected_output: Annotated[str, Field(strict=True, max_length=65536)] = Field(alias="expectedOutput")
    __properties: ClassVar[List[str]] = ["id", "name", "comparison", "validateX12", "input", "contentType", "params", "functionalGroupIndex", "transactionIndex", "expectedOutput"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,63}$/")
        return value

    @field_validator('name', mode="before")
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"\S", value):
            raise ValueError(r"must validate the regular expression /\S/")
        return value

    @field_validator('comparison')
    def comparison_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['EXACT_TEXT']):
            raise ValueError("must be one of enum values ('EXACT_TEXT')")
        return value

    @field_validator('content_type')
    def content_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['application/edi-x12', 'application/json', 'application/xml', 'text/xml']):
            raise ValueError("must be one of enum values ('application/edi-x12', 'application/json', 'application/xml', 'text/xml')")
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
        """Create an instance of MappingRegressionCase from a JSON string"""
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
        # set to None if params (nullable) is None
        # and model_fields_set contains the field
        if self.params is None and "params" in self.model_fields_set:
            _dict['params'] = None

        # set to None if functional_group_index (nullable) is None
        # and model_fields_set contains the field
        if self.functional_group_index is None and "functional_group_index" in self.model_fields_set:
            _dict['functionalGroupIndex'] = None

        # set to None if transaction_index (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_index is None and "transaction_index" in self.model_fields_set:
            _dict['transactionIndex'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappingRegressionCase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "name": obj.get("name"),
            "comparison": obj.get("comparison"),
            "validateX12": obj.get("validateX12"),
            "input": obj.get("input"),
            "contentType": obj.get("contentType"),
            "params": obj.get("params"),
            "functionalGroupIndex": obj.get("functionalGroupIndex"),
            "transactionIndex": obj.get("transactionIndex"),
            "expectedOutput": obj.get("expectedOutput")
        }.items() if key in obj})
        return _obj
