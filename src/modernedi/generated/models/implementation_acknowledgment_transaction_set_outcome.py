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
from modernedi.generated.models.implementation_acknowledgment_status import ImplementationAcknowledgmentStatus
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ImplementationAcknowledgmentTransactionSetOutcome(BaseModel):
    """
    ImplementationAcknowledgmentTransactionSetOutcome
    """ # noqa: E501
    functional_identifier_code: Optional[StrictStr] = Field(description="AK101 functional identifier code for the acknowledged group, such as `PO` or `IN`.", alias="functionalIdentifierCode", json_schema_extra={"examples": ["PO"]})
    functional_group_control_number: Optional[StrictStr] = Field(description="AK102 control number for the acknowledged functional group.", alias="functionalGroupControlNumber", json_schema_extra={"examples": ["17"]})
    transaction_set_identifier_code: Optional[StrictStr] = Field(description="AK201 transaction-set identifier code, such as `850` or `810`.", alias="transactionSetIdentifierCode", json_schema_extra={"examples": ["850"]})
    transaction_set_control_number: Optional[StrictStr] = Field(description="AK202 transaction-set control number.", alias="transactionSetControlNumber", json_schema_extra={"examples": ["0001"]})
    implementation_convention_reference: Optional[StrictStr] = Field(description="Raw AK203 implementation-convention reference echoed from the acknowledged ST03, or `null` when absent.", alias="implementationConventionReference", json_schema_extra={"examples": ["005010X222A1"]})
    status: ImplementationAcknowledgmentStatus
    acknowledgment_code: Optional[StrictStr] = Field(description="Original IK501 transaction-set acknowledgment code, when available. This raw code is preserved separately from normalized `status`; bare IK501 `A` is inconsistent and normalizes to `unknown` when its AK2 loop also reports IK3/IK4 error detail. ", alias="acknowledgmentCode", json_schema_extra={"examples": ["A"]})
    error_codes: List[StrictStr] = Field(description="Non-empty IK502 and later transaction-set syntax error codes.", alias="errorCodes")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["functionalIdentifierCode", "functionalGroupControlNumber", "transactionSetIdentifierCode", "transactionSetControlNumber", "implementationConventionReference", "status", "acknowledgmentCode", "errorCodes"]

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
        """Create an instance of ImplementationAcknowledgmentTransactionSetOutcome from a JSON string"""
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

        # set to None if transaction_set_identifier_code (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_set_identifier_code is None and "transaction_set_identifier_code" in self.model_fields_set:
            _dict['transactionSetIdentifierCode'] = None

        # set to None if transaction_set_control_number (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_set_control_number is None and "transaction_set_control_number" in self.model_fields_set:
            _dict['transactionSetControlNumber'] = None

        # set to None if implementation_convention_reference (nullable) is None
        # and model_fields_set contains the field
        if self.implementation_convention_reference is None and "implementation_convention_reference" in self.model_fields_set:
            _dict['implementationConventionReference'] = None

        # set to None if acknowledgment_code (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledgment_code is None and "acknowledgment_code" in self.model_fields_set:
            _dict['acknowledgmentCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ImplementationAcknowledgmentTransactionSetOutcome from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "functionalIdentifierCode": obj.get("functionalIdentifierCode"),
            "functionalGroupControlNumber": obj.get("functionalGroupControlNumber"),
            "transactionSetIdentifierCode": obj.get("transactionSetIdentifierCode"),
            "transactionSetControlNumber": obj.get("transactionSetControlNumber"),
            "implementationConventionReference": obj.get("implementationConventionReference"),
            "status": obj.get("status"),
            "acknowledgmentCode": obj.get("acknowledgmentCode"),
            "errorCodes": obj.get("errorCodes")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
