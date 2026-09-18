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
from typing import Any, ClassVar, Dict
from typing_extensions import Annotated
from uuid import UUID
from modernedi.generated.models.configuration_verification_syntax_tree import ConfigurationVerificationSyntaxTree
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationVerificationMapping(BaseModel):
    """
    Identity and coverage of one tested mapping.
    """ # noqa: E501
    mapping_resource_key: UUID = Field(description="Stable portable Mapping resource key.", alias="mappingResourceKey")
    candidate_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="candidateSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    cases_sha256: Annotated[str, Field(strict=True)] = Field(description="Lowercase hexadecimal SHA-256 digest.", alias="casesSha256", json_schema_extra={"examples": ["30d7e671476880c8d357370bf9a7c21fc59f55d2435073e92763f61d1c72f749"]})
    case_count: Annotated[int, Field(le=10, strict=True, ge=1)] = Field(description="Number of saved cases selected for this mapping.", alias="caseCount")
    syntax_tree: ConfigurationVerificationSyntaxTree = Field(alias="syntaxTree")
    __properties: ClassVar[List[str]] = ["mappingResourceKey", "candidateSha256", "casesSha256", "caseCount", "syntaxTree"]

    @field_validator('candidate_sha256', mode="before")
    def candidate_sha256_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9a-f]{64}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{64}$/")
        return value

    @field_validator('cases_sha256', mode="before")
    def cases_sha256_validate_regular_expression(cls, value):
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
        """Create an instance of ConfigurationVerificationMapping from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of syntax_tree
        if self.syntax_tree:
            _dict['syntaxTree'] = self.syntax_tree.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationVerificationMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "mappingResourceKey": obj.get("mappingResourceKey"),
            "candidateSha256": obj.get("candidateSha256"),
            "casesSha256": obj.get("casesSha256"),
            "caseCount": obj.get("caseCount"),
            "syntaxTree": ConfigurationVerificationSyntaxTree.from_dict(obj["syntaxTree"]) if obj.get("syntaxTree") is not None else None
        }.items() if key in obj})
        return _obj
