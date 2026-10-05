# coding: utf-8

"""Generated from the ModernEDI Integration API 1.36.0. Do not edit.

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
from modernedi.generated.models.configuration_scenario_case_check import ConfigurationScenarioCaseCheck
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationScenarioCaseResult(BaseModel):
    """
    ConfigurationScenarioCaseResult
    """ # noqa: E501
    scenario_binding_resource_key: UUID = Field(description="Binding owning this saved conversation test.", alias="scenarioBindingResourceKey")
    id: StrictStr = Field(description="Portable case ID.")
    name: StrictStr = Field(description="Portable case display name.")
    mode: StrictStr = Field(description="No live run, EDI send, transport receipt, or partner acknowledgement is created.")
    case_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="caseSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    expected_outcome: StrictStr = Field(description="Expected interpreter outcome. A negative test can pass by reproducing its named failing checks.", alias="expectedOutcome")
    status: StrictStr = Field(description="Whether actual interpreter results match all saved expectations. Mapping or document evaluation errors never satisfy negative expectations.")
    actual_outcome: Optional[StrictStr] = Field(description="Actual offline interpreter outcome; null when evaluation could not run.", alias="actualOutcome")
    actual_checks_sha256: Optional[Annotated[str, Field(strict=True)]] = Field(description="Hash of all actual check IDs, outcomes, and codes; null on evaluation errors.", alias="actualChecksSha256")
    diagnostic_code: Optional[StrictStr] = Field(description="Safe diagnostic category, or null when the saved test passed.", alias="diagnosticCode")
    check_count: Annotated[int, Field(strict=True, ge=0)] = Field(description="Total evaluated interpreter checks, including checks omitted from the bounded preview.", alias="checkCount")
    checks: Annotated[List[ConfigurationScenarioCaseCheck], Field(max_length=100)] = Field(description="Bounded preview, non-passing checks first. Contains no raw inputs, outputs, fact values, or engine error text.")
    __properties: ClassVar[List[str]] = ["scenarioBindingResourceKey", "id", "name", "mode", "caseSha256", "expectedOutcome", "status", "actualOutcome", "actualChecksSha256", "diagnosticCode", "checkCount", "checks"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['OFFLINE']):
            raise ValueError("must be one of enum values ('OFFLINE')")
        return value

    @field_validator('case_sha256', mode="before")
    def case_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('expected_outcome')
    def expected_outcome_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PASSED', 'FAILED', 'PENDING', 'INCONCLUSIVE']):
            raise ValueError("must be one of enum values ('PASSED', 'FAILED', 'PENDING', 'INCONCLUSIVE')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PASSED', 'FAILED', 'ERROR']):
            raise ValueError("must be one of enum values ('PASSED', 'FAILED', 'ERROR')")
        return value

    @field_validator('actual_outcome')
    def actual_outcome_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PASSED', 'FAILED', 'PENDING', 'INCONCLUSIVE']):
            raise ValueError("must be one of enum values ('PASSED', 'FAILED', 'PENDING', 'INCONCLUSIVE')")
        return value

    @field_validator('actual_checks_sha256', mode="before")
    def actual_checks_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^[a-f0-9]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[a-f0-9]{64}$/")
        return value

    @field_validator('diagnostic_code')
    def diagnostic_code_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EXPECTED_RESULT_MISMATCH', 'MAPPING_CASE_FAILED', 'DOCUMENT_EVALUATION_FAILED']):
            raise ValueError("must be one of enum values ('EXPECTED_RESULT_MISMATCH', 'MAPPING_CASE_FAILED', 'DOCUMENT_EVALUATION_FAILED')")
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
        """Create an instance of ConfigurationScenarioCaseResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in checks (list)
        _items = []
        if self.checks:
            for _item_checks in self.checks:
                if _item_checks:
                    _items.append(_item_checks.to_dict())
            _dict['checks'] = _items
        # set to None if actual_outcome (nullable) is None
        # and model_fields_set contains the field
        if self.actual_outcome is None and "actual_outcome" in self.model_fields_set:
            _dict['actualOutcome'] = None

        # set to None if actual_checks_sha256 (nullable) is None
        # and model_fields_set contains the field
        if self.actual_checks_sha256 is None and "actual_checks_sha256" in self.model_fields_set:
            _dict['actualChecksSha256'] = None

        # set to None if diagnostic_code (nullable) is None
        # and model_fields_set contains the field
        if self.diagnostic_code is None and "diagnostic_code" in self.model_fields_set:
            _dict['diagnosticCode'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationScenarioCaseResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "scenarioBindingResourceKey": obj.get("scenarioBindingResourceKey"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "mode": obj.get("mode"),
            "caseSha256": obj.get("caseSha256"),
            "expectedOutcome": obj.get("expectedOutcome"),
            "status": obj.get("status"),
            "actualOutcome": obj.get("actualOutcome"),
            "actualChecksSha256": obj.get("actualChecksSha256"),
            "diagnosticCode": obj.get("diagnosticCode"),
            "checkCount": obj.get("checkCount"),
            "checks": [ConfigurationScenarioCaseCheck.from_dict(_item) for _item in obj["checks"]] if obj.get("checks") is not None else None
        }.items() if key in obj})
        return _obj
