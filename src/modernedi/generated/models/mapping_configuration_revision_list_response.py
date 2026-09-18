# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from modernedi.generated.models.mapping_configuration_revision_detail import MappingConfigurationRevisionDetail
from modernedi.generated.models.mapping_configuration_revision_summary import MappingConfigurationRevisionSummary
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class MappingConfigurationRevisionListResponse(BaseModel):
    """
    Newest-first immutable mapping-configuration history plus the complete currently published transform source and configuration identity.
    """ # noqa: E501
    success: StrictBool = Field(description="Always `true`; failures use the documented error response instead.")
    mapping_id: Annotated[int, Field(strict=True, ge=1)] = Field(description="Stable workspace-scoped mapping id whose configuration history was requested.", alias="mappingId")
    current_etag: StrictStr = Field(description="Quoted ETag for the complete currently published mapping.", alias="currentEtag")
    current_revision: MappingConfigurationRevisionDetail = Field(description="Complete currently published transform source and exact configuration identity from the same locked snapshot as `currentEtag`. This is present even when its chronological revision entry is outside the current page.", alias="currentRevision")
    next_cursor: Optional[StrictStr] = Field(description="Opaque cursor for the next chronological page, or `null` when no older configuration revisions remain.", alias="nextCursor")
    has_more: StrictBool = Field(description="Whether another page is available through `nextCursor`.", alias="hasMore")
    revisions: List[MappingConfigurationRevisionSummary] = Field(description="One newest-first page of unique immutable mapping-configuration summaries. Identical source text can appear in multiple entries when another configuration value differs.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["success", "mappingId", "currentEtag", "currentRevision", "nextCursor", "hasMore", "revisions"]

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
        """Create an instance of MappingConfigurationRevisionListResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of current_revision
        if self.current_revision:
            _dict['currentRevision'] = self.current_revision.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in revisions (list)
        _items = []
        if self.revisions:
            for _item_revisions in self.revisions:
                if _item_revisions:
                    _items.append(_item_revisions.to_dict())
            _dict['revisions'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if next_cursor (nullable) is None
        # and model_fields_set contains the field
        if self.next_cursor is None and "next_cursor" in self.model_fields_set:
            _dict['nextCursor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MappingConfigurationRevisionListResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "success": obj.get("success"),
            "mappingId": obj.get("mappingId"),
            "currentEtag": obj.get("currentEtag"),
            "currentRevision": MappingConfigurationRevisionDetail.from_dict(obj["currentRevision"]) if obj.get("currentRevision") is not None else None,
            "nextCursor": obj.get("nextCursor"),
            "hasMore": obj.get("hasMore"),
            "revisions": [MappingConfigurationRevisionSummary.from_dict(_item) for _item in obj["revisions"]] if obj.get("revisions") is not None else None
        }.items() if key in obj})
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
