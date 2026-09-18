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
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2FunctionalAcknowledgmentSettings(BaseModel):
    """
    Optional automatic X12 acknowledgment MIME packaging for 997s and partner-enabled 999s. Omit the object or `messageStructure` to use `SIGNED_ENCRYPTED`.
    """ # noqa: E501
    message_structure: Optional[StrictStr] = Field(default='SIGNED_ENCRYPTED', description="MIME signing, encryption, and compression structure used when ModernEDI automatically sends an X12 acknowledgment (997 or partner-enabled 999) to this partner.", alias="messageStructure")
    __properties: ClassVar[List[str]] = ["messageStructure"]

    @field_validator('message_structure')
    def message_structure_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PLAIN', 'SIGNED', 'ENCRYPTED', 'SIGNED_ENCRYPTED', 'PLAIN_COMPRESSED', 'SIGNED_COMPRESSED', 'ENCRYPTED_COMPRESSED', 'ENCRYPTED_COMPRESSED_SIGNED']):
            raise ValueError("must be one of enum values ('PLAIN', 'SIGNED', 'ENCRYPTED', 'SIGNED_ENCRYPTED', 'PLAIN_COMPRESSED', 'SIGNED_COMPRESSED', 'ENCRYPTED_COMPRESSED', 'ENCRYPTED_COMPRESSED_SIGNED')")
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
        """Create an instance of As2FunctionalAcknowledgmentSettings from a JSON string"""
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
        """Create an instance of As2FunctionalAcknowledgmentSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "messageStructure": obj.get("messageStructure") if obj.get("messageStructure") is not None else 'SIGNED_ENCRYPTED'
        }.items() if key in obj})
        return _obj
