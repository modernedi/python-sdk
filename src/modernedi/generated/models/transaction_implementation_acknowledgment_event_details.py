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
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.implementation_acknowledgment_outcome import ImplementationAcknowledgmentOutcome
from modernedi.generated.models.implementation_acknowledgment_status import ImplementationAcknowledgmentStatus
from modernedi.generated.models.implementation_acknowledgment_transaction_set_outcome import ImplementationAcknowledgmentTransactionSetOutcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionImplementationAcknowledgmentEventDetails(BaseModel):
    """
    TransactionImplementationAcknowledgmentEventDetails
    """ # noqa: E501
    message_id: Optional[StrictStr] = Field(description="AS2 Message-Id of the stored 999.", alias="messageId")
    sent: Optional[StrictBool] = Field(description="Delivery/persistence completion flag from the retained 999 record, or `null` when unavailable. It does not identify sender direction; use the transaction direction and timeline event type.")
    outcome: ImplementationAcknowledgmentOutcome
    evaluation_scope: Optional[StrictStr] = Field(description="Whether the enclosing transaction was evaluated from its exact IK5 result, a unique AK9 group result, or the conservative whole-999 aggregate.", alias="evaluationScope")
    transaction_outcome: Optional[ImplementationAcknowledgmentTransactionSetOutcome] = Field(description="Exact AK2/IK5 result selected for the enclosing transaction, or `null`.", alias="transactionOutcome")
    evaluated_status: Optional[ImplementationAcknowledgmentStatus] = Field(description="Status selected by `evaluationScope`, or `null` when no outcome was attributable.", alias="evaluatedStatus")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["messageId", "sent", "outcome", "evaluationScope", "transactionOutcome", "evaluatedStatus"]

    @field_validator('evaluation_scope')
    def evaluation_scope_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['transaction_set', 'implementation_group', 'implementation_acknowledgment']):
            raise ValueError("must be one of enum values ('transaction_set', 'implementation_group', 'implementation_acknowledgment')")
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
        """Create an instance of TransactionImplementationAcknowledgmentEventDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of outcome
        if self.outcome:
            _dict['outcome'] = self.outcome.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction_outcome
        if self.transaction_outcome:
            _dict['transactionOutcome'] = self.transaction_outcome.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if message_id (nullable) is None
        # and model_fields_set contains the field
        if self.message_id is None and "message_id" in self.model_fields_set:
            _dict['messageId'] = None

        # set to None if sent (nullable) is None
        # and model_fields_set contains the field
        if self.sent is None and "sent" in self.model_fields_set:
            _dict['sent'] = None

        # set to None if evaluation_scope (nullable) is None
        # and model_fields_set contains the field
        if self.evaluation_scope is None and "evaluation_scope" in self.model_fields_set:
            _dict['evaluationScope'] = None

        # set to None if transaction_outcome (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_outcome is None and "transaction_outcome" in self.model_fields_set:
            _dict['transactionOutcome'] = None

        # set to None if evaluated_status (nullable) is None
        # and model_fields_set contains the field
        if self.evaluated_status is None and "evaluated_status" in self.model_fields_set:
            _dict['evaluatedStatus'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionImplementationAcknowledgmentEventDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "messageId": obj.get("messageId"),
            "sent": obj.get("sent"),
            "outcome": ImplementationAcknowledgmentOutcome.from_dict(obj["outcome"]) if obj.get("outcome") is not None else None,
            "evaluationScope": obj.get("evaluationScope"),
            "transactionOutcome": ImplementationAcknowledgmentTransactionSetOutcome.from_dict(obj["transactionOutcome"]) if obj.get("transactionOutcome") is not None else None,
            "evaluatedStatus": obj.get("evaluatedStatus")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
