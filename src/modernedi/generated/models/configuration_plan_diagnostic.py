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
from modernedi.generated.models.configuration_plan_resource_identity import ConfigurationPlanResourceIdentity
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationPlanDiagnostic(BaseModel):
    """
    One machine-readable planning error or warning. `pointer` is an RFC 6901 JSON Pointer into the submitted request body; source diagnostics may also identify an exact file, line, and column.
    """ # noqa: E501
    severity: StrictStr
    code: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Stable machine-readable diagnostic code.")
    message: Annotated[str, Field(min_length=1, strict=True)] = Field(description="Plain-language explanation suitable for an operator or authoring tool.")
    pointer: StrictStr = Field(description="RFC 6901 JSON Pointer into the submitted `ConfigurationPlanRequest`; the empty string identifies the request root.")
    file_path: Optional[StrictStr] = Field(default=None, description="Logical bundle path associated with this diagnostic when one file can be identified.", alias="filePath")
    resource: Optional[ConfigurationPlanResourceIdentity] = None
    line: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="One-based source line when a mapping compiler supplies a location.")
    column: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="One-based source column when a mapping compiler supplies a location.")
    __properties: ClassVar[List[str]] = ["severity", "code", "message", "pointer", "filePath", "resource", "line", "column"]

    @field_validator('severity')
    def severity_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ERROR', 'WARNING']):
            raise ValueError("must be one of enum values ('ERROR', 'WARNING')")
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
        """Create an instance of ConfigurationPlanDiagnostic from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resource
        if self.resource:
            _dict['resource'] = self.resource.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationPlanDiagnostic from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "severity": obj.get("severity"),
            "code": obj.get("code"),
            "message": obj.get("message"),
            "pointer": obj.get("pointer"),
            "filePath": obj.get("filePath"),
            "resource": ConfigurationPlanResourceIdentity.from_dict(obj["resource"]) if obj.get("resource") is not None else None,
            "line": obj.get("line"),
            "column": obj.get("column")
        }.items() if key in obj})
        return _obj
