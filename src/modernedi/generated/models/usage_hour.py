# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UsageHour(BaseModel):
    """
    Current UTC-day message and transaction volume for one UTC hour.
    """ # noqa: E501
    hour: Annotated[str, Field(strict=True)] = Field(description="Hour bucket label in `HH:00` form.", json_schema_extra={"examples": ["14:00"]})
    inbound_messages: StrictInt = Field(description="Distinct inbound AS2 messages accepted during this UTC hour.", alias="inboundMessages")
    outbound_messages: StrictInt = Field(description="Distinct outbound AS2 messages accepted during this UTC hour.", alias="outboundMessages")
    total_messages: StrictInt = Field(description="Combined inbound and outbound accepted messages during this UTC hour.", alias="totalMessages")
    transaction_rows: StrictInt = Field(description="Transaction-set rows recorded during this UTC hour; one AS2 message may contain multiple rows.", alias="transactionRows")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["hour", "inboundMessages", "outboundMessages", "totalMessages", "transactionRows"]

    @field_validator('hour', mode="before")
    def hour_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^(?:[01][0-9]|2[0-3]):00$", value):
            raise ValueError(r"must validate the regular expression /^(?:[01][0-9]|2[0-3]):00$/")
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
        """Create an instance of UsageHour from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsageHour from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "hour": obj.get("hour"),
            "inboundMessages": obj.get("inboundMessages"),
            "outboundMessages": obj.get("outboundMessages"),
            "totalMessages": obj.get("totalMessages"),
            "transactionRows": obj.get("transactionRows")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
