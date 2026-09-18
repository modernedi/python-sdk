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
from typing_extensions import Annotated
from modernedi.generated.models.functional_acknowledgment_group_summary import FunctionalAcknowledgmentGroupSummary
from modernedi.generated.models.functional_acknowledgment_summary import FunctionalAcknowledgmentSummary
from modernedi.generated.models.functional_acknowledgment_transaction_set_outcome import FunctionalAcknowledgmentTransactionSetOutcome
from modernedi.generated.models.implementation_acknowledgment_evaluation_scope import ImplementationAcknowledgmentEvaluationScope
from modernedi.generated.models.implementation_acknowledgment_status import ImplementationAcknowledgmentStatus
from modernedi.generated.models.implementation_acknowledgment_summary import ImplementationAcknowledgmentSummary
from modernedi.generated.models.implementation_acknowledgment_transaction_set_outcome import ImplementationAcknowledgmentTransactionSetOutcome
from modernedi.generated.models.technical_acknowledgment_outcome import TechnicalAcknowledgmentOutcome
from modernedi.generated.models.technical_acknowledgment_status import TechnicalAcknowledgmentStatus
from modernedi.generated.models.transaction_attention_reason import TransactionAttentionReason
from modernedi.generated.models.transaction_business_key import TransactionBusinessKey
from modernedi.generated.models.transaction_control_numbers import TransactionControlNumbers
from modernedi.generated.models.transaction_edi_metadata import TransactionEdiMetadata
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from modernedi.generated.models.transaction_mapping_status_summary import TransactionMappingStatusSummary
from modernedi.generated.models.transaction_set import TransactionSet
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionSummary(BaseModel):
    """
    Stable list-level transaction identity, partner context, acknowledgment state, and operator-attention projection.
    """ # noqa: E501
    id: StrictStr = Field(description="Convenience id formatted as `<messageId>/<transactionKey>`.", json_schema_extra={"examples": ["msg-850-api/17#0001"]})
    environment: TransactionEnvironmentValue
    needs_attention: StrictBool = Field(description="Stable operator-inbox signal. True when an unexpired watchlist entry is active, a mapping failure remains unresolved, or the 997 outcome selected by `functionalAckEvaluationScope` or the 999 outcome selected by `implementationAckEvaluationScope` is present and is not `accepted`, or neither a 997 nor a 999 was received for an eligible outbound transaction by `x12AcknowledgmentExpectedBy`, or a requested TA1 rejected the interchange, reported errors, could not be classified, or was not received by `technicalAckExpectedBy`, or when a managed output remained uncollected beyond its 15-minute pickup grace period, or when a delivered output was not acknowledged before its lease expired or was redelivered. A newly ready output inside the grace period and an active first lease are normal handoff progress and do not set this signal by themselves. ", alias="needsAttention")
    attention_reasons: List[TransactionAttentionReason] = Field(description="Active machine-readable reasons behind `needsAttention`.", alias="attentionReasons")
    on_watchlist: StrictBool = Field(description="True while an active watchlist entry exists for this transaction. Entries created through the Integration API remain active until `DELETE /v1/integration/transactions/{messageId}/{transactionKey}/watch` removes them. An active watch is also represented by the `watchlist` attention reason. ", alias="onWatchlist")
    mapping_status: TransactionMappingStatusSummary = Field(alias="mappingStatus")
    functional_ack_status: Optional[StrictStr] = Field(description="Compact 997 status selected for this transaction. ModernEDI uses a uniquely matched AK2/AK5 outcome when possible, otherwise the uniquely matched AK1/AK9 functional-group outcome, and only then the conservative whole-997 aggregate. Null means no attributable 997 status is currently available. Use `x12_ack_overdue` for an actionable missing X12 acknowledgment. ", alias="functionalAckStatus")
    implementation_ack_status: Optional[ImplementationAcknowledgmentStatus] = Field(description="Compact 999 status selected for this transaction. ModernEDI uses a uniquely matched AK2/IK5 result when possible. Group fallback conservatively reduces the matching AK9 status with every nested IK5 status, and whole-999 fallback reduces the aggregate with every flattened IK5 status. A non-accepted primary fallback remains authoritative. An accepted primary with any nested `unknown` becomes `unknown`; an accepted primary with any definitive non-clean nested result becomes `accepted_with_errors`, not the sibling's rejection or partial disposition. This prevents a raw accepted fallback from hiding a non-clean result or falsely assigning a sibling's disposition to this row, without changing the raw AK9 or IK5 fields. Null means no attributable 999 status is currently available. ", alias="implementationAckStatus")
    mdn_status: Optional[StrictStr] = Field(description="Compact normalized AS2 receipt-assurance status. Null means no MDN status applies or the asynchronous status projection has not indexed this row yet. Check `attentionSummary.freshness` on list responses before interpreting a null during projection bootstrap. ", alias="mdnStatus")
    message_id: StrictStr = Field(description="AS2 Message-Id for this transaction.", alias="messageId", json_schema_extra={"examples": ["msg-850-api"]})
    transaction_key: StrictStr = Field(description="Transaction identifier within the AS2 message, usually `GS06#ST02`.", alias="transactionKey", json_schema_extra={"examples": ["17#0001"]})
    reply_to_message_id: Optional[StrictStr] = Field(description="Present on outbound replies and points back to the inbound AS2 message id.", alias="replyToMessageId")
    reply_to_transaction_key: Optional[StrictStr] = Field(description="Exact inbound transaction key for an outbound reply, or `null` for a transaction that is not a reply. Related-transaction queries attach the reply only to this transaction inside `replyToMessageId`. ", alias="replyToTransactionKey")
    direction: StrictStr = Field(description="Direction across the ModernEDI boundary: inbound from the partner or outbound to the partner.", json_schema_extra={"examples": ["inbound"]})
    partner_name: StrictStr = Field(description="Partner name captured for display; use `partnerId` for stable automation across renames.", alias="partnerName", json_schema_extra={"examples": ["Customer One"]})
    partner_id: Optional[StrictInt] = Field(description="Persisted tenant-scoped partner id that authorizes this transaction and remains stable across partner renames.", alias="partnerId", json_schema_extra={"examples": [1]})
    partner_configuration_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(description="Lowercase SHA-256 of the exact partner runtime configuration recorded for this transaction, receipt, or acknowledgment. It is `null` for legacy rows written before configuration stamping. Scenario verification accepts persisted evidence only when this value exactly matches the partner configuration frozen into the applied binding. ", alias="partnerConfigurationSha256", json_schema_extra={"examples": ["0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"]})
    timestamp: str = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`.", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    transaction_set: TransactionSet = Field(alias="transactionSet")
    control_numbers: TransactionControlNumbers = Field(alias="controlNumbers")
    edi: TransactionEdiMetadata
    business_key: Optional[TransactionBusinessKey] = Field(description="Business key recorded on this transaction. Inbound keys come from the incoming map. Outbound keys are present when `/send`, `/reply`, or `/carbonCopy` supplied `businessKey` in the JSON request envelope; otherwise this is `null`. ", alias="businessKey")
    functional_ack_outcome: Optional[FunctionalAcknowledgmentSummary] = Field(description="Compact normalized whole-997 aggregate. Distinct AK1/AK9 groups are intentionally omitted from list responses; use `functionalAckGroupOutcome` for this row's selected compact group and transaction detail or the `functional-ack-x12` document metadata for every full group. A null value means no compact outcome was available, normally because no 997 is stored; list enrichment is fail-soft, so callers should use transaction detail before treating null as proof that no acknowledgment exists. Do not use the aggregate status as this row's status; use `functionalAckStatus` and `functionalAckEvaluationScope`. ", alias="functionalAckOutcome")
    functional_ack_transaction_outcome: Optional[FunctionalAcknowledgmentTransactionSetOutcome] = Field(description="Exact AK2/AK5 result matched to this row by GS06/AK102 and ST02/AK202, with a leading-zero-insensitive control-number fallback only when it yields one unique match. Null means no unique transaction-set result could be attributed. ", alias="functionalAckTransactionOutcome")
    functional_ack_group_outcome: Optional[FunctionalAcknowledgmentGroupSummary] = Field(description="Exact AK1/AK9 group matched to this row by GS06/AK102 and GS01/AK101. Exact control-number identity is preferred; a leading-zero-insensitive fallback is used only when it yields one unique group. Null means no group was uniquely attributable. This row-level projection omits the group's nested AK2 results to keep list, reply, and event payloads bounded; fetch transaction detail for the complete group tree. ", alias="functionalAckGroupOutcome")
    functional_ack_evaluation_scope: Optional[StrictStr] = Field(description="Outcome level ModernEDI used for `functional_ack_issue`. `transaction_set` uses a unique AK2/AK5 disposition while retaining the matching AK9 group separately. `functional_group` is used when AK2 is omitted or no unique transaction result exists. `functional_acknowledgment` is the conservative whole-997 fallback only when no AK1 group can be matched uniquely. Null means no 997 outcome was available. ", alias="functionalAckEvaluationScope")
    implementation_ack_outcome: Optional[ImplementationAcknowledgmentSummary] = Field(description="Compact normalized whole-999 result plus distinct AK1/AK9 group outcomes. A null value normally means no 999 is stored. This remains the acknowledgment-wide context even when ModernEDI can evaluate this row against a narrower group or transaction result. ", alias="implementationAckOutcome")
    implementation_ack_transaction_outcome: Optional[ImplementationAcknowledgmentTransactionSetOutcome] = Field(description="Exact AK2/IK5 result matched uniquely to this row by the functional-group and transaction-set identifiers. Null means no unique transaction-set result could be attributed. ", alias="implementationAckTransactionOutcome")
    implementation_ack_evaluation_scope: Optional[ImplementationAcknowledgmentEvaluationScope] = Field(description="Outcome level ModernEDI used for `implementation_ack_issue`. `transaction_set` selects a unique AK2/IK5 result; `implementation_group` selects a unique AK1/AK9 group and conservatively reduces it with nested IK5 statuses; `implementation_acknowledgment` conservatively reduces the aggregate with all flattened IK5 statuses when no unique group is attributable. Null means no 999 outcome was available. ", alias="implementationAckEvaluationScope")
    x12_acknowledgment_expected_by: Optional[str] = Field(description="Deadline used to classify a still-missing partner X12 acknowledgment for an eligible outbound business transaction. Outbound 997 and 999 acknowledgment documents are excluded. Receipt of either a correlated 997 or 999 satisfies the deadline. This is null when no deadline applies. Use the `x12_ack_overdue` attention reason, not this timestamp alone, as the authoritative active overdue signal. ModernEDI does not automatically resend the original X12 when the deadline passes. ", alias="x12AcknowledgmentExpectedBy")
    technical_ack_requested: StrictBool = Field(description="True when the outbound ISA14 requested a TA1 interchange acknowledgment. False for inbound traffic, outbound interchanges that did not request TA1, and legacy rows that predate this persisted signal.", alias="technicalAckRequested")
    technical_ack_status: TechnicalAcknowledgmentStatus = Field(alias="technicalAckStatus")
    technical_ack_expected_by: Optional[str] = Field(description="Deadline for a TA1 explicitly requested by outbound ISA14, or `null` when none was requested. Use `technical_ack_overdue` as the authoritative active overdue signal. ModernEDI does not automatically resend when this deadline passes.", alias="technicalAckExpectedBy")
    technical_ack_outcome: Optional[TechnicalAcknowledgmentOutcome] = Field(description="Parsed TA1 outcome correlated by the original AS2 message id, or `null` while a requested TA1 is still pending or when none was requested.", alias="technicalAckOutcome")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "environment", "needsAttention", "attentionReasons", "onWatchlist", "mappingStatus", "functionalAckStatus", "implementationAckStatus", "mdnStatus", "messageId", "transactionKey", "replyToMessageId", "replyToTransactionKey", "direction", "partnerName", "partnerId", "partnerConfigurationSha256", "timestamp", "transactionSet", "controlNumbers", "edi", "businessKey", "functionalAckOutcome", "functionalAckTransactionOutcome", "functionalAckGroupOutcome", "functionalAckEvaluationScope", "implementationAckOutcome", "implementationAckTransactionOutcome", "implementationAckEvaluationScope", "x12AcknowledgmentExpectedBy", "technicalAckRequested", "technicalAckStatus", "technicalAckExpectedBy", "technicalAckOutcome"]

    @field_validator('functional_ack_status')
    def functional_ack_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['accepted', 'accepted_with_errors', 'partially_accepted', 'rejected', 'unknown']):
            raise ValueError("must be one of enum values ('accepted', 'accepted_with_errors', 'partially_accepted', 'rejected', 'unknown')")
        return value

    @field_validator('mdn_status')
    def mdn_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['pending', 'processed', 'warning', 'rejected', 'invalid', 'mic_mismatch', 'overdue']):
            raise ValueError("must be one of enum values ('pending', 'processed', 'warning', 'rejected', 'invalid', 'mic_mismatch', 'overdue')")
        return value

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['inbound', 'outbound']):
            raise ValueError("must be one of enum values ('inbound', 'outbound')")
        return value

    @field_validator('partner_configuration_sha256', mode="before")
    def partner_configuration_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
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
        """Create an instance of TransactionSummary from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of mapping_status
        if self.mapping_status:
            _dict['mappingStatus'] = self.mapping_status.to_dict()
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

        # set to None if functional_ack_status (nullable) is None
        # and model_fields_set contains the field
        if self.functional_ack_status is None and "functional_ack_status" in self.model_fields_set:
            _dict['functionalAckStatus'] = None

        # set to None if implementation_ack_status (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_ack_status is None and "implementation_ack_status" in self.model_fields_set:
            _dict['implementationAckStatus'] = None

        # set to None if mdn_status (nullable) is None
        # and model_fields_set contains the field
        if self.mdn_status is None and "mdn_status" in self.model_fields_set:
            _dict['mdnStatus'] = None

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

        # set to None if partner_configuration_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.partner_configuration_sha256 is None and "partner_configuration_sha256" in self.model_fields_set:
            _dict['partnerConfigurationSha256'] = None

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
        """Create an instance of TransactionSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "environment": obj.get("environment"),
            "needsAttention": obj.get("needsAttention"),
            "attentionReasons": obj.get("attentionReasons"),
            "onWatchlist": obj.get("onWatchlist"),
            "mappingStatus": TransactionMappingStatusSummary.from_dict(obj["mappingStatus"]) if obj.get("mappingStatus") is not None else None,
            "functionalAckStatus": obj.get("functionalAckStatus"),
            "implementationAckStatus": obj.get("implementationAckStatus"),
            "mdnStatus": obj.get("mdnStatus"),
            "messageId": obj.get("messageId"),
            "transactionKey": obj.get("transactionKey"),
            "replyToMessageId": obj.get("replyToMessageId"),
            "replyToTransactionKey": obj.get("replyToTransactionKey"),
            "direction": obj.get("direction"),
            "partnerName": obj.get("partnerName"),
            "partnerId": obj.get("partnerId"),
            "partnerConfigurationSha256": obj.get("partnerConfigurationSha256"),
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
