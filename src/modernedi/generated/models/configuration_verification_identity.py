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
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from modernedi.generated.models.configuration_verification_mapping import ConfigurationVerificationMapping
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationVerificationIdentity(BaseModel):
    """
    Server-derived identity of the reviewed configuration and evaluator, not tenant-runtime execution evidence.
    """ # noqa: E501
    plan_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="planSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    desired_bundle_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="desiredBundleSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    base_snapshot_etag: StrictStr = Field(description="Exact workspace snapshot used to plan.", alias="baseSnapshotEtag")
    evaluator_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="evaluatorSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    mappings: Annotated[List[ConfigurationVerificationMapping], Field(min_length=1, max_length=25)] = Field(description="All desired mappings containing saved cases, sorted by resource key.")
    untested_mapping_count: Annotated[int, Field(strict=True, ge=0)] = Field(description="Desired mappings without saved cases. A passing suite does not cover these mappings.", alias="untestedMappingCount")
    case_count: Annotated[int, Field(le=100, strict=True, ge=1)] = Field(description="Total selected saved cases, including cases not reached before cancellation or timeout.", alias="caseCount")
    __properties: ClassVar[List[str]] = ["planSha256", "desiredBundleSha256", "baseSnapshotEtag", "evaluatorSha256", "mappings", "untestedMappingCount", "caseCount"]

    @field_validator('plan_sha256', mode="before")
    def plan_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('desired_bundle_sha256', mode="before")
    def desired_bundle_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('evaluator_sha256', mode="before")
    def evaluator_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
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
        """Create an instance of ConfigurationVerificationIdentity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in mappings (list)
        _items = []
        if self.mappings:
            for _item_mappings in self.mappings:
                if _item_mappings:
                    _items.append(_item_mappings.to_dict())
            _dict['mappings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationVerificationIdentity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "planSha256": obj.get("planSha256"),
            "desiredBundleSha256": obj.get("desiredBundleSha256"),
            "baseSnapshotEtag": obj.get("baseSnapshotEtag"),
            "evaluatorSha256": obj.get("evaluatorSha256"),
            "mappings": [ConfigurationVerificationMapping.from_dict(_item) for _item in obj["mappings"]] if obj.get("mappings") is not None else None,
            "untestedMappingCount": obj.get("untestedMappingCount"),
            "caseCount": obj.get("caseCount")
        }.items() if key in obj})
        return _obj
