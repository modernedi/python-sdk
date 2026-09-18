# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from modernedi.generated.models.configuration_plan_file import ConfigurationPlanFile
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationApplyRequest(BaseModel):
    """
    Exact applicable desired bundle and deterministic plan identity submitted for one aggregate configuration deployment. The files must be byte-for-byte and logically identical to those planned.
    """ # noqa: E501
    refresh_scenario_bindings: Optional[Annotated[List[UUID], Field(max_length=100)]] = Field(default=None, description="Optional binding resource keys to re-apply against the destination workspace's current runtime authority without changing their authored files. Include the same selection in plan and apply. Referenced mapping/partner changes also produce explicit dependent binding updates in the plan. This option is apply metadata and never enters Git files.", alias="refreshScenarioBindings")
    plan_sha256: Annotated[str, Field(strict=True)] = Field(description="Non-null deterministic plan identity returned by the immediately preceding applicable plan.", alias="planSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    verification_run_id: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="Optional explicit passing-evidence requirement. When supplied, the server requires a current, unapplied PASSED run for this exact bundle and plan, and links it to the apply atomically. Omit to apply without a verification gate.", alias="verificationRunId")
    files: Annotated[List[ConfigurationPlanFile], Field(min_length=1, max_length=5000)] = Field(description="The exact desired logical files used to compute `planSha256`, optionally including the one canonical advisory `_state/snapshot.json` file accepted by planning.")
    __properties: ClassVar[List[str]] = ["refreshScenarioBindings", "planSha256", "verificationRunId", "files"]

    @field_validator('plan_sha256', mode="before")
    def plan_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('verification_run_id', mode="before")
    def verification_run_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^verify-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(r"must validate the regular expression /^verify-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/")
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
        """Create an instance of ConfigurationApplyRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item_files in self.files:
                if _item_files:
                    _items.append(_item_files.to_dict())
            _dict['files'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationApplyRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "refreshScenarioBindings": obj.get("refreshScenarioBindings"),
            "planSha256": obj.get("planSha256"),
            "verificationRunId": obj.get("verificationRunId"),
            "files": [ConfigurationPlanFile.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None
        }.items() if key in obj})
        return _obj
