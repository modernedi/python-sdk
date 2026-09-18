# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from modernedi.generated.models.x12_element_validation_error import X12ElementValidationError
from modernedi.generated.models.x12_functional_group_validation_error import X12FunctionalGroupValidationError
from modernedi.generated.models.x12_interchange_summary import X12InterchangeSummary
from modernedi.generated.models.x12_segment_validation_error import X12SegmentValidationError
from modernedi.generated.models.x12_transaction_validation_error import X12TransactionValidationError
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class X12ValidationResult(BaseModel):
    """
    X12 well-formedness and validation diagnostics produced from the submitted interchange.
    """ # noqa: E501
    valid: StrictBool = Field(description="True only when parsing succeeded and no error- or failure-level X12 diagnostics were found.")
    well_formed: StrictBool = Field(description="True when ModernEDI could parse an interchange envelope; a well-formed document may still be invalid.", alias="wellFormed")
    errors: List[StrictStr] = Field(description="Human-readable parser or validation errors that prevent the submitted interchange from being considered valid.")
    warnings: List[StrictStr] = Field(description="Human-readable non-fatal findings that merit review but do not by themselves make `valid` false.")
    failures: List[StrictStr] = Field(description="Human-readable severe validation failures reported separately by the X12 validator.")
    disposition_error: Optional[StrictStr] = Field(description="Interchange-level error disposition text, or `null` when the validator did not report one.", alias="dispositionError")
    disposition_warning: Optional[StrictStr] = Field(description="Interchange-level warning disposition text, or `null` when the validator did not report one.", alias="dispositionWarning")
    disposition_failure: Optional[StrictStr] = Field(description="Interchange-level failure disposition text, or `null` when the validator did not report one.", alias="dispositionFailure")
    functional_group_errors: List[X12FunctionalGroupValidationError] = Field(description="Structured findings attached to a GS/GE functional group, with zero-based group indexes for correlation.", alias="functionalGroupErrors")
    transaction_errors: List[X12TransactionValidationError] = Field(description="Structured findings attached to an ST/SE transaction set, with zero-based group and transaction indexes.", alias="transactionErrors")
    segment_errors: List[X12SegmentValidationError] = Field(description="Structured segment-level X12 syntax findings, including the one-based position within the transaction.", alias="segmentErrors")
    element_errors: List[X12ElementValidationError] = Field(description="Structured data-element findings identifying the segment, element, optional composite component, and rejected value.", alias="elementErrors")
    interchange: Optional[X12InterchangeSummary] = Field(description="Parsed interchange summary with separators, groups, transactions, and segment previews; `null` when parsing did not produce an interchange.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["valid", "wellFormed", "errors", "warnings", "failures", "dispositionError", "dispositionWarning", "dispositionFailure", "functionalGroupErrors", "transactionErrors", "segmentErrors", "elementErrors", "interchange"]

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
        """Create an instance of X12ValidationResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in functional_group_errors (list)
        _items = []
        if self.functional_group_errors:
            for _item_functional_group_errors in self.functional_group_errors:
                if _item_functional_group_errors:
                    _items.append(_item_functional_group_errors.to_dict())
            _dict['functionalGroupErrors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in transaction_errors (list)
        _items = []
        if self.transaction_errors:
            for _item_transaction_errors in self.transaction_errors:
                if _item_transaction_errors:
                    _items.append(_item_transaction_errors.to_dict())
            _dict['transactionErrors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in segment_errors (list)
        _items = []
        if self.segment_errors:
            for _item_segment_errors in self.segment_errors:
                if _item_segment_errors:
                    _items.append(_item_segment_errors.to_dict())
            _dict['segmentErrors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in element_errors (list)
        _items = []
        if self.element_errors:
            for _item_element_errors in self.element_errors:
                if _item_element_errors:
                    _items.append(_item_element_errors.to_dict())
            _dict['elementErrors'] = _items
        # override the default output from pydantic by calling `to_dict()` of interchange
        if self.interchange:
            _dict['interchange'] = self.interchange.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if disposition_error (nullable) is None
        # and model_fields_set contains the field
        if self.disposition_error is None and "disposition_error" in self.model_fields_set:
            _dict['dispositionError'] = None

        # set to None if disposition_warning (nullable) is None
        # and model_fields_set contains the field
        if self.disposition_warning is None and "disposition_warning" in self.model_fields_set:
            _dict['dispositionWarning'] = None

        # set to None if disposition_failure (nullable) is None
        # and model_fields_set contains the field
        if self.disposition_failure is None and "disposition_failure" in self.model_fields_set:
            _dict['dispositionFailure'] = None

        # set to None if interchange (nullable) is None
        # and model_fields_set contains the field
        if self.interchange is None and "interchange" in self.model_fields_set:
            _dict['interchange'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of X12ValidationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "valid": obj.get("valid"),
            "wellFormed": obj.get("wellFormed"),
            "errors": obj.get("errors"),
            "warnings": obj.get("warnings"),
            "failures": obj.get("failures"),
            "dispositionError": obj.get("dispositionError"),
            "dispositionWarning": obj.get("dispositionWarning"),
            "dispositionFailure": obj.get("dispositionFailure"),
            "functionalGroupErrors": [X12FunctionalGroupValidationError.from_dict(_item) for _item in obj["functionalGroupErrors"]] if obj.get("functionalGroupErrors") is not None else None,
            "transactionErrors": [X12TransactionValidationError.from_dict(_item) for _item in obj["transactionErrors"]] if obj.get("transactionErrors") is not None else None,
            "segmentErrors": [X12SegmentValidationError.from_dict(_item) for _item in obj["segmentErrors"]] if obj.get("segmentErrors") is not None else None,
            "elementErrors": [X12ElementValidationError.from_dict(_item) for _item in obj["elementErrors"]] if obj.get("elementErrors") is not None else None,
            "interchange": X12InterchangeSummary.from_dict(obj["interchange"]) if obj.get("interchange") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
