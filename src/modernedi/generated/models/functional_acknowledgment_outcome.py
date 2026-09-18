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
from modernedi.generated.models.functional_acknowledgment_group_outcome import FunctionalAcknowledgmentGroupOutcome
from modernedi.generated.models.functional_acknowledgment_status import FunctionalAcknowledgmentStatus
from modernedi.generated.models.functional_acknowledgment_transaction_set_outcome import FunctionalAcknowledgmentTransactionSetOutcome
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class FunctionalAcknowledgmentOutcome(BaseModel):
    """
    Normalized whole-997 aggregate. The aggregate does not collapse the distinct AK1/AK9 group results or AK2/AK5 transaction-set results. `groups` preserves every AK101/AK102 identity, its AK901 disposition, its AK902-AK904 counts, and nested AK5 outcomes. A contradictory AK5/count rollup is reported as unknown rather than trusting an internally inconsistent 997. Whenever `status` is `unknown`, inspect `unknownReason` and fetch the `functional-ack-x12` document when the original body is needed. A false `parsed` value indicates a structural failure; an unsupported AK901, AK501, or syntax-error code can be structurally parsed while its status remains unknown. The `unsupported_acknowledgment_code` reason does not by itself prove that AK901 was unsupported. Only `accepted` is a clean automation completion. `accepted_with_errors` and `unknown` require review; `partially_accepted` and `rejected` are failure or rejection outcomes that require action.
    """ # noqa: E501
    status: FunctionalAcknowledgmentStatus
    acknowledgment_code: Optional[StrictStr] = Field(description="Common original AK901 code when every parsed group has the same code; otherwise `null`.", alias="acknowledgmentCode", json_schema_extra={"examples": ["A"]})
    summary: StrictStr = Field(description="Human-readable whole-997 aggregate result; transaction-scoped displays should use `evaluatedStatus` and the selected group or transaction outcome.", json_schema_extra={"examples": ["Functional group accepted; 1 of 1 received transaction set was accepted."]})
    parsed: StrictBool = Field(description="True when AK9 and all three AK902-AK904 counts were structurally valid.")
    unknown_reason: Optional[StrictStr] = Field(description="Machine-readable reason when `status` is `unknown`.", alias="unknownReason")
    included_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="Sum of AK902 across every parsed group, or `null` when any group count is unavailable or the sum overflows.", alias="includedTransactionSets")
    received_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="Sum of AK903 across every parsed group, or `null` when any group count is unavailable or the sum overflows.", alias="receivedTransactionSets")
    accepted_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="Sum of AK904 across every parsed group, or `null` when any group count is unavailable or the sum overflows.", alias="acceptedTransactionSets")
    error_codes: List[StrictStr] = Field(description="De-duplicated union of non-empty AK905 and later functional-group syntax error codes across every parsed group.", alias="errorCodes")
    groups: List[FunctionalAcknowledgmentGroupOutcome] = Field(description="Distinct AK1/AK9 functional-group outcomes in source order; no sibling group is collapsed into another.")
    transaction_sets: List[FunctionalAcknowledgmentTransactionSetOutcome] = Field(description="Transaction-set results from paired AK2 and AK5 segments. Each result repeats its parent AK101/AK102 identity so flattened results remain attributable when an interchange contains multiple 997 groups. ", alias="transactionSets")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["status", "acknowledgmentCode", "summary", "parsed", "unknownReason", "includedTransactionSets", "receivedTransactionSets", "acceptedTransactionSets", "errorCodes", "groups", "transactionSets"]

    @field_validator('unknown_reason')
    def unknown_reason_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['missing_x12', 'not_997', 'invalid_structure', 'missing_ak9', 'invalid_ak9', 'unsupported_acknowledgment_code', 'inconsistent_rollup']):
            raise ValueError("must be one of enum values ('missing_x12', 'not_997', 'invalid_structure', 'missing_ak9', 'invalid_ak9', 'unsupported_acknowledgment_code', 'inconsistent_rollup')")
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
        """Create an instance of FunctionalAcknowledgmentOutcome from a JSON string"""
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
        """Create an instance of FunctionalAcknowledgmentOutcome from a dict"""
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
            "groups": [FunctionalAcknowledgmentGroupOutcome.from_dict(_item) for _item in obj["groups"]] if obj.get("groups") is not None else None,
            "transactionSets": [FunctionalAcknowledgmentTransactionSetOutcome.from_dict(_item) for _item in obj["transactionSets"]] if obj.get("transactionSets") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
