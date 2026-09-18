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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class TransactionMappedOutputDelivery(BaseModel):
    """
    Handoff state for a mapped output stored on a transaction. This object is present on stored transaction-detail mapped outputs and omitted from response-only replay results, which do not enter the managed queue. `acknowledged` means acknowledged by your integration through the queue acknowledgment API or a successful mapped-output webhook; it does not prove how another application handled the document afterward.
    """ # noqa: E501
    applicability: StrictStr = Field(description="`managed_queue` exposes a current polling/webhook state; `not_applicable` is a transaction-record-only artifact. ")
    status: Optional[StrictStr] = Field(description="Current managed-queue state, or null when applicability is not `managed_queue`. `ready` includes a never-leased output and an output whose prior lease expired. `leased` means the visibility timeout is still active. `acknowledged` means acknowledged by your integration. ")
    available_at: Optional[str] = Field(description="UTC instant when this generated output version became available for polling or webhook delivery. A durable replay creates a new output version with a new availability instant. ", alias="availableAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    handoff_issue: Optional[StrictStr] = Field(description="Current actionable managed-output handoff issue, or null while the output is progressing normally, acknowledged, or not managed by the queue. `not_collected` means no first delivery lease was issued before the 15-minute pickup grace period expired. `acknowledgment_overdue` means the first lease expired without acknowledgment. `redelivered` means more than one delivery lease was issued without a later acknowledgment. ", alias="handoffIssue")
    attention_since: Optional[str] = Field(description="UTC instant when the current `handoffIssue` became actionable, or null when no handoff issue is active. For `not_collected`, this is 15 minutes after `availableAt`; for an overdue acknowledgment it is the first lease expiry; for a redelivery it is the most recent transition into the redelivered state. ", alias="attentionSince", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    output_id: Optional[StrictStr] = Field(description="Managed-queue correlation id for this generated output, or null when queue tracking does not apply. It is distinct from the mapped output's top-level transaction artifact `id`. It stays stable across ordinary processing retries that reproduce the same logical output. A successful durable replay creates a new id even when the regenerated content is identical. Acknowledgment still requires the latest `receiptHandle` returned by `GET /v1/mapped-outputs`; transaction detail does not provide that receipt handle. ", alias="outputId")
    delivery_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="Number of times the output has been leased for pull or webhook delivery attempts, or null when queue tracking does not apply. This count does not imply successful downstream processing. ", alias="deliveryCount")
    redelivered: Optional[StrictBool] = Field(description="True after more than one lease or delivery attempt; independent of the current status.")
    first_delivered_at: Optional[str] = Field(description="UTC instant when the output was first leased for a pull or webhook delivery attempt.", alias="firstDeliveredAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    last_delivered_at: Optional[str] = Field(description="UTC instant when the output was most recently leased for a pull or webhook delivery attempt.", alias="lastDeliveredAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    leased_until: Optional[str] = Field(description="UTC instant when the current visibility lease expires, or null when no lease has been issued.", alias="leasedUntil", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    acked_at: Optional[str] = Field(description="UTC instant when ModernEDI recorded acknowledgment by the customer's integration or a successful webhook response. This does not prove later ERP or business processing. ", alias="ackedAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["applicability", "status", "availableAt", "handoffIssue", "attentionSince", "outputId", "deliveryCount", "redelivered", "firstDeliveredAt", "lastDeliveredAt", "leasedUntil", "ackedAt"]

    @field_validator('applicability')
    def applicability_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['managed_queue', 'not_applicable']):
            raise ValueError("must be one of enum values ('managed_queue', 'not_applicable')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ready', 'leased', 'acknowledged']):
            raise ValueError("must be one of enum values ('ready', 'leased', 'acknowledged')")
        return value

    @field_validator('available_at', mode="before")
    def available_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('handoff_issue')
    def handoff_issue_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['not_collected', 'acknowledgment_overdue', 'redelivered']):
            raise ValueError("must be one of enum values ('not_collected', 'acknowledgment_overdue', 'redelivered')")
        return value

    @field_validator('attention_since', mode="before")
    def attention_since_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('first_delivered_at', mode="before")
    def first_delivered_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('last_delivered_at', mode="before")
    def last_delivered_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('leased_until', mode="before")
    def leased_until_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
        return value

    @field_validator('acked_at', mode="before")
    def acked_at_validate_regular_expression(cls, value):
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
        """Create an instance of TransactionMappedOutputDelivery from a JSON string"""
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

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if available_at (nullable) is None
        # and model_fields_set contains the field
        if self.available_at is None and "available_at" in self.model_fields_set:
            _dict['availableAt'] = None

        # set to None if handoff_issue (nullable) is None
        # and model_fields_set contains the field
        if self.handoff_issue is None and "handoff_issue" in self.model_fields_set:
            _dict['handoffIssue'] = None

        # set to None if attention_since (nullable) is None
        # and model_fields_set contains the field
        if self.attention_since is None and "attention_since" in self.model_fields_set:
            _dict['attentionSince'] = None

        # set to None if output_id (nullable) is None
        # and model_fields_set contains the field
        if self.output_id is None and "output_id" in self.model_fields_set:
            _dict['outputId'] = None

        # set to None if delivery_count (nullable) is None
        # and model_fields_set contains the field
        if self.delivery_count is None and "delivery_count" in self.model_fields_set:
            _dict['deliveryCount'] = None

        # set to None if redelivered (nullable) is None
        # and model_fields_set contains the field
        if self.redelivered is None and "redelivered" in self.model_fields_set:
            _dict['redelivered'] = None

        # set to None if first_delivered_at (nullable) is None
        # and model_fields_set contains the field
        if self.first_delivered_at is None and "first_delivered_at" in self.model_fields_set:
            _dict['firstDeliveredAt'] = None

        # set to None if last_delivered_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_delivered_at is None and "last_delivered_at" in self.model_fields_set:
            _dict['lastDeliveredAt'] = None

        # set to None if leased_until (nullable) is None
        # and model_fields_set contains the field
        if self.leased_until is None and "leased_until" in self.model_fields_set:
            _dict['leasedUntil'] = None

        # set to None if acked_at (nullable) is None
        # and model_fields_set contains the field
        if self.acked_at is None and "acked_at" in self.model_fields_set:
            _dict['ackedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionMappedOutputDelivery from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "applicability": obj.get("applicability"),
            "status": obj.get("status"),
            "availableAt": obj.get("availableAt"),
            "handoffIssue": obj.get("handoffIssue"),
            "attentionSince": obj.get("attentionSince"),
            "outputId": obj.get("outputId"),
            "deliveryCount": obj.get("deliveryCount"),
            "redelivered": obj.get("redelivered"),
            "firstDeliveredAt": obj.get("firstDeliveredAt"),
            "lastDeliveredAt": obj.get("lastDeliveredAt"),
            "leasedUntil": obj.get("leasedUntil"),
            "ackedAt": obj.get("ackedAt")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
