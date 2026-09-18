# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.x12_transaction_preview import X12TransactionPreview
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class X12TransactionSummary(BaseModel):
    """
    Parsed ST/SE transaction identity and readable segment preview.
    """ # noqa: E501
    functional_group_index: Annotated[int, Field(strict=True, ge=0)] = Field(description="Zero-based index of the containing functional group.", alias="functionalGroupIndex")
    transaction_index: Annotated[int, Field(strict=True, ge=0)] = Field(description="Zero-based transaction index within the group.", alias="transactionIndex")
    transaction_set_identifier_code: StrictStr = Field(description="ST01 transaction-set identifier, such as `850` or `810`.", alias="transactionSetIdentifierCode")
    transaction_set_description: Optional[StrictStr] = Field(description="Human-readable ST01 meaning, or `null` for an unknown code.", alias="transactionSetDescription")
    control_number: StrictStr = Field(description="ST02 transaction control number.", alias="controlNumber")
    preview: X12TransactionPreview
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["functionalGroupIndex", "transactionIndex", "transactionSetIdentifierCode", "transactionSetDescription", "controlNumber", "preview"]

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
        """Create an instance of X12TransactionSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of preview
        if self.preview:
            _dict['preview'] = self.preview.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if transaction_set_description (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_set_description is None and "transaction_set_description" in self.model_fields_set:
            _dict['transactionSetDescription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of X12TransactionSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "functionalGroupIndex": obj.get("functionalGroupIndex"),
            "transactionIndex": obj.get("transactionIndex"),
            "transactionSetIdentifierCode": obj.get("transactionSetIdentifierCode"),
            "transactionSetDescription": obj.get("transactionSetDescription"),
            "controlNumber": obj.get("controlNumber"),
            "preview": X12TransactionPreview.from_dict(obj["preview"]) if obj.get("preview") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
