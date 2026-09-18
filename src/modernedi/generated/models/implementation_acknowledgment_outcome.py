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
from typing_extensions import Annotated
from modernedi.generated.models.implementation_acknowledgment_group_outcome import ImplementationAcknowledgmentGroupOutcome
from modernedi.generated.models.implementation_acknowledgment_status import ImplementationAcknowledgmentStatus
from modernedi.generated.models.implementation_acknowledgment_transaction_set_outcome import ImplementationAcknowledgmentTransactionSetOutcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ImplementationAcknowledgmentOutcome(BaseModel):
    """
    Normalized X12 999 result. The aggregate status does not collapse the distinct AK1/AK9 group results or AK2/IK5 transaction-set results. `groups` preserves each AK101/AK102/AK103 identity and its AK9 rollup; `transactionSets` provides the same IK5 results as one attributable flat list. A 999 reports X12 syntax and relational validation. It does not indicate semantic or business acceptance, and it is not HIPAA implementation-guide certification. Only `accepted` is a clean automation completion.
    """ # noqa: E501
    status: ImplementationAcknowledgmentStatus
    acknowledgment_code: Optional[StrictStr] = Field(description="Aggregate acknowledgment code when one value represents the whole 999, or `null` for mixed or unavailable group results.", alias="acknowledgmentCode", json_schema_extra={"examples": ["A"]})
    summary: StrictStr = Field(description="Human-readable aggregate result suitable for a transaction timeline or status panel.", json_schema_extra={"examples": ["Implementation acknowledgment accepted; 1 of 1 received transaction set was accepted."]})
    parsed: StrictBool = Field(description="True when the 999 structure and required AK9 rollups were parsed successfully.")
    unknown_reason: Optional[StrictStr] = Field(description="Machine-readable reason when `status` is `unknown`.", alias="unknownReason")
    included_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="Aggregate count of transaction sets included across the acknowledged groups, when available.", alias="includedTransactionSets")
    received_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="Aggregate count of transaction sets received across the acknowledged groups, when available.", alias="receivedTransactionSets")
    accepted_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="Aggregate count of received transaction sets accepted across the acknowledged groups, when available.", alias="acceptedTransactionSets")
    error_codes: List[StrictStr] = Field(description="Distinct non-empty syntax error codes reported by the 999.", alias="errorCodes")
    groups: List[ImplementationAcknowledgmentGroupOutcome] = Field(description="Distinct AK1/AK9 implementation-group outcomes in source order.")
    transaction_sets: List[ImplementationAcknowledgmentTransactionSetOutcome] = Field(description="Flattened AK2/IK5 transaction-set outcomes; each result repeats its parent AK101/AK102 identity for attribution.", alias="transactionSets")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["status", "acknowledgmentCode", "summary", "parsed", "unknownReason", "includedTransactionSets", "receivedTransactionSets", "acceptedTransactionSets", "errorCodes", "groups", "transactionSets"]

    @field_validator('unknown_reason')
    def unknown_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['missing_x12', 'not_999', 'invalid_structure', 'missing_ak9', 'invalid_ak9', 'unsupported_acknowledgment_code', 'inconsistent_rollup']):
            raise ValueError("must be one of enum values ('missing_x12', 'not_999', 'invalid_structure', 'missing_ak9', 'invalid_ak9', 'unsupported_acknowledgment_code', 'inconsistent_rollup')")
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
        """Create an instance of ImplementationAcknowledgmentOutcome from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in groups (list)
        _items = []
        if self.groups:
            for _item_groups in self.groups:
                if _item_groups:
                    _items.append(_item_groups.to_dict())
            _dict['groups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transaction_sets (list)
        _items = []
        if self.transaction_sets:
            for _item_transaction_sets in self.transaction_sets:
                if _item_transaction_sets:
                    _items.append(_item_transaction_sets.to_dict())
            _dict['transactionSets'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if acknowledgment_code (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledgment_code is None and "acknowledgment_code" in self.model_fields_set:
            _dict['acknowledgmentCode'] = None

        # set to None if unknown_reason (nullable) is None
        # and model_fields_set contains the field
        if self.unknown_reason is None and "unknown_reason" in self.model_fields_set:
            _dict['unknownReason'] = None

        # set to None if included_transaction_sets (nullable) is None
        # and model_fields_set contains the field
        if self.included_transaction_sets is None and "included_transaction_sets" in self.model_fields_set:
            _dict['includedTransactionSets'] = None

        # set to None if received_transaction_sets (nullable) is None
        # and model_fields_set contains the field
        if self.received_transaction_sets is None and "received_transaction_sets" in self.model_fields_set:
            _dict['receivedTransactionSets'] = None

        # set to None if accepted_transaction_sets (nullable) is None
        # and model_fields_set contains the field
        if self.accepted_transaction_sets is None and "accepted_transaction_sets" in self.model_fields_set:
            _dict['acceptedTransactionSets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImplementationAcknowledgmentOutcome from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "status": obj.get("status"),
            "acknowledgmentCode": obj.get("acknowledgmentCode"),
            "summary": obj.get("summary"),
            "parsed": obj.get("parsed"),
            "unknownReason": obj.get("unknownReason"),
            "includedTransactionSets": obj.get("includedTransactionSets"),
            "receivedTransactionSets": obj.get("receivedTransactionSets"),
            "acceptedTransactionSets": obj.get("acceptedTransactionSets"),
            "errorCodes": obj.get("errorCodes"),
            "groups": [ImplementationAcknowledgmentGroupOutcome.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "transactionSets": [ImplementationAcknowledgmentTransactionSetOutcome.from_dict(_item) for _item in obj["transactionSets"]] if obj.get("transactionSets") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
