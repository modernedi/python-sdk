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
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from uuid import UUID
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationVerificationCaseResult(BaseModel):
    """
    Exact text comparison and optional generated-X12 validation outcome. A case fails if either requested check fails. Raw inputs, outputs and engine diagnostic text are never retained.
    """ # noqa: E501
    mapping_resource_key: UUID = Field(description="Mapping owning this case.", alias="mappingResourceKey")
    id: StrictStr = Field(description="Portable case ID.")
    name: StrictStr = Field(description="Portable case display name.")
    status: StrictStr = Field(description="Outcome of this executed case.")
    case_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="caseSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    expected_output_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="expectedOutputSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    actual_output_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(description="Actual output hash, or null when execution produced no output.", alias="actualOutputSha256")
    x12_validation_status: Optional[StrictStr] = Field(default=None, description="Present only when the saved outgoing case requested validateX12. Uses the frozen mapping syntax tree and the same document preparation and validation as outgoing preview/send. A FAILED case may have matching expected/actual hashes when X12 validation failed.", alias="x12ValidationStatus")
    __properties: ClassVar[List[str]] = ["mappingResourceKey", "id", "name", "status", "caseSha256", "expectedOutputSha256", "actualOutputSha256", "x12ValidationStatus"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PASSED', 'FAILED', 'ERROR']):
            raise ValueError("must be one of enum values ('PASSED', 'FAILED', 'ERROR')")
        return value

    @field_validator('case_sha256', mode="before")
    def case_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('expected_output_sha256', mode="before")
    def expected_output_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('actual_output_sha256', mode="before")
    def actual_output_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[a-f0-9]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{64}$/")
        return value

    @field_validator('x12_validation_status')
    def x12_validation_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PASSED', 'FAILED', 'ERROR']):
            raise ValueError("must be one of enum values ('PASSED', 'FAILED', 'ERROR')")
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
        """Create an instance of ConfigurationVerificationCaseResult from a JSON string"""
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
        # set to None if actual_output_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.actual_output_sha256 is None and "actual_output_sha256" in self.model_fields_set:
            _dict['actualOutputSha256'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationVerificationCaseResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "mappingResourceKey": obj.get("mappingResourceKey"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "caseSha256": obj.get("caseSha256"),
            "expectedOutputSha256": obj.get("expectedOutputSha256"),
            "actualOutputSha256": obj.get("actualOutputSha256"),
            "x12ValidationStatus": obj.get("x12ValidationStatus")
        }.items() if key in obj})
        return _obj
