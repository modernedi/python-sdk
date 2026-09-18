# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from modernedi.generated.models.mapping_business_key import MappingBusinessKey
from modernedi.generated.models.mapping_delivered_metadata import MappingDeliveredMetadata
from modernedi.generated.models.mapping_output_configuration import MappingOutputConfiguration
from modernedi.generated.models.mapping_transform import MappingTransform
from modernedi.generated.models.syntax_tree_catalog_binding import SyntaxTreeCatalogBinding
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappingConfiguration(BaseModel):
    """
    Complete published map, transform source, output contract, provenance controls, and concurrency ETag.
    """ # noqa: E501
    mapping_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="Stable workspace-scoped mapping id used for reads, updates, history, and deletion.", alias="mappingId")
    partner_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="Stable workspace-scoped partner id whose X12 traffic this map handles.", alias="partnerId")
    direction: StrictStr = Field(description="`INCOMING` transforms partner X12 to application data; `OUTGOING` transforms application data to partner X12.")
    x12_version: StrictStr = Field(description="Normalized X12 version, such as `4010`.", alias="x12Version", json_schema_extra={"examples": ["4010"]})
    functional_identifier_code: StrictStr = Field(description="X12 GS01 functional identifier enum name.", alias="functionalIdentifierCode", json_schema_extra={"examples": ["PO"]})
    transaction_set_identifier_code: StrictStr = Field(description="X12 ST01 transaction-set identifier without a leading underscore.", alias="transactionSetIdentifierCode", json_schema_extra={"examples": ["850"]})
    syntax_tree_catalog: Optional[SyntaxTreeCatalogBinding] = Field(default=None, alias="syntaxTreeCatalog")
    transform: MappingTransform
    output: MappingOutputConfiguration
    business_key: Optional[MappingBusinessKey] = Field(default=None, alias="businessKey")
    delivered_metadata: Optional[MappingDeliveredMetadata] = Field(default=None, description="Present only for incoming mappings.", alias="deliveredMetadata")
    configuration_resource_key: UUID = Field(description="Portable mapping identity used by exported configuration documents and aggregate plan/apply. Unlike the numeric workspace-local `mappingId`, this key remains stable when the configuration moves between workspaces.", alias="configurationResourceKey")
    etag: StrictStr = Field(description="Quoted SHA-256 configuration ETag.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["mappingId", "partnerId", "direction", "x12Version", "functionalIdentifierCode", "transactionSetIdentifierCode", "syntaxTreeCatalog", "transform", "output", "businessKey", "deliveredMetadata", "configurationResourceKey", "etag"]

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['INCOMING', 'OUTGOING']):
            raise ValueError("must be one of enum values ('INCOMING', 'OUTGOING')")
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
        """Create an instance of MappingConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of syntax_tree_catalog
        if self.syntax_tree_catalog:
            _dict['syntaxTreeCatalog'] = self.syntax_tree_catalog.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transform
        if self.transform:
            _dict['transform'] = self.transform.to_dict()
        # override the default output from pydantic by calling `to_dict()` of output
        if self.output:
            _dict['output'] = self.output.to_dict()
        # override the default output from pydantic by calling `to_dict()` of business_key
        if self.business_key:
            _dict['businessKey'] = self.business_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivered_metadata
        if self.delivered_metadata:
            _dict['deliveredMetadata'] = self.delivered_metadata.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappingConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "mappingId": obj.get("mappingId"),
            "partnerId": obj.get("partnerId"),
            "direction": obj.get("direction"),
            "x12Version": obj.get("x12Version"),
            "functionalIdentifierCode": obj.get("functionalIdentifierCode"),
            "transactionSetIdentifierCode": obj.get("transactionSetIdentifierCode"),
            "syntaxTreeCatalog": SyntaxTreeCatalogBinding.from_dict(obj["syntaxTreeCatalog"]) if obj.get("syntaxTreeCatalog") is not None else None,
            "transform": MappingTransform.from_dict(obj["transform"]) if obj.get("transform") is not None else None,
            "output": MappingOutputConfiguration.from_dict(obj["output"]) if obj.get("output") is not None else None,
            "businessKey": MappingBusinessKey.from_dict(obj["businessKey"]) if obj.get("businessKey") is not None else None,
            "deliveredMetadata": MappingDeliveredMetadata.from_dict(obj["deliveredMetadata"]) if obj.get("deliveredMetadata") is not None else None,
            "configurationResourceKey": obj.get("configurationResourceKey"),
            "etag": obj.get("etag")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
