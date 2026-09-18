# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class UsageSignals(BaseModel):
    """
    Current-day workload-shape indicators derived from accepted transaction rows and message ids.
    """ # noqa: E501
    transaction_rows_today: StrictInt = Field(description="Total transaction-set rows recorded today; may exceed message count when interchanges are batched.", alias="transactionRowsToday")
    multi_transaction_message_ids_today: StrictInt = Field(description="Distinct AS2 message ids that contained more than one transaction row today.", alias="multiTransactionMessageIdsToday")
    busiest_hour: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="UTC `HH:00` bucket with the most messages today, or `null` when no messages were recorded.", alias="busiestHour", json_schema_extra={"examples": ["18:00"]})
    busiest_hour_messages: StrictInt = Field(description="Distinct AS2 message count in `busiestHour`, or zero when there is no busiest hour.", alias="busiestHourMessages")
    top_partner_name: Optional[StrictStr] = Field(default=None, description="Partner with the most messages today, or `null` when no partner-attributed messages were recorded.", alias="topPartnerName")
    top_partner_messages: StrictInt = Field(description="Distinct AS2 message count for `topPartnerName`, or zero when no top partner exists.", alias="topPartnerMessages")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["transactionRowsToday", "multiTransactionMessageIdsToday", "busiestHour", "busiestHourMessages", "topPartnerName", "topPartnerMessages"]

    @field_validator('busiest_hour', mode="before")
    def busiest_hour_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of UsageSignals from a JSON string"""
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

        # set to None if busiest_hour (nullable) is None
        # and model_fields_set contains the field
        if self.busiest_hour is None and "busiest_hour" in self.model_fields_set:
            _dict['busiestHour'] = None

        # set to None if top_partner_name (nullable) is None
        # and model_fields_set contains the field
        if self.top_partner_name is None and "top_partner_name" in self.model_fields_set:
            _dict['topPartnerName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UsageSignals from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "transactionRowsToday": obj.get("transactionRowsToday"),
            "multiTransactionMessageIdsToday": obj.get("multiTransactionMessageIdsToday"),
            "busiestHour": obj.get("busiestHour"),
            "busiestHourMessages": obj.get("busiestHourMessages"),
            "topPartnerName": obj.get("topPartnerName"),
            "topPartnerMessages": obj.get("topPartnerMessages")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
