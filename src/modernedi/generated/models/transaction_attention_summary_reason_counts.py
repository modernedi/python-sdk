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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionAttentionSummaryReasonCounts(BaseModel):
    """
    Active transaction counts by independently applicable attention reason.
    """ # noqa: E501
    mapping_failure: Annotated[int, Field(strict=True, ge=0)] = Field(description="Transactions with one or more unresolved mapping attempts.", alias="mappingFailure")
    functional_ack_issue: Annotated[int, Field(strict=True, ge=0)] = Field(description="Transactions with a received 997 that was not cleanly accepted.", alias="functionalAckIssue")
    implementation_ack_issue: Annotated[int, Field(strict=True, ge=0)] = Field(description="Transactions with a received 999 whose selected IK5 or AK9 result was not cleanly accepted.", alias="implementationAckIssue")
    x12_ack_overdue: Annotated[int, Field(strict=True, ge=0)] = Field(description="Eligible outbound transactions with neither a 997 nor a 999 received by their response deadline.", alias="x12AckOverdue")
    technical_ack_issue: Annotated[int, Field(strict=True, ge=0)] = Field(description="Outbound transactions whose requested TA1 rejected the interchange, reported errors, or could not be classified.", alias="technicalAckIssue")
    technical_ack_overdue: Annotated[int, Field(strict=True, ge=0)] = Field(description="Outbound transactions whose ISA14 requested a TA1 that was not received by its response deadline.", alias="technicalAckOverdue")
    as2_mdn_attention: Annotated[int, Field(strict=True, ge=0)] = Field(description="Outbound transactions whose AS2 MDN is overdue or was received with a warning, rejection, validation failure, or content-MIC mismatch.", alias="as2MdnAttention")
    mapped_output_not_collected: Annotated[int, Field(strict=True, ge=0)] = Field(description="Transactions with at least one managed output that was not collected within the 15-minute pickup grace period.", alias="mappedOutputNotCollected")
    mapped_output_ack_overdue: Annotated[int, Field(strict=True, ge=0)] = Field(description="Transactions with an expired unacknowledged output lease or an unacknowledged redelivery.", alias="mappedOutputAckOverdue")
    watchlist: Annotated[int, Field(strict=True, ge=0)] = Field(description="Transactions placed on an active operator watchlist independently of automated failure signals.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["mappingFailure", "functionalAckIssue", "implementationAckIssue", "x12AckOverdue", "technicalAckIssue", "technicalAckOverdue", "as2MdnAttention", "mappedOutputNotCollected", "mappedOutputAckOverdue", "watchlist"]

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
        """Create an instance of TransactionAttentionSummaryReasonCounts from a JSON string"""
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
        """Create an instance of TransactionAttentionSummaryReasonCounts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "mappingFailure": obj.get("mappingFailure"),
            "functionalAckIssue": obj.get("functionalAckIssue"),
            "implementationAckIssue": obj.get("implementationAckIssue"),
            "x12AckOverdue": obj.get("x12AckOverdue"),
            "technicalAckIssue": obj.get("technicalAckIssue"),
            "technicalAckOverdue": obj.get("technicalAckOverdue"),
            "as2MdnAttention": obj.get("as2MdnAttention"),
            "mappedOutputNotCollected": obj.get("mappedOutputNotCollected"),
            "mappedOutputAckOverdue": obj.get("mappedOutputAckOverdue"),
            "watchlist": obj.get("watchlist")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
