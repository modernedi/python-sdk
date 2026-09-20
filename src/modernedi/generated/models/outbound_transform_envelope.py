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
from modernedi.generated.models.outbound_business_key import OutboundBusinessKey
from modernedi.generated.models.outbound_transform_envelope_input import OutboundTransformEnvelopeInput
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class OutboundTransformEnvelope(BaseModel):
    """
    OutboundTransformEnvelope
    """ # noqa: E501
    content_type: StrictStr = Field(description="Content type of `input` and the outgoing map to select. Use this envelope with HTTP `Content-Type: application/vnd.modernedi.outbound+json` when the source input is XML, text, or JSON with extra transform params. Ordinary `application/json` is always treated as the source document itself. ", alias="contentType", json_schema_extra={"examples": ["application/xml"]})
    input: Optional[OutboundTransformEnvelopeInput]
    business_key: Optional[OutboundBusinessKey] = Field(default=None, description="Optional business identifier to store on the outbound transaction record, such as an invoice number, ASN number, BOL number, shipment id, or other value your system uses for reconciliation. This is recorded for transaction search and display only; it does not affect outgoing-map selection or transform execution. ", alias="businessKey")
    params: Optional[Dict[str, Any]] = Field(default=None, description="Optional transform parameters. For XSLT maps, each key is bound as an external stylesheet parameter with the same simple, unqualified name. `json` and `text` are reserved by ModernEDI. JSON strings map to `xs:string`, integers to integer numbers, decimals to decimal numbers, booleans to `xs:boolean`, null to an empty sequence, objects to `map(xs:string, item()*)`, and arrays to XDM sequences. Arrays of objects therefore work with declarations such as `<xsl:param name=\"pallets\" as=\"map(xs:string, xs:anyAtomicType)*\" required=\"yes\"/>`. JSLT still uses `.` as its current input, but for JSLT maps ModernEDI evaluates the map with a root wrapper object shaped as `{ \"input\": <source>, \"params\": <params> }`. Source fields are therefore read as `.input.invoice.number` instead of directly from the root, and params are read as `.params.bolNumber`, `.params.pallets[0]`, and so on. When JSLT repeated output needs params inside a `for` loop, bind `.params` before the loop, such as `let params = .params`, and read `$params.bolNumber` inside the loop because `.` is the current source item there. Use `required=\"yes\"` for XSLT params that every live request must supply. Params JSON files in the mapper editor are used only for test-running a map; they are not live defaults for this API. In the mapper editor, params are standalone JSON fixture files that can be edited like other workspace files and selected when test-running the map. While authoring JSLT, the editor uses the selected source and params fixture files for completions, diagnostics, and quick fixes for wrapper root mistakes, missing sample paths, and `get-key` object-key typos. ", json_schema_extra={"examples": [{"bolNumber": "BOL-DEMO-8842", "totalWeightInLbs": 1232.54, "transactionSetControlNumber": "000002321", "pallets": [{"buyerSku": "DEMO-SKU-001", "itemNumber": "DEMO-ITEM-001", "numCases": 187, "sscc18": "000000000000000101"}]}]})
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["contentType", "input", "businessKey", "params"]

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
        """Create an instance of OutboundTransformEnvelope from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of input
        if self.input:
            _dict['input'] = self.input.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_key
        if self.business_key:
            _dict['businessKey'] = self.business_key.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if input (nullable) is None
        # and model_fields_set contains the field
        if self.input is None and "input" in self.model_fields_set:
            _dict['input'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OutboundTransformEnvelope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "contentType": obj.get("contentType"),
            "input": OutboundTransformEnvelopeInput.from_dict(obj["input"]) if obj.get("input") is not None else None,
            "businessKey": OutboundBusinessKey.from_dict(obj["businessKey"]) if obj.get("businessKey") is not None else None,
            "params": obj.get("params")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
