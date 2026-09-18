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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ScenarioEvidenceMappingAuthority(BaseModel):
    """
    ScenarioEvidenceMappingAuthority
    """ # noqa: E501
    step_id: Annotated[str, Field(strict=True)] = Field(description="A stable identifier beginning with a letter and containing at most 128 letters, digits, underscores, or hyphens.", alias="stepId")
    id: Annotated[int, Field(strict=True, ge=1)]
    partner_id: Annotated[int, Field(strict=True, ge=1)] = Field(alias="partnerId")
    direction: StrictStr
    x12_version: Annotated[str, Field(strict=True)] = Field(alias="x12Version")
    transaction_set: Annotated[str, Field(strict=True)] = Field(alias="transactionSet")
    configuration_etag: Annotated[str, Field(min_length=1, strict=True)] = Field(alias="configurationEtag")
    map_file_sha256_hash: Annotated[str, Field(strict=True)] = Field(alias="mapFileSha256Hash")
    __properties: ClassVar[List[str]] = ["stepId", "id", "partnerId", "direction", "x12Version", "transactionSet", "configurationEtag", "mapFileSha256Hash"]

    @field_validator('step_id', mode="before")
    def step_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z][A-Za-z0-9_-]{0,127}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z][A-Za-z0-9_-]{0,127}$/")
        return value

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['incoming', 'outgoing']):
            raise ValueError("must be one of enum values ('incoming', 'outgoing')")
        return value

    @field_validator('x12_version', mode="before")
    def x12_version_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9]{6}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{6}$/")
        return value

    @field_validator('transaction_set', mode="before")
    def transaction_set_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[0-9]{3}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]{3}$/")
        return value

    @field_validator('map_file_sha256_hash', mode="before")
    def map_file_sha256_hash_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if isinstance(value, str) and not re.match(r"^[A-Za-z0-9+\/]{42}[AEIMQUYcgkosw048]=$", value):
            raise ValueError(r"must validate the regular expression /^[A-Za-z0-9+\/]{42}[AEIMQUYcgkosw048]=$/")
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
        """Create an instance of ScenarioEvidenceMappingAuthority from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ScenarioEvidenceMappingAuthority from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "stepId": obj.get("stepId"),
            "id": obj.get("id"),
            "partnerId": obj.get("partnerId"),
            "direction": obj.get("direction"),
            "x12Version": obj.get("x12Version"),
            "transactionSet": obj.get("transactionSet"),
            "configurationEtag": obj.get("configurationEtag"),
            "mapFileSha256Hash": obj.get("mapFileSha256Hash")
        }.items() if key in obj})
        return _obj
