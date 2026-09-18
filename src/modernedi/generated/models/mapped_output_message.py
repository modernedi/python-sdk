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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.mapped_output_mapping import MappedOutputMapping
from modernedi.generated.models.mapping_purpose import MappingPurpose
from modernedi.generated.models.transaction_business_key import TransactionBusinessKey
from modernedi.generated.models.transaction_control_numbers import TransactionControlNumbers
from modernedi.generated.models.transaction_edi_metadata import TransactionEdiMetadata
from modernedi.generated.models.transaction_environment_value import TransactionEnvironmentValue
from modernedi.generated.models.transaction_set import TransactionSet
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappedOutputMessage(BaseModel):
    """
    One mapped application document leased from ModernEDI's managed output queue.
    """ # noqa: E501
    id: StrictStr = Field(description="Stable id for this generated output version, used when marking the message received. A later durable regeneration can produce a new id for the same `messageId` and `mappedOutputKey`. ")
    receipt_handle: StrictStr = Field(description="Token from the latest poll response, required when marking the message received.", alias="receiptHandle")
    delivery_count: StrictInt = Field(description="Number of pull or webhook delivery leases issued for this generated output version.", alias="deliveryCount")
    leased_until: Optional[str] = Field(default=None, description="UTC instant when ModernEDI may return this message again if it has not been marked received.", alias="leasedUntil")
    message_id: StrictStr = Field(description="Original inbound AS2 message id. Use this value as `originalMessageId` when sending a reply with `/v1/as2/reply`. ", alias="messageId")
    transaction_key: StrictStr = Field(description="Transaction identifier within the AS2 message, usually `GS06#ST02`.", alias="transactionKey")
    partner_name: Optional[StrictStr] = Field(default=None, description="Partner name. Omitted when `deliveredMetadata.partner` is `false`.", alias="partnerName")
    environment: TransactionEnvironmentValue
    partner_id: Optional[StrictInt] = Field(default=None, description="Persisted tenant-scoped partner id. Omitted when `deliveredMetadata.partner` is `false`.", alias="partnerId")
    transaction_timestamp: Optional[str] = Field(default=None, description="Source transaction timestamp. Omitted when `deliveredMetadata.transactionTimestamp` is `false`.", alias="transactionTimestamp", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    transaction_set: Optional[TransactionSet] = Field(default=None, description="Transaction-set code and description. Omitted when `deliveredMetadata.transactionSet` is `false`.", alias="transactionSet")
    control_numbers: Optional[TransactionControlNumbers] = Field(default=None, description="X12 transaction and functional-group control numbers. Individual properties are omitted according to `deliveredMetadata.transactionControlNumber` and `deliveredMetadata.functionalGroupControlNumber`; the object is omitted when both are `false`. ", alias="controlNumbers")
    edi: Optional[TransactionEdiMetadata] = Field(default=None, description="Optional X12 context controlled by `deliveredMetadata.transactionSet`, `x12Version`, `functionalIdentifierCode`, and `segmentTerminator`. The object is omitted when all four are `false`. ")
    mapping: Optional[MappedOutputMapping] = None
    mapped_output_key: StrictStr = Field(description="Unique mapped-output key inside the transaction.", alias="mappedOutputKey")
    sequence_number: StrictInt = Field(description="Zero-based output order when one source transaction produces multiple mapped documents.", alias="sequenceNumber")
    purpose: MappingPurpose
    content_type: Optional[StrictStr] = Field(default=None, description="Media type for `payload`, such as `application/json` or `application/xml`.", alias="contentType", json_schema_extra={"examples": ["application/json"]})
    created_at: Optional[str] = Field(default=None, description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="createdAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    business_key: Optional[TransactionBusinessKey] = Field(default=None, description="Map-derived business identifier for customer reconciliation, or `null` when the map did not produce one.", alias="businessKey")
    extra_fields: Optional[Dict[str, StrictStr]] = Field(default=None, description="Runtime routing metadata recorded with the generated output, such as `{\"destination\":\"managedQueue\"}`. This is not the customer-selectable context; use the mapping's `deliveredMetadata` flags for that. ", alias="extraFields")
    payload: Optional[StrictStr] = Field(default=None, description="Mapped document body. Parse according to `contentType`.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "receiptHandle", "deliveryCount", "leasedUntil", "messageId", "transactionKey", "partnerName", "environment", "partnerId", "transactionTimestamp", "transactionSet", "controlNumbers", "edi", "mapping", "mappedOutputKey", "sequenceNumber", "purpose", "contentType", "createdAt", "businessKey", "extraFields", "payload"]

    @field_validator('transaction_timestamp', mode="before")
    def transaction_timestamp_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('created_at', mode="before")
    def created_at_validate_regular_expression(cls, value):
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
        """Create an instance of MappedOutputMessage from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of mapping
        if self.mapping:
            _dict['mapping'] = self.mapping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_key
        if self.business_key:
            _dict['businessKey'] = self.business_key.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if leased_until (nullable) is None
        # and model_fields_set contains the field
        if self.leased_until is None and "leased_until" in self.model_fields_set:
            _dict['leasedUntil'] = None

        # set to None if content_type (nullable) is None
        # and model_fields_set contains the field
        if self.content_type is None and "content_type" in self.model_fields_set:
            _dict['contentType'] = None

        # set to None if created_at (nullable) is None
        # and model_fields_set contains the field
        if self.created_at is None and "created_at" in self.model_fields_set:
            _dict['createdAt'] = None

        # set to None if business_key (nullable) is None
        # and model_fields_set contains the field
        if self.business_key is None and "business_key" in self.model_fields_set:
            _dict['businessKey'] = None

        # set to None if payload (nullable) is None
        # and model_fields_set contains the field
        if self.payload is None and "payload" in self.model_fields_set:
            _dict['payload'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappedOutputMessage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "receiptHandle": obj.get("receiptHandle"),
            "deliveryCount": obj.get("deliveryCount"),
            "leasedUntil": obj.get("leasedUntil"),
            "messageId": obj.get("messageId"),
            "transactionKey": obj.get("transactionKey"),
            "partnerName": obj.get("partnerName"),
            "environment": obj.get("environment"),
            "partnerId": obj.get("partnerId"),
            "transactionTimestamp": obj.get("transactionTimestamp"),
            "transactionSet": TransactionSet.from_dict(obj["transactionSet"]) if obj.get("transactionSet") is not None else None,
            "controlNumbers": TransactionControlNumbers.from_dict(obj["controlNumbers"]) if obj.get("controlNumbers") is not None else None,
            "edi": TransactionEdiMetadata.from_dict(obj["edi"]) if obj.get("edi") is not None else None,
            "mapping": MappedOutputMapping.from_dict(obj["mapping"]) if obj.get("mapping") is not None else None,
            "mappedOutputKey": obj.get("mappedOutputKey"),
            "sequenceNumber": obj.get("sequenceNumber"),
            "purpose": obj.get("purpose"),
            "contentType": obj.get("contentType"),
            "createdAt": obj.get("createdAt"),
            "businessKey": TransactionBusinessKey.from_dict(obj["businessKey"]) if obj.get("businessKey") is not None else None,
            "extraFields": obj.get("extraFields"),
            "payload": obj.get("payload")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
