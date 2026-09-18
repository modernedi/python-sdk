# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class ConfigurationPartnerSeparatorSet(BaseModel):
    """
    ConfigurationPartnerSeparatorSet
    """ # noqa: E501
    element_separator: Annotated[str, Field(min_length=1, strict=True, max_length=1)] = Field(alias="elementSeparator")
    sub_element_separator: Annotated[str, Field(min_length=1, strict=True, max_length=1)] = Field(alias="subElementSeparator")
    segment_terminator: Annotated[str, Field(min_length=1, strict=True, max_length=1)] = Field(alias="segmentTerminator")
    repetition_separator: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=1)]] = Field(description="Repetition separator, or `null` when the selected X12 version does not use one.", alias="repetitionSeparator")
    __properties: ClassVar[List[str]] = ["elementSeparator", "subElementSeparator", "segmentTerminator", "repetitionSeparator"]

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
        """Create an instance of ConfigurationPartnerSeparatorSet from a JSON string"""
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
        # set to None if repetition_separator (nullable) is None
        # and model_fields_set contains the field
        if self.repetition_separator is None and "repetition_separator" in self.model_fields_set:
            _dict['repetitionSeparator'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConfigurationPartnerSeparatorSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "elementSeparator": obj.get("elementSeparator"),
            "subElementSeparator": obj.get("subElementSeparator"),
            "segmentTerminator": obj.get("segmentTerminator"),
            "repetitionSeparator": obj.get("repetitionSeparator")
        }.items() if key in obj})
        return _obj
