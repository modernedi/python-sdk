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
from modernedi.generated.models.configuration_mapping_output import ConfigurationMappingOutput
from modernedi.generated.models.configuration_mapping_runtime import ConfigurationMappingRuntime
from modernedi.generated.models.configuration_mapping_transform import ConfigurationMappingTransform
from modernedi.generated.models.mapping_business_key import MappingBusinessKey
from modernedi.generated.models.mapping_delivered_metadata import MappingDeliveredMetadata
from modernedi.generated.models.mapping_regression_case import MappingRegressionCase
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationMappingSpec(BaseModel):
    """
    Published mapping configuration without its database id, API ETag, or server-resolved syntax-tree provenance. The partner reference and source reference are portable bundle values.
    """ # noqa: E501
    regression_cases: Optional[Annotated[List[MappingRegressionCase], Field(min_length=1, max_length=10)]] = Field(default=None, description="Optional saved editor tests. Omit when empty; sort by unique case id. The canonical JSON array must fit within 256 KiB. Fixtures enter configuration and Git history, so use sanitized sample data. Editing only these cases does not change the live mapping or refresh scenario bindings. Stored cases do not assert a passing result and do not gate apply. ", alias="regressionCases")
    partner_key: UUID = Field(description="Portable key of the partner resource this mapping handles.", alias="partnerKey")
    direction: StrictStr
    x12_version: StrictStr = Field(description="Normalized X12 version, such as `4010`.", alias="x12Version")
    functional_identifier_code: StrictStr = Field(description="X12 GS01 functional identifier enum name.", alias="functionalIdentifierCode")
    transaction_set_identifier_code: StrictStr = Field(description="X12 ST01 transaction-set identifier without a leading underscore.", alias="transactionSetIdentifierCode")
    transform: ConfigurationMappingTransform
    output: ConfigurationMappingOutput
    business_key: Optional[MappingBusinessKey] = Field(default=None, alias="businessKey")
    delivered_metadata: Optional[MappingDeliveredMetadata] = Field(default=None, alias="deliveredMetadata")
    runtime: ConfigurationMappingRuntime
    __properties: ClassVar[List[str]] = ["regressionCases", "partnerKey", "direction", "x12Version", "functionalIdentifierCode", "transactionSetIdentifierCode", "transform", "output", "businessKey", "deliveredMetadata", "runtime"]

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
        """Create an instance of ConfigurationMappingSpec from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in regression_cases (list)
        _items = []
        if self.regression_cases:
            for _item_regression_cases in self.regression_cases:
                if _item_regression_cases:
                    _items.append(_item_regression_cases.to_dict())
            _dict['regressionCases'] = _items
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
        # override the default output from pydantic by calling `to_dict()` of runtime
        if self.runtime:
            _dict['runtime'] = self.runtime.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationMappingSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "regressionCases": [MappingRegressionCase.from_dict(_item) for _item in obj["regressionCases"]] if obj.get("regressionCases") is not None else None,
            "partnerKey": obj.get("partnerKey"),
            "direction": obj.get("direction"),
            "x12Version": obj.get("x12Version"),
            "functionalIdentifierCode": obj.get("functionalIdentifierCode"),
            "transactionSetIdentifierCode": obj.get("transactionSetIdentifierCode"),
            "transform": ConfigurationMappingTransform.from_dict(obj["transform"]) if obj.get("transform") is not None else None,
            "output": ConfigurationMappingOutput.from_dict(obj["output"]) if obj.get("output") is not None else None,
            "businessKey": MappingBusinessKey.from_dict(obj["businessKey"]) if obj.get("businessKey") is not None else None,
            "deliveredMetadata": MappingDeliveredMetadata.from_dict(obj["deliveredMetadata"]) if obj.get("deliveredMetadata") is not None else None,
            "runtime": ConfigurationMappingRuntime.from_dict(obj["runtime"]) if obj.get("runtime") is not None else None
        }.items() if key in obj})
        return _obj
