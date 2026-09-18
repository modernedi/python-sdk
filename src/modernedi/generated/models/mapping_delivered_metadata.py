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
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappingDeliveredMetadata(BaseModel):
    """
    Selects optional source and mapping context included in `GET /v1/mapped-outputs` message objects and the webhook's nested `message` object. Every field defaults to `true`. Setting a field to `false` omits its corresponding message property; queue identifiers, receipt handles, payload, content type, purpose, and business key remain present. Webhook-envelope routing fields such as `tenantId` and `partnerId` also remain present.
    """ # noqa: E501
    partner: Optional[StrictBool] = Field(default=True, description="Include `partnerName` and tenant-scoped `partnerId` in the mapped-output message.")
    transaction_timestamp: Optional[StrictBool] = Field(default=True, description="Include the source transaction's persisted `transactionTimestamp`.", alias="transactionTimestamp")
    transaction_set: Optional[StrictBool] = Field(default=True, description="Include `transactionSet` and the equivalent `edi.transactionGroupType` value.", alias="transactionSet")
    transaction_control_number: Optional[StrictBool] = Field(default=True, description="Include `controlNumbers.transaction` (X12 ST02).", alias="transactionControlNumber")
    functional_group_control_number: Optional[StrictBool] = Field(default=True, description="Include `controlNumbers.functionalGroup` (X12 GS06).", alias="functionalGroupControlNumber")
    x12_version: Optional[StrictBool] = Field(default=True, description="Include `edi.x12Version`, derived from the parsed interchange version.", alias="x12Version")
    functional_identifier_code: Optional[StrictBool] = Field(default=True, description="Include `edi.functionalIdentifierCode` (X12 GS01).", alias="functionalIdentifierCode")
    segment_terminator: Optional[StrictBool] = Field(default=True, description="Include `edi.segmentTerminator`.", alias="segmentTerminator")
    mapping_source_hash: Optional[StrictBool] = Field(default=True, description="Include `mapping.fileSha256Hash`, the Base64-encoded SHA-256 hash of the map source that generated this output.", alias="mappingSourceHash")
    __properties: ClassVar[List[str]] = ["partner", "transactionTimestamp", "transactionSet", "transactionControlNumber", "functionalGroupControlNumber", "x12Version", "functionalIdentifierCode", "segmentTerminator", "mappingSourceHash"]

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
        """Create an instance of MappingDeliveredMetadata from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * Fields omitted by the caller stay omitted; explicit null and false values survive.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_unset=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappingDeliveredMetadata from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "partner": obj.get("partner") if obj.get("partner") is not None else True,
            "transactionTimestamp": obj.get("transactionTimestamp") if obj.get("transactionTimestamp") is not None else True,
            "transactionSet": obj.get("transactionSet") if obj.get("transactionSet") is not None else True,
            "transactionControlNumber": obj.get("transactionControlNumber") if obj.get("transactionControlNumber") is not None else True,
            "functionalGroupControlNumber": obj.get("functionalGroupControlNumber") if obj.get("functionalGroupControlNumber") is not None else True,
            "x12Version": obj.get("x12Version") if obj.get("x12Version") is not None else True,
            "functionalIdentifierCode": obj.get("functionalIdentifierCode") if obj.get("functionalIdentifierCode") is not None else True,
            "segmentTerminator": obj.get("segmentTerminator") if obj.get("segmentTerminator") is not None else True,
            "mappingSourceHash": obj.get("mappingSourceHash") if obj.get("mappingSourceHash") is not None else True
        }.items() if key in obj})
        return _obj
