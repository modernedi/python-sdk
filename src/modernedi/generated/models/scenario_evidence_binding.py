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
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from modernedi.generated.models.scenario_evidence_authority import ScenarioEvidenceAuthority
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceBinding(BaseModel):
    """
    ScenarioEvidenceBinding
    """ # noqa: E501
    id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.")
    revision: Annotated[int, Field(strict=True, ge=0)]
    name: Annotated[str, Field(min_length=1, strict=True)]
    snapshot_content_sha256: Annotated[str, Field(strict=True)] = Field(alias="snapshotContentSha256")
    definition_content_sha256: Annotated[str, Field(strict=True)] = Field(alias="definitionContentSha256")
    adapter_id: StrictStr = Field(alias="adapterId")
    environment: StrictStr
    authority: ScenarioEvidenceAuthority
    __properties: ClassVar[List[str]] = ["id", "revision", "name", "snapshotContentSha256", "definitionContentSha256", "adapterId", "environment", "authority"]

    @field_validator('id', mode="before")
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('snapshot_content_sha256', mode="before")
    def snapshot_content_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('definition_content_sha256', mode="before")
    def definition_content_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('adapter_id')
    def adapter_id_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['scenario-graph-interpreter-v1']):
            raise ValueError("must be one of enum values ('scenario-graph-interpreter-v1')")
        return value

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['production', 'test']):
            raise ValueError("must be one of enum values ('production', 'test')")
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
        """Create an instance of ScenarioEvidenceBinding from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of authority
        if self.authority:
            _dict['authority'] = self.authority.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceBinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "id": obj.get("id"),
            "revision": obj.get("revision"),
            "name": obj.get("name"),
            "snapshotContentSha256": obj.get("snapshotContentSha256"),
            "definitionContentSha256": obj.get("definitionContentSha256"),
            "adapterId": obj.get("adapterId"),
            "environment": obj.get("environment"),
            "authority": ScenarioEvidenceAuthority.from_dict(obj["authority"]) if obj.get("authority") is not None else None
        }.items() if key in obj})
        return _obj
