# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.functional_acknowledgment_status import FunctionalAcknowledgmentStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class FunctionalAcknowledgmentGroupSummary(BaseModel):
    """
    Compact AK1/AK9 group selected for one transaction row; nested AK2 results are intentionally omitted.
    """ # noqa: E501
    functional_identifier_code: Optional[StrictStr] = Field(description="AK101 functional identifier code for the acknowledged group.", alias="functionalIdentifierCode")
    functional_group_control_number: Optional[StrictStr] = Field(description="AK102 control number for the acknowledged functional group.", alias="functionalGroupControlNumber")
    functional_group_version: Optional[StrictStr] = Field(description="Raw AK103 functional-group version, or `null` when omitted.", alias="functionalGroupVersion")
    status: FunctionalAcknowledgmentStatus
    acknowledgment_code: Optional[StrictStr] = Field(description="Original AK901 acknowledgment code for this functional group.", alias="acknowledgmentCode")
    included_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="AK902 for this functional group.", alias="includedTransactionSets")
    received_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="AK903 for this functional group.", alias="receivedTransactionSets")
    accepted_transaction_sets: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(description="AK904 for this functional group; this count is distinct from an AK5 disposition.", alias="acceptedTransactionSets")
    error_codes: List[StrictStr] = Field(description="Non-empty AK905 and later functional-group syntax error codes.", alias="errorCodes")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["functionalIdentifierCode", "functionalGroupControlNumber", "functionalGroupVersion", "status", "acknowledgmentCode", "includedTransactionSets", "receivedTransactionSets", "acceptedTransactionSets", "errorCodes"]

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
        """Create an instance of FunctionalAcknowledgmentGroupSummary from a JSON string"""
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

        # set to None if functional_identifier_code (nullable) is None
        # and model_fields_set contains the field
        if self.functional_identifier_code is None and "functional_identifier_code" in self.model_fields_set:
            _dict['functionalIdentifierCode'] = None

        # set to None if functional_group_control_number (nullable) is None
        # and model_fields_set contains the field
        if self.functional_group_control_number is None and "functional_group_control_number" in self.model_fields_set:
            _dict['functionalGroupControlNumber'] = None

        # set to None if functional_group_version (nullable) is None
        # and model_fields_set contains the field
        if self.functional_group_version is None and "functional_group_version" in self.model_fields_set:
            _dict['functionalGroupVersion'] = None

        # set to None if acknowledgment_code (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledgment_code is None and "acknowledgment_code" in self.model_fields_set:
            _dict['acknowledgmentCode'] = None

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
        """Create an instance of FunctionalAcknowledgmentGroupSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "functionalIdentifierCode": obj.get("functionalIdentifierCode"),
            "functionalGroupControlNumber": obj.get("functionalGroupControlNumber"),
            "functionalGroupVersion": obj.get("functionalGroupVersion"),
            "status": obj.get("status"),
            "acknowledgmentCode": obj.get("acknowledgmentCode"),
            "includedTransactionSets": obj.get("includedTransactionSets"),
            "receivedTransactionSets": obj.get("receivedTransactionSets"),
            "acceptedTransactionSets": obj.get("acceptedTransactionSets"),
            "errorCodes": obj.get("errorCodes")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
