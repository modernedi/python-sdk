# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.functional_acknowledgment_detail import FunctionalAcknowledgmentDetail
from modernedi.generated.models.implementation_acknowledgment_detail import ImplementationAcknowledgmentDetail
from modernedi.generated.models.stored_transaction_mapped_output import StoredTransactionMappedOutput
from modernedi.generated.models.technical_acknowledgment_detail import TechnicalAcknowledgmentDetail
from modernedi.generated.models.transaction_attention_reason import TransactionAttentionReason
from modernedi.generated.models.transaction_document_metadata import TransactionDocumentMetadata
from modernedi.generated.models.transaction_event import TransactionEvent
from modernedi.generated.models.transaction_mapping_status import TransactionMappingStatus
from modernedi.generated.models.transaction_mdn import TransactionMdn
from modernedi.generated.models.transaction_summary import TransactionSummary
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionDetail(BaseModel):
    """
    Metadata-first operator aggregate spanning mapping provenance, queue custody, normalized acknowledgments, a document index, and compact related-reply summaries.
    """ # noqa: E501
    needs_attention: StrictBool = Field(description="True when the transaction has an active operational watch, an unresolved mapping failure, or a 997 or 999 acknowledgment outcome other than `accepted`, when neither acknowledgment was received for an eligible outbound transaction by `x12AcknowledgmentExpectedBy`, when a requested TA1 rejected the interchange, reported errors, could not be classified, or was not received by `technicalAckExpectedBy`, when a managed output remained uncollected beyond its 15-minute pickup grace period, or when a delivered output was not acknowledged before its lease expired or was redelivered. A newly ready output inside the grace period and an active first lease are normal handoff progress and do not set this signal by themselves. ", alias="needsAttention")
    attention_reasons: List[TransactionAttentionReason] = Field(description="Active machine-readable reasons behind `needsAttention`.", alias="attentionReasons")
    mapping_status: TransactionMappingStatus = Field(alias="mappingStatus")
    summary: TransactionSummary
    mapped_outputs: List[StoredTransactionMappedOutput] = Field(description="Metadata, mapping provenance, and managed-delivery state for inbound mapped outputs. Payload bodies are available through the document endpoints. Outbound reply transactions return an empty array.", alias="mappedOutputs")
    mdn: Optional[TransactionMdn] = Field(description="Normalized AS2 receipt metadata without the report body. Fetch `mdn-report` from the document endpoint to inspect that body.")
    functional_ack: Optional[FunctionalAcknowledgmentDetail] = Field(description="Normalized X12 functional-acknowledgment metadata without the X12 body. Fetch `functional-ack-x12` from the document endpoint to inspect it.", alias="functionalAck")
    implementation_ack: Optional[ImplementationAcknowledgmentDetail] = Field(description="Normalized X12 999 implementation-acknowledgment metadata without the X12 body. Fetch `implementation-ack-x12` from the document endpoint to inspect it.", alias="implementationAck")
    technical_ack: Optional[TechnicalAcknowledgmentDetail] = Field(description="Technical-acknowledgment transport metadata without X12 or HTTP response bodies, or `null` when none was recorded. Fetch the indexed document to inspect a body.", alias="technicalAck")
    documents: List[TransactionDocumentMetadata] = Field(description="Metadata index of retained source, mapped-output, acknowledgment, and HTTP-response documents.")
    events: List[TransactionEvent] = Field(description="Chronological operational timeline derived from persisted transaction artifacts.")
    related_transactions: List[TransactionSummary] = Field(description="Compact summaries of outbound replies linked to this inbound transaction. Fetch a selected reply's detail on demand.", alias="relatedTransactions")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["needsAttention", "attentionReasons", "mappingStatus", "summary", "mappedOutputs", "mdn", "functionalAck", "implementationAck", "technicalAck", "documents", "events", "relatedTransactions"]

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
        """Create an instance of TransactionDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in mapped_outputs (list)
        _items = []
        if self.mapped_outputs:
            for _item_mapped_outputs in self.mapped_outputs:
                if _item_mapped_outputs:
                    _items.append(_item_mapped_outputs.to_dict())
            _dict['mappedOutputs'] = _items
        # override the default output from pydantic by calling `to_dict()` of mdn
        if self.mdn:
            _dict['mdn'] = self.mdn.to_dict()
        # override the default output from pydantic by calling `to_dict()` of functional_ack
        if self.functional_ack:
            _dict['functionalAck'] = self.functional_ack.to_dict()
        # override the default output from pydantic by calling `to_dict()` of implementation_ack
        if self.implementation_ack:
            _dict['implementationAck'] = self.implementation_ack.to_dict()
        # override the default output from pydantic by calling `to_dict()` of technical_ack
        if self.technical_ack:
            _dict['technicalAck'] = self.technical_ack.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in documents (list)
        _items = []
        if self.documents:
            for _item_documents in self.documents:
                if _item_documents:
                    _items.append(_item_documents.to_dict())
            _dict['documents'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item_events in self.events:
                if _item_events:
                    _items.append(_item_events.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in related_transactions (list)
        _items = []
        if self.related_transactions:
            for _item_related_transactions in self.related_transactions:
                if _item_related_transactions:
                    _items.append(_item_related_transactions.to_dict())
            _dict['relatedTransactions'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if mdn (nullable) is None
        # and model_fields_set contains the field
        if self.mdn is None and "mdn" in self.model_fields_set:
            _dict['mdn'] = None

        # set to None if functional_ack (nullable) is None
        # and model_fields_set contains the field
        if self.functional_ack is None and "functional_ack" in self.model_fields_set:
            _dict['functionalAck'] = None

        # set to None if implementation_ack (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_ack is None and "implementation_ack" in self.model_fields_set:
            _dict['implementationAck'] = None

        # set to None if technical_ack (nullable) is None
        # and model_fields_set contains the field
        if self.technical_ack is None and "technical_ack" in self.model_fields_set:
            _dict['technicalAck'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "needsAttention": obj.get("needsAttention"),
            "attentionReasons": obj.get("attentionReasons"),
            "mappingStatus": TransactionMappingStatus.from_dict(obj["mappingStatus"]) if obj.get("mappingStatus") is not None else None,
            "summary": TransactionSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "mappedOutputs": [StoredTransactionMappedOutput.from_dict(_item) for _item in obj["mappedOutputs"]] if obj.get("mappedOutputs") is not None else None,
            "mdn": TransactionMdn.from_dict(obj["mdn"]) if obj.get("mdn") is not None else None,
            "functionalAck": FunctionalAcknowledgmentDetail.from_dict(obj["functionalAck"]) if obj.get("functionalAck") is not None else None,
            "implementationAck": ImplementationAcknowledgmentDetail.from_dict(obj["implementationAck"]) if obj.get("implementationAck") is not None else None,
            "technicalAck": TechnicalAcknowledgmentDetail.from_dict(obj["technicalAck"]) if obj.get("technicalAck") is not None else None,
            "documents": [TransactionDocumentMetadata.from_dict(_item) for _item in obj["documents"]] if obj.get("documents") is not None else None,
            "events": [TransactionEvent.from_dict(_item) for _item in obj["events"]] if obj.get("events") is not None else None,
            "relatedTransactions": [TransactionSummary.from_dict(_item) for _item in obj["relatedTransactions"]] if obj.get("relatedTransactions") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
