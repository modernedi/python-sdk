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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.functional_acknowledgment_group_summary import FunctionalAcknowledgmentGroupSummary
from modernedi.generated.models.functional_acknowledgment_summary import FunctionalAcknowledgmentSummary
from modernedi.generated.models.functional_acknowledgment_transaction_set_outcome import FunctionalAcknowledgmentTransactionSetOutcome
from modernedi.generated.models.implementation_acknowledgment_summary import ImplementationAcknowledgmentSummary
from modernedi.generated.models.implementation_acknowledgment_transaction_set_outcome import ImplementationAcknowledgmentTransactionSetOutcome
from modernedi.generated.models.technical_acknowledgment_outcome import TechnicalAcknowledgmentOutcome
from modernedi.generated.models.technical_acknowledgment_status import TechnicalAcknowledgmentStatus
from modernedi.generated.models.transaction_business_key import TransactionBusinessKey
from modernedi.generated.models.transaction_control_numbers import TransactionControlNumbers
from modernedi.generated.models.transaction_edi_metadata import TransactionEdiMetadata
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from modernedi.generated.models.transaction_set import TransactionSet
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionTimelineSummary(BaseModel):
    """
    Stable transaction identity used inside transaction and reply timeline events. It intentionally omits the current attention and mapping projections; refetch transaction detail for authoritative current state.
    """ # noqa: E501
    id: StrictStr = Field(description="Convenience id formatted as `<messageId>/<transactionKey>`.")
    environment: TransactionEnvironmentValue
    message_id: StrictStr = Field(description="AS2 Message-Id that identifies the transaction for detail and correlation requests.", alias="messageId")
    transaction_key: StrictStr = Field(description="Transaction identifier within the AS2 message, usually `GS06#ST02`.", alias="transactionKey")
    reply_to_message_id: Optional[StrictStr] = Field(description="Source inbound message for an outbound reply, or `null`.", alias="replyToMessageId")
    reply_to_transaction_key: Optional[StrictStr] = Field(description="Exact source transaction for an outbound reply, or `null` for a non-reply.", alias="replyToTransactionKey")
    direction: StrictStr = Field(description="Direction across the ModernEDI boundary at the time this timeline snapshot was created.")
    partner_name: StrictStr = Field(description="Partner name captured at processing time.", alias="partnerName")
    partner_id: Optional[StrictInt] = Field(description="Stable tenant-scoped partner id.", alias="partnerId")
    timestamp: str = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`.", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    transaction_set: TransactionSet = Field(alias="transactionSet")
    control_numbers: TransactionControlNumbers = Field(alias="controlNumbers")
    edi: TransactionEdiMetadata
    business_key: Optional[TransactionBusinessKey] = Field(alias="businessKey")
    functional_ack_outcome: Optional[FunctionalAcknowledgmentSummary] = Field(alias="functionalAckOutcome")
    functional_ack_transaction_outcome: Optional[FunctionalAcknowledgmentTransactionSetOutcome] = Field(description="Exact AK2/AK5 outcome uniquely attributable to this transaction, or `null`.", alias="functionalAckTransactionOutcome")
    functional_ack_group_outcome: Optional[FunctionalAcknowledgmentGroupSummary] = Field(description="Compact AK1/AK9 group outcome uniquely attributable to this transaction, or `null`.", alias="functionalAckGroupOutcome")
    functional_ack_evaluation_scope: Optional[StrictStr] = Field(description="Whether operator status used the exact transaction-set result, the matching group, or the whole-997 ambiguity fallback.", alias="functionalAckEvaluationScope")
    implementation_ack_outcome: Optional[ImplementationAcknowledgmentSummary] = Field(description="Compact aggregate and group-level 999 context, or `null` when no 999 was attributable.", alias="implementationAckOutcome")
    implementation_ack_transaction_outcome: Optional[ImplementationAcknowledgmentTransactionSetOutcome] = Field(description="Exact AK2/IK5 outcome uniquely attributable to this transaction, or `null`.", alias="implementationAckTransactionOutcome")
    implementation_ack_evaluation_scope: Optional[StrictStr] = Field(description="Whether operator status used the exact IK5 result, a unique AK9 group result, or the conservative whole-999 aggregate.", alias="implementationAckEvaluationScope")
    x12_acknowledgment_expected_by: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="x12AcknowledgmentExpectedBy", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    technical_ack_requested: StrictBool = Field(description="Whether outbound ISA14 requested a TA1 for this timeline snapshot.", alias="technicalAckRequested")
    technical_ack_status: TechnicalAcknowledgmentStatus = Field(alias="technicalAckStatus")
    technical_ack_expected_by: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="technicalAckExpectedBy", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    technical_ack_outcome: Optional[TechnicalAcknowledgmentOutcome] = Field(description="Parsed TA1 outcome correlated to the interchange represented by this timeline snapshot, or `null` while no TA1 is available. Use `technicalAckStatus` and the `technical_ack_overdue` attention reason to distinguish not requested, pending, and overdue states; a null outcome alone is not evidence that the partner accepted the interchange. ", alias="technicalAckOutcome")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "environment", "messageId", "transactionKey", "replyToMessageId", "replyToTransactionKey", "direction", "partnerName", "partnerId", "timestamp", "transactionSet", "controlNumbers", "edi", "businessKey", "functionalAckOutcome", "functionalAckTransactionOutcome", "functionalAckGroupOutcome", "functionalAckEvaluationScope", "implementationAckOutcome", "implementationAckTransactionOutcome", "implementationAckEvaluationScope", "x12AcknowledgmentExpectedBy", "technicalAckRequested", "technicalAckStatus", "technicalAckExpectedBy", "technicalAckOutcome"]

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['inbound', 'outbound']):
            raise ValueError("must be one of enum values ('inbound', 'outbound')")
        return value

    @field_validator('timestamp', mode="before")
    def timestamp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('functional_ack_evaluation_scope')
    def functional_ack_evaluation_scope_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['transaction_set', 'functional_group', 'functional_acknowledgment']):
            raise ValueError("must be one of enum values ('transaction_set', 'functional_group', 'functional_acknowledgment')")
        return value

    @field_validator('implementation_ack_evaluation_scope')
    def implementation_ack_evaluation_scope_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['transaction_set', 'implementation_group', 'implementation_acknowledgment']):
            raise ValueError("must be one of enum values ('transaction_set', 'implementation_group', 'implementation_acknowledgment')")
        return value

    @field_validator('x12_acknowledgment_expected_by', mode="before")
    def x12_acknowledgment_expected_by_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('technical_ack_expected_by', mode="before")
    def technical_ack_expected_by_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
        """Create an instance of TransactionTimelineSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of transaction_set
        if self.transaction_set:
            _dict['transactionSet'] = self.transaction_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of control_numbers
        if self.control_numbers:
            _dict['controlNumbers'] = self.control_numbers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edi
        if self.edi:
            _dict['edi'] = self.edi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_key
        if self.business_key:
            _dict['businessKey'] = self.business_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of functional_ack_outcome
        if self.functional_ack_outcome:
            _dict['functionalAckOutcome'] = self.functional_ack_outcome.to_dict()
        # override the default output from pydantic by calling `to_dict()` of functional_ack_transaction_outcome
        if self.functional_ack_transaction_outcome:
            _dict['functionalAckTransactionOutcome'] = self.functional_ack_transaction_outcome.to_dict()
        # override the default output from pydantic by calling `to_dict()` of functional_ack_group_outcome
        if self.functional_ack_group_outcome:
            _dict['functionalAckGroupOutcome'] = self.functional_ack_group_outcome.to_dict()
        # override the default output from pydantic by calling `to_dict()` of implementation_ack_outcome
        if self.implementation_ack_outcome:
            _dict['implementationAckOutcome'] = self.implementation_ack_outcome.to_dict()
        # override the default output from pydantic by calling `to_dict()` of implementation_ack_transaction_outcome
        if self.implementation_ack_transaction_outcome:
            _dict['implementationAckTransactionOutcome'] = self.implementation_ack_transaction_outcome.to_dict()
        # override the default output from pydantic by calling `to_dict()` of technical_ack_outcome
        if self.technical_ack_outcome:
            _dict['technicalAckOutcome'] = self.technical_ack_outcome.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if reply_to_message_id (nullable) is None
        # and model_fields_set contains the field
        if self.reply_to_message_id is None and "reply_to_message_id" in self.model_fields_set:
            _dict['replyToMessageId'] = None

        # set to None if reply_to_transaction_key (nullable) is None
        # and model_fields_set contains the field
        if self.reply_to_transaction_key is None and "reply_to_transaction_key" in self.model_fields_set:
            _dict['replyToTransactionKey'] = None

        # set to None if partner_id (nullable) is None
        # and model_fields_set contains the field
        if self.partner_id is None and "partner_id" in self.model_fields_set:
            _dict['partnerId'] = None

        # set to None if business_key (nullable) is None
        # and model_fields_set contains the field
        if self.business_key is None and "business_key" in self.model_fields_set:
            _dict['businessKey'] = None

        # set to None if functional_ack_outcome (nullable) is None
        # and model_fields_set contains the field
        if self.functional_ack_outcome is None and "functional_ack_outcome" in self.model_fields_set:
            _dict['functionalAckOutcome'] = None

        # set to None if functional_ack_transaction_outcome (nullable) is None
        # and model_fields_set contains the field
        if self.functional_ack_transaction_outcome is None and "functional_ack_transaction_outcome" in self.model_fields_set:
            _dict['functionalAckTransactionOutcome'] = None

        # set to None if functional_ack_group_outcome (nullable) is None
        # and model_fields_set contains the field
        if self.functional_ack_group_outcome is None and "functional_ack_group_outcome" in self.model_fields_set:
            _dict['functionalAckGroupOutcome'] = None

        # set to None if functional_ack_evaluation_scope (nullable) is None
        # and model_fields_set contains the field
        if self.functional_ack_evaluation_scope is None and "functional_ack_evaluation_scope" in self.model_fields_set:
            _dict['functionalAckEvaluationScope'] = None

        # set to None if implementation_ack_outcome (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_ack_outcome is None and "implementation_ack_outcome" in self.model_fields_set:
            _dict['implementationAckOutcome'] = None

        # set to None if implementation_ack_transaction_outcome (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_ack_transaction_outcome is None and "implementation_ack_transaction_outcome" in self.model_fields_set:
            _dict['implementationAckTransactionOutcome'] = None

        # set to None if implementation_ack_evaluation_scope (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_ack_evaluation_scope is None and "implementation_ack_evaluation_scope" in self.model_fields_set:
            _dict['implementationAckEvaluationScope'] = None

        # set to None if x12_acknowledgment_expected_by (nullable) is None
        # and model_fields_set contains the field
        if self.x12_acknowledgment_expected_by is None and "x12_acknowledgment_expected_by" in self.model_fields_set:
            _dict['x12AcknowledgmentExpectedBy'] = None

        # set to None if technical_ack_expected_by (nullable) is None
        # and model_fields_set contains the field
        if self.technical_ack_expected_by is None and "technical_ack_expected_by" in self.model_fields_set:
            _dict['technicalAckExpectedBy'] = None

        # set to None if technical_ack_outcome (nullable) is None
        # and model_fields_set contains the field
        if self.technical_ack_outcome is None and "technical_ack_outcome" in self.model_fields_set:
            _dict['technicalAckOutcome'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionTimelineSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "environment": obj.get("environment"),
            "messageId": obj.get("messageId"),
            "transactionKey": obj.get("transactionKey"),
            "replyToMessageId": obj.get("replyToMessageId"),
            "replyToTransactionKey": obj.get("replyToTransactionKey"),
            "direction": obj.get("direction"),
            "partnerName": obj.get("partnerName"),
            "partnerId": obj.get("partnerId"),
            "timestamp": obj.get("timestamp"),
            "transactionSet": TransactionSet.from_dict(obj["transactionSet"]) if obj.get("transactionSet") is not None else None,
            "controlNumbers": TransactionControlNumbers.from_dict(obj["controlNumbers"]) if obj.get("controlNumbers") is not None else None,
            "edi": TransactionEdiMetadata.from_dict(obj["edi"]) if obj.get("edi") is not None else None,
            "businessKey": TransactionBusinessKey.from_dict(obj["businessKey"]) if obj.get("businessKey") is not None else None,
            "functionalAckOutcome": FunctionalAcknowledgmentSummary.from_dict(obj["functionalAckOutcome"]) if obj.get("functionalAckOutcome") is not None else None,
            "functionalAckTransactionOutcome": FunctionalAcknowledgmentTransactionSetOutcome.from_dict(obj["functionalAckTransactionOutcome"]) if obj.get("functionalAckTransactionOutcome") is not None else None,
            "functionalAckGroupOutcome": FunctionalAcknowledgmentGroupSummary.from_dict(obj["functionalAckGroupOutcome"]) if obj.get("functionalAckGroupOutcome") is not None else None,
            "functionalAckEvaluationScope": obj.get("functionalAckEvaluationScope"),
            "implementationAckOutcome": ImplementationAcknowledgmentSummary.from_dict(obj["implementationAckOutcome"]) if obj.get("implementationAckOutcome") is not None else None,
            "implementationAckTransactionOutcome": ImplementationAcknowledgmentTransactionSetOutcome.from_dict(obj["implementationAckTransactionOutcome"]) if obj.get("implementationAckTransactionOutcome") is not None else None,
            "implementationAckEvaluationScope": obj.get("implementationAckEvaluationScope"),
            "x12AcknowledgmentExpectedBy": obj.get("x12AcknowledgmentExpectedBy"),
            "technicalAckRequested": obj.get("technicalAckRequested"),
            "technicalAckStatus": obj.get("technicalAckStatus"),
            "technicalAckExpectedBy": obj.get("technicalAckExpectedBy"),
            "technicalAckOutcome": TechnicalAcknowledgmentOutcome.from_dict(obj["technicalAckOutcome"]) if obj.get("technicalAckOutcome") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
