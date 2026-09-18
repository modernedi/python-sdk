# coding: utf-8

"""Generated from the ModernEDI Integration API 1.35.0. Do not edit.

OpenAPI Generator 7.24.0; see the package README for usage.
"""

from __future__ import annotations
from typing import Any, ClassVar, Dict, List, Optional, Set, Union
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self
from pydantic_core import to_jsonable_python

class As2MdnSettings(BaseModel):
    """
    Optional MDN interoperability controls. Omitted values default to unencrypted MDNs and synchronous error dispositions.
    """ # noqa: E501
    encrypt: Optional[StrictBool] = Field(default=False, description="When true, ModernEDI attempts to encrypt MDNs returned for inbound messages with the partner certificate and configured outbound encryption algorithm. If MDN encryption itself fails, ModernEDI returns an unencrypted error MDN so the partner still receives a disposition.")
    force_synchronous_for_errors: Optional[StrictBool] = Field(default=True, description="When true, an inbound processing failure or error is returned as a synchronous MDN even when the normal receipt flow is asynchronous.", alias="forceSynchronousForErrors")
    __properties: ClassVar[List[str]] = ["encrypt", "forceSynchronousForErrors"]

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
        """Create an instance of As2MdnSettings from a JSON string"""
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
        """Create an instance of As2MdnSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({key: value for key, value in {
            "encrypt": obj.get("encrypt") if obj.get("encrypt") is not None else False,
            "forceSynchronousForErrors": obj.get("forceSynchronousForErrors") if obj.get("forceSynchronousForErrors") is not None else True
        }.items() if key in obj})
        return _obj
