# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappingRuntimeMappingHealth(BaseModel):
    """
    MappingRuntimeMappingHealth
    """ # noqa: E501
    mapping_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(description="Mapping id, or `null` for a request that failed before map selection.", alias="mappingId")
    map_file: Optional[StrictStr] = Field(description="Transform filename, or `null` when no map was selected.", alias="mapFile")
    map_file_sha256_hash: Optional[StrictStr] = Field(description="Base64 SHA-256 hash of the attempted mapping source, when known.", alias="mapFileSha256Hash")
    current_revision: StrictBool = Field(description="Whether the grouped attempt hash is still the currently published source.", alias="currentRevision")
    direction: Optional[StrictStr] = Field(description="Mapping direction, or `null` when it was not attributable.")
    partner_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(description="Tenant-scoped partner id, or `null` when no partner was resolved.", alias="partnerId")
    partner_name: Optional[StrictStr] = Field(description="Partner name captured for the attempt, when known.", alias="partnerName")
    latest_at: Optional[str] = Field(description="UTC RFC 3339 instant with exactly nine fractional digits and a trailing `Z`, or `null`.", alias="latestAt", json_schema_extra={"examples": ["2026-07-15T18:30:00Z"]})
    failure_count: Annotated[int, Field(strict=True, ge=0)] = Field(description="Unresolved failures in this group.", alias="failureCount")
    recovered_count: Annotated[int, Field(strict=True, ge=0)] = Field(description="Resolved failures in this group.", alias="recoveredCount")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["mappingId", "mapFile", "mapFileSha256Hash", "currentRevision", "direction", "partnerId", "partnerName", "latestAt", "failureCount", "recoveredCount"]

    @field_validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['inbound', 'outbound']):
            raise ValueError("must be one of enum values ('inbound', 'outbound')")
        return value

    @field_validator('latest_at', mode="before")
    def latest_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if isinstance(value, str) and not re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$", value):
            raise ValueError(r"must validate the regular expression /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{9}Z$/")
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
        """Create an instance of MappingRuntimeMappingHealth from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if mapping_id (nullable) is None
        # and model_fields_set contains the field
        if self.mapping_id is None and "mapping_id" in self.model_fields_set:
            _dict['mappingId'] = None

        # set to None if map_file (nullable) is None
        # and model_fields_set contains the field
        if self.map_file is None and "map_file" in self.model_fields_set:
            _dict['mapFile'] = None

        # set to None if map_file_sha256_hash (nullable) is None
        # and model_fields_set contains the field
        if self.map_file_sha256_hash is None and "map_file_sha256_hash" in self.model_fields_set:
            _dict['mapFileSha256Hash'] = None

        # set to None if direction (nullable) is None
        # and model_fields_set contains the field
        if self.direction is None and "direction" in self.model_fields_set:
            _dict['direction'] = None

        # set to None if partner_id (nullable) is None
        # and model_fields_set contains the field
        if self.partner_id is None and "partner_id" in self.model_fields_set:
            _dict['partnerId'] = None

        # set to None if partner_name (nullable) is None
        # and model_fields_set contains the field
        if self.partner_name is None and "partner_name" in self.model_fields_set:
            _dict['partnerName'] = None

        # set to None if latest_at (nullable) is None
        # and model_fields_set contains the field
        if self.latest_at is None and "latest_at" in self.model_fields_set:
            _dict['latestAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappingRuntimeMappingHealth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "mappingId": obj.get("mappingId"),
            "mapFile": obj.get("mapFile"),
            "mapFileSha256Hash": obj.get("mapFileSha256Hash"),
            "currentRevision": obj.get("currentRevision"),
            "direction": obj.get("direction"),
            "partnerId": obj.get("partnerId"),
            "partnerName": obj.get("partnerName"),
            "latestAt": obj.get("latestAt"),
            "failureCount": obj.get("failureCount"),
            "recoveredCount": obj.get("recoveredCount")
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
